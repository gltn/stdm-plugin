# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rptLayout.ui'
#
# Created: Tue Nov 15 08:55:21 2011
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmRptLayout(object):
    def setupUi(self, frmRptLayout):
        frmRptLayout.setObjectName(_fromUtf8("frmRptLayout"))
        frmRptLayout.resize(345, 328)
        self.gridLayout = QtGui.QGridLayout(frmRptLayout)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(frmRptLayout)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 325, 308))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.cboPageSize = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.cboPageSize.setObjectName(_fromUtf8("cboPageSize"))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.cboPageSize.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cboPageSize)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.cboPageOrien = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.cboPageOrien.setObjectName(_fromUtf8("cboPageOrien"))
        self.cboPageOrien.addItem(_fromUtf8(""))
        self.cboPageOrien.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cboPageOrien)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.txtTopMargin = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtTopMargin.setMaxLength(10)
        self.txtTopMargin.setObjectName(_fromUtf8("txtTopMargin"))
        self.verticalLayout.addWidget(self.txtTopMargin)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.txtBtMargin = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtBtMargin.setMaxLength(10)
        self.txtBtMargin.setObjectName(_fromUtf8("txtBtMargin"))
        self.verticalLayout.addWidget(self.txtBtMargin)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.txtLeftMargin = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtLeftMargin.setMaxLength(10)
        self.txtLeftMargin.setObjectName(_fromUtf8("txtLeftMargin"))
        self.verticalLayout.addWidget(self.txtLeftMargin)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.txtRightMargin = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtRightMargin.setMaxLength(10)
        self.txtRightMargin.setObjectName(_fromUtf8("txtRightMargin"))
        self.verticalLayout.addWidget(self.txtRightMargin)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(frmRptLayout)
        QtCore.QMetaObject.connectSlotsByName(frmRptLayout)

    def retranslateUi(self, frmRptLayout):
        frmRptLayout.setWindowTitle(QtGui.QApplication.translate("frmRptLayout", "Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmRptLayout", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(0, QtGui.QApplication.translate("frmRptLayout", "A0", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(1, QtGui.QApplication.translate("frmRptLayout", "A1", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(2, QtGui.QApplication.translate("frmRptLayout", "A2", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(3, QtGui.QApplication.translate("frmRptLayout", "A3", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(4, QtGui.QApplication.translate("frmRptLayout", "A4", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(5, QtGui.QApplication.translate("frmRptLayout", "A5", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(6, QtGui.QApplication.translate("frmRptLayout", "A6", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(7, QtGui.QApplication.translate("frmRptLayout", "LETTER", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(8, QtGui.QApplication.translate("frmRptLayout", "LEGAL", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(9, QtGui.QApplication.translate("frmRptLayout", "B0", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(10, QtGui.QApplication.translate("frmRptLayout", "B1", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(11, QtGui.QApplication.translate("frmRptLayout", "B2", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(12, QtGui.QApplication.translate("frmRptLayout", "B3", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(13, QtGui.QApplication.translate("frmRptLayout", "B4", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(14, QtGui.QApplication.translate("frmRptLayout", "B5", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageSize.setItemText(15, QtGui.QApplication.translate("frmRptLayout", "B6", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmRptLayout", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageOrien.setItemText(0, QtGui.QApplication.translate("frmRptLayout", "Potrait", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPageOrien.setItemText(1, QtGui.QApplication.translate("frmRptLayout", "Landscape", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmRptLayout", "Top Margin (cm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmRptLayout", "Bottom Margin (cm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmRptLayout", "Left Margin (cm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmRptLayout", "Right Margin (cm)", None, QtGui.QApplication.UnicodeUTF8))

