# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_third_examination.ui'
#
# Created: Sat Jul  6 21:38:10 2019
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_ThirdExam_Wzd(object):
    def setupUi(self, ThirdExam_Wzd):
        ThirdExam_Wzd.setObjectName(_fromUtf8("ThirdExam_Wzd"))
        ThirdExam_Wzd.resize(638, 725)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.gridLayout = QtGui.QGridLayout(self.wizardPage2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title_frame_2 = QtGui.QFrame(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame_2.sizePolicy().hasHeightForWidth())
        self.title_frame_2.setSizePolicy(sizePolicy)
        self.title_frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.title_frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.title_frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.title_frame_2.setObjectName(_fromUtf8("title_frame_2"))
        self.title_label_2 = QtGui.QLabel(self.title_frame_2)
        self.title_label_2.setGeometry(QtCore.QRect(10, 0, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_label_2.setFont(font)
        self.title_label_2.setObjectName(_fromUtf8("title_label_2"))
        self.subtitle_label_2 = QtGui.QLabel(self.title_frame_2)
        self.subtitle_label_2.setGeometry(QtCore.QRect(10, 20, 331, 16))
        self.subtitle_label_2.setObjectName(_fromUtf8("subtitle_label_2"))
        self.gridLayout.addWidget(self.title_frame_2, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 210))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.layoutPlan_frame = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutPlan_frame.sizePolicy().hasHeightForWidth())
        self.layoutPlan_frame.setSizePolicy(sizePolicy)
        self.layoutPlan_frame.setMinimumSize(QtCore.QSize(0, 400))
        self.layoutPlan_frame.setFrameShape(QtGui.QFrame.Box)
        self.layoutPlan_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.layoutPlan_frame.setObjectName(_fromUtf8("layoutPlan_frame"))
        self.gridLayout_2.addWidget(self.layoutPlan_frame, 1, 0, 1, 1)
        self.landHoldPlan_frame = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.landHoldPlan_frame.sizePolicy().hasHeightForWidth())
        self.landHoldPlan_frame.setSizePolicy(sizePolicy)
        self.landHoldPlan_frame.setMinimumSize(QtCore.QSize(0, 400))
        self.landHoldPlan_frame.setFrameShape(QtGui.QFrame.Box)
        self.landHoldPlan_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.landHoldPlan_frame.setObjectName(_fromUtf8("landHoldPlan_frame"))
        self.gridLayout_2.addWidget(self.landHoldPlan_frame, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkBox = QtGui.QCheckBox(self.frame_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_5.addWidget(self.checkBox, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_5.addWidget(self.pushButton, 3, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_5.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_5.addWidget(self.textEdit, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        ThirdExam_Wzd.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.gridLayout_4 = QtGui.QGridLayout(self.wizardPage)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.title_frame_3 = QtGui.QFrame(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame_3.sizePolicy().hasHeightForWidth())
        self.title_frame_3.setSizePolicy(sizePolicy)
        self.title_frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.title_frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.title_frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.title_frame_3.setObjectName(_fromUtf8("title_frame_3"))
        self.title_label_3 = QtGui.QLabel(self.title_frame_3)
        self.title_label_3.setGeometry(QtCore.QRect(10, 0, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_label_3.setFont(font)
        self.title_label_3.setObjectName(_fromUtf8("title_label_3"))
        self.subtitle_label_3 = QtGui.QLabel(self.title_frame_3)
        self.subtitle_label_3.setGeometry(QtCore.QRect(10, 20, 311, 16))
        self.subtitle_label_3.setObjectName(_fromUtf8("subtitle_label_3"))
        self.gridLayout_4.addWidget(self.title_frame_3, 0, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.wizardPage)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.treeView = QtGui.QTreeView(self.frame_4)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout_3.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.wizardPage)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)
        ThirdExam_Wzd.addPage(self.wizardPage)

        self.retranslateUi(ThirdExam_Wzd)
        QtCore.QMetaObject.connectSlotsByName(ThirdExam_Wzd)

    def retranslateUi(self, ThirdExam_Wzd):
        ThirdExam_Wzd.setWindowTitle(_translate("ThirdExam_Wzd", "Third Examination", None))
        self.title_label_2.setText(_translate("ThirdExam_Wzd", "Validation", None))
        self.subtitle_label_2.setText(_translate("ThirdExam_Wzd", "This screen enables comparisons of layout plan and land hold plan ", None))
        self.label_2.setText(_translate("ThirdExam_Wzd", "Layout Plan", None))
        self.label_7.setText(_translate("ThirdExam_Wzd", "Land Hold Plan", None))
        self.checkBox.setText(_translate("ThirdExam_Wzd", "Approve", None))
        self.pushButton.setText(_translate("ThirdExam_Wzd", "Finish", None))
        self.checkBox_2.setText(_translate("ThirdExam_Wzd", "Disapprove with comments below", None))
        self.label_6.setText(_translate("ThirdExam_Wzd", "Click Next to proceed to examination ", None))
        self.title_label_3.setText(_translate("ThirdExam_Wzd", "Summary", None))
        self.subtitle_label_3.setText(_translate("ThirdExam_Wzd", "Below is an output of the examination process.", None))
        self.label_8.setText(_translate("ThirdExam_Wzd", "Confirm the details. Click finish if details are ok or go back to previous steps to edit", None))

