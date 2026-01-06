# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Tue Jan 21 22:29:38 2014
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


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(360, 315)
        self.buttonBox = QtWidgets.QDialogButtonBox(aboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 280, 311, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setGeometry(QtCore.QRect(70, 126, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.labelVersion = QtWidgets.QLabel(aboutDialog)
        self.labelVersion.setGeometry(QtCore.QRect(190, 126, 161, 20))
        self.labelVersion.setObjectName("labelVersion")
        self.label_2 = QtWidgets.QLabel(aboutDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 341, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(aboutDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 331, 71))
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(aboutDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 341, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(aboutDialog)
        self.buttonBox.accepted.connect(aboutDialog.accept)
        self.buttonBox.rejected.connect(aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About", None))
        self.label.setText(_translate("aboutDialog", "PyBitmessage", None))
        self.labelVersion.setText(_translate("aboutDialog", "version ?", None))
        self.label_2.setText(
            _translate(
                "aboutDialog",
                "<html><head/><body><p>Copyright © 2012-2014 Jonathan Warren<br/>Copyright © 2013-2014 The Bitmessage Developers</p></body></html>",
                None,
            )
        )
        self.label_3.setText(
            _translate(
                "aboutDialog",
                '<html><head/><body><p>Distributed under the MIT/X11 software license; see <a href="http://www.opensource.org/licenses/mit-license.php"><span style=" text-decoration: underline; color:#0000ff;">http://www.opensource.org/licenses/mit-license.php</span></a></p></body></html>',
                None,
            )
        )
        self.label_5.setText(_translate("aboutDialog", "This is Beta software.", None))
