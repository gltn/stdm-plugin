# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_import_data.ui'
#
# Created: Wed Mar 09 08:33:57 2022
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmImport(object):
    def setupUi(self, frmImport):
        frmImport.setObjectName(_fromUtf8("frmImport"))
        frmImport.resize(690, 596)
        frmImport.setModal(False)
        frmImport.setWizardStyle(QtGui.QWizard.ModernStyle)
        frmImport.setOptions(QtGui.QWizard.HelpButtonOnRight)
        self.pgSource = QtGui.QWizardPage()
        self.pgSource.setObjectName(_fromUtf8("pgSource"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pgSource)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.pgSource)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.txtDataSource = QtGui.QLineEdit(self.groupBox)
        self.txtDataSource.setMaxLength(200)
        self.txtDataSource.setObjectName(_fromUtf8("txtDataSource"))
        self.horizontalLayout_2.addWidget(self.txtDataSource)
        self.btnBrowseSource = QtGui.QPushButton(self.groupBox)
        self.btnBrowseSource.setObjectName(_fromUtf8("btnBrowseSource"))
        self.horizontalLayout_2.addWidget(self.btnBrowseSource)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.pgSource)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbTextType = QtGui.QRadioButton(self.groupBox_2)
        self.rbTextType.setChecked(True)
        self.rbTextType.setObjectName(_fromUtf8("rbTextType"))
        self.horizontalLayout.addWidget(self.rbTextType)
        self.rbSpType = QtGui.QRadioButton(self.groupBox_2)
        self.rbSpType.setObjectName(_fromUtf8("rbSpType"))
        self.horizontalLayout.addWidget(self.rbSpType)
        self.rbKoboMedia = QtGui.QRadioButton(self.groupBox_2)
        self.rbKoboMedia.setObjectName(_fromUtf8("rbKoboMedia"))
        self.horizontalLayout.addWidget(self.rbKoboMedia)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gbKobo = QtGui.QGroupBox(self.pgSource)
        self.gbKobo.setObjectName(_fromUtf8("gbKobo"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gbKobo)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_6 = QtGui.QLabel(self.gbKobo)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        self.edtMediaUrl = QtGui.QLineEdit(self.gbKobo)
        self.edtMediaUrl.setReadOnly(False)
        self.edtMediaUrl.setObjectName(_fromUtf8("edtMediaUrl"))
        self.gridLayout_4.addWidget(self.edtMediaUrl, 0, 1, 1, 1)
        self.edtKoboUsername = QtGui.QLineEdit(self.gbKobo)
        self.edtKoboUsername.setReadOnly(False)
        self.edtKoboUsername.setObjectName(_fromUtf8("edtKoboUsername"))
        self.gridLayout_4.addWidget(self.edtKoboUsername, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gbKobo)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.edtKoboPassword = QtGui.QLineEdit(self.gbKobo)
        self.edtKoboPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.edtKoboPassword.setObjectName(_fromUtf8("edtKoboPassword"))
        self.gridLayout_4.addWidget(self.edtKoboPassword, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gbKobo)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.cbSaveCredit = QtGui.QCheckBox(self.gbKobo)
        self.cbSaveCredit.setObjectName(_fromUtf8("cbSaveCredit"))
        self.gridLayout_4.addWidget(self.cbSaveCredit, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.gbKobo)
        frmImport.addPage(self.pgSource)
        self.destTable = QtGui.QWizardPage()
        self.destTable.setObjectName(_fromUtf8("destTable"))
        self.gridLayout_2 = QtGui.QGridLayout(self.destTable)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.destTable)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lstDestTables = QtGui.QListWidget(self.groupBox_3)
        self.lstDestTables.setObjectName(_fromUtf8("lstDestTables"))
        self.gridLayout.addWidget(self.lstDestTables, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.destTable)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.geomClm = QtGui.QComboBox(self.groupBox_4)
        self.geomClm.setEnabled(False)
        self.geomClm.setMinimumSize(QtCore.QSize(100, 0))
        self.geomClm.setMaximumSize(QtCore.QSize(100, 16777215))
        self.geomClm.setObjectName(_fromUtf8("geomClm"))
        self.gridLayout_5.addWidget(self.geomClm, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 4, 0, 1, 1)
        self.rbAppend = QtGui.QRadioButton(self.groupBox_4)
        self.rbAppend.setChecked(True)
        self.rbAppend.setObjectName(_fromUtf8("rbAppend"))
        self.gridLayout_5.addWidget(self.rbAppend, 1, 0, 1, 1)
        self.rbOverwrite = QtGui.QRadioButton(self.groupBox_4)
        self.rbOverwrite.setObjectName(_fromUtf8("rbOverwrite"))
        self.gridLayout_5.addWidget(self.rbOverwrite, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)
        frmImport.addPage(self.destTable)
        self.assignColumns = QtGui.QWizardPage()
        self.assignColumns.setObjectName(_fromUtf8("assignColumns"))
        self.gridLayout_3 = QtGui.QGridLayout(self.assignColumns)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.assignColumns)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnSrcUp = QtGui.QPushButton(self.groupBox_5)
        self.btnSrcUp.setMinimumSize(QtCore.QSize(0, 0))
        self.btnSrcUp.setMaximumSize(QtCore.QSize(33, 16777215))
        self.btnSrcUp.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSrcUp.setIcon(icon)
        self.btnSrcUp.setObjectName(_fromUtf8("btnSrcUp"))
        self.verticalLayout_2.addWidget(self.btnSrcUp)
        self.btnSrcDown = QtGui.QPushButton(self.groupBox_5)
        self.btnSrcDown.setMaximumSize(QtCore.QSize(33, 16777215))
        self.btnSrcDown.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSrcDown.setIcon(icon1)
        self.btnSrcDown.setObjectName(_fromUtf8("btnSrcDown"))
        self.verticalLayout_2.addWidget(self.btnSrcDown)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lstSrcFields = QtGui.QListWidget(self.groupBox_5)
        self.lstSrcFields.setMinimumSize(QtCore.QSize(0, 250))
        self.lstSrcFields.setProperty("showDropIndicator", True)
        self.lstSrcFields.setDragEnabled(True)
        self.lstSrcFields.setDragDropOverwriteMode(True)
        self.lstSrcFields.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lstSrcFields.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lstSrcFields.setAlternatingRowColors(True)
        self.lstSrcFields.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lstSrcFields.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lstSrcFields.setObjectName(_fromUtf8("lstSrcFields"))
        self.verticalLayout_3.addWidget(self.lstSrcFields)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnSrcAll = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSrcAll.sizePolicy().hasHeightForWidth())
        self.btnSrcAll.setSizePolicy(sizePolicy)
        self.btnSrcAll.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSrcAll.setObjectName(_fromUtf8("btnSrcAll"))
        self.horizontalLayout_3.addWidget(self.btnSrcAll)
        self.btnSrcNone = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSrcNone.sizePolicy().hasHeightForWidth())
        self.btnSrcNone.setSizePolicy(sizePolicy)
        self.btnSrcNone.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSrcNone.setObjectName(_fromUtf8("btnSrcNone"))
        self.horizontalLayout_3.addWidget(self.btnSrcNone)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.assignColumns)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lstTargetFields = QtGui.QListWidget(self.groupBox_6)
        self.lstTargetFields.setMinimumSize(QtCore.QSize(0, 250))
        self.lstTargetFields.setProperty("showDropIndicator", True)
        self.lstTargetFields.setDragEnabled(True)
        self.lstTargetFields.setDragDropOverwriteMode(True)
        self.lstTargetFields.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lstTargetFields.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lstTargetFields.setAlternatingRowColors(True)
        self.lstTargetFields.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lstTargetFields.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lstTargetFields.setObjectName(_fromUtf8("lstTargetFields"))
        self.verticalLayout_5.addWidget(self.lstTargetFields)
        self.chk_virtual = QtGui.QCheckBox(self.groupBox_6)
        self.chk_virtual.setObjectName(_fromUtf8("chk_virtual"))
        self.verticalLayout_5.addWidget(self.chk_virtual)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_6)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.btn_add_translator = QtGui.QToolButton(self.groupBox_6)
        self.btn_add_translator.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_add_translator.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_translator.setIcon(icon2)
        self.btn_add_translator.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.btn_add_translator.setObjectName(_fromUtf8("btn_add_translator"))
        self.horizontalLayout_5.addWidget(self.btn_add_translator)
        self.btn_edit_translator = QtGui.QToolButton(self.groupBox_6)
        self.btn_edit_translator.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_edit_translator.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_translator.setIcon(icon3)
        self.btn_edit_translator.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.btn_edit_translator.setObjectName(_fromUtf8("btn_edit_translator"))
        self.horizontalLayout_5.addWidget(self.btn_edit_translator)
        self.btn_delete_translator = QtGui.QToolButton(self.groupBox_6)
        self.btn_delete_translator.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_delete_translator.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete_translator.setIcon(icon4)
        self.btn_delete_translator.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.btn_delete_translator.setObjectName(_fromUtf8("btn_delete_translator"))
        self.horizontalLayout_5.addWidget(self.btn_delete_translator)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.btnDestUp = QtGui.QPushButton(self.groupBox_6)
        self.btnDestUp.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnDestUp.setText(_fromUtf8(""))
        self.btnDestUp.setIcon(icon)
        self.btnDestUp.setObjectName(_fromUtf8("btnDestUp"))
        self.verticalLayout_4.addWidget(self.btnDestUp)
        self.btnDestDown = QtGui.QPushButton(self.groupBox_6)
        self.btnDestDown.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnDestDown.setText(_fromUtf8(""))
        self.btnDestDown.setIcon(icon1)
        self.btnDestDown.setObjectName(_fromUtf8("btnDestDown"))
        self.verticalLayout_4.addWidget(self.btnDestDown)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 1, 1, 1)
        frmImport.addPage(self.assignColumns)

        self.retranslateUi(frmImport)
        QtCore.QMetaObject.connectSlotsByName(frmImport)

    def retranslateUi(self, frmImport):
        frmImport.setWindowTitle(_translate("frmImport", "Import to STDM", None))
        self.pgSource.setTitle(_translate("frmImport", "Source Data", None))
        self.pgSource.setSubTitle(_translate("frmImport", "Specify the location of the source file and representative data type.", None))
        self.groupBox.setTitle(_translate("frmImport", "Source:", None))
        self.label.setText(_translate("frmImport", "Dataset", None))
        self.btnBrowseSource.setText(_translate("frmImport", "Browse", None))
        self.groupBox_2.setTitle(_translate("frmImport", "Destination Repository Type:", None))
        self.rbTextType.setText(_translate("frmImport", "Textual Data", None))
        self.rbSpType.setText(_translate("frmImport", "Spatial Data", None))
        self.rbKoboMedia.setText(_translate("frmImport", "Kobo Images", None))
        self.gbKobo.setTitle(_translate("frmImport", "Kobo Settings", None))
        self.label_6.setText(_translate("frmImport", "Kobo Password:", None))
        self.label_4.setText(_translate("frmImport", "Media URL:", None))
        self.label_5.setText(_translate("frmImport", "Kobo Username:", None))
        self.cbSaveCredit.setText(_translate("frmImport", "Save Credentials", None))
        self.destTable.setTitle(_translate("frmImport", "Copy Table", None))
        self.destTable.setSubTitle(_translate("frmImport", "Destination table and import options.", None))
        self.groupBox_3.setTitle(_translate("frmImport", "Select Destination Table:", None))
        self.groupBox_4.setTitle(_translate("frmImport", "Options:", None))
        self.label_2.setText(_translate("frmImport", "Geometry Column:", None))
        self.rbAppend.setText(_translate("frmImport", "A&ppend Data", None))
        self.rbOverwrite.setText(_translate("frmImport", "&Overwrite Existing", None))
        self.assignColumns.setTitle(_translate("frmImport", "Assign Columns", None))
        self.assignColumns.setSubTitle(_translate("frmImport", "Match source and destination table columns.", None))
        self.groupBox_5.setTitle(_translate("frmImport", "Source Table:", None))
        self.btnSrcAll.setText(_translate("frmImport", "Select All", None))
        self.btnSrcNone.setText(_translate("frmImport", "Unsellect All", None))
        self.groupBox_6.setTitle(_translate("frmImport", "Destination Table:", None))
        self.lstTargetFields.setSortingEnabled(False)
        self.chk_virtual.setText(_translate("frmImport", "Show virtual columns", None))
        self.label_3.setText(_translate("frmImport", "Value translators:", None))
        self.btn_add_translator.setToolTip(_translate("frmImport", "Add value translator", None))
        self.btn_add_translator.setWhatsThis(_translate("frmImport", "<html><head/><body><p>Use value translators to transform the value from the corresponding source table column in order to adopt it to a format that adaptible to the destination column.</p></body></html>", None))
        self.btn_edit_translator.setToolTip(_translate("frmImport", "Edit value translator", None))
        self.btn_delete_translator.setToolTip(_translate("frmImport", "Delete value translator", None))

