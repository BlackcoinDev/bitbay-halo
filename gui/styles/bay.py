import os

from PyQt6 import QtCore, QtGui, QtWidgets

from . import bay_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


def setupFonts(main_window):
    fonts_path = main_window.ApplicationPath + "/gui" + "/fonts"
    ttf_files = [f for f in os.listdir(fonts_path) if os.path.isfile(os.path.join(fonts_path, f)) and f.endswith(".ttf")]
    for f in ttf_files:
        QtGui.QFontDatabase.addApplicationFont(os.path.join(fonts_path, f))
    font = QtGui.QFont("Roboto", 12, 0)
    font.setPixelSize(15)
    # QtWidgets.QApplication.setFont(font)
    main_window.setFont(font)


def setupFontsForeign(main_window):
    fonts_path = main_window.ApplicationPath + "/gui" + "/fonts"
    ttf_files = [f for f in os.listdir(fonts_path) if os.path.isfile(os.path.join(fonts_path, f)) and f.endswith(".ttf")]
    for f in ttf_files:
        QtGui.QFontDatabase.addApplicationFont(os.path.join(fonts_path, f))
    font = QtGui.QFont("Arial Unicode MS", 12, 0)
    font.setPixelSize(15)
    # QtWidgets.QApplication.setFont(font)
    main_window.setFont(font)


def applyCssFiles(ui, main_window):
    base = main_window.ApplicationPath + "/gui/styles"
    qss_main = open(base + "/bay/mainwindow.css", "r")
    main_window.setStyleSheet(qss_main.read())
    qss_left = open(base + "/bay/leftpanel.css", "r")
    ui.leftPanel.setStyleSheet(qss_left.read())
    qss_home = open(base + "/bay/dashboard.css", "r")
    ui.tab.setStyleSheet(qss_home.read())
    qss_send = open(base + "/bay/sendpanel.css", "r")
    ui.SendBitcoins.setStyleSheet(qss_send.read())
    qss_recv = open(base + "/bay/receivepanel.css", "r")
    ui.ReceiveBitcoins.setStyleSheet(qss_recv.read())
    qss_hist = open(base + "/bay/historypanel.css", "r")
    ui.History.setStyleSheet(qss_hist.read())
    qss_market = open(base + "/bay/marketpanel.css", "r")
    ui.Market.setStyleSheet(qss_market.read())
    qss_makeoffer = open(base + "/bay/makeoffer.css", "r")
    ui.MakeAnOffer.setStyleSheet(qss_makeoffer.read())
    ui.MakeAnOffer.gb_create.layout().setSpacing(7)
    qss_chat = open(base + "/bay/chatpanel.css", "r")
    ui.Chat.setStyleSheet(qss_chat.read())
    qss_offers = open(base + "/bay/offerspanel.css", "r")
    ui.PendingOffers.setStyleSheet(qss_offers.read())
    qss_contracts = open(base + "/bay/contractspanel.css", "r")
    ui.OpenContracts.setStyleSheet(qss_contracts.read())
    qss_contacts = open(base + "/bay/contactspanel.css", "r")
    ui.Contacts.setStyleSheet(qss_contacts.read())


def apply(ui, main_window):
    main_window.setObjectName(_fromUtf8("MainWindow"))

    applyCssFiles(ui, main_window)

    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(main_window.ApplicationPath + "/images/BitBay.png"),
        QtGui.QIcon.Mode.Normal,
        QtGui.QIcon.State.Off,
    )
    main_window.setWindowIcon(icon)

    ui.webView.setHtml(_fromUtf8("<iframe src=" + ui.NewCoin["IRC"] + " width='100%' height='500'></iframe></div></div></div>"))
    # if ui.NewCoin.has_key('Moderator') and ui.NewCoin['Moderator']==1:
    #    ui.label_25.setText(ui._translate("MainWindow", "Welcome to the BitBay Marketplace: Moderator version", None))

    ui.tb_copyAddressToClipboard.setIcon(QtGui.QIcon(":/icons/copy"))
    ui.tb_sendPanelHelp.setIconSize(QtCore.QSize(32, 32))
    ui.tb_sendPanelHelp.setIcon(QtGui.QIcon(":/icons/help"))
    ui.AdvancedSend.setIconSize(QtCore.QSize(24, 24))
    ui.AdvancedSend.setIcon(QtGui.QIcon(":/icons/gear1"))
    ui.ExplainReceive.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainReceive.setIcon(QtGui.QIcon(":/icons/help"))
    ui.CopyAddressToClipboard.setIcon(QtGui.QIcon(":/icons/copy"))
    ui.CopyAddressToClipboard_2.setIcon(QtGui.QIcon(":/icons/copy"))
    ui.AddEmail_2.setIcon(QtGui.QIcon(":/icons/copy"))
    ui.ExplainHistory.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainHistory.setIcon(QtGui.QIcon(":/icons/help"))
    ui.CopyAddressToClipboard_5.setIcon(QtGui.QIcon(":/icons/copy"))
    ui.ExplainMarket.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainMarket.setIcon(QtGui.QIcon(":/icons/help"))
    ui.ExplainContracts.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainContracts.setIcon(QtGui.QIcon(":/icons/help"))
    ui.ExplainPending.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainPending.setIcon(QtGui.QIcon(":/icons/help"))
    ui.ExplainOpen.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainOpen.setIcon(QtGui.QIcon(":/icons/help"))
    ui.History.Refresh.setIconSize(QtCore.QSize(24, 24))
    ui.History.Refresh.setIcon(QtGui.QIcon(":/icons/reload"))
    ui.instantexplain.setIconSize(QtCore.QSize(32, 32))
    ui.instantexplain.setIcon(QtGui.QIcon(":/icons/help"))
    ui.ExplainAutoBackupOffer.setIconSize(QtCore.QSize(32, 32))
    ui.ExplainAutoBackupOffer.setIcon(QtGui.QIcon(":/icons/help"))

    ui.Market.tb_list.setIcon(QtGui.QIcon(":/icons/list"))
    ui.Market.tb_cards.setIcon(QtGui.QIcon(":/icons/cards"))

    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/images/attention_off"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

    main_window.setWindowTitle(ui._translate("MainWindow", "BitBay", None))

    ui.Symbol_1.setText(ui._translate("MainWindow", "BAY", None))
    ui.Symbol_2.setText(ui._translate("MainWindow", "BAY", None))
    ui.Symbol_4.setText(ui._translate("MainWindow", "BAY", None))
    ui.Symbol_3.setText(ui._translate("MainWindow", "BAY", None))
    ui.Symbol_5.setText(ui._translate("MainWindow", "BAY", None))

    ui.ReceiveBitcoins.receiveCoinAddressLabel.setText(ui._translate("MainWindow", "Your BitBay Address:", None))
    ui.tab.MyAddress_7.setText(ui._translate("MainWindow", "Your BitBay Address:", None))
