# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addaddressdialog.ui'
#
# Created: Sat Nov 30 20:35:38 2013
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


class Ui_AddAddressDialog(object):
    def setupUi(self, AddAddressDialog):
        AddAddressDialog.setObjectName("AddAddressDialog")
        AddAddressDialog.resize(368, 162)
        self.formLayout = QtWidgets.QFormLayout(AddAddressDialog)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(AddAddressDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)
        self.newAddressLabel = QtWidgets.QLineEdit(AddAddressDialog)
        self.newAddressLabel.setObjectName("newAddressLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.newAddressLabel)
        self.label = QtWidgets.QLabel(AddAddressDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEditAddress = QtWidgets.QLineEdit(AddAddressDialog)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.lineEditAddress)
        self.labelAddressCheck = QtWidgets.QLabel(AddAddressDialog)
        self.labelAddressCheck.setText(_fromUtf8(""))
        self.labelAddressCheck.setWordWrap(True)
        self.labelAddressCheck.setObjectName("labelAddressCheck")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.labelAddressCheck)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddAddressDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.retranslateUi(AddAddressDialog)
        self.buttonBox.accepted.connect(AddAddressDialog.accept)
        self.buttonBox.rejected.connect(AddAddressDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddAddressDialog)

    def retranslateUi(self, AddAddressDialog):
        AddAddressDialog.setWindowTitle(_translate("AddAddressDialog", "Add new entry", None))
        self.label_2.setText(_translate("AddAddressDialog", "Label", None))
        self.label.setText(_translate("AddAddressDialog", "Address", None))
