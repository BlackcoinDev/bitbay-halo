import os

from PyQt6 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


def apply(ui, mainWindow):
    mainWindow.setObjectName(_fromUtf8("MainWindow"))

    qss_base = open(mainWindow.ApplicationPath + "/gui/styles" + "/base.css", "r")
    qss_blk = open(mainWindow.ApplicationPath + "/gui/styles" + "/blk.css", "r")
    mainWindow.setStyleSheet(qss_base.read() + qss_blk.read())

    # MainWindow.resize(991, 724)
    # MainWindow.setMinimumSize(QtCore.QSize(991, 724))
    # ui.ApplicationPath.replace("\\","/")
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(_fromUtf8(ui.ApplicationPath + "/images/BlackHalo.png")),
        QtGui.QIcon.Mode.Normal,
        QtGui.QIcon.State.Off,
    )
    mainWindow.setWindowIcon(icon)
    # if ui.NewCoin['Moderator']==1:
    #    ui.label_25.setText(ui._translate("MainWindow", "Welcome to the Halo Marketplace: Moderator version", None))
    ui.webView.setHtml(
        _fromUtf8("<iframe src=" + ui.NewCoin["IRC"] + " width='100%' height='500'></iframe></div></div></div>")
    )
    # ui.MarketBox.setItemText(0, ui._translate("MainWindow", ui.NewCoin['default market'], None))

    icon1 = QtGui.QIcon()
    icon1.addPixmap(
        QtGui.QPixmap(_fromUtf8(ui.ApplicationPath + "/images/icon_attention_inactive.png")),
        QtGui.QIcon.Mode.Normal,
        QtGui.QIcon.State.Off,
    )

    mainWindow.setWindowTitle(ui._translate("MainWindow", "BlackHalo", None))

    ui.tab.MyAddress_7.setText(ui._translate("MainWindow", "Your Blackcoin Address:", None))

    ui.Symbol_1.setText(ui._translate("MainWindow", "BC", None))
    ui.Symbol_2.setText(ui._translate("MainWindow", "BC", None))
    ui.Symbol_4.setText(ui._translate("MainWindow", "BC", None))
    ui.Symbol_3.setText(ui._translate("MainWindow", "BC", None))

    ui.ReceiveBitcoins.receiveCoinAddressLabel.setText(ui._translate("MainWindow", "Your Blackcoin Address:", None))

    ui.Symbol_5.setText(ui._translate("MainWindow", "BC", None))
