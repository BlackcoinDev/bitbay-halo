# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created: Wed Jul 24 12:42:01 2013
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


class Ui_connectDialog(object):
    def setupUi(self, connectDialog):
        connectDialog.setObjectName("connectDialog")
        connectDialog.resize(400, 124)
        self.gridLayout = QtWidgets.QGridLayout(connectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(connectDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.radioButtonConnectNow = QtWidgets.QRadioButton(connectDialog)
        self.radioButtonConnectNow.setChecked(True)
        self.radioButtonConnectNow.setObjectName("radioButtonConnectNow")
        self.gridLayout.addWidget(self.radioButtonConnectNow, 1, 0, 1, 2)
        self.radioButtonConfigureNetwork = QtWidgets.QRadioButton(connectDialog)
        self.radioButtonConfigureNetwork.setObjectName("radioButtonConfigureNetwork")
        self.gridLayout.addWidget(self.radioButtonConfigureNetwork, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(185, 24, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(connectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(connectDialog)
        self.buttonBox.accepted.connect(connectDialog.accept)
        self.buttonBox.rejected.connect(connectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(connectDialog)

    def retranslateUi(self, connectDialog):
        connectDialog.setWindowTitle(_translate("connectDialog", "Bitmessage", None))
        self.label.setText(_translate("connectDialog", "Bitmessage won't connect to anyone until you let it. ", None))
        self.radioButtonConnectNow.setText(_translate("connectDialog", "Connect now", None))
        self.radioButtonConfigureNetwork.setText(_translate("connectDialog", "Let me configure special network settings first", None))
