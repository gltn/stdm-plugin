"""
/***************************************************************************
Name                 : New STR Wizard
Description          : Wizard that enables users to define a new social tenure
                       relationship.
Date                 : 3/July/2013
copyright            : (C) 2013 by John Gitau
email                : gkahiu@gmail.com
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
import logging
from collections import OrderedDict

from stdm.data.qtmodels import BaseSTDMTableModel
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sqlalchemy

from notification import NotificationBar, ERROR, INFO, WARNING
from sourcedocument import *

from stdm.data.database import (
    STDMDb,
    Base
)
from stdm.settings import (
    current_profile
)
from stdm.utils.util import (
    format_name,
    entity_display_columns,
    model_display_data
)
from stdm.data.configuration import entity_model

from stdm.navigation import (
    TreeSummaryLoader,
    WebSpatialLoader,
    GMAP_SATELLITE,
    OSM
)
from stdm.utils import *
from stdm.utils.util import (
    lookup_id_to_value
)
from ui_new_str import Ui_frmNewSTR

LOGGER = logging.getLogger('stdm')

class newSTRWiz(QWizard, Ui_frmNewSTR):
    """
    This class enable users choose party,
    spatial unit, social tenure, and supporting
    document to create a social tenure relationship.
    """
    def __init__(self, plugin):
        """
        Initializes the ui file, party, spatial unit, social
        tenure type, and supporting document pages.
        It also defines class properties.
        :param plugin: STDM plugin
        :type plugin: STDMQGISLoader
        :returns: None
        :rtype: NoneType
        """
        QWizard.__init__(self, plugin.iface.mainWindow())
        ## TODO when forms are done check if db insert
        ## TODO is ordered as shown
        ## TODO in party and str_type pages and each
        ## TODO party and str_type matches.
        ## TODO Use OrderDict if mismatch found
        self.setupUi(self)
        #STR Variables
        self.sel_party = []
        self.sel_spatial_unit = []
        self.sel_str_type = []
        self.row = 0 # number of party rows
        # Current profile instance and properties
        self.curr_profile = current_profile()

        self.party = self.curr_profile.social_tenure.party

        self.spatial_unit = self.curr_profile.social_tenure.spatial_unit

        self.str_type = self.curr_profile.\
            social_tenure.tenure_type_collection

        self.init_party()
        self.party_header = []

        self.init_spatial_unit()
        self.docs_tab_index = None
        self.docs_tab = None
        self.doc_types = None
        self.init_document_type()


        # Connect signal when the finish
        # button is clicked
        btnFinish = self.button(
            QWizard.FinishButton
        )

    def init_party(self):
        """
        Initialize the party page
        :returns:None
        :rtype: NoneType
        """
        self.party_notice = NotificationBar(self.vlPersonNotif)

        party_data = []
        vertical_layout = QVBoxLayout(
            self.tvPersonInfo
        )
        party_table = self.create_table(
            self.tvPersonInfo, vertical_layout
        )

        self.add_table_headers(
            self.party, party_data, party_table
        )

        self.AddPartybtn.clicked.connect(
            lambda: self.add_record(
                party_table, self.party, party_data
            )
        )

        self.AddPartybtn.clicked.connect(
            self.init_str_type
        )

        self.RemovePartybtn.clicked.connect(
            lambda: self.remove_row(
                party_table, self.party_notice
            )
        )

    def init_spatial_unit(self):
        """
        Initialize the spatial unit page.
        :returns: None
        :rtype: NoneType
        """
        self.spatial_unit_notice = NotificationBar(
            self.vlPropNotif
        )
        self.gpOLTitle = self.gpOpenLayers.title()
        
        # Flag for checking whether
        # OpenLayers base maps have been loaded
        self.olLoaded = False

        spatial_unit_data = []
        vertical_layout = QVBoxLayout(
            self.tvPropInfo
        )
        spatial_unit_table = self.create_table(
            self.tvPropInfo,
            vertical_layout
        )
        self.add_table_headers(
            self.spatial_unit,
            spatial_unit_data,
            spatial_unit_table
        )
        self.AddSpatialUnitbtn.clicked.connect(
            lambda: self.add_record(
                spatial_unit_table,
                self.spatial_unit,
                spatial_unit_data
            )
        )
        self.RemoveSpatialUnitbtn.clicked.connect(
            lambda: self.remove_row(
                spatial_unit_table, self.party_notice
            )
        )
        #Connect signals
        QObject.connect(
            self.gpOpenLayers,
            SIGNAL("toggled(bool)"),
            self.on_enable_ol_groupbox
        )
        QObject.connect(
            self.zoomSlider,
            SIGNAL("sliderReleased()"),
            self.on_zoom_changed
        )
        QObject.connect(
            self.btnResetMap,
            SIGNAL("clicked()"),
            self._onResetMap
        )
        
        #Start background thread
        self.propBrowser = WebSpatialLoader(
            self.propWebView, self
        )
        self.connect(
            self.propBrowser,
            SIGNAL("loadError(QString)"),
            self.on_property_browser_error
        )
        self.connect(
            self.propBrowser,
            SIGNAL("loadProgress(int)"),
            self.on_property_browser_loading
        )
        self.connect(
            self.propBrowser,
            SIGNAL("loadFinished(bool)"),
            self.on_property_browser_finished
        )
        self.connect(
            self.propBrowser,
            SIGNAL("zoomChanged(int)"),
            self.onMapZoomLevelChanged
        )

        #Connect signals
        QObject.connect(
            self.rbGMaps,
            SIGNAL("toggled(bool)"),
            self.onLoadGMaps
        )
        QObject.connect(
            self.rbOSM,
            SIGNAL("toggled(bool)"),
            self.onLoadOSM
        )

    def remove_row(self, table_view, notification):
        """
        A slot that removes a selected party or
        spatial unit record/row.
        :param table_view: The table view in which
            the row is removed.
        :type table_view: QTableView
        :param notification: The notification
        :type notification: NotificationBar object
        :returns: None
        :rtype: NoneType
        """
        if len(table_view.selectedIndexes()) > 0:
            row_index = table_view.selectedIndexes()[0]
            table_view.model().removeRow(
                row_index.row(), row_index
            )
            table_view.model().layoutChanged.emit()
            if notification == self.party_notice:
                self.remove_str_type(row_index.row())

        else:
            msg = QApplication.translate(
                        "newSTRWiz",
                        "Please select a row you"
                        " would like to remove. "
            )
            notification.clear()
            notification.insertNotification(msg, ERROR)


    def remove_str_type(self, row_position):
        """
        Removes corresponding social tenure type
        row when a party row is removed.
        :param row_position: Party row position that is removed.
        :type row_position: integer
        :returns: None
        :rtype: NoneType
        """
        # As there are two tableviews in str type page
        # due to an additional tableview for social
        # tenure type combo (FreezeTableWidget),
        # we have to multiply by 2 to get the correct
        # position of str_type row to be removed
        matching_table = row_position * 2
        for position, item in enumerate(
                self.frmWizSTRType.findChildren(QTableView)
        ):
            if item.__class__.__name__ == 'FreezeTableWidget':
                if position == matching_table:
                    self.verticalLayout_11.removeWidget(item)
                    item.deleteLater()


    def initializePage(self, id):
        """
        Initialize summary page based on user
        selections.
        :param id: the page id of the wizard
        :type id: QWizard id
        :returns: None
        :rtype: NoneType
        """
        if id == 5:
            self.buildSummary()

    def create_table(self, parent, container):
        """
        Creates an empty QTableView in party and
        spatial unit pages.
        :param parent: The parent of the tableview
        :type parent: QWidget
        :param container: The layout that holds the parent
        :type parent: QVBoxLayout
        :returns: QTableView
        :rtype: QTableView
        """
        table_view = QTableView()

        table_view.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        table_view.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        table_view.setAlternatingRowColors(True)

        container.setSpacing(4)
        container.setMargin(5)
        grid_layout = QGridLayout(parent)
        grid_layout.setHorizontalSpacing(5)
        grid_layout.setColumnStretch(4, 5)
        container.addLayout(grid_layout)
        container.addWidget(table_view)
        # For reduce the height for spatial unit
        if parent == self.tvPropInfo:
            table_view.setMinimumSize(QSize(55, 30))
            table_view.setMaximumSize(QSize(5550, 75))
        return table_view

    def create_str_type_table(
            self, parent, container, table_data, headers
    ):
        """
        Creates social tenure type table that is composed
        of each selected party rows with a combobox for
        social tenure type.
        :param parent:  The parent of the tableview
        :type parent: QWidget
        :param container: The layout that holds the parent
        :type container: QVBoxLayout
        :param table_data: The table data that is composed
            of the added party record. It is empty when
            the method is called. But gets populated inside
            the model.
        :type table_data: List
        :param headers: Header of the tableview
        :type headers: List
        :return: QTableView
        :rtype: QTableView
        """
        table_view = FreezeTableWidget(
            table_data, headers, parent
        )
        table_view.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        table_view.SelectionMode(
            QAbstractItemView.NoSelection
        )
        container.setSpacing(4)
        container.setMargin(5)
        grid_layout = QGridLayout(parent)
        grid_layout.setHorizontalSpacing(5)
        grid_layout.setColumnStretch(4, 5)
        container.addLayout(grid_layout)
        container.addWidget(table_view)

        return table_view

    def update_table_view(self, table_view, str_type):
        """
        Updates a tableview by resizing row and headers
        to content size and by hiding id columns
        :param table_view: The table view to be updated.
        :type table_view: QTableView
        :param str_type: A boolean that sets if it is
        for str type table or not.
        :type str_type: Boolean
        :return: None
        :rtype: NoneType
        """
        # show grid
        table_view.setShowGrid(True)
        # set column width to fit contents
        table_view.resizeColumnsToContents()
        # set row height
        table_view.resizeRowsToContents()
        # enable sorting
        table_view.setSortingEnabled(False)
        if str_type:
            table_view.hideColumn(1)
        else:
            table_view.hideColumn(0)

    def prepare_table_model(
            self, tableview, table_data, headers, parent
    ):
        table_model = BaseSTDMTableModel(
            table_data, headers, parent
        )
        tableview.setModel(table_model)

        tableview.horizontalHeader().setResizeMode(
            QHeaderView.Interactive
        )
        tableview.verticalHeader().setVisible(True)

    def add_table_headers(
            self, entity, table_data, tableview, str_type=False
    ):
        """
        Adds headers data for tableview columns. The
        headers comes from the selected entity.
        :param entity: The entity for which the table
        header is created for.
        :type entity: Entity Object
        :param table_data: The table data of the table view.
        :type table_data: List
        :param tableview: The tableview in which the header
        is added in.
        :type tableview: QTableView
        :param str_type: A boolean whether the header is for
        str_type or not.
        :type str_type: Boolean
        :return: List of Table headers
        :rtype: List
        """
        db_model = entity_model(entity, True)
        headers = []
        #Load headers
        if db_model is not None:
            entity_display_columns(self.party)
            # Append str type if the method is used for str_type
            if str_type:
                #First (ID) column will always be hidden
                headers.append('Social Tenure Type')

            for col in entity_display_columns(entity):
                headers.append(format_name(col))
            if not str_type:
                self.prepare_table_model(
                    tableview, table_data, headers, self
                )
        if entity == self.party:
            self.party_header = headers

        if str_type:
            return headers
        else:
            self.update_table_view(tableview, str_type)

    def add_record(
            self, table_view, entity, table_data, str_type=False
    ):
        """

        :param table_view:
        :type table_view:
        :param entity:
        :type entity:
        :param table_data:
        :type table_data:
        :param str_type:
        :type str_type:
        :return:
        :rtype:
        """
        data = OrderedDict()
        db_model = entity_model(entity, True)
        db_obj = db_model()

        if str_type:
            data['social_tenure_type'] = None

        for col in entity_display_columns(entity):
            attr = getattr(db_model, col)

            value = db_obj.queryObject([attr]).all()
            if len(value) > 0:
                value = value[0][0]
            else:
                return
            # change id to value if lookup, else return the same value
            value = lookup_id_to_value(
                self.curr_profile, col, value
            )
            data[col] = value
        if entity == self.spatial_unit:
            if table_view.model().rowCount() > 0:
                table_view.model().rowCount(0)
                table_view.model().removeRow(0)

        table_data.append(data.values())
        # Get the id and set it to self.sel_spatial_unit
        # so that it can be previewed on the map under
        # the preview tab.
        if entity == self.spatial_unit:
            spatial_unit_id = self.get_spatial_unit_data()
            self.set_record_to_model(
                self.spatial_unit, spatial_unit_id
            )
        table_view.model().layoutChanged.emit()
        self.update_table_view(table_view, str_type)


    def get_table_data(self, table_view, str_type=True):
        """
        Gets the data from a table_view.
        :param table_view: The table view from when
        the data is pulled.
        :type table_view: QTableView
        :param str_type: A boolean whether the header is for
        str_type or not.
        :type str_type: Boolean
        :return: A list containing a list of ids of
        the selected str related table or str_type value.
        :rtype: List
        """
        model = table_view.model()
        table_data = []


        if str_type:
            str_type_idx = model.index(0, 0)
            party_id_idx = model.index(0, 1)

            if model.data(
                party_id_idx, Qt.DisplayRole
            ) is not None:
                table_data.append(model.data(
                    party_id_idx, Qt.DisplayRole
                ))
                table_data.append(model.data(
                    str_type_idx, Qt.DisplayRole
                ))
        else:
            spatial_unit_idx = model.index(0, 0)
            table_data.append(model.data(
                spatial_unit_idx, Qt.DisplayRole
            ))

        return table_data

    def get_party_str_type_data(self):
        """
        Gets party and str_type data from str_type
        page (page 3 of the wizard). It uses
        get_table_data() method.
        :return: A list containing a list of ids of
        the selected str related table or str_type value.
        :rtype: List
        """
        str_types = []
        party_ids = []

        for item in self.frmWizSTRType.findChildren(QTableView):
            if item.__class__.__name__ == 'FreezeTableWidget':

                if len(self.get_table_data(item)) > 0:
                    party_id, str_type = self.get_table_data(item)
                    party_ids.append(party_id)
                    str_types.append(str_type)

        return party_ids, str_types

    def get_spatial_unit_data(self):
        """
        Gets spatial unit data from spatial unit
        page (page 2 of the wizard). It uses
        get_table_data() method.
        :return: A list containing a list of ids of
        spatial units select.
        :rtype: List
        """
        spatial_unit_id = None
        for item in self.tvPropInfo.findChildren(QTableView):
            if item is not None:
                spatial_unit_id = self.get_table_data(item, False)
                break

        return spatial_unit_id

    def set_record_to_model(self, entity, sel_attr):
        """
        Sets selected record data to model and stores it as
        a list model.
        :param entity: The entity from which the model is created.
        :type entity: Entity object
        :param sel_attr: List of selected records that is the
        return from get_spatial_unit_data() or
        get_party_str_type_data()
        :type sel_attr: List
        :return: None
        :rtype: NoneType
        """
        db_model = entity_model(entity, True)
        db_obj = db_model()
        if entity == self.party:
            self.sel_party = []
            for sel_id in sel_attr:
                party_query = db_obj.queryObject(
                    entity_display_columns(entity)
                ).filter(
                db_model.id == sel_id
                ).first()
                self.sel_party.append(party_query)

        if entity == self.spatial_unit:
            self.sel_spatial_unit = []
            spatial_unit_query = db_obj.queryObject().filter(
            db_model.id == sel_attr[0]
            ).first()
            self.sel_spatial_unit.append(spatial_unit_query)

        if entity == self.str_type:
            self.sel_str_type = []

            for sel_value in sel_attr:
                str_query = db_obj.queryObject().filter(
                    db_model.value == sel_value
                ).all()

                sel_str_type_id = getattr(
                    str_query[0],
                    'id',
                    None
                )
                self.sel_str_type.append(sel_str_type_id)

    def init_str_type(self):
        """
        Initialize 'Social Tenure Type page.
        :return: None
        :rtype: NoteType
        """
        party_data = []
        headers = self.add_table_headers(
            self.party,
            party_data,
            None,
            True
        )
        party_table = self.create_str_type_table(
            self.STRTypeWidget,
            self.verticalLayout_11,
            party_data,
            headers
        )

        self.add_record(
            party_table,
            self.party,
            party_data,
            True
        )

        self.notifSTR = NotificationBar(
            self.vlSTRTypeNotif
        )

    def init_document_type(self):
        """
        Initializes the document type combobox by
        populating data.
        :return: None
        :rtype: NoneType
        """
        self.sourceDocManager = SourceDocumentManager()
        doc_entity = self.curr_profile.social_tenure.\
            supporting_doc.document_type_entity

        doc_type_model = entity_model(doc_entity)

        Docs = doc_type_model()
        doc_type_list = Docs.queryObject().all()
        self.doc_types = [(doc.id, doc.value) for doc in doc_type_list]
        self.doc_types = OrderedDict(self.doc_types)
        self.docs_tab = QTabWidget()
        self.docs_tab_index = OrderedDict()

        for i, (id, doc) in enumerate(self.doc_types.iteritems()):
            self.docs_tab_index[doc] = i
            tabWidget = QWidget()
            tabWidget.setObjectName(doc)
            tab_layout = QVBoxLayout()
            tabWidget.setLayout(tab_layout)
            self.docs_tab.addTab(tabWidget, doc)
            self.cboDocType.addItem(doc, id)
        self.vlDocTitleDeed.addWidget(self.docs_tab, 1)

        # self.cboDocType.setCurrentIndex(-1)
        self.vlSourceDocNotif = NotificationBar(
            self.vlSourceDocNotif
        )

        self.cboDocType.currentIndexChanged.connect(
            self.match_doc_combo_to_tab
        )
        self.docs_tab.currentChanged.connect(
            self.match_doc_tab_to_combo
        )
        self.initSourceDocument()
        self.cboDocType.currentIndexChanged.connect(
            self.initSourceDocument
        )
        self.btnAddTitleDeed.clicked.connect(
            self.onUploadTitleDeed
        )

    def match_doc_combo_to_tab(self):

        combo_text = self.cboDocType.currentText()
        if combo_text is not None and len(combo_text) > 0:
            index = self.docs_tab_index[combo_text]
            self.docs_tab.setCurrentIndex(index)

    def match_doc_tab_to_combo(self):
        doc_tab_index = self.docs_tab.currentIndex()
        self.cboDocType.setCurrentIndex(doc_tab_index)

    def initSourceDocument(self):
        """
        Initialize the supporting document page.
        :return: None
        :rtype: NoneType
        """
        doc_text = self.cboDocType.currentText()
        cbo_index = self.cboDocType.currentIndex()
        doc_id = self.cboDocType.itemData(cbo_index)

        widget = self.docs_tab.findChild(QWidget, doc_text)
        layout = widget.findChild(QVBoxLayout)

        self.sourceDocManager.registerContainer(
            layout, doc_id
        )

    def onUploadTitleDeed(self):
        '''
        Slot raised when the user clicks
        to upload a title deed
        '''
        titleStr = QApplication.translate(
            "newSTRWiz",
            "Specify the Document File Location"
        )
        titles = self.selectSourceDocumentDialog(titleStr)

        cbo_index = self.cboDocType.currentIndex()
        doc_id = self.cboDocType.itemData(cbo_index)

        for title in titles:
            self.sourceDocManager.insertDocumentFromFile(
                title,
                doc_id,
                self.curr_profile.social_tenure
            )

    def selectSourceDocumentDialog(self, title):
        '''
        Displays a file dialog for a user
        to specify a source document
        '''
        files = QFileDialog.getOpenFileNames(
            self, title, "/home", "Source "
                                  "Documents (*.jpg *.jpeg *.png *.bmp *.tiff *.svg)"
        )
        return files

    def uploadDocument(self, path, containerid):
        '''
        Upload source document
        '''
        self.sourceDocManager.insertDocumentFromFile(
            path, containerid, self.curr_profile.social_tenure
        )

    def buildSummary(self):
        """
        Display summary information in the tree view.
        :return: None
        :rtype: NoneType
        """
        summaryTreeLoader = TreeSummaryLoader(self.twSTRSummary)

        sel_party, sel_str_types = self.get_party_str_type_data()
        # Add each str type next to each party.
        for q_obj, item in zip(self.sel_party, sel_str_types):
            party_mapping = model_display_data(
                q_obj, self.party, self.curr_profile
            )

            summaryTreeLoader.addCollection(
                party_mapping,
                QApplication.translate(
                    "newSTRWiz","Party Information"),
                ":/plugins/stdm/images/icons/user.png"
            )

            str_mapping = self.map_str_type(item)
            summaryTreeLoader.addCollection(
                str_mapping,
                QApplication.translate(
                    "newSTRWiz",
                    "Social Tenure Relationship Information"),
                ":/plugins/stdm/images/icons/social_tenure.png"
            )

        for q_obj in self.sel_spatial_unit:
            spatial_unit_mapping = model_display_data(
                q_obj, self.spatial_unit, self.curr_profile
            )

            summaryTreeLoader.addCollection(
                spatial_unit_mapping,
                QApplication.translate(
                    "newSTRWiz", "Spatial Unit Information"),
                ":/plugins/stdm/images/icons/property.png"
            )

        #Check the source documents based on the type of property
        srcDocMapping = self.sourceDocManager.attributeMapping()

        summaryTreeLoader.addCollection(
            srcDocMapping,
            QApplication.translate(
                "newSTRWiz","Source Documents"),
            ":/plugins/stdm/images/icons/attachment.png"
        )
      
        summaryTreeLoader.display()  

    def validateCurrentPage(self):
        """
        Validate the current page before
        proceeding to the next one and gets and 
        sets data from each page so that it can be used
        in on_create_str.
        :return: None
        :rtype: NoneType
        """
        isValid = True
        currPageIndex = self.currentId()       
        
        #Validate person information
        if currPageIndex == 1:

            if self.get_party_str_type_data() is not None:
                party_ids, str_type = self.get_party_str_type_data()
                if len(party_ids) > 0:
                    self.set_record_to_model(self.party, party_ids)

            if len(self.sel_party) == 0:
                msg = QApplication.translate(
                    "newSTRWiz",
                    "Please choose a person for whom you are "
                    "defining the social tenure relationship for."
                )

                self.party_notice.clear()
                self.party_notice.insertNotification(msg, ERROR)
                isValid = False

        #Validate property information
        if currPageIndex == 2:

            if len(self.sel_spatial_unit) == 0:
                msg = QApplication.translate(
                    "newSTRWiz",
                    "Please specify the spatial unit to reference. "
                    "Use the filter capability below."
                )
                self.spatial_unit_notice.clear()
                self.spatial_unit_notice.insertNotification(
                    msg, ERROR
                )
                isValid = False
        #Validate STR Type
        if currPageIndex == 3:
            #Get current selected index
            str_types = []
            if self.get_party_str_type_data() is not None:
                party_ids, str_types = self.get_party_str_type_data()


            if None in str_types or ' ' in str_types or len(str_types) < 1:
                msg = QApplication.translate(
                    'newSTRWiz',
                    'Please select an item in the drop down '
                    'menu under each Social Tenure Type column.'
                )
                self.notifSTR.clear()
                self.notifSTR.insertErrorNotification(msg)
                isValid = False
            if isValid != False:
                self.set_record_to_model(
                    self.str_type, str_types
                )
        #Validate source document    
        if currPageIndex == 4:

            currIndex = self.cboDocType.currentIndex()
            if currIndex ==-1:
                msg = QApplication.translate(
                    "newSTRWiz",
                    "Please select document type from the list"
                )
                self.notifSourceDoc.clear()
                self.notifSourceDoc.insertErrorNotification(msg)


        if currPageIndex == 5:
            isValid = self.on_create_str()
        return isValid
    
    def on_create_str(self):
        """
        Slot raised when the user clicks on Finish
        button in order to create a new STR entry.
        :return: None
        :rtype: NoneType
        """
        isValid = True

        #Create a progress dialog
        prog_dialog = QProgressDialog(self)
        prog_dialog.setWindowTitle(
            QApplication.translate(
                "newSTRWiz",
                "Creating New STR"
            )
        )


        str_model, str_doc_model = entity_model(
            self.curr_profile.social_tenure, False, True
        )
        _str_model_obj = str_model()
        #_str_doc_obj = str_doc_model()

        prog_dialog.setRange(
            0,
            len(self.sel_party)
        )
        prog_dialog.show()
        try:
            str_model_objs = []
            model_objs = self.sourceDocManager.model_objects(
                self.curr_profile.social_tenure
            )
            # Social tenure table insertion
            for i, (sel_party, str_type_id) in enumerate(
                    zip(self.sel_party, self.sel_str_type)
            ):
                str_obj = str_model(
                    party_id = sel_party.id,
                    spatial_unit_id = self.sel_spatial_unit[0].id,
                    tenure_type = str_type_id
                )

                prog_dialog.setValue(i)
                # Insert Supporting Document if there a
                # supporting document is uploaded.
                if len(model_objs) > 0:
                    # loop for each document type,
                    # model_obj is a model object for one document type.
                    for model_obj in model_objs:
                        # doc_obj stands for each file
                        # uploaded under a document type
                        for doc_obj in model_obj.keys():
                            str_obj.documents.append(doc_obj)

                str_model_objs.append(str_obj)
            _str_model_obj.saveMany(str_model_objs)

            strMsg = unicode(QApplication.translate(
                "newSTRWiz",
                "The social tenure relationship has "
                "been successfully created!"
            ))
            QMessageBox.information(
                self, QApplication.translate(
                    "newSTRWiz", "STR Creation"
                ),
                strMsg
            )

        # except sqlalchemy.exc.OperationalError as oe:
        #     errMsg = oe.message
        #     QMessageBox.critical(
        #         self,
        #         QApplication.translate(
        #             "newSTRWiz", "Unexpected Error"
        #         ),
        #         errMsg
        #     )
        #     prog_dialog.hide()
        #     isValid = False

        except sqlalchemy.exc.IntegrityError as ie:
            errMsg = ie.message
            QMessageBox.critical(
                self,
                QApplication.translate(
                    "newSTRWiz", "Duplicate Relationship Error"
                ),
                errMsg
            )
            prog_dialog.hide()
            isValid = False

        # except Exception as e:
        #     errMsg = str(e)
        #     QMessageBox.critical(
        #         self,
        #         QApplication.translate(
        #             'newSTRWiz','Unexpected Error'
        #         ),
        #         errMsg
        #     )
        #
        #     isValid = False
        finally:
            STDMDb.instance().session.rollback()
            prog_dialog.hide()

        return isValid

    def supporting_document_insert(self, str_model_objects, str_supp_doc_model, progress):
        """
        Checks if supporting document exists for the current profile.
        Inserts supporting document object into database, it exists.
        And disables the supporting document page if it doesn't.
        :param str_model_objects: Social tenure model object
        :type str_model_objects: SQL Alchemy object
        :return: None
        :rtype:
        """

        # str_supp_doc_model = entity_model(
        #     str_supp_doc_model
        # )
        str_supp_doc_model_obj = str_supp_doc_model()
        # social_tenure_relationship_supporting_document
        # save dict - for saveMany
        str_doc_objs = OrderedDict()
        # Check if supporting document exists for the profile
        # and disable the page, if it doesn't

        for obj in str_model_objects.keys():
            # model_objs is a list of list for each
            # document_type uploaded
            model_objs = self.sourceDocManager.model_objects(
                self.curr_profile.social_tenure.supporting_doc
            )

            if len(model_objs) > 0:
                # loop for each document type,
                # model_obj is an obj for one document type.
                for i, model_obj in enumerate(model_objs):
                    # doc_obj stands for each file
                    # uploaded under a document type
                    for doc_obj, doc_type_id in model_obj.iteritems():
                        # insert in supporting_document table
                        doc_obj.save()
                        str_doc_obj = str_supp_doc_model(
                            social_tenure_relationship_id=obj.id,
                            supporting_doc_id = doc_obj.id,
                            document_type=doc_type_id
                        )
                        # collect for saveMany
                        str_doc_objs[str_doc_obj] = str_doc_obj
                    progress.setValue(len(self.sel_party) + i + 1)
                # Insert in social_tenure_relationship_
                # supporting_document table
                str_supp_doc_model_obj.saveMany(
                    str_doc_objs.values()
                )

    def on_property_browser_error(self, err):
        """
        Slot raised when an error occurs when
        loading items in the property browser
        :param err: The error message to be displayed
        :type err: QString
        :return: None
        :rtype: NoneType
        """
        self.spatial_unit_notice.clear()
        self.spatial_unit_notice.insertNotification(
            err, ERROR
        )
        
    def on_property_browser_loading(self, progress):
        """
        Slot raised when the property browser is
        loading. Displays the progress of the
        page loading as a percentage.
        :param progress: load progress
        :type progress: Integer
        :return: None
        :rtype: NoneType
        """
        if progress <= 0 or progress >= 100:
            self.gpOpenLayers.setTitle(self.gpOLTitle)
        else:
            self.gpOpenLayers.setTitle(
                "%s (Loading...%s%%)"%(
                    str(self.gpOLTitle),
                    str(progress)
                )
            )
            
    def on_property_browser_finished(self, status):
        """
        Slot raised when the property browser
        finishes loading the content
        :param status: Boolean of the load status.
        :type status: Boolean
        :return: None
        :rtype: NoneType
        """
        if status:
            self.olLoaded = True
            self.overlayProperty()
        else:
            self.spatial_unit_notice.clear()
            msg = QApplication.translate(
                "newSTRWiz",
                "Error - The property map cannot be loaded."
            )
            self.spatial_unit_notice.insertErrorNotification(msg)
        
    def on_enable_ol_groupbox(self, state):
        """
        Slot raised when a user chooses to select
        the group box for enabling/disabling to view
        the property in OpenLayers.
        :param state: Boolean of the load status.
        :type state: Boolean
        :return: None
        :rtype: NoneType
        """
        if state:

            if len(self.sel_spatial_unit) < 1:
                self.spatial_unit_notice.clear()
                msg = QApplication.translate(
                    "newSTRWiz",
                    "You have to add a spatial unit record "
                    "in order to be able to preview it."
                )
                self.spatial_unit_notice.insertWarningNotification(msg)                
                self.gpOpenLayers.setChecked(False)
                return  
            
            #Load property overlay
            if not self.olLoaded:                
                self.propBrowser.load()            
                   
        else:
            #Remove overlay
            self.propBrowser.removeOverlay()     
            
    def on_zoom_changed(self):
        """
        Slot raised when the zoom value in the slider changes.
        This is only raised once the user
        releases the slider with the mouse.
        :return: None
        :rtype: NoneType
        """
        zoom = self.zoomSlider.value()        
        self.propBrowser.zoom_to_level(zoom)


    def map_str_type(self, item):
        """
        Loads the selected social tenure type into an
        ordered dictionary for the summary page treeview
        :param item: The social tenure type
        :type item: OrderedDict
        :return: 
        :rtype: 
        """
        str_mapping = OrderedDict()
        str_mapping[
            QApplication.translate(
                "newSTRWiz","Tenure Type"
            )
        ] = item
        return str_mapping

    def onLoadGMaps(self,state):
        '''
        Slot raised when a user clicks to set
        Google Maps Satellite as the base layer
        '''
        if state:                     
            self.propBrowser.setBaseLayer(
                GMAP_SATELLITE
            )
        
    def onLoadOSM(self,state):
        '''
        Slot raised when a user clicks to set
        OSM as the base layer
        '''
        if state:                     
            self.propBrowser.setBaseLayer(OSM)
            
    def onMapZoomLevelChanged(self,level):
        '''
        Slot which is raised when the zoom
        level of the map changes.
        '''
        self.zoomSlider.setValue(level)
       
    def _onResetMap(self):
        '''
        Slot raised when the user clicks
        to reset the property
        location in the map.
        '''
        self.propBrowser.zoom_to_extents()
       
    def overlayProperty(self):
        '''
        Overlay property boundaries on
        the basemap imagery
        '''
        geometry_col_name = [c.name for c in
            self.spatial_unit.columns.values()
            if c.TYPE_INFO == 'GEOMETRY'
        ]
        for geom in geometry_col_name:
            self.propBrowser.add_overlay(
                self.sel_spatial_unit[0], geom
            )


class ComboBoxDelegate(QItemDelegate):
    def __init__(self, parent = None):

        QItemDelegate.__init__(self, parent)
        self.row = 0
        self.curr_profile = current_profile()

    def str_type_combo (self):
        """
        A slot raised to add new str type
        matched with the party.
        :return: None
        """
        str_type_cbo = QComboBox()
        str_type_cbo.setObjectName(
            'STRTypeCbo'+str(self.row+1)
        )
        self.row = self.row + 1
        return str_type_cbo

    def str_type_set_data(self):
        str_lookup_obj = self.curr_profile.social_tenure.\
            tenure_type_collection
        str_types = entity_model(str_lookup_obj, True)
        str_type_obj = str_types()
        self.str_type_data = str_type_obj.queryObject().all()
        strType = [ids.value for ids in self.str_type_data]
        strType.insert(0, " ")
        return strType

    def createEditor(self, parent, option, index):
        str_combo = QComboBox(parent)
        str_combo.insertItems(
            0, self.str_type_set_data()
        )
        return str_combo

    def setEditorData( self, comboBox, index ):
        list_item_index = index.model().data(
            index, Qt.DisplayRole
        )
        if list_item_index is not None and \
                not isinstance(list_item_index, (unicode, int)):
            value = list_item_index.toInt()
            comboBox.setCurrentIndex(value[0])

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(
            index,
            editor.itemData(
            value, Qt.DisplayRole)
        )

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class FreezeTableWidget(QTableView):
    def __init__(
            self, table_data, headers, parent = None, *args
    ):
        QTableView.__init__(self, parent, *args)
        # set the table model
        table_model = BaseSTDMTableModel(
            table_data, headers, parent
        )
        # set the proxy model
        proxy_model = QSortFilterProxyModel(self)
        proxy_model.setSourceModel(table_model)

        # Assign a data model for TableView
        self.setModel(table_model)

        # frozen_table_view - first column
        self.frozen_table_view = QTableView(self)
        # Set the model for the widget, fixed column
        self.frozen_table_view.setModel(table_model)
        # Hide row headers
        self.frozen_table_view.verticalHeader().hide()
        # Widget does not accept focus
        self.frozen_table_view.setFocusPolicy(
            Qt.StrongFocus|Qt.TabFocus|Qt.ClickFocus
        )
        # The user can not resize columns
        self.frozen_table_view.horizontalHeader().\
            setResizeMode(QHeaderView.Fixed)
        # Style frozentable view
        self.frozen_table_view.setStyleSheet(
            '''
            border: none;
            background-color: #eee;
            selection-color: black;
            selection-background-color: #ddd;
            '''
        )
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(5)
        self.shadow.setOffset(2)
        self.shadow.setYOffset(0)
        self.frozen_table_view.setGraphicsEffect(self.shadow)

        # Remove the scroll bar
        self.frozen_table_view.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        self.frozen_table_view.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        # Puts more widgets to the foreground
        self.viewport().stackUnder(self.frozen_table_view)
        # # Log in to edit mode - even with one click
        # Set the properties of the column headings
        hh = self.horizontalHeader()
        # Text alignment centered
        hh.setDefaultAlignment(Qt.AlignCenter)

        # Set the width of columns by content
        self.resizeColumnsToContents()


        # Set the width of columns
        columns_count = table_model.columnCount(self)
        for col in xrange(columns_count):
            if col == 0:
                # Set the size
                self.horizontalHeader().resizeSection(
                    col, 60
                )
                # Fix width
                self.horizontalHeader().setResizeMode(
                    col, QHeaderView.Fixed
                )
                # Width of a fixed column - as in the main widget
                self.frozen_table_view.setColumnWidth(
                    col, self.columnWidth(col)
                )
            elif col == 1:
                self.horizontalHeader().resizeSection(
                    col, 150
                )
                self.horizontalHeader().setResizeMode(
                    col, QHeaderView.Fixed
                )
                self.frozen_table_view.setColumnWidth(
                    col, self.columnWidth(col)
                )
            else:
                self.horizontalHeader().resizeSection(
                    col, 100
                )
                # Hide unnecessary columns in the widget fixed columns
                self.frozen_table_view.setColumnHidden(
                    col, True
                )

        # Set properties header lines
        vh = self.verticalHeader()
        vh.setDefaultSectionSize(25) # height lines
        # text alignment centered
        vh.setDefaultAlignment(Qt.AlignCenter) 
        vh.setVisible(True)
        # Height of rows - as in the main widget
        self.frozen_table_view.verticalHeader().\
            setDefaultSectionSize(
            vh.defaultSectionSize()
        )

        # Show our optional widget
        self.frozen_table_view.show()
        # Set the size of him like the main
        self.update_frozen_table_geometry()

        self.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel
        )
        self.setVerticalScrollMode(
            QAbstractItemView.ScrollPerPixel
        )
        self.frozen_table_view.setVerticalScrollMode(
            QAbstractItemView.ScrollPerPixel
        )
        delegate = ComboBoxDelegate()

        # Set delegate to add combobox under
        # social tenure type column
        self.frozen_table_view.setItemDelegate(
            delegate
        )
        self.frozen_table_view.setItemDelegateForColumn(
            0, delegate
        )
        index = self.frozen_table_view.model().index(
            0, 0, QModelIndex()
        )
        self.frozen_table_view.model().setData(
            index, '', Qt.EditRole
        )

        self.frozen_table_view.setEditTriggers(
            QAbstractItemView.AllEditTriggers
        )
        size_policy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth()
        )
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(55, 75))
        self.setMaximumSize(QSize(5550, 75))
        self.setGeometry(QRect(0, 0, 619, 75))
        # set column width to fit contents
        self.frozen_table_view.resizeColumnsToContents()
        # set row height
        self.frozen_table_view.resizeRowsToContents()
        # Create a connection

        # Connect the headers and scrollbars of
        # both tableviews together
        self.horizontalHeader().sectionResized.connect(
            self.update_section_width
        )
        self.verticalHeader().sectionResized.connect(
            self.update_section_height
        )
        self.frozen_table_view.verticalScrollBar().\
            valueChanged.connect(
            self.verticalScrollBar().setValue
        )
        self.verticalScrollBar().valueChanged.connect(
            self.frozen_table_view.verticalScrollBar().setValue
        )

    def update_section_width(
            self, logicalIndex, oldSize, newSize
    ):
        if logicalIndex==0 or logicalIndex==1:
            self.frozen_table_view.setColumnWidth(
                logicalIndex, newSize
            )
            self.update_frozen_table_geometry()

    def update_section_height(
            self, logicalIndex, oldSize, newSize
    ):
        self.frozen_table_view.setRowHeight(
            logicalIndex, newSize
        )

    def resizeEvent(self, event):
        QTableView.resizeEvent(self, event)
        try:
            self.update_frozen_table_geometry()
        except Exception as log:
            print log

    def scrollTo(self, index, hint):
        if index.column() > 1:
            QTableView.scrollTo(self, index, hint)

    def update_frozen_table_geometry(self):
        if self.verticalHeader().isVisible():
            self.frozen_table_view.setGeometry(
                self.verticalHeader().width() +
                self.frameWidth(),
                self.frameWidth(),
                self.columnWidth(0) +
                self.columnWidth(1),
                self.viewport().height() +
                self.horizontalHeader().height()
            )
        else:
            self.frozen_table_view.setGeometry(
                self.frameWidth(),
                self.frameWidth(),
                self.columnWidth(0) + self.columnWidth(1),
                self.viewport().height() +
                self.horizontalHeader().height()
            )

    # move_cursor override function for correct
    # left to scroll the keyboard.
    def move_cursor(self, cursor_action, modifiers):
        current = QTableView.move_cursor(
            self, cursor_action, modifiers
        )
        if cursor_action == self.MoveLeft and current.column() > 1 and \
                        self.visualRect(current).topLeft().x() < \
                        (self.frozen_table_view.columnWidth(0) +
                             self.frozen_table_view.columnWidth(1)):
            new_value = self.horizontalScrollBar().value() + \
                       self.visualRect(current).topLeft().x() - \
                       (self.frozen_table_view.columnWidth(0) +
                        self.frozen_table_view.columnWidth(1))
            self.horizontalScrollBar().setValue(new_value)
        return current
