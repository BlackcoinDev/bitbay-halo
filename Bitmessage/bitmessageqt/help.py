# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created: Mon Mar 11 11:20:54 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_helpDialog(object):
    def setupUi(self, helpDialog):
        helpDialog.setObjectName("helpDialog")
        helpDialog.resize(335, 96)
        self.formLayout = QtWidgets.QFormLayout(helpDialog)
        self.formLayout.setObjectName("formLayout")
        self.labelHelpURI = QtWidgets.QLabel(helpDialog)
        self.labelHelpURI.setOpenExternalLinks(True)
        self.labelHelpURI.setObjectName("labelHelpURI")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelHelpURI)
        self.label = QtWidgets.QLabel(helpDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.formLayout.setItem(2, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(helpDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.retranslateUi(helpDialog)
        self.buttonBox.accepted.connect(helpDialog.accept)
        self.buttonBox.rejected.connect(helpDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

    def retranslateUi(self, helpDialog):
        helpDialog.setWindowTitle(
            QtWidgets.QApplication.translate("helpDialog", "Help", None, QtWidgets.QApplication.UnicodeUTF8)
        )
        self.labelHelpURI.setText(
            QtWidgets.QApplication.translate(
                "helpDialog",
                '<a href="http://Bitmessage.org/wiki/PyBitmessage_Help">http://Bitmessage.org/wiki/PyBitmessage_Help</a>',
                None,
                QtWidgets.QApplication.UnicodeUTF8,
            )
        )
        self.label.setText(
            QtWidgets.QApplication.translate(
                "helpDialog",
                "As Bitmessage is a collaborative project, help can be found online in the Bitmessage Wiki:",
                None,
                QtWidgets.QApplication.UnicodeUTF8,
            )
        )
