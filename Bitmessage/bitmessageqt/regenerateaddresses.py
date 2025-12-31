# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regenerateaddresses.ui'
#
# Created: Sun Sep 15 23:50:23 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_regenerateAddressesDialog(object):
    def setupUi(self, regenerateAddressesDialog):
        regenerateAddressesDialog.setObjectName("regenerateAddressesDialog")
        regenerateAddressesDialog.resize(532, 332)
        self.gridLayout_2 = QtWidgets.QGridLayout(regenerateAddressesDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(regenerateAddressesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(regenerateAddressesDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEditPassphrase = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPassphrase.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText
        )
        self.lineEditPassphrase.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassphrase.setObjectName("lineEditPassphrase")
        self.gridLayout.addWidget(self.lineEditPassphrase, 2, 0, 1, 5)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 3)
        self.spinBoxNumberOfAddressesToMake = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxNumberOfAddressesToMake.sizePolicy().hasHeightForWidth())
        self.spinBoxNumberOfAddressesToMake.setSizePolicy(sizePolicy)
        self.spinBoxNumberOfAddressesToMake.setMinimum(1)
        self.spinBoxNumberOfAddressesToMake.setProperty("value", 8)
        self.spinBoxNumberOfAddressesToMake.setObjectName("spinBoxNumberOfAddressesToMake")
        self.gridLayout.addWidget(self.spinBoxNumberOfAddressesToMake, 3, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            132, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.lineEditAddressVersionNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditAddressVersionNumber.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditAddressVersionNumber.sizePolicy().hasHeightForWidth())
        self.lineEditAddressVersionNumber.setSizePolicy(sizePolicy)
        self.lineEditAddressVersionNumber.setMaximumSize(QtCore.QSize(31, 16777215))
        self.lineEditAddressVersionNumber.setText(_fromUtf8(""))
        self.lineEditAddressVersionNumber.setObjectName("lineEditAddressVersionNumber")
        self.gridLayout.addWidget(self.lineEditAddressVersionNumber, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEditStreamNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditStreamNumber.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditStreamNumber.sizePolicy().hasHeightForWidth())
        self.lineEditStreamNumber.setSizePolicy(sizePolicy)
        self.lineEditStreamNumber.setMaximumSize(QtCore.QSize(31, 16777215))
        self.lineEditStreamNumber.setObjectName("lineEditStreamNumber")
        self.gridLayout.addWidget(self.lineEditStreamNumber, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            325, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout.addItem(spacerItem2, 5, 2, 1, 3)
        self.checkBoxEighteenByteRipe = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxEighteenByteRipe.setObjectName("checkBoxEighteenByteRipe")
        self.gridLayout.addWidget(self.checkBoxEighteenByteRipe, 6, 0, 1, 5)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(regenerateAddressesDialog)
        self.buttonBox.accepted.connect(regenerateAddressesDialog.accept)
        self.buttonBox.rejected.connect(regenerateAddressesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(regenerateAddressesDialog)

    def retranslateUi(self, regenerateAddressesDialog):
        regenerateAddressesDialog.setWindowTitle(
            _translate("regenerateAddressesDialog", "Regenerate Existing Addresses", None)
        )
        self.groupBox.setTitle(_translate("regenerateAddressesDialog", "Regenerate existing addresses", None))
        self.label_6.setText(_translate("regenerateAddressesDialog", "Passphrase", None))
        self.label_11.setText(
            _translate("regenerateAddressesDialog", "Number of addresses to make based on your passphrase:", None)
        )
        self.label_2.setText(_translate("regenerateAddressesDialog", "Address version number:", None))
        self.label_3.setText(_translate("regenerateAddressesDialog", "Stream number:", None))
        self.lineEditStreamNumber.setText(_translate("regenerateAddressesDialog", "1", None))
        self.checkBoxEighteenByteRipe.setText(
            _translate(
                "regenerateAddressesDialog",
                "Spend several minutes of extra computing time to make the address(es) 1 or 2 characters shorter",
                None,
            )
        )
        self.label_4.setText(
            _translate(
                "regenerateAddressesDialog",
                "You must check (or not check) this box just like you did (or didn't) when you made your addresses the first time.",
                None,
            )
        )
        self.label.setText(
            _translate(
                "regenerateAddressesDialog",
                "If you have previously made deterministic addresses but lost them due to an accident (like hard drive failure), you can regenerate them here. If you used the random number generator to make your addresses then this form will be of no use to you.",
                None,
            )
        )
