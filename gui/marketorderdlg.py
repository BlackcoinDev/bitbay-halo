
import os
import sys
from PyQt6 import QtCore, QtGui, uic

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

class MyForm(QtWidgets.QDialog):
    def setupUi(self, Form):
        appfont = QtGui.QFont()
        appfont.setPixelSize(11)
        Form.setObjectName(_fromUtf8("Form"))

        base = os.path.abspath(os.path.dirname(__file__))
        qss_main = open(base+'/styles/bay/generic.css', 'r').read()
        qss_tmpl = open(base+'/styles/bay/generic.css', 'r').read()
        Form.setStyleSheet(qss_main+qss_tmpl)

        uic.loadUi(os.path.abspath(os.path.dirname(__file__))+'/forms/MarketOrder1.ui', Form)

        Form.MarketExplanation.setIconSize(QtCore.QSize(32,32))
        Form.MarketExplanation.setIcon(QtGui.QIcon(":/icons/help"))

        font = QtGui.QFont("Roboto", 12, 0)
        font.setPixelSize(15)
        Form.setFont(font)

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    import styles
    import styles.base_rc

    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtGui.QStyleFactory.create("Windows"))
    dlg = MyForm()
    dlg.show()
    sys.exit(app.exec())
