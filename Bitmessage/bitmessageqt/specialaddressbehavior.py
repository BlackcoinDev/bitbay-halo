# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specialaddressbehavior.ui'
#
# Created: Fri Apr 26 17:43:31 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets, QtWidgets, QtWidgets, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SpecialAddressBehaviorDialog(object):
    def setupUi(self, SpecialAddressBehaviorDialog):
        SpecialAddressBehaviorDialog.setObjectName("SpecialAddressBehaviorDialog")
        SpecialAddressBehaviorDialog.resize(386, 172)
        self.gridLayout = QtWidgets.QGridLayout(SpecialAddressBehaviorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonBehaveNormalAddress = QtWidgets.QRadioButton(SpecialAddressBehaviorDialog)
        self.radioButtonBehaveNormalAddress.setChecked(True)
        self.radioButtonBehaveNormalAddress.setObjectName("radioButtonBehaveNormalAddress")
        self.gridLayout.addWidget(self.radioButtonBehaveNormalAddress, 0, 0, 1, 1)
        self.radioButtonBehaviorMailingList = QtWidgets.QRadioButton(SpecialAddressBehaviorDialog)
        self.radioButtonBehaviorMailingList.setObjectName("radioButtonBehaviorMailingList")
        self.gridLayout.addWidget(self.radioButtonBehaviorMailingList, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(SpecialAddressBehaviorDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(SpecialAddressBehaviorDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEditMailingListName = QtWidgets.QLineEdit(SpecialAddressBehaviorDialog)
        self.lineEditMailingListName.setEnabled(False)
        self.lineEditMailingListName.setObjectName("lineEditMailingListName")
        self.gridLayout.addWidget(self.lineEditMailingListName, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpecialAddressBehaviorDialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(368, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(SpecialAddressBehaviorDialog)
        self.buttonBox.accepted.connect(SpecialAddressBehaviorDialog.accept)
        self.buttonBox.rejected.connect(SpecialAddressBehaviorDialog.reject)
        self.radioButtonBehaviorMailingList.clicked.connect(self.lineEditMailingListName.setEnabled)
        self.radioButtonBehaveNormalAddress.clicked.connect(self.lineEditMailingListName.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(SpecialAddressBehaviorDialog)
        SpecialAddressBehaviorDialog.setTabOrder(self.radioButtonBehaveNormalAddress, self.radioButtonBehaviorMailingList)
        SpecialAddressBehaviorDialog.setTabOrder(self.radioButtonBehaviorMailingList, self.lineEditMailingListName)
        SpecialAddressBehaviorDialog.setTabOrder(self.lineEditMailingListName, self.buttonBox)

    def retranslateUi(self, SpecialAddressBehaviorDialog):
        SpecialAddressBehaviorDialog.setWindowTitle(QtWidgets.QApplication.translate("SpecialAddressBehaviorDialog", "Special Address Behavior", None, QtWidgets.QApplication.UnicodeUTF8))
        self.radioButtonBehaveNormalAddress.setText(QtWidgets.QApplication.translate("SpecialAddressBehaviorDialog", "Behave as a normal address", None, QtWidgets.QApplication.UnicodeUTF8))
        self.radioButtonBehaviorMailingList.setText(QtWidgets.QApplication.translate("SpecialAddressBehaviorDialog", "Behave as a pseudo-mailing-list address", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setText(QtWidgets.QApplication.translate("SpecialAddressBehaviorDialog", "Mail received to a pseudo-mailing-list address will be automatically broadcast to subscribers (and thus will be public).", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_2.setText(QtWidgets.QApplication.translate("SpecialAddressBehaviorDialog", "Name of the pseudo-mailing-list:", None, QtWidgets.QApplication.UnicodeUTF8))

