import os
import sys

from PyQt6 import QtCore, QtGui, uic


class Explanations(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        base = os.path.abspath(os.path.dirname(__file__))
        uic.loadUi(base + "/forms/HelpBox1.ui", self)
        qss_main = open(base + "/styles/bay/mainwindow.css", "r").read()
        self.setStyleSheet(qss_main)
        text01 = open(base + "/help/text01.htm", "r").read()
        text02 = open(base + "/help/text02.htm", "r").read()
        text03 = open(base + "/help/text03.htm", "r").read()
        text04 = open(base + "/help/text04.htm", "r").read()
        text05 = open(base + "/help/text05.htm", "r").read()
        text06 = open(base + "/help/text06.htm", "r").read()
        text07 = open(base + "/help/text07.htm", "r").read()
        text08 = open(base + "/help/text08.htm", "r").read()
        text09 = open(base + "/help/text09.htm", "r").read()
        text10 = open(base + "/help/text10.htm", "r").read()
        self.IntroductionTips.setHtml(text01)
        self.IntroductionTips_2.setHtml(text02)
        self.IntroductionTips_3.setHtml(text03)
        self.IntroductionTips_4.setHtml(text04)
        self.IntroductionTips_5.setHtml(text05)
        self.IntroductionTips_6.setHtml(text06)
        self.IntroductionTips_7.setHtml(text07)
        self.IntroductionTips_8.setHtml(text08)
        self.IntroductionTips_9.setHtml(text09)
        self.IntroductionTips_10.setHtml(text10)

    def retranslateUi(self, Form):
        self.setWindowTitle("Help.")


if __name__ == "__main__":
    import os
    import sys

    app = QtWidgets.QApplication(sys.argv)

    dlg = Explanations(None)
    dlg.exec()
