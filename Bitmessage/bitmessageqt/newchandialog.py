# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newchandialog.ui'
#
# Created: Wed Aug  7 16:51:29 2013
#      by: PyQt4 UI code generator 4.10
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


class Ui_newChanDialog(object):
    def setupUi(self, newChanDialog):
        newChanDialog.setObjectName("newChanDialog")
        newChanDialog.resize(553, 422)
        newChanDialog.setMinimumSize(QtCore.QSize(0, 0))
        self.formLayout = QtWidgets.QFormLayout(newChanDialog)
        self.formLayout.setObjectName("formLayout")
        self.radioButtonCreateChan = QtWidgets.QRadioButton(newChanDialog)
        self.radioButtonCreateChan.setObjectName("radioButtonCreateChan")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.radioButtonCreateChan)
        self.radioButtonJoinChan = QtWidgets.QRadioButton(newChanDialog)
        self.radioButtonJoinChan.setChecked(True)
        self.radioButtonJoinChan.setObjectName("radioButtonJoinChan")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.radioButtonJoinChan)
        self.groupBoxCreateChan = QtWidgets.QGroupBox(newChanDialog)
        self.groupBoxCreateChan.setObjectName("groupBoxCreateChan")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCreateChan)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBoxCreateChan)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBoxCreateChan)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEditChanNameCreate = QtWidgets.QLineEdit(self.groupBoxCreateChan)
        self.lineEditChanNameCreate.setObjectName("lineEditChanNameCreate")
        self.gridLayout.addWidget(self.lineEditChanNameCreate, 2, 0, 1, 1)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.groupBoxCreateChan)
        self.groupBoxJoinChan = QtWidgets.QGroupBox(newChanDialog)
        self.groupBoxJoinChan.setObjectName("groupBoxJoinChan")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxJoinChan)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBoxJoinChan)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBoxJoinChan)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditChanNameJoin = QtWidgets.QLineEdit(self.groupBoxJoinChan)
        self.lineEditChanNameJoin.setObjectName("lineEditChanNameJoin")
        self.gridLayout_2.addWidget(self.lineEditChanNameJoin, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBoxJoinChan)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEditChanBitmessageAddress = QtWidgets.QLineEdit(self.groupBoxJoinChan)
        self.lineEditChanBitmessageAddress.setObjectName("lineEditChanBitmessageAddress")
        self.gridLayout_2.addWidget(self.lineEditChanBitmessageAddress, 4, 0, 1, 1)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.groupBoxJoinChan)
        spacerItem = QtWidgets.QSpacerItem(389, 2, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(newChanDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.retranslateUi(newChanDialog)
        self.buttonBox.accepted.connect(newChanDialog.accept)
        self.buttonBox.rejected.connect(newChanDialog.reject)
        self.radioButtonJoinChan.toggled.connect(self.groupBoxJoinChan.setShown)
        self.radioButtonCreateChan.toggled.connect(self.groupBoxCreateChan.setShown)
        QtCore.QMetaObject.connectSlotsByName(newChanDialog)
        newChanDialog.setTabOrder(self.radioButtonJoinChan, self.radioButtonCreateChan)
        newChanDialog.setTabOrder(self.radioButtonCreateChan, self.lineEditChanNameCreate)
        newChanDialog.setTabOrder(self.lineEditChanNameCreate, self.lineEditChanNameJoin)
        newChanDialog.setTabOrder(self.lineEditChanNameJoin, self.lineEditChanBitmessageAddress)
        newChanDialog.setTabOrder(self.lineEditChanBitmessageAddress, self.buttonBox)

    def retranslateUi(self, newChanDialog):
        newChanDialog.setWindowTitle(_translate("newChanDialog", "Dialog", None))
        self.radioButtonCreateChan.setText(_translate("newChanDialog", "Create a new chan", None))
        self.radioButtonJoinChan.setText(_translate("newChanDialog", "Join a chan", None))
        self.groupBoxCreateChan.setTitle(_translate("newChanDialog", "Create a chan", None))
        self.label_4.setText(
            _translate(
                "newChanDialog",
                "<html><head/><body><p>Enter a name for your chan. If you choose a sufficiently complex chan name (like a strong and unique passphrase) and none of your friends share it publicly then the chan will be secure and private. If you and someone else both create a chan with the same chan name then it is currently very likely that they will be the same chan.</p></body></html>",
                None,
            )
        )
        self.label_5.setText(_translate("newChanDialog", "Chan name:", None))
        self.groupBoxJoinChan.setTitle(_translate("newChanDialog", "Join a chan", None))
        self.label.setText(
            _translate(
                "newChanDialog",
                "<html><head/><body><p>A chan exists when a group of people share the same decryption keys. The keys and bitmessage address used by a chan are generated from a human-friendly word or phrase (the chan name). To send a message to everyone in the chan, send a normal person-to-person message to the chan address.</p><p>Chans are experimental and completely unmoderatable.</p></body></html>",
                None,
            )
        )
        self.label_2.setText(_translate("newChanDialog", "Chan name:", None))
        self.label_3.setText(_translate("newChanDialog", "Chan bitmessage address:", None))
