# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newaddressdialog.ui'
#
# Created: Sun Sep 15 23:53:31 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets


# Qt6/Python3: strings are already Unicode, no QString.fromUtf8 needed
def _fromUtf8(s: str) -> str:
    return s


# Qt6: translate() no longer takes an encoding parameter
def _translate(context: str, text: str, disambig: str | None) -> str:
    return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_NewAddressDialog(object):
    def setupUi(self, NewAddressDialog):
        NewAddressDialog.setObjectName("NewAddressDialog")
        NewAddressDialog.resize(723, 704)
        self.formLayout = QtWidgets.QFormLayout(NewAddressDialog)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(NewAddressDialog)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label)
        self.label_5 = QtWidgets.QLabel(NewAddressDialog)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_5)
        self.line = QtWidgets.QFrame(NewAddressDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(100, 2))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.line)
        self.radioButtonRandomAddress = QtWidgets.QRadioButton(NewAddressDialog)
        self.radioButtonRandomAddress.setChecked(True)
        self.radioButtonRandomAddress.setObjectName("radioButtonRandomAddress")
        self.buttonGroup = QtGui.QButtonGroup(NewAddressDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonRandomAddress)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.radioButtonRandomAddress)
        self.radioButtonDeterministicAddress = QtWidgets.QRadioButton(NewAddressDialog)
        self.radioButtonDeterministicAddress.setObjectName("radioButtonDeterministicAddress")
        self.buttonGroup.addButton(self.radioButtonDeterministicAddress)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.radioButtonDeterministicAddress)
        self.checkBoxEighteenByteRipe = QtWidgets.QCheckBox(NewAddressDialog)
        self.checkBoxEighteenByteRipe.setObjectName("checkBoxEighteenByteRipe")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.checkBoxEighteenByteRipe)
        self.groupBoxDeterministic = QtWidgets.QGroupBox(NewAddressDialog)
        self.groupBoxDeterministic.setObjectName("groupBoxDeterministic")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxDeterministic)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBoxDeterministic)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBoxDeterministic)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 3)
        self.spinBoxNumberOfAddressesToMake = QtWidgets.QSpinBox(self.groupBoxDeterministic)
        self.spinBoxNumberOfAddressesToMake.setMinimum(1)
        self.spinBoxNumberOfAddressesToMake.setProperty("value", 8)
        self.spinBoxNumberOfAddressesToMake.setObjectName("spinBoxNumberOfAddressesToMake")
        self.gridLayout.addWidget(self.spinBoxNumberOfAddressesToMake, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBoxDeterministic)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBoxDeterministic)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBoxDeterministic)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBoxDeterministic)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEditPassphraseAgain = QtWidgets.QLineEdit(self.groupBoxDeterministic)
        self.lineEditPassphraseAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassphraseAgain.setObjectName("lineEditPassphraseAgain")
        self.gridLayout.addWidget(self.lineEditPassphraseAgain, 3, 0, 1, 4)
        self.lineEditPassphrase = QtWidgets.QLineEdit(self.groupBoxDeterministic)
        self.lineEditPassphrase.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText)
        self.lineEditPassphrase.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassphrase.setObjectName("lineEditPassphrase")
        self.gridLayout.addWidget(self.lineEditPassphrase, 1, 0, 1, 4)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.groupBoxDeterministic)
        self.groupBox = QtWidgets.QGroupBox(NewAddressDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.newaddresslabel = QtWidgets.QLineEdit(self.groupBox)
        self.newaddresslabel.setObjectName("newaddresslabel")
        self.gridLayout_2.addWidget(self.newaddresslabel, 1, 0, 1, 2)
        self.radioButtonMostAvailable = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMostAvailable.setChecked(True)
        self.radioButtonMostAvailable.setObjectName("radioButtonMostAvailable")
        self.gridLayout_2.addWidget(self.radioButtonMostAvailable, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)
        self.radioButtonExisting = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonExisting.setChecked(False)
        self.radioButtonExisting.setObjectName("radioButtonExisting")
        self.gridLayout_2.addWidget(self.radioButtonExisting, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 1)
        self.comboBoxExisting = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxExisting.setEnabled(False)
        self.comboBoxExisting.setEditable(True)
        self.comboBoxExisting.setObjectName("comboBoxExisting")
        self.gridLayout_2.addWidget(self.comboBoxExisting, 6, 1, 1, 1)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewAddressDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(160, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.buttonBox)

        self.retranslateUi(NewAddressDialog)
        self.buttonBox.accepted.connect(NewAddressDialog.accept)
        self.buttonBox.rejected.connect(NewAddressDialog.reject)
        self.radioButtonExisting.toggled.connect(self.comboBoxExisting.setEnabled)
        self.radioButtonDeterministicAddress.toggled.connect(self.groupBoxDeterministic.setShown)
        self.radioButtonRandomAddress.toggled.connect(self.groupBox.setShown)
        QtCore.QMetaObject.connectSlotsByName(NewAddressDialog)
        NewAddressDialog.setTabOrder(self.radioButtonRandomAddress, self.radioButtonDeterministicAddress)
        NewAddressDialog.setTabOrder(self.radioButtonDeterministicAddress, self.newaddresslabel)
        NewAddressDialog.setTabOrder(self.newaddresslabel, self.radioButtonMostAvailable)
        NewAddressDialog.setTabOrder(self.radioButtonMostAvailable, self.radioButtonExisting)
        NewAddressDialog.setTabOrder(self.radioButtonExisting, self.comboBoxExisting)
        NewAddressDialog.setTabOrder(self.comboBoxExisting, self.lineEditPassphrase)
        NewAddressDialog.setTabOrder(self.lineEditPassphrase, self.lineEditPassphraseAgain)
        NewAddressDialog.setTabOrder(self.lineEditPassphraseAgain, self.spinBoxNumberOfAddressesToMake)
        NewAddressDialog.setTabOrder(self.spinBoxNumberOfAddressesToMake, self.checkBoxEighteenByteRipe)
        NewAddressDialog.setTabOrder(self.checkBoxEighteenByteRipe, self.buttonBox)

    def retranslateUi(self, NewAddressDialog):
        NewAddressDialog.setWindowTitle(_translate("NewAddressDialog", "Create new Address", None))
        self.label.setText(
            _translate(
                "NewAddressDialog",
                'Here you may generate as many addresses as you like. Indeed, creating and '
                'abandoning addresses is encouraged. You may generate addresses by using either '
                'random numbers or by using a passphrase. If you use a passphrase, the address is '
                'called a "deterministic" address.\n'
                "The 'Random Number' option is selected by default but deterministic addresses "
                "have several pros and cons:",
                None,
            )
        )
        self.label_5.setText(
            _translate(
                "NewAddressDialog",
                '<html><head/><body><p><span style=" font-weight:600;">Pros:<br/></span>'
                'You can recreate your addresses on any computer from memory. <br/>'
                'You need-not worry about backing up your keys.dat file as long as you can '
                'remember your passphrase. <br/><span style=" font-weight:600;">Cons:<br/></span>'
                'You must remember (or write down) your passphrase if you expect to be able to '
                'recreate your keys if they are lost. <br/>You must remember the address version '
                'number and the stream number along with your passphrase. <br/>If you choose a '
                'weak passphrase and someone on the Internet can brute-force it, they can read '
                'your messages and send messages as you.</p></body></html>',
                None,
            )
        )
        self.radioButtonRandomAddress.setText(_translate("NewAddressDialog", "Use a random number generator to make an address", None))
        self.radioButtonDeterministicAddress.setText(_translate("NewAddressDialog", "Use a passphrase to make addresses", None))
        self.checkBoxEighteenByteRipe.setText(
            _translate(
                "NewAddressDialog",
                "Spend several minutes of extra computing time to make the address(es) 1 or 2 characters shorter",
                None,
            )
        )
        self.groupBoxDeterministic.setTitle(_translate("NewAddressDialog", "Make deterministic addresses", None))
        self.label_9.setText(_translate("NewAddressDialog", "Address version number: 4", None))
        self.label_8.setText(_translate("NewAddressDialog", "In addition to your passphrase, you must remember these numbers:", None))
        self.label_6.setText(_translate("NewAddressDialog", "Passphrase", None))
        self.label_11.setText(_translate("NewAddressDialog", "Number of addresses to make based on your passphrase:", None))
        self.label_10.setText(_translate("NewAddressDialog", "Stream number: 1", None))
        self.label_7.setText(_translate("NewAddressDialog", "Retype passphrase", None))
        self.groupBox.setTitle(_translate("NewAddressDialog", "Randomly generate address", None))
        self.label_2.setText(_translate("NewAddressDialog", "Label (not shown to anyone except you)", None))
        self.radioButtonMostAvailable.setText(_translate("NewAddressDialog", "Use the most available stream", None))
        self.label_3.setText(_translate("NewAddressDialog", " (best if this is the first of many addresses you will create)", None))
        self.radioButtonExisting.setText(_translate("NewAddressDialog", "Use the same stream as an existing address", None))
        self.label_4.setText(_translate("NewAddressDialog", "(saves you some bandwidth and processing power)", None))
