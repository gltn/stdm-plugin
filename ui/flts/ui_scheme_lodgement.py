# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scheme_lodgement.ui'
#
# Created: Sun Jul  7 12:35:28 2019
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

class Ui_LodgeScheme_Wzd(object):
    def setupUi(self, LodgeScheme_Wzd):
        LodgeScheme_Wzd.setObjectName(_fromUtf8("LodgeScheme_Wzd"))
        LodgeScheme_Wzd.setEnabled(True)
        LodgeScheme_Wzd.resize(763, 514)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LodgeScheme_Wzd.sizePolicy().hasHeightForWidth())
        LodgeScheme_Wzd.setSizePolicy(sizePolicy)
        LodgeScheme_Wzd.setMinimumSize(QtCore.QSize(410, 150))
        LodgeScheme_Wzd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        LodgeScheme_Wzd.setAcceptDrops(False)
        LodgeScheme_Wzd.setOptions(QtGui.QWizard.NoBackButtonOnStartPage)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.wizardPage1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.title_Label1 = QtGui.QLabel(self.wizardPage1)
        self.title_Label1.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_Label1.setFont(font)
        self.title_Label1.setObjectName(_fromUtf8("title_Label1"))
        self.gridLayout_2.addWidget(self.title_Label1, 0, 0, 1, 1)
        self.desc_Label1 = QtGui.QLabel(self.wizardPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_Label1.sizePolicy().hasHeightForWidth())
        self.desc_Label1.setSizePolicy(sizePolicy)
        self.desc_Label1.setObjectName(_fromUtf8("desc_Label1"))
        self.gridLayout_2.addWidget(self.desc_Label1, 1, 0, 1, 1)
        self.frame = QtGui.QFrame(self.wizardPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 200))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.wizardPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        LodgeScheme_Wzd.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.gridLayout = QtGui.QGridLayout(self.wizardPage2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_3 = QtGui.QFrame(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.desc_Label2 = QtGui.QLabel(self.frame_3)
        self.desc_Label2.setObjectName(_fromUtf8("desc_Label2"))
        self.horizontalLayout.addWidget(self.desc_Label2)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 2)
        self.holders_lineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.holders_lineEdit.setEnabled(True)
        self.holders_lineEdit.setObjectName(_fromUtf8("holders_lineEdit"))
        self.gridLayout.addWidget(self.holders_lineEdit, 2, 0, 1, 1)
        self.fileDisplay_textEdit = QtGui.QTextEdit(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDisplay_textEdit.sizePolicy().hasHeightForWidth())
        self.fileDisplay_textEdit.setSizePolicy(sizePolicy)
        self.fileDisplay_textEdit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.fileDisplay_textEdit.setObjectName(_fromUtf8("fileDisplay_textEdit"))
        self.gridLayout.addWidget(self.fileDisplay_textEdit, 4, 0, 1, 2)
        self.browse_pushBtn = QtGui.QPushButton(self.wizardPage2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../Downloads/firefox/search-folder-icon_1607739.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_pushBtn.setIcon(icon)
        self.browse_pushBtn.setDefault(True)
        self.browse_pushBtn.setObjectName(_fromUtf8("browse_pushBtn"))
        self.gridLayout.addWidget(self.browse_pushBtn, 2, 1, 1, 1)
        self.upload_pushBtn = QtGui.QPushButton(self.wizardPage2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../Downloads/firefox/upload_1-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_pushBtn.setIcon(icon1)
        self.upload_pushBtn.setDefault(False)
        self.upload_pushBtn.setFlat(False)
        self.upload_pushBtn.setObjectName(_fromUtf8("upload_pushBtn"))
        self.gridLayout.addWidget(self.upload_pushBtn, 3, 1, 1, 1)
        self.frame_2 = QtGui.QFrame(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 15))
        self.frame_2.setMaximumSize(QtCore.QSize(600, 200))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.title_Label2 = QtGui.QLabel(self.frame_2)
        self.title_Label2.setGeometry(QtCore.QRect(10, 0, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_Label2.setFont(font)
        self.title_Label2.setObjectName(_fromUtf8("title_Label2"))
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)
        LodgeScheme_Wzd.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_4 = QtGui.QFrame(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 15))
        self.frame_4.setMaximumSize(QtCore.QSize(600, 200))
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.title_Label2_3 = QtGui.QLabel(self.frame_4)
        self.title_Label2_3.setGeometry(QtCore.QRect(10, 0, 571, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_Label2_3.setFont(font)
        self.title_Label2_3.setLineWidth(0)
        self.title_Label2_3.setObjectName(_fromUtf8("title_Label2_3"))
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.wizardPage)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.desc_Label2_2 = QtGui.QLabel(self.frame_5)
        self.desc_Label2_2.setLineWidth(0)
        self.desc_Label2_2.setObjectName(_fromUtf8("desc_Label2_2"))
        self.horizontalLayout_2.addWidget(self.desc_Label2_2)
        self.verticalLayout.addWidget(self.frame_5)
        self.holders_tblWdg = QtGui.QTableWidget(self.wizardPage)
        self.holders_tblWdg.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.holders_tblWdg.sizePolicy().hasHeightForWidth())
        self.holders_tblWdg.setSizePolicy(sizePolicy)
        self.holders_tblWdg.setMinimumSize(QtCore.QSize(0, 0))
        self.holders_tblWdg.setMaximumSize(QtCore.QSize(600, 16777215))
        self.holders_tblWdg.setSizeIncrement(QtCore.QSize(200, 0))
        self.holders_tblWdg.setFrameShape(QtGui.QFrame.NoFrame)
        self.holders_tblWdg.setObjectName(_fromUtf8("holders_tblWdg"))
        self.holders_tblWdg.setColumnCount(4)
        self.holders_tblWdg.setRowCount(9)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.holders_tblWdg.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.holders_tblWdg.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.holders_tblWdg.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.holders_tblWdg.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.holders_tblWdg.setItem(2, 3, item)
        self.verticalLayout.addWidget(self.holders_tblWdg)
        LodgeScheme_Wzd.addPage(self.wizardPage)
        self.wizardPage_2 = QtGui.QWizardPage()
        self.wizardPage_2.setObjectName(_fromUtf8("wizardPage_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.wizardPage_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame_6 = QtGui.QFrame(self.wizardPage_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_6.setSizeIncrement(QtCore.QSize(0, 30))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.title_Label2_4 = QtGui.QLabel(self.frame_6)
        self.title_Label2_4.setGeometry(QtCore.QRect(10, 10, 112, 13))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_Label2_4.sizePolicy().hasHeightForWidth())
        self.title_Label2_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_Label2_4.setFont(font)
        self.title_Label2_4.setLineWidth(0)
        self.title_Label2_4.setObjectName(_fromUtf8("title_Label2_4"))
        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 1)
        self.frame_7 = QtGui.QFrame(self.wizardPage_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_7.setSizeIncrement(QtCore.QSize(0, 30))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.title_Label2_5 = QtGui.QLabel(self.frame_7)
        self.title_Label2_5.setGeometry(QtCore.QRect(10, 10, 591, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_Label2_5.sizePolicy().hasHeightForWidth())
        self.title_Label2_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.title_Label2_5.setFont(font)
        self.title_Label2_5.setLineWidth(0)
        self.title_Label2_5.setObjectName(_fromUtf8("title_Label2_5"))
        self.gridLayout_4.addWidget(self.frame_7, 1, 0, 1, 1)
        self.blockArea_frame = QtGui.QFrame(self.wizardPage_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockArea_frame.sizePolicy().hasHeightForWidth())
        self.blockArea_frame.setSizePolicy(sizePolicy)
        self.blockArea_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.blockArea_frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.blockArea_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.blockArea_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.blockArea_frame.setLineWidth(0)
        self.blockArea_frame.setObjectName(_fromUtf8("blockArea_frame"))
        self.blockArea_lineEdit = QtGui.QLineEdit(self.blockArea_frame)
        self.blockArea_lineEdit.setGeometry(QtCore.QRect(140, 30, 181, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockArea_lineEdit.sizePolicy().hasHeightForWidth())
        self.blockArea_lineEdit.setSizePolicy(sizePolicy)
        self.blockArea_lineEdit.setText(_fromUtf8(""))
        self.blockArea_lineEdit.setReadOnly(True)
        self.blockArea_lineEdit.setObjectName(_fromUtf8("blockArea_lineEdit"))
        self.blockArea_label = QtGui.QLabel(self.blockArea_frame)
        self.blockArea_label.setGeometry(QtCore.QRect(30, 30, 103, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockArea_label.sizePolicy().hasHeightForWidth())
        self.blockArea_label.setSizePolicy(sizePolicy)
        self.blockArea_label.setObjectName(_fromUtf8("blockArea_label"))
        self.gridLayout_4.addWidget(self.blockArea_frame, 2, 0, 1, 1)
        LodgeScheme_Wzd.addPage(self.wizardPage_2)
        self.wizardPage_3 = QtGui.QWizardPage()
        self.wizardPage_3.setObjectName(_fromUtf8("wizardPage_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.wizardPage_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.title_label5 = QtGui.QLabel(self.wizardPage_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label5.sizePolicy().hasHeightForWidth())
        self.title_label5.setSizePolicy(sizePolicy)
        self.title_label5.setMinimumSize(QtCore.QSize(0, 10))
        self.title_label5.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_label5.setFont(font)
        self.title_label5.setObjectName(_fromUtf8("title_label5"))
        self.verticalLayout_5.addWidget(self.title_label5)
        self.desc_Label2_4 = QtGui.QLabel(self.wizardPage_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_Label2_4.sizePolicy().hasHeightForWidth())
        self.desc_Label2_4.setSizePolicy(sizePolicy)
        self.desc_Label2_4.setMinimumSize(QtCore.QSize(0, 50))
        self.desc_Label2_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.desc_Label2_4.setObjectName(_fromUtf8("desc_Label2_4"))
        self.verticalLayout_5.addWidget(self.desc_Label2_4)
        self.frame_8 = QtGui.QFrame(self.wizardPage_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 0))
        self.frame_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.registrationDivision_cbx = QtGui.QComboBox(self.frame_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registrationDivision_cbx.sizePolicy().hasHeightForWidth())
        self.registrationDivision_cbx.setSizePolicy(sizePolicy)
        self.registrationDivision_cbx.setMinimumSize(QtCore.QSize(0, 20))
        self.registrationDivision_cbx.setMaximumSize(QtCore.QSize(150, 1))
        self.registrationDivision_cbx.setSizeIncrement(QtCore.QSize(30, 5))
        self.registrationDivision_cbx.setObjectName(_fromUtf8("registrationDivision_cbx"))
        self.gridLayout_3.addWidget(self.registrationDivision_cbx, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame_8)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_8)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        LodgeScheme_Wzd.addPage(self.wizardPage_3)
        self.wizardPage_4 = QtGui.QWizardPage()
        self.wizardPage_4.setObjectName(_fromUtf8("wizardPage_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wizardPage_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.title_Label2_6 = QtGui.QLabel(self.wizardPage_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_Label2_6.setFont(font)
        self.title_Label2_6.setObjectName(_fromUtf8("title_Label2_6"))
        self.verticalLayout_2.addWidget(self.title_Label2_6)
        self.desc_Label2_5 = QtGui.QLabel(self.wizardPage_4)
        self.desc_Label2_5.setObjectName(_fromUtf8("desc_Label2_5"))
        self.verticalLayout_2.addWidget(self.desc_Label2_5)
        self.tr_summary = QtGui.QTreeView(self.wizardPage_4)
        self.tr_summary.setObjectName(_fromUtf8("tr_summary"))
        self.verticalLayout_2.addWidget(self.tr_summary)
        self.desc_Label2_6 = QtGui.QLabel(self.wizardPage_4)
        self.desc_Label2_6.setObjectName(_fromUtf8("desc_Label2_6"))
        self.verticalLayout_2.addWidget(self.desc_Label2_6)
        LodgeScheme_Wzd.addPage(self.wizardPage_4)

        self.retranslateUi(LodgeScheme_Wzd)
        QtCore.QMetaObject.connectSlotsByName(LodgeScheme_Wzd)

    def retranslateUi(self, LodgeScheme_Wzd):
        LodgeScheme_Wzd.setWindowTitle(_translate("LodgeScheme_Wzd", "Lodgement of Scheme", "Step 1 of 5"))
        self.title_Label1.setText(_translate("LodgeScheme_Wzd", "New Land Hold Scheme", None))
        self.desc_Label1.setText(_translate("LodgeScheme_Wzd", "A new scheme number has been generated and is shown below", None))
        self.label_2.setText(_translate("LodgeScheme_Wzd", "Scheme Number: ", None))
        self.label_4.setText(_translate("LodgeScheme_Wzd", "This number will be logged and used in the next steps", None))
        self.label_5.setText(_translate("LodgeScheme_Wzd", "If you would like to end this process click \'cancel\' below, otherwise click \'next to proceed", None))
        self.desc_Label2.setText(_translate("LodgeScheme_Wzd", "This step entails locating and importing the list of holders file.  ", None))
        self.browse_pushBtn.setText(_translate("LodgeScheme_Wzd", "Browse...", None))
        self.upload_pushBtn.setText(_translate("LodgeScheme_Wzd", "Upload", None))
        self.title_Label2.setText(_translate("LodgeScheme_Wzd", "Import holders", None))
        self.title_Label2_3.setText(_translate("LodgeScheme_Wzd", "Upload Documents", None))
        self.desc_Label2_2.setText(_translate("LodgeScheme_Wzd", "Below is a list for importing the required documents. Upload all the documents to proceed.", None))
        item = self.holders_tblWdg.verticalHeaderItem(0)
        item.setText(_translate("LodgeScheme_Wzd", "Notice of Scheme Establishment", None))
        item = self.holders_tblWdg.verticalHeaderItem(1)
        item.setText(_translate("LodgeScheme_Wzd", "Explanatory Report", None))
        item = self.holders_tblWdg.verticalHeaderItem(2)
        item.setText(_translate("LodgeScheme_Wzd", "Council Resolution", None))
        item = self.holders_tblWdg.verticalHeaderItem(3)
        item.setText(_translate("LodgeScheme_Wzd", "Title Deed of Blockerf", None))
        item = self.holders_tblWdg.verticalHeaderItem(4)
        item.setText(_translate("LodgeScheme_Wzd", "Cover Certificate", None))
        item = self.holders_tblWdg.verticalHeaderItem(5)
        item.setText(_translate("LodgeScheme_Wzd", "List of Potential Holders", None))
        item = self.holders_tblWdg.verticalHeaderItem(6)
        item.setText(_translate("LodgeScheme_Wzd", "Transfer Contract", None))
        item = self.holders_tblWdg.verticalHeaderItem(7)
        item.setText(_translate("LodgeScheme_Wzd", "Document Imposing Conditions", None))
        item = self.holders_tblWdg.verticalHeaderItem(8)
        item.setText(_translate("LodgeScheme_Wzd", "Digital Layout Plan", None))
        item = self.holders_tblWdg.horizontalHeaderItem(0)
        item.setText(_translate("LodgeScheme_Wzd", "Type", None))
        item = self.holders_tblWdg.horizontalHeaderItem(1)
        item.setText(_translate("LodgeScheme_Wzd", "Status", None))
        item = self.holders_tblWdg.horizontalHeaderItem(2)
        item.setText(_translate("LodgeScheme_Wzd", "Link", None))
        item = self.holders_tblWdg.horizontalHeaderItem(3)
        item.setText(_translate("LodgeScheme_Wzd", "Browse", None))
        __sortingEnabled = self.holders_tblWdg.isSortingEnabled()
        self.holders_tblWdg.setSortingEnabled(False)
        self.holders_tblWdg.setSortingEnabled(__sortingEnabled)
        self.title_Label2_4.setText(_translate("LodgeScheme_Wzd", "Block Measure Data", None))
        self.title_Label2_5.setText(_translate("LodgeScheme_Wzd", "Below is the block measure value retrieved from land information systems", None))
        self.blockArea_label.setText(_translate("LodgeScheme_Wzd", "Block Area (hectares)", None))
        self.title_label5.setText(_translate("LodgeScheme_Wzd", "Registration Division Letter", None))
        self.desc_Label2_4.setText(_translate("LodgeScheme_Wzd", "This screen lets you select the division of registration. ", None))
        self.label.setText(_translate("LodgeScheme_Wzd", "Registration division selector", None))
        self.title_Label2_6.setText(_translate("LodgeScheme_Wzd", "Summary", None))
        self.desc_Label2_5.setText(_translate("LodgeScheme_Wzd", "Confirm the saved data from the previous steps.  ", None))
        self.desc_Label2_6.setText(_translate("LodgeScheme_Wzd", "Click finish if satisfied with the information.", None))

