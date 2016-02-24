# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : create_lookup
Description          : Create new lookup entities
Date                 : 02/January/2016
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

from ui_lookup_entity import Ui_dlgLookup
from PyQt4.QtCore import *
from PyQt4.QtGui import (
		QDialog, 
		QApplication, 
		QMessageBox
		)

#from stdm.data import (
		#writeTable, 
		#renameTable,
		#inheritTableColumn, 
		#writeTableColumn,
		#writeLookup,
		#checktableExist,
		#ConfigTableReader, 
		#table_column_exist
		#)

#from stdm.data.config_utils import setUniversalCode

from stdm.data.configuration.entity import *
from stdm.data.configuration.value_list import ValueList, CodeValue, value_list_factory

class LookupEditor(QDialog, Ui_dlgLookup):
    def __init__(self, parent, profile):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.initGui()

	self.profile = profile
	#self.form_parent = parent
	self.lookup = None

    def initGui(self):
	    self.edtName.setFocus()
	
    def format_lookup_name(self, name):
	    formatted_name = str(name).strip()
	    formatted_name = formatted_name.replace(' ', "_")
	    return formatted_name.lower()
    
    def add_lookup(self):
  	    self.lookup = self.profile.create_entity(self.format_lookup_name(unicode(self.edtName.text())), value_list_factory)
    	    self.profile.add_entity(self.lookup)
	    #self.form_parent.lookup_view_model.add_entity(lookup)
	    
    def accept(self):
	    if self.edtName.text()=='':
		    self.ErrorInfoMessage(QApplication.translate("LookupEditor","Lookup name is not given!"))
		    return

            self.add_lookup()
	    
	    self.done(1)

    def reject(self):
	    self.done(0)
    
    def ErrorInfoMessage(self, Message):
        # Error Message Box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("STDM")
        msg.setText(Message)
        msg.exec_()  
