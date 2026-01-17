# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iconglossary.ui'
#
# Created: Thu Jun 13 20:15:48 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets


# Qt6/Python3: strings are already Unicode, no QString.fromUtf8 needed
def _fromUtf8(s: str) -> str:
    return s


# Qt6: translate() no longer takes an encoding parameter
def _translate(context: str, text: str, disambig: str | None) -> str:
    return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_iconGlossaryDialog(object):
    def setupUi(self, iconGlossaryDialog):
        iconGlossaryDialog.setObjectName("iconGlossaryDialog")
        iconGlossaryDialog.resize(424, 282)
        self.gridLayout = QtWidgets.QGridLayout(iconGlossaryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(iconGlossaryDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/images/redicon.png"))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/images/yellowicon.png"))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 73, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 2, 1)
        self.labelPortNumber = QtWidgets.QLabel(self.groupBox)
        self.labelPortNumber.setObjectName("labelPortNumber")
        self.gridLayout_2.addWidget(self.labelPortNumber, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/images/greenicon.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(iconGlossaryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(iconGlossaryDialog)
        self.buttonBox.accepted.connect(iconGlossaryDialog.accept)
        self.buttonBox.rejected.connect(iconGlossaryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(iconGlossaryDialog)

    def retranslateUi(self, iconGlossaryDialog):
        iconGlossaryDialog.setWindowTitle(_translate("iconGlossaryDialog", "Icon Glossary", None))
        self.groupBox.setTitle(_translate("iconGlossaryDialog", "Icon Glossary", None))
        self.label_2.setText(_translate("iconGlossaryDialog", "You have no connections with other peers. ", None))
        self.label_4.setText(
            _translate(
                "iconGlossaryDialog",
                "You have made at least one connection to a peer using an outgoing connection but "
                "you have not yet received any incoming connections. Your firewall or home router "
                "probably isn't configured to forward incoming TCP connections to your computer. "
                "Bitmessage will work just fine but it would help the Bitmessage network if you "
                "allowed for incoming connections and will help you be a better-connected node.",
                None,
            )
        )
        self.labelPortNumber.setText(_translate("iconGlossaryDialog", "You are using TCP port ?. (This can be changed in the settings).", None))
        self.label_6.setText(
            _translate(
                "iconGlossaryDialog",
                "You do have connections with other peers and your firewall is correctly configured.",
                None,
            )
        )


from . import bitmessage_icons_rc  # noqa: E402,F401
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    iconGlossaryDialog = QtWidgets.QDialog()
    ui = Ui_iconGlossaryDialog()
    ui.setupUi(iconGlossaryDialog)
    iconGlossaryDialog.show()
    sys.exit(app.exec())
