# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dtime_property.ui'
#
# Created: Sun Feb 21 12:25:21 2016
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

class Ui_DTimeProperty(object):
    def setupUi(self, DTimeProperty):
        DTimeProperty.setObjectName(_fromUtf8("DTimeProperty"))
        DTimeProperty.resize(246, 106)
        self.buttonBox = QtGui.QDialogButtonBox(DTimeProperty)
        self.buttonBox.setGeometry(QtCore.QRect(70, 80, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.edtMinDTime = QtGui.QDateTimeEdit(DTimeProperty)
        self.edtMinDTime.setGeometry(QtCore.QRect(95, 10, 130, 20))
        self.edtMinDTime.setCalendarPopup(True)
        self.edtMinDTime.setObjectName(_fromUtf8("edtMinDTime"))
        self.edtMaxDTime = QtGui.QDateTimeEdit(DTimeProperty)
        self.edtMaxDTime.setGeometry(QtCore.QRect(95, 42, 130, 20))
        self.edtMaxDTime.setCalendarPopup(True)
        self.edtMaxDTime.setObjectName(_fromUtf8("edtMaxDTime"))
        self.label_2 = QtGui.QLabel(DTimeProperty)
        self.label_2.setGeometry(QtCore.QRect(20, 42, 69, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(DTimeProperty)
        self.label.setGeometry(QtCore.QRect(20, 10, 65, 16))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(DTimeProperty)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DTimeProperty.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DTimeProperty.reject)
        QtCore.QMetaObject.connectSlotsByName(DTimeProperty)

    def retranslateUi(self, DTimeProperty):
        DTimeProperty.setWindowTitle(_translate("DTimeProperty", "Datetime properties", None))
        self.label_2.setText(_translate("DTimeProperty", "Maximum date", None))
        self.label.setText(_translate("DTimeProperty", "Minimum date", None))

