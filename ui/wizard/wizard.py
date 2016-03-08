"""
/***************************************************************************
Name                 : wizard
Description          : STDM profile configuration wizard
Date                 : 06/January/2016
copyright            : (C) 2015 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import platform
import os
import sys
import logging

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from stdm.data.configuration.stdm_configuration import StdmConfiguration, Profile
from stdm.data.configuration.entity import entity_factory, Entity
from stdm.data.configuration.entity_relation import EntityRelation 
from stdm.data.configuration.columns import BaseColumn
from stdm.data.configuration.value_list import ValueList, CodeValue, value_list_factory
from stdm.data.configuration.social_tenure import *
from stdm.data.configuration.config_updater import ConfigurationSchemaUpdater
from stdm.data.configuration.db_items import DbItem
from stdm.settings.config_serializer import ConfigurationFileSerializer 
from stdm.data.configuration.exception import ConfigurationException

from custom_item_model import *

from ui_stdm_config import Ui_STDMWizard
from ui_entity import Ui_dlgEntity
from profile_editor import ProfileEditor
from create_entity import EntityEditor
from column_editor import ColumnEditor
from create_lookup import LookupEditor
from create_lookup_value import ValueEditor

# create logger
LOGGER = logging.getLogger('stdm')
LOGGER.setLevel(logging.DEBUG)

LIC_PAGE, PATH_PAGE, PROFILE_PAGE, ENTITY_PAGE, STR_PAGE, FINAL_PAGE = range(0, 6)

REG_KEY = "HKEY_CURRENT_USER\\Software\\QGIS\\QGIS2\\STDM"

class ConfigWizard(QWizard, Ui_STDMWizard):
    def __init__(self, parent):
        QWizard.__init__(self, parent)
        self.setupUi(self)
        self.register_fields()


        # directory path settings
        self.btnDocPath.clicked.connect(self.support_doc_path)
        self.btnDocOutput.clicked.connect(self.output_path)
        self.btnTemplates.clicked.connect(self.template_path)

        # profile
        self.cboProfile.currentIndexChanged.connect(self.profile_changed)

        self.btnNewP.clicked.connect(self.new_profile)
        self.btnPDelete.clicked.connect(self.delete_profile)
        
        # register enitity model to different view controllers
        self.entity_model = EntitiesModel()
        self.pftableView.setModel(self.entity_model)
        self.pftableView.setColumnWidth(0, 250)

        self.lvEntities.setModel(self.entity_model)	
        
        self.entity_item_model = self.lvEntities.selectionModel()

        self.entity_item_model.selectionChanged.connect(self.entity_changed)

        self.col_view_model = ColumnEntitiesModel()
        self.tbvColumns.setModel(self.col_view_model)
        
        self.cboParty.setModel(self.entity_model)
        self.cboSPUnit.setModel(self.entity_model)

        # STR view model
        self.party_item_model = STRColumnEntitiesModel()
        #self.lvParty.setModel(self.party_item_model)

        self.spunit_item_model = STRColumnEntitiesModel()
        #self.lvSpatialUnit.setModel(self.spunit_item_model)

        self.cboParty.currentIndexChanged.connect(self.party_changed)

        self.cboSPUnit.currentIndexChanged.connect(self.spatial_unit_changed)
        
        # profile page : Add entities
        self.btnNewEntity.clicked.connect(self.new_entity)
        self.btnEditEntity.clicked.connect(self.edit_entity)
        self.btnDeleteEntity.clicked.connect(self.delete_entity)

        # Entity customization
        self.btnAddColumn.clicked.connect(self.new_column)
        self.btnEditColumn.clicked.connect(self.edit_column)
        self.btnDeleteColumn.clicked.connect(self.delete_column)

        # lookup
        self.lookup_view_model = LookupEntitiesModel()
        self.lvLookups.setModel(self.lookup_view_model)

        self.btnAddLookup.clicked.connect(self.new_lookup)
        self.btnEditLookup.clicked.connect(self.edit_lookup)
        self.btnDeleteLookup.clicked.connect(self.delete_lookup)

        self.lookup_item_model = self.lvLookups.selectionModel()
        self.lookup_item_model.selectionChanged.connect(self.lookup_changed)

        # lookup values
        self.lookup_value_view_model = QStandardItemModel(self.lvLookupValues)
        self.btnAddLkupValue.clicked.connect(self.add_lookup_value)
        self.btnEditLkupValue.clicked.connect(self.edit_lookup_value)
        self.btnDeleteLkupValue.clicked.connect(self.delete_lookup_value)

        self.edtDocPath.setFocus()

        self.setStartId(0)

        self.is_config_done = False
        self.stdm_config = StdmConfiguration.instance()  
        self.stdm_config.profile_added.connect(self.cbo_add_profile)

        # if StdmConfiguration instance is not empty, load profiles
        if len(self.stdm_config.profiles) > 0:
            self.reload_profiles()

    def reload_profiles(self):
        """
        Read and load the profiles from StdmConfiguration instance
        """
        profiles = []
        for profile in self.stdm_config.profiles.values():
            for entity in profile.entities.values():
                self.connect_entity_signals(entity)
            profiles.append(profile.name)
        self.cbo_add_profiles(profiles)
        self.lvLookups.setCurrentIndex(self.lvLookups.model().index(0,0))
        self.lvEntities.setCurrentIndex(self.lvEntities.model().index(0,0))

    def connect_entity_signals(self, entity):
        entity.column_added.connect(self.add_column_item)
        entity.column_removed.connect(self.delete_column_item)

    def validate_str(self):
        if self.entity_model.rowCount() == 0:
            return False, "No entities for creating Social Tenure Relationship"

        if self.cboParty.currentIndex() == self.cboSPUnit.currentIndex():
            return False, "Party and Spatial Unit entities cannot be the same!"

        profile = self.current_profile()
        spatial_unit = profile.entity_by_name(unicode( \
                self.cboSPUnit.currentText()))

        if not spatial_unit.has_geometry_column():
            return False, "Spatial unit entity should have a geometry column!"

        return True, "Ok"

    def index_spatial_unit_table(self):
        for index, entity in enumerate(self.entity_model.entities().values()):
            if entity.has_geometry_column():
                return index
        return 0

    def validate_empty_lookups(self):
        """
        Verifys that all lookups in the current profile
        have values. Returns true if all have values else false
        rtype: bool
        """
        valid = True
        profile  = self.current_profile()
        if not profile:
            return valid
        for vl in profile.value_lists():
            if vl.is_empty():
                valid = False
                show_message("Lookup %s has no values" % vl.short_name)
                break
        return valid

    def fmt_path_str(self, path):
        """
        param path: string representing the windows path
        type path: str
        Returns a directory path string formatted in a unix format
        rtype: str
        """
        rpath = r''.join(unicode(path))
        return rpath.replace("\\", "/")


    def read_settings_path(self, reg_key, os_path):
        """
        param reg_key: Registry key where to read path setting
        type reg_key: str
        param os_path: os directory to use if the reg_key is not set
        type os_path: str
        Returns path settings from the registry or an os folder
        rtype: str
        """
        settings = QtCore.QSettings(REG_KEY, QtCore.QSettings.NativeFormat)
        try:
            if len(settings.value(reg_key).toString()) > 0:
                reg_doc_path = self.fmt_path_str(settings.value(reg_key).toString())
            else:
                reg_doc_path = None
        except:
            reg_doc_path = self.fmt_path_str(settings.value(reg_key))
            if reg_doc_path.title() == 'None' or reg_doc_path.strip()=='':
                reg_doc_path = None

        if reg_doc_path is not None:
            return reg_doc_path
        else:
            doc_path = os.path.expanduser('~')+os_path
            if not os.path.exists(doc_path):
                os.makedirs(doc_path) 
            return self.fmt_path_str(doc_path)

    def validateCurrentPage(self):
        validPage = True

        if self.currentId() == LIC_PAGE:
            doc_path = self.read_settings_path('documents', '/.stdm/documents/')
            self.edtDocPath.setText(doc_path)

            output_path = self.read_settings_path('outputs', 
                    '/.stdm/reports/outputs')
            self.edtOutputPath.setText(output_path)

            templates_path = self.read_settings_path('templates',
                    '/.stdm/reports/templates')
            self.edtTemplatePath.setText(templates_path)

            return validPage

        if self.currentId() == 3:
            self.party_changed(0)
            # get an entity with a geometry column
            idx = self.index_spatial_unit_table()
            self.cboSPUnit.setCurrentIndex(idx)
            self.spatial_unit_changed(idx)
            # verify that lookup entities have values
            validPage = self.validate_empty_lookups()
            return validPage

        if self.currentId() == 4:
            validPage, msg = self.validate_str()

            if validPage:
                profile = self.current_profile()
                party = profile.entity_by_name(unicode( \
                        self.cboParty.currentText()))
                spatial_unit = profile.entity_by_name(unicode( \
                        self.cboSPUnit.currentText()))

                profile.set_social_tenure_attr(SocialTenure.PARTY, party)
                profile.set_social_tenure_attr(SocialTenure.SPATIAL_UNIT, spatial_unit)
            else:
                show_message(QApplication.translate("Configuration Wizard", msg))

        if self.currentId() == 5: # FINAL_PAGE:
            # last page
            # commit config to DB
            config_updater = ConfigurationSchemaUpdater()

            config_updater.update_started.connect(self.config_update_started)
            config_updater.update_progress.connect(self.config_update_progress)
            config_updater.update_completed.connect(self.config_update_completed)

            config_updater.exec_()

            if self.is_config_done:
                # write config to a file
                config_path = os.path.expanduser('~')+'/.stdm/configuration.stc'
                cfs = ConfigurationFileSerializer(config_path)
                try:
                    cfs.save()
                except(ConfigurationException, IOError) as e:
                    show_message(QApplication.translate("Configuration Wizard", \
                            unicode(e)))
                    validPage = False
                
            if validPage:
                show_message(QApplication.translate("Configuration Wizard", \
                        "Configuration saved successfully."))

        return validPage

    def config_update_started(self):
        self.txtHtml.append("Config update started ...")

    def config_update_progress(self, info_id, msg):
        self.txtHtml.append(unicode(info_id)+" : "+msg)

    def config_update_completed(self, status):
        if status:
            self.txtHtml.append("Configuration updated successully.")
            self.is_config_done = True
        else:
            self.txtHtml.append("Failed to update configuration. Check error logs.")
            self.is_config_done = False

    def register_fields(self):
        self.setOption(self.HaveHelpButton, True)  
        page_count = self.page(1)
        page_count.registerField("Accept", self.rbAccpt)
        page_count.registerField("Reject", self.rbReject)

    def support_doc_path(self):
        try:
            dir_name = self.open_dir_chooser(QApplication.translate( \
                    "STDM Configuration", 
                    "Select a directory for supporting documents"), 
                    str(self.edtDocPath.text()))

            #dir_path = dir_name.first()
            
            self.edtDocPath.setText(dir_name)
        except:
            LOGGER.debug("Error setting support document path!")
            raise

    def output_path(self):
        try:
            dir_name = self.open_dir_chooser(QApplication.translate( \
                    "STDM Configuration",
                    "Select a directory for outputting generated documents"),
                    str(self.edtOutputPath.text()))

            #dir_path = dir_name.first()
            self.edtOutputPath.setText(dir_name)
        except:
            LOGGER.debug("Error setting support document path!")

    def template_path(self):
        try:
            dir_name = self.open_dir_chooser(QApplication.translate( \
                    "STDM Configuration",
                    "Select a directory for document templates"),
                    str(self.edtTemplatePath.text()))

            #dir_path = dir_name.first()
            self.edtTemplatePath.setText(dir_name)
        except:
            LOGGER.debug("Error setting support document path!")

    def open_dir_chooser(self, message, dir=None):
        sel_dir = str(QtGui.QFileDialog.getExistingDirectory(
                self, "Select Folder", ""))
        return sel_dir
        
        #dir_dlg = QFileDialog(self, message, dir)
        #dir_dlg.setFileMode(QFileDialog.Directory)
        #dir_dlg.setOption(QFileDialog.ShowDirsOnly, True)
        #if dir_dlg.exec_() == QDialog.Accepted:
            #sel_dir = dir_dlg.selectedFiles()
            #if len(sel_dir) > 0:
                #show_message(QApplication.translate("Configuration Wizard", \
                        #str(type(sel_dir)) ))
                #return sel_dir

    def add_entity_item(self, entity):
        """
        param entity: Instance of a new entity
        type entity: BaseColumn
        """
        if entity.TYPE_INFO not in ['SUPPORTING_DOCUMENT',
                    'SOCIAL_TENURE', 'ADMINISTRATIVE_SPATIAL_UNIT',
                    'ENTITY_SUPPORTING_DOCUMENT','VALUE_LIST', 'ASSOCIATION_ENTITY']:
            self.entity_model.add_entity(entity)

    def delete_entity_item(self, name):
        """
        param name: Name of entity to delete
        type name: str
        """
        items = self.entity_model.findItems(name)
        if len(items) > 0:
            self.entity_model.removeRow(items[0].row())

    def cbo_add_profile(self, profile):
        """
        param profile: List of profile to add in a combobox
        type profile: list
        """
        profiles = []
        profiles.append(profile.name)
        self.cboProfile.insertItems(0, profiles)
        self.cboProfile.setCurrentIndex(0)

    def cbo_add_profiles(self, profiles):
        """
        param profiles: list of profiles to add in the profile combobox
        type profiles: list
        """
        self.cboProfile.insertItems(0, profiles)
        self.cboProfile.setCurrentIndex(0)

    #PROFILE
    def new_profile(self):
        """
        Creates a new instance of a profile and adds it to the
        StdmConfiguration singleton
        """
        editor = ProfileEditor(self)
        result = editor.exec_()
        if result == 1:
            profile = self.stdm_config.create_profile(editor.profile_name)
            profile.entity_added.connect(self.add_entity_item)
            profile.entity_removed.connect(self.delete_entity_item)
            self.stdm_config.add_profile(profile)

    def current_profile(self):
        """
        Returns an instance of the selected profile in the 
        profile combobox
        rtype: Profile
        """
        profile = None
        prof_name = self.cboProfile.currentText()
        if len(prof_name) > 0:
            profile = self.stdm_config.profile(unicode(prof_name))
        return profile

    def delete_profile(self):
        """
        Delete the current selected profile
        """
        if self.cboProfile.count() == 1:
            show_message(QApplication.translate("Configuration Wizard", \
                    "Cannot delete last profile!"))
            return

        profile_name = self.cboProfile.currentText()
        if not self.stdm_config.remove_profile(profile_name):
            show_message(QApplication.translate("Configuration Wizard", \
                    "Unable to delete profile!"))
            return
        self.set_profile_cbo()

    def get_profiles(self):
        profiles = []
        for profile in self.stdm_config.profiles.items():
                profiles.append(profile[0])

        return profiles

    def set_profile_cbo(self):
        profiles = self.get_profiles()
        self.cboProfile.clear()
        self.cboProfile.insertItems(0, profiles)
        self.cboProfile.setCurrentIndex(0)

    def add_column_item(self, column):
        print "Column added triggered...."
        self.col_view_model.add_entity(column)
        self.party_item_model.add_entity(column)
        self.spunit_item_model.add_entity(column)

    def delete_column_item(self, name):
        model_item, column, row_id = self.get_model_entity(self.tbvColumns)
        self.col_view_model.delete_entity(column)
        self.col_view_model.removeRow(row_id)
        self.party_item_model.removeRow(row_id)
        self.spunit_item_model.removeRow(row_id)

    def new_entity(self):
        """
        Creates a new entity and adds it to the current profile
        """
        profile = self.current_profile()
        if profile:
            editor = EntityEditor(self, profile)
            editor.exec_()
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No profile selected to add entity!"))

    def edit_entity(self):
        """
        Edit selected entity
        """
        if len(self.pftableView.selectedIndexes())==0:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No entity selected for edit!"))
            return
        model_item, entity, row_id = self.get_model_entity(self.pftableView)
        if model_item:
            profile = self.current_profile()
            editor = EntityEditor(self, profile, entity)
            result = editor.exec_()
            if result == 1:
                model_item.delete_entity(entity)
                model_item.removeRow(row_id)

    def delete_entity(self):
        """
        Delete selected entity
        """
        if len(self.pftableView.selectedIndexes())==0:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No entity selected for deletion!"))
            return

        model_item, entity, row_id = self.get_model_entity(self.pftableView)
        if model_item:
            model_item.delete_entity(entity)
            # delete entity from selected profile
            profile = self.current_profile()
            profile.remove_entity(entity.short_name)
            model_item.removeRow(row_id)

    def clear_view_model(self, view_model):
        rows = view_model.rowCount()
        for i in range(rows):
            view_model.removeRow(i)
        view_model.clear()

    def set_view_model(self, view_model):
        self.pftableView.setModel(view_model)
        self.lvEntities.setModel(view_model)
        self.cboParty.setModel(view_model)
        self.cboSPUnit.setModel(view_model)

    def populate_view_model(self, profile):
        for entity in profile.entities.values():
            # if item is "deleted", don't show it
            if entity.action == DbItem.DROP:
                continue

            if entity.TYPE_INFO not in ['SUPPORTING_DOCUMENT',
                    'SOCIAL_TENURE', 'ADMINISTRATIVE_SPATIAL_UNIT',
                    'ENTITY_SUPPORTING_DOCUMENT']:

                if entity.TYPE_INFO == 'VALUE_LIST':
                    self.lookup_view_model.add_entity(entity)
                    self.addValues_byEntity(entity)
                else:
                    self.entity_model.add_entity(entity)

    def connect_signals(self):
        self.entity_item_model = self.lvEntities.selectionModel()
        self.entity_item_model.selectionChanged.connect(self.entity_changed)

        self.lookup_item_model = self.lvLookups.selectionModel()
        self.lookup_item_model.selectionChanged.connect(self.lookup_changed)

        self.cboParty.currentIndexChanged.emit(self.cboParty.currentIndex())
        self.cboSPUnit.currentIndexChanged.emit(self.cboSPUnit.currentIndex())

    def switch_profile(self, name):
        profile = self.stdm_config.profile(unicode(name))  #profiles.values()[sel_id]

        # clear view models
        self.clear_view_model(self.entity_model)
        self.clear_view_model(self.col_view_model)
        self.clear_view_model(self.lookup_view_model)
        self.clear_view_model(self.lookup_value_view_model)
        self.clear_view_model(self.party_item_model)
        self.clear_view_model(self.spunit_item_model)

        self.entity_model = EntitiesModel()
        self.set_view_model(self.entity_model)

        self.col_view_model = ColumnEntitiesModel()
        self.tbvColumns.setModel(self.col_view_model)

        self.lookup_view_model = LookupEntitiesModel()
        self.lvLookups.setModel(self.lookup_view_model)
        self.lvLookupValues.setModel(self.lookup_value_view_model)

        # from profile entities to view_model
        self.populate_view_model(profile)

        self.connect_signals()

    def profile_changed(self, row_id):
        self.switch_profile(self.cboProfile.currentText())
		
    def _create_ent(self, profile, entity_name):
        entity = profile.create_entity(entity_name, entity_factory)
        self.connect_entity_signals(entity)
        profile.add_entity(entity)

    def get_model_entity(self, view):
        sel_id = -1
        entity = None
        model_item = view.currentIndex().model()
        if model_item:
            sel_id = view.currentIndex().row()
            entity = model_item.entities().items()[sel_id][1]

        return (model_item, entity, sel_id)

		
    def addColumns(self, v_model, columns):
        """
        param v_model: Instance of EntitiesModel
        type v_model: EntitiesModel
        param columns: List of column names to insert in v_model
        type columns: list
        """
        for column in columns:
            if column.user_editable():
                v_model.add_entity(column)

    def entity_changed(self, selected, diselected):
        """
        triggered when you select an entity, clears an existing column entity
        model and create a new one.
        Get the columns of the selected entity, add them to the newly created
        column entity model
        """
        row_id = self.entity_item_model.currentIndex().row()
        if row_id > -1:
            view_model = self.entity_item_model.currentIndex().model()
            self.col_view_model.clear()
            self.col_view_model = ColumnEntitiesModel()

            columns = view_model.entity_byId(row_id).columns.values()
            self.addColumns(self.col_view_model, columns)

            self.tbvColumns.setModel(self.col_view_model)

    def party_changed(self, row_id):
        cbo_model = self.cboParty.model()
        try:
            columns = cbo_model.entity_byId(row_id).columns.values()
            self.party_item_model.clear()
            self.party_item_model = STRColumnEntitiesModel()
            self.addColumns(self.party_item_model, columns)
            #self.lvParty.setModel(self.party_item_model)
        except:
            pass

    def spatial_unit_changed(self, row_id):
        cbo_model = self.cboSPUnit.model()
        try:
            columns = cbo_model.entity_byId(row_id).columns.values()
            self.spunit_item_model.clear()
            self.spunit_item_model = STRColumnEntitiesModel()
            self.addColumns(self.spunit_item_model, columns)
            #self.lvSpatialUnit.setModel(self.spunit_item_model)
        except:
            pass

    def _make_column(self, id, col_name, entity):
        '''
        Helper function
        '''
        col = BaseColumn.registered_types.values()[id](col_name, entity)
        return col

    def new_column(self):
        if len(self.lvEntities.selectedIndexes())==0:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No entity selected to add column!"))
            return
        model_item, entity, row_id = self.get_model_entity(self.lvEntities)
        if model_item:
            profile = self.current_profile()

            params={}
            params['entity']=entity
            params['profile']=profile
            editor = ColumnEditor(self, **params)
            result = editor.exec_()
            if result == 1:
                if editor.type_info == 'LOOKUP':
                    self.clear_lookup_view()
                    self.populate_lookup_view(profile)

    def edit_column(self):
        """
        Edit selected column.
        Allow editting of columns that have not yet being persisted on the DB
        """
        rid, column = self._get_column(self.tbvColumns)
        
        if column and column.action == DbItem.CREATE:
            row_id, entity = self._get_entity(self.lvEntities)

            params = {}
            params['column'] = column
            params['entity'] = entity
            params['profile'] = self.current_profile()
            
            editor = ColumnEditor(self, **params)
            result = editor.exec_()
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No column selected for edit!"))

    def clear_lookup_view(self):
        self.clear_view_model(self.lookup_view_model)
        self.lookup_view_model = LookupEntitiesModel()
        self.lvLookups.setModel(self.lookup_view_model)
        self.lookup_item_model = self.lvLookups.selectionModel()
        self.lookup_item_model.selectionChanged.connect(self.lookup_changed)
        
    def populate_lookup_view(self, profile):
        for entity in profile.entities.values():
            # if item is "deleted", don't show it
            if entity.action == DbItem.DROP:
                continue
            if entity.TYPE_INFO == 'VALUE_LIST':
                self.lookup_view_model.add_entity(entity)
                self.addValues_byEntity(entity)

    def _get_entity_item(self, view):
        model_item, entity, row_id = self.get_model_entity(view)
        if model_item:
            entity_item = model_item.entities().values()[row_id]
            return row_id, entity_item

    def _get_column(self, view):
        model_item, entity, row_id = self.get_model_entity(view)
        row_id = -1
        column = None
        if model_item:
            column = model_item.entities().values()[row_id]
        return row_id, column

    def _get_entity(self, view):
        model_item, entity, row_id = self.get_model_entity(view)
        if entity:
            return row_id, entity

    def delete_column(self):
        row_id, column = self._get_column(self.tbvColumns)
        if column:
            ent_id, entity = self._get_entity(self.lvEntities)
            # delete from the entity
            entity.remove_column(column.name)
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No column selected for deletion!"))
	
    def new_lookup(self):
        profile = self.current_profile()
        if profile:
            editor = LookupEditor(self, profile)
            result = editor.exec_()
            if result == 1:
                self.lookup_view_model.add_entity(editor.lookup)
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No profile selected to add lookup!"))

    def new_lookup_test(self):
        profile = self.current_profile()
        if profile:
            gender_lookup = profile.create_entity('gender', value_list_factory)
            mstatus = profile.create_entity('marital status', value_list_factory)

            profile.add_entity(gender_lookup)
            profile.add_entity(mstatus)

            self.lookup_view_model.add_entity(gender_lookup)
            self.lookup_view_model.add_entity(mstatus)

    def edit_lookup(self):
        profile = self.current_profile()
        if profile:
            if len(self.lvLookups.selectedIndexes()) > 0:
                row_id, lookup = self._get_entity_item(self.lvLookups)
                editor = LookupEditor(self, profile, lookup)
                result = editor.exec_()
                if result == 1:
                    self.lookup_view_model.removeRow(row_id)
                    self.lookup_view_model.add_entity(editor.lookup)
            else:
                show_message(QApplication.translate("Configuration Wizard", \
                        "No lookup selected for edit!"))
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "Nothing to edit!"))

    def delete_lookup(self):
        profile = self.current_profile()
        if profile:
            if len(self.lvLookups.selectedIndexes()) > 0:
                row_id, lookup = self._get_entity_item(self.lvLookups)
                profile.remove_entity(lookup.short_name)
                self.lookup_view_model.removeRow(row_id)
            else:
                show_message(QApplication.translate("Configuration Wizard", \
                        "No lookup selected for deletion!"))
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "Nothing to delete!"))

    def addValues_byEntity(self, entity):
        for v in entity.values:
            cv = entity.code_value(v)
            if cv.updated_value == '':
                txt = cv.value
            else:
                txt = cv.updated_value

            val = QStandardItem(txt)
            self.lookup_value_view_model.appendRow(val)

    def add_values(self, values):
        self.lookup_value_view_model.clear()
        for v in values:
            val = QStandardItem(v.value)
            self.lookup_value_view_model.appendRow(val)
                 
    def add_lookup_value_test(self):
        row_id, lookup = self._get_entity_item(self.lvLookups)
        # check lookup <> None
        lookup.add_code_value(CodeValue('M','Male'))
        lookup.add_code_value(CodeValue('F','Female'))
        self.addValues(lookup.Values())
        self.lvLookupValues.setModel(self.lookup_value_view_model)

    def lookup_changed(self, selected, diselected):
        row_id = self.lookup_item_model.currentIndex().row()
        if row_id == -1:
            return
        view_model = self.lookup_item_model.currentIndex().model()
        self.lookup_value_view_model.clear()
        self.addValues_byEntity(view_model.entity_byId(row_id))
        self.lvLookupValues.setModel(self.lookup_value_view_model)

    def add_lookup_value(self):
        if len(self.lvLookups.selectedIndexes()) == 0:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No lookup selected to add value!"))
            return

        row_id, lookup = self._get_entity_item(self.lvLookups)
        if lookup:
            value_editor = ValueEditor(self, lookup)
            result = value_editor.exec_()
            if result == 1:
                self.add_values(value_editor.lookup.values.values())
                self.lvLookupValues.setModel(self.lookup_value_view_model)

    def edit_lookup_value(self):
        if len(self.lvLookupValues.selectedIndexes() ) == 0:
            show_message(QApplication.translate("Configuration Wizard", \
                    "No value selected for edit!"))
            return
        # get selected lookup value
        model_index = self.lvLookupValues.selectedIndexes()[0]
        value_text = self.lookup_value_view_model.itemFromIndex(model_index).text()

        # get selected lookup
        row_id, lookup = self._get_entity_item(self.lvLookups)
        lookup_view_model = self.lookup_item_model.currentIndex().model().entity_byId(row_id)

        code_value = lookup_view_model.values[unicode(value_text)]

        value_editor = ValueEditor(self, lookup, code_value)
        result = value_editor.exec_()
        if result == 1:
            self.addValues(value_editor.lookup.Values())

        #new_value = 'Alien'
        #if self.lookup_item_model.currentIndex().model().entity_byId(row_id).rename(unicode(value_text), new_value):
        #self.lookup_value_view_model.itemFromIndex(model_index).setText(new_value)
        #cv = self.lookup_item_model.currentIndex().model().entity_byId(row_id).code_value(unicode(value_text))
        else:
            show_message(QApplication.translate("Configuration Wizard", \
                    "Select value to edit"))

    def delete_lookup_value(self):
        if len(self.lvLookupValues.selectedIndexes() ) == 0:
            show_message(QApplication.translate("Configuration Wizard", \
                    "Select value to delete"))
            return

        row_id, lookup = self._get_entity_item(self.lvLookups)
        model_index = self.lvLookupValues.selectedIndexes()[0]
        value_text = self.lookup_value_view_model.itemFromIndex(model_index).text()
        lookup.remove_value(unicode(value_text))
        self.addValues(lookup.Values())
        print "Value removed ...."

    def edit_lookup_value_test(self):
        if len(self.lvLookupValues.selectedIndexes() ) > 0:
            # get selected lookup value
            model_index = self.lvLookupValues.selectedIndexes()[0]
            value_text = self.lookup_value_view_model.itemFromIndex(model_index).text()

            # get selected lookup
            row_id = self.lookup_item_model.currentIndex().row()
            #lookup_view_model = self.lookup_item_model.currentIndex().model()

            new_value = 'Alien'

            if self.lookup_item_model.currentIndex().model().entity_byId(row_id).rename(unicode(value_text), new_value):
                self.lookup_value_view_model.itemFromIndex(model_index).setText(new_value)
                cv = self.lookup_item_model.currentIndex().model().entity_byId(row_id).code_value(unicode(value_text))

    def get_str_columns(self, item_model):
        return [item_model.item(row) for row in range(item_model.rowCount()) \
                if item_model.item(row).checkState()==Qt.Checked]

class Launcher(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.create_main_frame()

    def create_main_frame(self):
        page = QWidget()
        self.button = QPushButton('Wizard', page)
        self.setCentralWidget(page)
        self.button.clicked.connect(self.open_wizard)

    def open_wizard(self):
        window = QWidget()
        configWiz = ConfigWizard(window)
        configWiz.exec_()

def show_message(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(QApplication.translate("STDM Configuration Wizard","STDM"))
    msg.setText(QApplication.translate("STDM Configuration Wizard",message))
    msg.exec_()

def createLogger():
    # create console handler and set level to debug
    ch = logging.FileHandler("stdm.log")
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    LOGGER.addHandler(ch)

def start_gui():
    print "starting graphical user interface ..."
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    app.exec_()

    #window = QWidget()
    #configWiz = ConfigWizard(window)
    #configWiz.exec_()

def start_cli():
    print "starting command line interface ..."
    import sys
    createLogger()
    app = QApplication(sys.argv)
    window = QWidget()
    cw = ConfigWizard(window)

    # create profiles
    cw.new_profile()

    # print profiles
    print "profiles ..."
    for profile in cw.stdm_config.profiles.items():
        print profile

    # get first profile
    profile = cw.stdm_config.profiles['test']

    print "current profile ...", profile

    # create entities
    ent_name = "Party"
    cw._create_ent(profile, ent_name)

    ent_name = "Spatial"
    cw._create_ent(profile, ent_name)

    # print entities
    print "Entities ..."
    for entity in profile.entities.items():
        print entity

    fk_entity = profile.entities['Spatial']
    fk_editor = ColumnEditor(cw, fk_entity, profile)
    fk_editor.type_info = 'BIGINT'
    attrs = {'colname':'FK_parent_col', 'index':True, 'unique':True}
    fk_editor.attributes(**attrs)
    fk_column = fk_editor.create_column()

    print 
    print ">"*100
    for k, v in fk_column.__dict__.iteritems():
        print k, v

    print "<"*100

    fk_editor.entity.add_column(fk_column)

    # get a "party" entity
    entity = profile.entities['Party']
    editor = ColumnEditor(cw, entity, profile)
    editor.run_test()

    #print BaseColumn.registered_types.values()

    editor.type_info = 'VARCHAR'
    attrs = {'maximum':80, 'value':'varchar_column','colname':'name'}
    editor.attributes(**attrs)
    column = editor.create_column()
    editor.entity.add_column(column)

    editor.type_info = 'VARCHAR'
    attrs = {'maximum':15, 'value':'','colname':'code'}
    editor.attributes(**attrs)
    column = editor.create_column()
    editor.entity.add_column(column)

    editor.type_info = 'GEOMETRY'
    attrs = {'srid':102022, 'geom_type':1,'colname':'geoloc'}
    editor.attributes(**attrs)
    column = editor.create_column()
    print
    print ">>> Geometry Type / projection <<< "
    print column.geometry_type(), "/", column.projection()
    print

    editor.entity.add_column(column)

    editor.type_info = 'BIGINT'
    attrs = {'colname':'regnum'}
    editor.attributes(**attrs)
    child_col = editor.create_column()
    editor.entity.add_column(child_col)

    print "CHILD: ", child_col

    editor.type_info = 'FOREIGN_KEY'
    er = {'parent':profile.entities['Spatial'], 'parent_column':fk_column, 
            'child':entity, 'child_column':child_col,
            'display_columns':['id', 'name']}
    entity_relation = EntityRelation(profile, **er)

    attrs = {'colname':'rent', 'entity_relation': entity_relation}
    editor.attributes(**attrs)
    
    column = editor.create_column()
    editor.entity.add_column(column)

    print editor.entity.columns
    return editor

if __name__=='__main__':
    import sys

    editor = None

    createLogger()

    if len(sys.argv) > 1:
        if sys.argv[1]=='cli':
            start_cli()
        else:
            start_gui()
    else:
        start_gui()
