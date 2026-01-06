# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsubscriptiondialog.ui'
#
# Created: Sat Nov 30 21:53:38 2013
#      by: PyQt4 UI code generator 4.10.3
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


class Ui_NewSubscriptionDialog(object):
    def setupUi(self, NewSubscriptionDialog):
        NewSubscriptionDialog.setObjectName("NewSubscriptionDialog")
        NewSubscriptionDialog.resize(368, 173)
        self.formLayout = QtWidgets.QFormLayout(NewSubscriptionDialog)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(NewSubscriptionDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.newsubscriptionlabel = QtWidgets.QLineEdit(NewSubscriptionDialog)
        self.newsubscriptionlabel.setObjectName("newsubscriptionlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.newsubscriptionlabel)
        self.label = QtWidgets.QLabel(NewSubscriptionDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEditSubscriptionAddress = QtWidgets.QLineEdit(NewSubscriptionDialog)
        self.lineEditSubscriptionAddress.setObjectName("lineEditSubscriptionAddress")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.lineEditSubscriptionAddress)
        self.labelAddressCheck = QtWidgets.QLabel(NewSubscriptionDialog)
        self.labelAddressCheck.setText(_fromUtf8(""))
        self.labelAddressCheck.setWordWrap(True)
        self.labelAddressCheck.setObjectName("labelAddressCheck")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.labelAddressCheck)
        self.checkBoxDisplayMessagesAlreadyInInventory = QtWidgets.QCheckBox(NewSubscriptionDialog)
        self.checkBoxDisplayMessagesAlreadyInInventory.setEnabled(False)
        self.checkBoxDisplayMessagesAlreadyInInventory.setObjectName("checkBoxDisplayMessagesAlreadyInInventory")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.checkBoxDisplayMessagesAlreadyInInventory)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewSubscriptionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.retranslateUi(NewSubscriptionDialog)
        self.buttonBox.accepted.connect(NewSubscriptionDialog.accept)
        self.buttonBox.rejected.connect(NewSubscriptionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewSubscriptionDialog)

    def retranslateUi(self, NewSubscriptionDialog):
        NewSubscriptionDialog.setWindowTitle(_translate("NewSubscriptionDialog", "Add new entry", None))
        self.label_2.setText(_translate("NewSubscriptionDialog", "Label", None))
        self.label.setText(_translate("NewSubscriptionDialog", "Address", None))
        self.checkBoxDisplayMessagesAlreadyInInventory.setText(_translate("NewSubscriptionDialog", "CheckBox", None))
