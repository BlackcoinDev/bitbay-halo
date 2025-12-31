# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ANewBitHalo.ui'
#
# Created: Wed Nov 12 19:50:27 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtWebEngineCore, QtCore, QtGui, QtWidgets, uic, QtWebEngineWidgets
import os
import sys
from . import styles
from .styles import base_rc

def _fromUtf8(s):
    return s
#import goslate
import traceback
import ast
from yandex_translate import YandexTranslate

#gstrans = goslate.Goslate()
ytrans = YandexTranslate('trnsl.1.1.20170227T075822Z.710cc070687ef49d.4773b96b2fa3e9cea7df423e9ab798c58d504036')
def compareFont(Label1, Label2):
    try:
        f=Label1.font()
        f2=Label2.font()
        s=f.pixelSize()
        s2=f2.pixelSize()
        if s==-1:
            s=f.pointSize()
            s2=f2.pointSize()
        if s > s2:
            Label1.setFont(Label2.font())
        else:
            Label2.setFont(Label1.font())
    except:
        traceback.print_exc()
    return True

class myQLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kargs):
        super(myQLineEdit, self).__init__(*args, **kargs)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,QtWidgets.QSizePolicy.Policy.Expanding))  
        self.setReadOnly(True)
        self.setMinSize(12)

    def setMinSize(self, minfs):        

        f = self.font()
        f.setPixelSize(minfs)
        f.setFamily(_fromUtf8("Roboto"))
        br = QtGui.QFontMetrics(f).boundingRect(self.text())

        self.setMinimumSize(QtCore.QSize(320, 20))
        self.setStyleSheet("""QLineEdit { background-color: white; color: black; font: bold }""")

    def setText(self, text):
        QtWidgets.QLineEdit.setText(self, text)
        self.resizeText()

    def resizeEvent(self, event):
        super(myQLineEdit, self).resizeEvent(event)
        self.resizeText()

    def resizeText(self):
        if not self.text():
            return

        #--- fetch current parameters ----

        f = self.font()
        cr = self.contentsRect()

        #--- find the font size that fits the contentsRect ---

        fs = 1                    
        while True:

            f.setPixelSize(fs)
            br =  QtGui.QFontMetrics(f).boundingRect(self.text())

            if br.height() <= cr.height() and br.width() <= cr.width():
                fs += 1
            else:
                f.setPixelSize(max(fs - 1, 1)) # backtrack
                break  

        #--- update font size ---

        self.setFont(f)

class Ui_MainWindow(object):
    try:
        def _translate(self, context, text, disambig):
            _encoding = QtWidgets.QApplication.UnicodeUTF8
            if self.language!="DEFAULT" and self.language!="en":
                if self.language not in self.translations:
                    self.translations[self.language]={}
                if text not in self.translations[self.language]:
                    if text=="":
                        return ""
                    self.translist.append(text)
                else:
                    try:
                        translateThis=ast.literal_eval(self.translations[self.language][text])
                    except:
                        translateThis=""
                    return (translateThis)
            return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        def _translate(self, context, text, disambig):
            return QtWidgets.QApplication.translate(context, text, disambig)

    def GTranslate(self):
        try:
            if self.translist==[]:
                return False
            if self.language=="en" or self.language=="DEFAULT":
                self.translist=[]
                return False
            if self.yandexAPI == "": #For now google translate is too slow without API access although this can be expanded upon
                print("Yandex API key not available")
                return False
            else:
                ytrans = YandexTranslate(self.yandexAPI)
            #The Yandex site has a 10K text size limit, so we do multiple requests
            xpos=0
            numby=0
            posy=1
            listoflists=[]
            testlist=ast.literal_eval(str(self.translist))
            endoflist=len(testlist)
            for trans in testlist:
                numby+=len(trans)
                if numby>7000:
                    listoflists.append(testlist[xpos:posy])
                    numby=0
                    xpos=posy
                else:
                    if posy==endoflist:
                        listoflists.append(testlist[xpos:posy])
                posy+=1
            resp=[]
            for mytranslist in listoflists:
                resp1=ytrans.translate(mytranslist, self.language)
                resp1=resp1['text']
                for respy in resp1:
                    resp.append(respy)
            #resp = ytrans.translate(ast.literal_eval(str(self.translist)), self.language)
            #resp = resp['text']
            pos=0
            for trans in resp:
                langtext = QtWidgets.QLabel()
                langtext.setText(trans)
                x=langtext.text()
                st=repr(x)
                st=st.replace("PyQt6.str(","")[:-1]
                translateThis=ast.literal_eval(st)
                self.translations[self.language][self.translist[pos]]=st
                pos+=1
            self.translist=[]
            return True
        except:
            print(self.translist)
            traceback.print_exc()
            return False

    def setupLeftPanel(self, left_panel):
        self.leftPanel = left_panel
        self.leftPanel.setObjectName("leftPanel")
        self.gridLayout.addWidget(self.leftPanel, 0, 0, 1, 1)

        left_panel_vbox = QtWidgets.QVBoxLayout(self.leftPanel)
        left_panel_vbox.setContentsMargins(0, 0, 0, 0)
        left_panel_vbox.setSpacing(0)

        self.leftPanelLogoWidget = QtWidgets.QWidget()
        self.leftPanelLogoWidget.setObjectName("leftPanelLogoWidget")
        left_panel_vbox.addWidget(self.leftPanelLogoWidget)

        tabsGroup = QtGui.QButtonGroup(self.leftPanel);

        tb_dashboard = QtWidgets.QToolButton()
        self.tb_dashboard=tb_dashboard
        tb_dashboard.setObjectName("dashboardButton")
        tb_dashboard.setText(self._translate("MainWindow", "Dashboard", None))
        tb_dashboard.setIconSize(QtCore.QSize(20,20))
        tb_dashboard.setIcon(QtGui.QIcon(":/icons/dashboard"))
        tb_dashboard.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_dashboard.setCheckable(True)
        tb_dashboard.setChecked(True)
        tb_dashboard.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.tab),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_dashboard)
        left_panel_vbox.addWidget(tb_dashboard)

        l_wallet = QtWidgets.QLabel()
        self.l_wallet=l_wallet
        l_wallet.setObjectName("walletLeftPanelLabel")
        l_wallet.setText(self._translate("MainWindow", "WALLET", None))
        left_panel_vbox.addWidget(l_wallet)

        tb_send = QtWidgets.QToolButton()
        self.tb_send=tb_send
        tb_send.setObjectName("sendButton")
        tb_send.setText(self._translate("MainWindow", "Send", None))
        tb_send.setIconSize(QtCore.QSize(20,20))
        tb_send.setIcon(QtGui.QIcon(":/icons/send"))
        tb_send.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_send.setCheckable(True)
        tb_send.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.SendBitcoins),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_send)
        left_panel_vbox.addWidget(tb_send)

        tb_receive = QtWidgets.QToolButton()
        self.tb_receive=tb_receive
        tb_receive.setObjectName("receiveButton")
        tb_receive.setText(self._translate("MainWindow", "Receive", None))
        tb_receive.setIconSize(QtCore.QSize(20,20))
        tb_receive.setIcon(QtGui.QIcon(":/icons/receive"))
        tb_receive.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_receive.setCheckable(True)
        tb_receive.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.ReceiveBitcoins),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_receive)
        left_panel_vbox.addWidget(tb_receive)

        tb_history = QtWidgets.QToolButton()
        self.tb_history=tb_history
        tb_history.setObjectName("historyButton")
        tb_history.setText(self._translate("MainWindow", "History", None))
        tb_history.setIconSize(QtCore.QSize(20,20))
        tb_history.setIcon(QtGui.QIcon(":/icons/history"))
        tb_history.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_history.setCheckable(True)
        tb_history.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.History),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_history)
        left_panel_vbox.addWidget(tb_history)

        l_smart_contracts = QtWidgets.QLabel()
        self.l_smart_contracts=l_smart_contracts
        l_smart_contracts.setObjectName("smartContractsLeftPanelLabel")
        l_smart_contracts.setText(self._translate("MainWindow", "SMART CONTRACTS", None))
        left_panel_vbox.addWidget(l_smart_contracts)

        tb_market = QtWidgets.QToolButton()
        self.tb_market=tb_market
        tb_market.setObjectName("marketButton")
        tb_market.setText(self._translate("MainWindow", "Marketplace", None))
        tb_market.setIconSize(QtCore.QSize(20,20))
        tb_market.setIcon(QtGui.QIcon(":/icons/marketplace"))
        tb_market.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_market.setCheckable(True)
        tb_market.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.Market),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.Alignment())
        ))
        tabsGroup.addButton(tb_market)
        left_panel_vbox.addWidget(tb_market)

        tb_makeanoffer = QtWidgets.QToolButton()
        self.tb_makeanoffer=tb_makeanoffer
        tb_makeanoffer.setObjectName("marketButton")
        tb_makeanoffer.setText(self._translate("MainWindow", "Make an offer", None))
        tb_makeanoffer.setIconSize(QtCore.QSize(20,20))
        tb_makeanoffer.setIcon(QtGui.QIcon(":/icons/makeanoffer"))
        tb_makeanoffer.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_makeanoffer.setCheckable(True)
        tb_makeanoffer.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.MakeAnOffer),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_makeanoffer)
        left_panel_vbox.addWidget(tb_makeanoffer)

        tb_pending_offer = QtWidgets.QToolButton()
        self.tb_pending_offer=tb_pending_offer
        tb_pending_offer.setObjectName("pendingOfferButton")
        tb_pending_offer.setText(self._translate("MainWindow", "Pending offers", None))
        tb_pending_offer.setIconSize(QtCore.QSize(20,20))
        tb_pending_offer.setIcon(QtGui.QIcon(":/icons/pendingoffer"))
        tb_pending_offer.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_pending_offer.setCheckable(True)
        tb_pending_offer.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.PendingOffers),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_pending_offer)
        left_panel_vbox.addWidget(tb_pending_offer)

        tb_contracts = QtWidgets.QToolButton()
        self.tb_contracts=tb_contracts
        tb_contracts.setObjectName("contractsButton")
        tb_contracts.setText(self._translate("MainWindow", "Contracts", None))
        tb_contracts.setIconSize(QtCore.QSize(20,20))
        tb_contracts.setIcon(QtGui.QIcon(":/icons/contracts"))
        tb_contracts.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_contracts.setCheckable(True)
        tb_contracts.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.OpenContracts),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_contracts)
        left_panel_vbox.addWidget(tb_contracts)

        tb_chat = QtWidgets.QToolButton()
        self.tb_chat=tb_chat
        tb_chat.setObjectName("chatButton")
        tb_chat.setText(self._translate("MainWindow", "Chat", None))
        tb_chat.setIconSize(QtCore.QSize(20,20))
        tb_chat.setIcon(QtGui.QIcon(":/icons/chat"))
        tb_chat.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_chat.setCheckable(True)
        tb_chat.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.Chat),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_chat)
        left_panel_vbox.addWidget(tb_chat)

        left_panel_vbox.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))

        tb_contacts = QtWidgets.QToolButton()
        self.tb_contacts=tb_contacts
        tb_contacts.setObjectName("contactsButton")
        tb_contacts.setText(self._translate("MainWindow", "Contacts", None))
        tb_contacts.setIconSize(QtCore.QSize(20,20))
        tb_contacts.setIcon(QtGui.QIcon(":/icons/contacts"))
        tb_contacts.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        tb_contacts.setCheckable(True)
        tb_contacts.clicked.connect(lambda: (
            self.Tabs.setCurrentWidget(self.Contacts),
            self.mainPanelWidget.setMaximumWidth(1100),
            self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter)
        ))
        tabsGroup.addButton(tb_contacts)
        left_panel_vbox.addWidget(tb_contacts)

        left_panel_vbox.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding))

    def setupMarketView(self, main_window):
        self.Market = QtWidgets.QWidget()
        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/MarketPanel.ui', self.Market)

        self.ShowWhat       = self.Market.ShowWhat
        self.SearchEdit     = self.Market.SearchEdit
        self.Search         = self.Market.Search
        self.ExplainMarket  = self.Market.ExplainMarket
        self.MarketBox      = self.Market.MarketBox
        self.OfferBox       = self.Market.OfferBox
        self.PostToMarket   = self.Market.PostToMarket
        self.SettingsMarket = self.Market.SettingsMarket
        self.JoinChan       = self.Market.JoinChan
        self.LeaveChan      = self.Market.LeaveChan
        self.OfferTable     = self.Market.OfferTable

        self.Market.tb_list.clicked.connect(lambda: self.Market.st_tables.setCurrentIndex(0))
        self.Market.tb_cards.clicked.connect(lambda: self.Market.st_tables.setCurrentIndex(1))

        page_cards_vbox = QtWidgets.QVBoxLayout(self.Market.page_cards)
        page_cards_vbox.setContentsMargins(0, 0, 0, 0)
        page_cards_vbox.setSpacing(0)

        class CardsTableView(QtWidgets.QTableView):
            def __init__(self, *args, **kargs):
                super(CardsTableView, self).__init__(*args, **kargs)
                self.clicked.connect(self.itemClicked)
            def resizeEvent(self, re):
                super(CardsTableView, self).resizeEvent(re)
                w = re.size().width()
                self.model().setViewWidth(w)
            cellPressed = QtCore.pyqtSignal(int, int)
            def itemClicked(self,prx_mi):
                prx = self.model()
                src = self.model().sourceModel()
                src_mi = prx.mapToSource(prx_mi)
                self.cellPressed.emit(src_mi.row(),0)

        tv_cards = CardsTableView()
        tv_cards.setObjectName("tv_cards")
        tv_cards.verticalHeader().hide()
        tv_cards.horizontalHeader().hide()
        page_cards_vbox.addWidget(tv_cards)

        class CardsTableDelegate(QtGui.QItemDelegate):
            def __init__(self, *args, **kargs):
                super(CardsTableDelegate, self).__init__(*args, **kargs)
                self.iconSize = 146
                self.textSize = 13
            def paint(self, painter, option, index):
                if option.state & QtGui.QStyle.State_Selected:
                    painter.fillRect(option.rect, option.palette.highlight())
                vdata = index.data(QtCore.Qt.DecorationRole)
                if vdata.type()==QtCore.QVariant.Icon:
                    icon = QtGui.QIcon(vdata)
                    sp = QtCore.QSize(self.iconSize,self.iconSize)
                    s = QtCore.QSizeF(icon.actualSize(sp))
                    if s.isValid():
                        if s.width()>s.height():
                            r = s.width()/146.0
                            s = s/r
                        else:
                            r = s.height()/146.0
                            s = s/r
                        pix = icon.pixmap(sp)
                        r = QtCore.QRect(option.rect)
                        r.setHeight(r.width())
                        r.adjust(2,2,-2,-2)
                        if s.width() > s.height():
                            dy = (s.width()-s.height())/2
                            r.adjust(0,dy,0,-dy)
                        else:
                            dx = (s.height()-s.width())/2
                            r.adjust(dx,0,-dx,0)
                        painter.drawPixmap(r, pix)
                r1 = option.rect

                t1data = index.data(QtCore.Qt.UserRole+100+2).toString()
                t2data = index.data(QtCore.Qt.UserRole+100+3).toString()
                t3data = index.data(QtCore.Qt.UserRole+100+1).toString()
                t1data = t1data.replace('\n',' ')
                t2data = t2data.replace('\n',' ')
                t3data = t3data.replace('\n',' ')

                font = QtGui.QFont("Roboto", 12, 0)
                font.setPixelSize(self.textSize)
                painter.setFont(font)
                painter.setPen(QtGui.QColor("#404040"))
                font_metrics = QtGui.QFontMetrics(font)

                r1.adjust(0,self.iconSize,0,0)
                r1.setHeight(self.textSize+1)
                t1data = font_metrics.elidedText(t1data, QtCore.Qt.ElideRight, r1.width())
                painter.drawText(QtCore.QRectF(r1).adjusted(0,0,0,3), t1data)

                r2 = r1
                r2.adjust(0,self.textSize+1,0,self.textSize+1)
                t2data = font_metrics.elidedText(t2data, QtCore.Qt.ElideRight, r2.width())
                painter.drawText(QtCore.QRectF(r2).adjusted(0,0,0,3), t2data)

                r3 = r2
                r3.adjust(0,self.textSize+1,0,self.textSize+1)
                t3data = font_metrics.elidedText(t3data, QtCore.Qt.ElideRight, r3.width())
                painter.setPen(QtGui.QColor("#8080e0"))
                painter.drawText(QtCore.QRectF(r3).adjusted(0,0,0,3), t3data)

        class CardsTableModel(QtGui.QAbstractProxyModel):
            def __init__(self, *args, **kargs):
                super(CardsTableModel, self).__init__(*args, **kargs)
                self.rows = 0
                self.cols = 1
            def setSourceModel(self, sm):
                super(CardsTableModel, self).setSourceModel(sm)
                sm.dataChanged.connect( self.reset)
                sm.rowsInserted.connect( self.reset)
                sm.rowsRemoved.connect( self.reset)
                sm.modelReset.connect( self.reset)
            def rowCount(self, parent =QtCore.QModelIndex()):
                if parent.isValid(): return 0
                return self.rows
            def columnCount(self, parent =QtCore.QModelIndex()):
                if parent.isValid(): return 0
                return self.cols
            def index(self, row, col, parent =QtCore.QModelIndex()):
                if parent.isValid(): return QtCore.QModelIndex()
                return self.createIndex(row,col);
            def parent(self, idx =QtCore.QModelIndex()):
                return QtCore.QModelIndex()
            def mapToSource (self, prx_mi):
                if not prx_mi.isValid(): return QtCore.QModelIndex()
                r = prx_mi.row()
                c = prx_mi.column()
                n = r*self.cols+c
                src_mi = self.sourceModel().index(n, 0, QtCore.QModelIndex())
                return src_mi
            def mapFromSource (self, src_mi):
                if not src_mi.isValid(): return QtCore.QModelIndex()
                n = src_mi.row()
                r = n/self.cols
                c = n % self.cols
                src_mi = self.index(r, c, QtCore.QModelIndex())
                return src_mi
            def setViewForRowCounting(self, view):
                self.viewForRowCounting = view
            def setViewWidth(self, w):
                n = self.sourceModel().rowCount()
                if n==0 or w==0:
                    self.rows = 0
                    self.cols = 0
                    self.reset()
                    return
                card_w = 150
                self.cols = max(1,min(n,w/card_w))
                self.rows = min(n,max(1,n/self.cols))
                if (self.cols*self.rows)<n:
                    self.rows = self.rows+1
                self.reset()
                for r in range(0,self.rows):
                    self.viewForRowCounting.setRowHeight(r, 200)
                for c in range(0,self.cols):
                    self.viewForRowCounting.setColumnWidth(c, 150)
            def data(self, prx_idx, role):
                if role>=QtCore.Qt.UserRole+100 and role<QtCore.Qt.UserRole+200:
                    req_col = role-(QtCore.Qt.UserRole+100)
                    src_mi = self.mapToSource(prx_idx)
                    if src_mi.isValid():
                        src_mi_req = src_mi.model().index(src_mi.row(),req_col)
                        return src_mi_req.data()
                return super(CardsTableModel, self).data(prx_idx, role)

        proxy = CardsTableModel(main_window)
        proxy.setViewForRowCounting(tv_cards)
        proxy.setSourceModel(self.Market.OfferTable.model())
        tv_cards.setIconSize(QtCore.QSize(100,100))
        tv_cards.setModel(proxy)
        self.cardsViewTable = tv_cards

        delegate = CardsTableDelegate(main_window)
        tv_cards.setItemDelegate(delegate)

        icon26 = QtGui.QIcon()
        icon27 = QtGui.QIcon()

        icon26.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_search_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_join_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.Tabs.addWidget(self.Market)

    def setupMyFonts(self, main_window):
        if not hasattr(self, 'language'):
            self.language="en"
        if hasattr(self, 'style'):
            if hasattr(self.style, 'setupFonts'):
                if self.language=="DEFAULT" or self.language=="en":
                    self.style.setupFonts(main_window)
                else:
                    self.style.setupFontsForeign(main_window)

    def setWalletLocked(self, is_locked):
        ic = QtGui.QIcon()
        if is_locked:
            ic.addPixmap(QtGui.QPixmap(":/icons/ind_locked"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        else: ic.addPixmap(QtGui.QPixmap(self.ApplicationPath+"/gui"+"/icons/bitbay/ind_unlocked.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tb_indicatorsLock.setIcon(ic)

    def setStakingActive(self, is_active):
        ic = QtGui.QIcon()
        if is_active:
            ic.addPixmap(QtGui.QPixmap(":/icons/ind_stake_on"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        else: ic.addPixmap(QtGui.QPixmap(":/icons/ind_stake_off"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tb_indicatorsStake.setIcon(ic)

    def setCoinPeersCount(self, peers_count):
        ic = QtGui.QIcon()
        if peers_count <1:      ic.addPixmap(QtGui.QPixmap(":/icons/ind_net0"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        elif peers_count <5:    ic.addPixmap(QtGui.QPixmap(":/icons/ind_net1"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        elif peers_count <9:    ic.addPixmap(QtGui.QPixmap(":/icons/ind_net2"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        elif peers_count <15:   ic.addPixmap(QtGui.QPixmap(":/icons/ind_net3"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        else:
            ic.addPixmap(QtGui.QPixmap(":/icons/ind_net4"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tb_indicatorsNet.setIcon(ic)

    def setBlockchainInSync(self, is_sync):
        ic = QtGui.QIcon()
        if is_sync:
            ic.addPixmap(QtGui.QPixmap(":/icons/ind_sync"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        else: ic.addPixmap(QtGui.QPixmap(":/icons/ind_unsync"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tb_indicatorsSync.setIcon(ic)

    def setupUi(self, main_window):
        self.translist=[]

        self.setupMyFonts(main_window)

        if not hasattr(self, 'NewCoin'):
            self.NewCoin={}

        self.translist=[]
        self.NewCoin['IRC']="http://webchat.freenode.net?channels=BitHalo,#Blackcoin&amp;uio=OT10cnVlJjExPTIzNg6b"

        #db = QtGui.QFontDatabase()
        #for f in db.families():
        #    print(str(f.toUtf8()))
        #print(list(map(str, QtWidgets.QStyleFactory.keys())))

        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Windows"))

        main_window.setObjectName(_fromUtf8("MainWindow"))
        main_window.setMinimumSize(QtCore.QSize(990, 720))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/BitHalo.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        main_window.setWindowIcon(icon)
        main_window.setStatusBar(None)

        self.centralwidget = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        main_window.setCentralWidget(self.centralwidget)

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.setupLeftPanel(QtWidgets.QWidget())

        self.bottomPanel = QtWidgets.QWidget()
        self.bottomPanel.setFixedHeight(42)
        self.bottomPanel.setObjectName(_fromUtf8("bottomPanel"))
        self.gridLayout.addWidget(self.bottomPanel, 1, 0, 1, 2)

        bottom_panel_hbox = QtWidgets.QHBoxLayout(self.bottomPanel)
        bottom_panel_hbox.setContentsMargins(0, 0, 0, 0)
        bottom_panel_hbox.setSpacing(0)

        self.indicatorsBar = QtWidgets.QWidget()
        self.indicatorsBar.setObjectName(_fromUtf8("indicatorsBar"))
        bottom_panel_hbox.addWidget(self.indicatorsBar)

        indicators_bar_hbox = QtWidgets.QHBoxLayout(self.indicatorsBar)
        indicators_bar_hbox.setContentsMargins(0, 0, 0, 0)
        indicators_bar_hbox.setSpacing(12)
        indicators_bar_hbox.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed))

        ic_locked = QtGui.QIcon()
        ic_locked.addPixmap(QtGui.QPixmap(":/icons/ind_locked"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.tb_indicatorsLock = QtWidgets.QToolButton()
        self.tb_indicatorsLock.setStyleSheet("QToolButton{background: transparent; border: 0px;}")
        self.tb_indicatorsLock.setObjectName("tb_indicatorsLock")
        self.tb_indicatorsLock.setIconSize(QtCore.QSize(22,22))
        self.tb_indicatorsLock.setMinimumSize(QtCore.QSize(22,22))
        self.tb_indicatorsLock.setIcon(ic_locked)
        self.tb_indicatorsLock.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_indicatorsLock.setCheckable(False)
        #self.tb_indicatorsLock.clicked.connect(lambda: pass)
        indicators_bar_hbox.addWidget(self.tb_indicatorsLock)

        ic_stake = QtGui.QIcon()
        ic_stake.addPixmap(QtGui.QPixmap(":/icons/ind_stake_off"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.tb_indicatorsStake = QtWidgets.QToolButton()
        self.tb_indicatorsStake.setStyleSheet("QToolButton{background: transparent; border: 0px;}")
        self.tb_indicatorsStake.setObjectName("tb_indicatorsStake")
        self.tb_indicatorsStake.setIconSize(QtCore.QSize(22,22))
        self.tb_indicatorsStake.setMinimumSize(QtCore.QSize(22,22))
        self.tb_indicatorsStake.setIcon(ic_stake)
        self.tb_indicatorsStake.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_indicatorsStake.setCheckable(False)
        #self.tb_indicatorsLock.clicked.connect(lambda: pass)
        indicators_bar_hbox.addWidget(self.tb_indicatorsStake)

        ic_net = QtGui.QIcon()
        ic_net.addPixmap(QtGui.QPixmap(":/icons/ind_net0"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.tb_indicatorsNet = QtWidgets.QToolButton()
        self.tb_indicatorsNet.setStyleSheet("QToolButton{background: transparent; border: 0px;}")
        self.tb_indicatorsNet.setObjectName("tb_indicatorsNet")
        self.tb_indicatorsNet.setIconSize(QtCore.QSize(22,22))
        self.tb_indicatorsNet.setMinimumSize(QtCore.QSize(22,22))
        self.tb_indicatorsNet.setIcon(ic_net)
        self.tb_indicatorsNet.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_indicatorsNet.setCheckable(False)
        #self.tb_indicatorsLock.clicked.connect(lambda: pass)
        indicators_bar_hbox.addWidget(self.tb_indicatorsNet)

        ic_sync = QtGui.QIcon()
        ic_sync.addPixmap(QtGui.QPixmap(":/icons/ind_unsync"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.tb_indicatorsSync = QtWidgets.QToolButton()
        self.tb_indicatorsSync.setStyleSheet("QToolButton{background: transparent; border: 0px;}")
        self.tb_indicatorsSync.setObjectName("tb_indicatorsSync")
        self.tb_indicatorsSync.setIconSize(QtCore.QSize(22,22))
        self.tb_indicatorsSync.setMinimumSize(QtCore.QSize(22,22))
        self.tb_indicatorsSync.setIcon(ic_sync)
        self.tb_indicatorsSync.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_indicatorsSync.setCheckable(False)
        #self.tb_indicatorsLock.clicked.20.connect( QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed))

        self.labelProgress = QtWidgets.QLabel()
        self.labelProgress.setObjectName(_fromUtf8("labelProgress"))
        self.labelProgress.setText("Synchronizing.")
        bottom_panel_hbox.addWidget(self.labelProgress)

        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(10)
        bottom_panel_hbox.addWidget(self.progressBar)

        self.Rescan = QtWidgets.QToolButton()
        self.Rescan.setObjectName("rescanButton")
        self.Rescan.setText(self._translate("MainWindow", "Rescan", None))
        self.Rescan.setIconSize(QtCore.QSize(20,20))
        self.Rescan.setIcon(QtGui.QIcon(":/icons/rescan"))
        self.Rescan.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        bottom_panel_hbox.addWidget(self.Rescan)
        bottom_panel_hbox.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))

        self.mainPanelWidget = QtWidgets.QWidget()
        self.mainPanelWidget.setObjectName("mainPanelWidget")
        self.mainPanelWidget.setMaximumWidth(1100)

        main_panel_vbox = QtWidgets.QVBoxLayout(self.mainPanelWidget)
        main_panel_vbox.setContentsMargins(0, 0, 0, 0)
        main_panel_vbox.setSpacing(0)

        top_panel = QtWidgets.QWidget()
        top_panel.setObjectName("topPanelWidget")
        main_panel_vbox.addWidget(top_panel)

        self.Tabs = QtWidgets.QStackedWidget()
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        main_panel_vbox.addWidget(self.Tabs)

        self.gridLayout.addWidget(self.mainPanelWidget, 0, 1, 1, 1)
        self.gridLayout.setAlignment(self.mainPanelWidget, QtCore.Qt.AlignmentFlag.AlignHCenter);

        self.tab = QtWidgets.QWidget()
        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/HomePanel.ui', self.tab)
        self.tab.le_actualBalance=myQLineEdit(self.tab.le_actualBalance)
        self.tab.le_availableBalance=myQLineEdit(self.tab.le_availableBalance)
        self.tb_copyAddressToClipboard = self.tab.tb_copyAddressToClipboard
        self.l_availableBalance = self.tab.l_availableBalance
        self.WelcomeActualBalance = self.tab.l_actualBalance
        self.WelcomeAvailableBalance = self.tab.l_availableBalance
        self.MyBalance_3 = self.tab.le_actualBalance
        self.MyBalance_4 = self.tab.le_availableBalance
        self.Symbol_1 = self.tab.Symbol_1
        self.Symbol_2 = self.tab.Symbol_2
        self.OpenAccount = self.tab.OpenAccount
        self.JointAccount = self.tab.JointAccount
        self.HireSomeone = self.tab.HireSomeone
        self.Barter = self.tab.Barter
        self.Custom = self.tab.Custom
        self.FindJob = self.tab.FindJob
        self.BuyAnything = self.tab.BuyAnything
        self.BuyCoins = self.tab.BuyCoins
        self.VideoLibrary = self.tab.VideoLibrary
        self.Conversion = self.tab.Conversion

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_attention_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_copypaste_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_openaccount_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_jointaccount_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_hire_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_trade_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_contract_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_findjob_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_buysell_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_buycoins_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_video_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_rescan_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.Tabs.addWidget(self.tab)
        self.SendBitcoins = QtWidgets.QWidget()

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/SendPanel.ui', self.SendBitcoins)
        self.SendBitcoins.le_actualBalance=myQLineEdit(self.SendBitcoins.le_actualBalance)
        self.SendBitcoins.le_availableBalance=myQLineEdit(self.SendBitcoins.le_availableBalance)

        self.PayToLabel = self.SendBitcoins.PayToLabel
        self.AmountLabel = self.SendBitcoins.AmountLabel
        self.FeeLabel = self.SendBitcoins.FeeLabel
        self.l_actualBalance = self.SendBitcoins.l_actualBalance
        self.l_availableBalance = self.SendBitcoins.l_availableBalance
        self.SendActualBalance = self.SendBitcoins.l_actualBalance
        self.SendAvailableBalance = self.SendBitcoins.l_availableBalance
        self.MyBalance_7 = self.SendBitcoins.le_actualBalance
        self.MyBalance_8 = self.SendBitcoins.le_availableBalance
        self.Symbol_3 = self.SendBitcoins.Symbol_3
        self.Symbol_4 = self.SendBitcoins.Symbol_4
        self.AdvancedSend = self.SendBitcoins.AdvancedSend
        self.tb_sendPanelHelp = self.SendBitcoins.tb_sendPanelHelp
        self.SendMyBitcoins = self.SendBitcoins.SendMyBitcoins
        self.CreateSignatureOne = self.SendBitcoins.CreateSignatureOne
        self.OpenBitSignatureAndSend = self.SendBitcoins.OpenBitSignatureAndSend
        self.BitAmount = self.SendBitcoins.BitAmount
        self.BitFee = self.SendBitcoins.BitFee
        self.BitPayTo = self.SendBitcoins.BitPayTo

        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_gear_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_makeoffer_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_add_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.Tabs.addWidget(self.SendBitcoins)
        self.ReceiveBitcoins = QtWidgets.QWidget()

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/ReceivePanel.ui', self.ReceiveBitcoins)
        #self.ReceiveBitcoins.layout().setAlignment(self.ReceiveBitcoins.receiveCoinsGroupBox, QtCore.Qt.AlignmentFlag.AlignLeft);

        self.ExplainReceive = self.ReceiveBitcoins.ExplainReceive
        self.ExplainSpend = self.tb_sendPanelHelp
        self.CopyAddressToClipboard = self.ReceiveBitcoins.CopyAddressToClipboard
        self.CopyAddressToClipboard_2 = self.ReceiveBitcoins.CopyAddressToClipboard_2
        self.CopyAddressToClipboard_3 = self.tb_copyAddressToClipboard
        self.BitmessageStatus = self.ReceiveBitcoins.BitmessageStatus
        self.EnableBitmessage = self.ReceiveBitcoins.EnableBitmessage
        self.EnableIRC = self.ReceiveBitcoins.EnableIRC
        self.MyEmail = self.ReceiveBitcoins.MyEmail
        self.AddEmail_2 = self.ReceiveBitcoins.AddEmail_2
        self.EmailStatus = self.ReceiveBitcoins.EmailStatus
        self.EmailBox = self.ReceiveBitcoins.EmailBox
        self.AddEmail = self.ReceiveBitcoins.AddEmail
        self.EnableEmail = self.ReceiveBitcoins.EnableEmail
        self.OutboxButton = self.ReceiveBitcoins.OutboxButton

        self.Tabs.addWidget(self.ReceiveBitcoins)

        self.History = QtWidgets.QWidget()

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/HistoryPanel.ui', self.History)
        self.History.FullHistory.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.History.le_myAddress.setReadOnly(True)
        self.History.le_balance.setReadOnly(True)

        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_export_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.CopyAddressToClipboard_5 = self.History.CopyAddressToClipboard_5
        self.HistoryBalance = self.History.HistoryBalance
        self.MyBalance = self.History.le_balance
        self.Symbol_5 = self.History.Symbol_5
        self.TitleRecent = self.History.TitleRecent
        self.KeysConnected = self.History.KeysConnected
        self.Refresh = self.History.Refresh
        self.History_Title = self.History.History_Title
        self.ExplainHistory = self.History.ExplainHistory
        self.FullHistory = self.History.FullHistory
        self.ExportToCSV = self.History.ExportToCSV
        self.ClearHistory = self.History.ClearHistory
        self.HistorylistWidget = self.History.HistorylistWidget

        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_trash_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.Tabs.addWidget(self.History)
        self.Chat = QtWidgets.QWidget()
        self.Chat.setObjectName(_fromUtf8("Chat"))

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/ChatPanel.ui', self.Chat)
        self.Chat.webView = QtWebEngineWidgets.QWebEngineView(self.Chat.gb_chat)
        self.Chat.gridLayout.addWidget(self.Chat.webView, 0, 0, 1, 1)
        self.Chat.webView.setEnabled(True)        

        self.webView = self.Chat.webView
        self.webView.setHtml(_fromUtf8("<iframe src="+self.NewCoin['IRC']+" width='100%' height='500'></iframe></div></div></div>"))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.Tabs.addWidget(self.Chat)
        self.MakeAnOffer = QtWidgets.QWidget()

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/MakeOfferPanel.ui', self.MakeAnOffer)

        self.ExplainContracts = self.MakeAnOffer.ExplainContracts
        self.SendLabel_3 = self.MakeAnOffer.SendLabel_3
        self.SendLabel_4 = self.MakeAnOffer.SendLabel_4
        self.AttachImage = self.MakeAnOffer.AttachImage
        self.SendLabel = self.MakeAnOffer.SendLabel
        self.ContractTo = self.MakeAnOffer.ContractTo
        self.ContractAmount = self.MakeAnOffer.ContractAmount
        self.ContractAmountLabel = self.MakeAnOffer.ContractAmountLabel
        self.InstantAmount = self.MakeAnOffer.InstantAmount
        self.YouDeposit = self.MakeAnOffer.YouDeposit
        self.TheyDeposit = self.MakeAnOffer.TheyDeposit
        self.ContractTime = self.MakeAnOffer.ContractTime
        self.DescriptionBox = self.MakeAnOffer.DescriptionBox
        self.ImageBox = self.MakeAnOffer.ImageBox
        self.WhoPays = self.MakeAnOffer.WhoPays
        self.ContractFeeLabel = self.MakeAnOffer.ContractFeeLabel
        self.DepositLabel = self.MakeAnOffer.DepositLabel
        self.TheDepositLabel = self.MakeAnOffer.TheDepositLabel
        self.TimeToCompleteLabel = self.MakeAnOffer.TimeToCompleteLabel
        self.DaysMultiplier = self.MakeAnOffer.DaysMultiplier
        self.AutoBackupLabel_2 = self.MakeAnOffer.AutoBackupLabel_2
        self.ExplainAutoBackupOffer = self.MakeAnOffer.ExplainAutoBackupOffer
        self.TxBackupPath = self.MakeAnOffer.TxBackupPath
        self.BrowseTxBackup = self.MakeAnOffer.BrowseTxBackup
        self.InstantRefundLabel = self.MakeAnOffer.InstantRefundLabel
        self.instantexplain = self.MakeAnOffer.instantexplain
        self.InstantAmountLabel = self.MakeAnOffer.InstantAmountLabel
        self.InstantWhoPays = self.MakeAnOffer.InstantWhoPays
        self.SendContract = self.MakeAnOffer.SendContract
        self.ContractFee = self.MakeAnOffer.ContractFee
        self.ContractFeeLabel = self.MakeAnOffer.ContractFeeLabel

        self.Tabs.addWidget(self.MakeAnOffer)

        self.PendingOffers = QtWidgets.QWidget()

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/PendingOffersPanel.ui', self.PendingOffers)

        self.checkBox = self.PendingOffers.checkBox
        self.FilterCustom = self.PendingOffers.FilterCustom
        self.DisableSpamFilter = self.PendingOffers.DisableSpamFilter
        self.ExplainPending = self.PendingOffers.ExplainPending
        self.MyPendingOffers = self.PendingOffers.MyPendingOffers

        self.Tabs.addWidget(self.PendingOffers)

        self.OpenContracts = QtWidgets.QWidget()

        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/OpenContractsPanel.ui', self.OpenContracts)

        self.ExplainOpen = self.OpenContracts.ExplainOpen
        self.MyOpenContracts = self.OpenContracts.MyOpenContracts

        self.Tabs.addWidget(self.OpenContracts)

        self.setupMarketView(main_window)

        self.Contacts = QtWidgets.QWidget()
        uic.loadUi(self.ApplicationPath+"/gui"+'/forms/ContactsPanel.ui', self.Contacts)

        self.NewContact = self.Contacts.NewContact
        self.BackupContacts = self.Contacts.BackupContacts
        self.ContactTable = self.Contacts.ContactTable

        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_addcontact_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/gui"+"/images/icon_backup_active.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.Tabs.addWidget(self.Contacts)

        self.menubar = QtWidgets.QMenuBar(main_window)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuDonate = QtWidgets.QMenu(self.menubar)
        self.menuDonate.setObjectName(_fromUtf8("menuDonate"))
        main_window.setMenuBar(self.menubar)
        self.actionNew_Wallet = QtGui.QAction(main_window)
        self.actionNew_Wallet.setObjectName(_fromUtf8("actionNew_Wallet"))
        self.actionOpen_Wallet = QtGui.QAction(main_window)
        self.actionOpen_Wallet.setObjectName(_fromUtf8("actionOpen_Wallet"))
        self.actionSave_Copy = QtGui.QAction(main_window)
        self.actionSave_Copy.setObjectName(_fromUtf8("actionSave_Copy"))
        self.actionEncrypt_Keyfile = QtGui.QAction(main_window)
        self.actionEncrypt_Keyfile.setObjectName(_fromUtf8("actionEncrypt_Keyfile"))
        self.actionEncrypt_Decrypt = QtGui.QAction(main_window)
        self.actionEncrypt_Decrypt.setObjectName(_fromUtf8("actionEcrypt_Decrypt"))
        self.actionSign_Verify = QtGui.QAction(main_window)
        self.actionSign_Verify.setObjectName(_fromUtf8("actionSign_Verify"))
        self.actionExit = QtGui.QAction(main_window)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(main_window)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionDocumentation_2 = QtGui.QAction(main_window)
        self.actionDocumentation_2.setObjectName(_fromUtf8("actionDocumentation_2"))
        self.actionOfficial_Website = QtGui.QAction(main_window)
        self.actionOfficial_Website.setObjectName(_fromUtf8("actionOfficial_Website"))
        self.actionDynamic_Peg_Info = QtGui.QAction(main_window)
        self.actionDynamic_Peg_Info.setObjectName(_fromUtf8("actionDynamic_Peg_Info"))
        self.actionBuy_me_a_beer = QtGui.QAction(main_window)
        self.actionBuy_me_a_beer.setObjectName(_fromUtf8("actionBuy_me_a_beer"))
        self.actionKey_To_Image = QtGui.QAction(main_window)
        self.actionKey_To_Image.setObjectName(_fromUtf8("actionKey_To_Image"))
        self.actionUnlock_Wallet = QtGui.QAction(main_window)
        self.actionUnlock_Wallet.setObjectName(_fromUtf8("Unlock_Wallet"))
        self.actionLanguage = QtGui.QAction(main_window)
        self.actionLanguage.setObjectName(_fromUtf8("Language"))
        self.actionGeneral_Settings = QtGui.QAction(main_window)
        self.actionGeneral_Settings.setObjectName(_fromUtf8("General_Settings"))
        self.actionAdvanced_Sending = QtGui.QAction(main_window)
        self.actionAdvanced_Sending.setObjectName(_fromUtf8("Advanced_Sending"))
        self.actionTranslation_Editor = QtGui.QAction(main_window)
        self.actionTranslation_Editor.setObjectName(_fromUtf8("Translation_Editor"))
        self.actionAPI = QtGui.QAction(main_window)
        self.actionAPI.setObjectName(_fromUtf8("Activate_API"))
        self.DConsole = QtGui.QAction(main_window)
        self.DConsole.setObjectName(_fromUtf8("Debug Console"))

        self.menuFile.addAction(self.actionNew_Wallet)
        self.menuFile.addAction(self.actionOpen_Wallet)
        self.menuFile.addAction(self.actionSave_Copy)
        self.menuFile.addAction(self.actionEncrypt_Keyfile)
        self.menuFile.addAction(self.actionKey_To_Image)
        self.menuFile.addAction(self.actionUnlock_Wallet)
        self.menuFile.addAction(self.actionEncrypt_Decrypt)
        self.menuFile.addAction(self.actionSign_Verify)
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionLanguage)
        self.menuSettings.addAction(self.actionGeneral_Settings)
        self.menuSettings.addAction(self.actionAdvanced_Sending)
        self.menuSettings.addAction(self.actionTranslation_Editor)
        self.menuSettings.addAction(self.actionAPI)
        self.menuSettings.addAction(self.DConsole)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDocumentation_2)
        self.menuHelp.addAction(self.actionOfficial_Website)
        self.menuHelp.addAction(self.actionDynamic_Peg_Info)
        self.menuDonate.addAction(self.actionBuy_me_a_beer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuDonate.menuAction())
        self.retranslateUi(main_window)

        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.setIcons()

        if hasattr(self, 'style'):
            if hasattr(self.style, 'apply'):
                self.style.apply(self, main_window)

        self.commandLinkButton = QtWidgets.QPushButton(self.centralwidget)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(500, 40))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(900, 40))
        self.commandLinkButton.move(450,25)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(_fromUtf8("QPushButton#commandLinkButton {\n"
        "    font: bold 14px \"Roboto\";\n"
        "color: #f2f2f2;\n"
        "    background-color: Transparent;\n"
        "    background-repeat:no-repeat;\n"
        "    border: none;\n"
        "    outline:none;\n"
        "     \n"
        "}\n"
        " QPushButton#commandLinkButton:pressed {\n"
        "    background-color: Transparent;\n"
        "    background-repeat:no-repeat;\n"
        "    border: none;\n"
        "    outline:none;\n"
        "\n"
        " }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(self.ApplicationPath+"/images/icon_attention_inactive.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton.setDefault(False)
        self.commandLinkButton.setFlat(False)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))

    def setIcons(self):
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/tabs/home_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon13.addPixmap(QtGui.QPixmap(":/icons/tabs/home_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(0,icon13)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/tabs/send_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon17.addPixmap(QtGui.QPixmap(":/icons/tabs/send_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(1,icon17)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/tabs/receive_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon18.addPixmap(QtGui.QPixmap(":/icons/tabs/receive_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(2,icon18)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/tabs/history_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon21.addPixmap(QtGui.QPixmap(":/icons/tabs/history_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(3,icon21)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/tabs/chat_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon22.addPixmap(QtGui.QPixmap(":/icons/tabs/chat_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(4,icon22)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/tabs/makeoffer_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon23.addPixmap(QtGui.QPixmap(":/icons/tabs/makeoffer_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(5,icon23)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/tabs/pendingoffers_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon24.addPixmap(QtGui.QPixmap(":/icons/tabs/pendingoffers_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(6,icon24)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/tabs/orders_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon25.addPixmap(QtGui.QPixmap(":/icons/tabs/orders_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(7,icon25)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/icons/tabs/market_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon28.addPixmap(QtGui.QPixmap(":/icons/tabs/market_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(8,icon28)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/icons/tabs/contacts_on"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon31.addPixmap(QtGui.QPixmap(":/icons/tabs/contacts_off"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        #self.Tabs.setTabIcon(9,icon31)
        self.tab.OpenAccount.setIconSize(QtCore.QSize(80,80))
        self.tab.OpenAccount.setIcon(QtGui.QIcon(":/icons/openwallet"))
        self.tab.JointAccount.setIconSize(QtCore.QSize(80,80))
        self.tab.JointAccount.setIcon(QtGui.QIcon(":/icons/newaccount"))
        self.tab.VideoLibrary.setIconSize(QtCore.QSize(80,80))
        self.tab.VideoLibrary.setIcon(QtGui.QIcon(":/icons/tutorialvideos"))
        self.tab.supportButton.setIconSize(QtCore.QSize(80,80))
        self.tab.supportButton.setIcon(QtGui.QIcon(":/icons/support"))
        self.tab.BuyAnything.setIconSize(QtCore.QSize(80,80))
        self.tab.BuyAnything.setIcon(QtGui.QIcon(":/icons/buysellanything"))
        self.tab.Custom.setIconSize(QtCore.QSize(80,80))
        self.tab.Custom.setIcon(QtGui.QIcon(":/icons/customcontract"))
        self.tab.BuyCoins.setIconSize(QtCore.QSize(80,80))
        self.tab.BuyCoins.setIcon(QtGui.QIcon(":/icons/buysellcoins"))
        self.tab.Barter.setIconSize(QtCore.QSize(80,80))
        self.tab.Barter.setIcon(QtGui.QIcon(":/icons/bartertrade"))
        self.tab.FindJob.setIconSize(QtCore.QSize(80,80))
        self.tab.FindJob.setIcon(QtGui.QIcon(":/icons/findajob"))
        self.tab.HireSomeone.setIconSize(QtCore.QSize(80,80))
        self.tab.HireSomeone.setIcon(QtGui.QIcon(":/icons/hiresomeone"))

    def retranslateUi(self, MainWindow):
        self.retranslateUi2(MainWindow)
        res=self.GTranslate()#Check to see if we have translations
        if res==True:
            self.retranslateUi2(MainWindow)
        self.adjustSize()

    def retranslateUi2(self, MainWindow):
        m=self._translate("MainWindow","Not connected to internet!", None)
        MainWindow.setWindowTitle(self._translate("MainWindow", "BitHalo", None))
        self.tab.tb_copyAddressToClipboard.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.tb_dashboard.setText(self._translate("MainWindow", "Dashboard", None))
        self.l_wallet.setText(self._translate("MainWindow", "WALLET", None))
        self.tb_send.setText(self._translate("MainWindow", "Send", None))
        self.tb_receive.setText(self._translate("MainWindow", "Receive", None))
        self.tb_history.setText(self._translate("MainWindow", "History", None))
        self.l_smart_contracts.setText(self._translate("MainWindow", "SMART CONTRACTS", None))
        self.tb_market.setText(self._translate("MainWindow", "Marketplace", None))
        self.tb_makeanoffer.setText(self._translate("MainWindow", "Make an offer", None))
        self.tb_pending_offer.setText(self._translate("MainWindow", "Pending offers", None))
        self.tb_contracts.setText(self._translate("MainWindow", "Contracts", None))
        self.tb_chat.setText(self._translate("MainWindow", "Chat", None))
        self.tb_contacts.setText(self._translate("MainWindow", "Contacts", None))
        self.tab.walletsGroupBox.setTitle(self._translate("MainWindow", "Wallets", None))
        self.tab.smartContractsGroupBox.setTitle(self._translate("MainWindow", "Smart Contracts", None))
        self.tab.needHelpGroupBox.setTitle(self._translate("MainWindow", "Need Help?", None))
        self.tab.supportButton.setText(self._translate("MainWindow", "Support", None))
        self.SendBitcoins.sendCoinsGroupBox.setTitle(self._translate("MainWindow", "Send BitBay", None))
        self.SendBitcoins.twoStepSendGroupBox.setTitle(self._translate("MainWindow", "Two Step Send", None))
        self.SendBitcoins.l_stepOne.setText(self._translate("MainWindow", "Fill out the payment form above. Then open your first private key file and email/send the signature it creates to your 2nd location/party.", None))
        self.SendBitcoins.l_stepTwo.setText(self._translate("MainWindow", "Open the other parties signature file, sign and review the payment details. If everything looks good, send it.", None))
        self.SendBitcoins.l_stepOneHead.setText(self._translate("MainWindow", "Step 1", None))
        self.SendBitcoins.l_stepTwoHead.setText(self._translate("MainWindow", "Step 2", None))
        self.ReceiveBitcoins.receiveCoinsGroupBox.setTitle(self._translate("MainWindow", "Receive BitBay and Contracts", None))
        self.History.gb_history.setTitle(self._translate("MainWindow", "History", None))
        self.Market.gb_market.setTitle(self._translate("MainWindow", "Market", None))
        self.Market.label_2.setText(self._translate("MainWindow", "These markets are decentralized. However volunteers may moderate.", None))
        self.Market.l_noPostIllegal.setText(self._translate("MainWindow", "Do not post illegal content to the market or you may get blocked.", None))
        self.Market.MarketRules.setText(self._translate("MainWindow", "These revolutionary markets are a way of connecting to people worldwide.", None))
        self.Market.label_4.setText(self._translate("MainWindow", "Market:", None))
        self.MakeAnOffer.gb_create.setTitle(self._translate("MainWindow", "Create a Smart Contract", None))
        self.PendingOffers.gb_pendingOffers.setTitle(self._translate("MainWindow", "Pending Offers", None))
        self.OpenContracts.gb_openContracts.setTitle(self._translate("MainWindow", "Open Contracts", None))
        self.Chat.gb_chat.setTitle(self._translate("MainWindow", "Chat", None))
        self.Contacts.gb_contacts.setTitle(self._translate("MainWindow", "Contacts", None))
        self.Contacts.ContactLabel.setText(self._translate("MainWindow", "Add contacts to your BitBay Address Book", None))

        self.tab.l_actualBalance.setText(self._translate("MainWindow", "Actual Balance:", None))
        self.tab.l_availableBalance.setText(self._translate("MainWindow", "Available Balance:", None))
        self.Symbol_1.setText(self._translate("MainWindow", "BTC", None))
        self.Symbol_2.setText(self._translate("MainWindow", "BTC", None))
        self.OpenAccount.setText(self._translate("MainWindow", "Open Account", None))
        self.JointAccount.setToolTip(self._translate("MainWindow", "New Account", None))
        self.JointAccount.setText(self._translate("MainWindow", "New Account", None))
        self.HireSomeone.setToolTip(self._translate("MainWindow", "Hire Someone", None))
        self.HireSomeone.setText(self._translate("MainWindow", "Hire Someone", None))
        self.Barter.setToolTip(self._translate("MainWindow", "Barter / Trade", None))
        self.Barter.setText(self._translate("MainWindow", "Barter/Trade", None))
        self.Custom.setToolTip(self._translate("MainWindow", "Custom Contract", None))
        self.Custom.setText(self._translate("MainWindow", "Custom Contract", None))
        self.FindJob.setToolTip(self._translate("MainWindow", "Find A Job", None))
        self.FindJob.setText(self._translate("MainWindow", "Find A Job", None))
        self.BuyAnything.setToolTip(self._translate("MainWindow", "Buy / Sell Anything", None))
        self.BuyAnything.setText(self._translate("MainWindow", "Buy/Sell Anything", None))
        self.BuyCoins.setToolTip(self._translate("MainWindow", "Buy / Sell Coins", None))
        self.BuyCoins.setText(self._translate("MainWindow", "Buy/Sell Coins", None))
        self.VideoLibrary.setToolTip(self._translate("MainWindow", "Video Library", None))
        self.VideoLibrary.setText(self._translate("MainWindow", "Video Library", None))
        self.labelProgress.setText(self._translate("MainWindow", "Synchronizing.", None))
        self.Rescan.setToolTip(self._translate("MainWindow", "Rescan", None))
        self.Rescan.setText(self._translate("MainWindow", "Rescan", None))
        self.PayToLabel.setText(self._translate("MainWindow", "Pay To:", None))
        self.AmountLabel.setText(self._translate("MainWindow", "Amount:", None))
        #self.BitFee.setText(self._translate("MainWindow", "0.0002", None))
        self.FeeLabel.setText(self._translate("MainWindow", "Fee:", None))
        self.SendBitcoins.l_actualBalance.setText(self._translate("MainWindow", "Actual Balance:", None))
        self.SendBitcoins.l_availableBalance.setText(self._translate("MainWindow", "Available Balance:", None))
        self.Symbol_3.setText(self._translate("MainWindow", "BTC", None))
        self.Symbol_4.setText(self._translate("MainWindow", "BTC", None))
        self.AdvancedSend.setToolTip(self._translate("MainWindow", "Advanced Sending", None))
        self.AdvancedSend.setText(self._translate("MainWindow", "Advanced Sending", None))
        self.tb_sendPanelHelp.setToolTip(self._translate("MainWindow", "Help", None))
        self.tb_sendPanelHelp.setText(self._translate("MainWindow", "?", None))
        self.SendMyBitcoins.setToolTip(self._translate("MainWindow", "Send", None))
        self.SendMyBitcoins.setText(self._translate("MainWindow", "Send", None))
        self.CreateSignatureOne.setToolTip(self._translate("MainWindow", "Create Signature File", None))
        self.CreateSignatureOne.setText(self._translate("MainWindow", "Create Signature File", None))
        self.OpenBitSignatureAndSend.setToolTip(self._translate("MainWindow", "Open Signature File, Sign and Send", None))
        self.OpenBitSignatureAndSend.setText(self._translate("MainWindow", "Open Signature File, Sign and Send", None))
        self.ExplainReceive.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainReceive.setText(self._translate("MainWindow", "?", None))
        self.CopyAddressToClipboard.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.ReceiveBitcoins.receiveBitMessageAddressLabel.setText(self._translate("MainWindow", "Your BitMessage Address: ", None))
        self.CopyAddressToClipboard_2.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.BitmessageStatus.setText(self._translate("MainWindow", "Status:", None))
        self.EnableBitmessage.setText(self._translate("MainWindow", "Enable Bitmessage", None))
        self.EnableIRC.setText(self._translate("MainWindow", "Enable IRC contracting", None))
        self.MyEmail.setText(self._translate("MainWindow", "Your Email Address: ", None))
        self.AddEmail_2.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.EmailStatus.setText(self._translate("MainWindow", "Status:", None))
        self.EmailBox.setPlaceholderText(self._translate("MainWindow", "Enter your Email here and then click the\"Add/Change\" button.", None))
        self.AddEmail.setToolTip(self._translate("MainWindow", "Add / Change Email", None))
        self.AddEmail.setText(self._translate("MainWindow", "Add/Change", None))
        self.EnableEmail.setText(self._translate("MainWindow", "Enable Email (Encrypted)", None))
        self.OutboxButton.setToolTip(self._translate("MainWindow", "Outbox", None))
        self.OutboxButton.setText(self._translate("MainWindow", "Outbox", None))
        self.History.MyAddress_2.setText(self._translate("MainWindow", "Your Address", None))
        self.CopyAddressToClipboard_5.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.HistoryBalance.setText(self._translate("MainWindow", "Balance:", None))
        self.Symbol_5.setText(self._translate("MainWindow", "BTC", None))
        self.TitleRecent.setText(self._translate("MainWindow", "Account Details", None))
        self.KeysConnected.setText(self._translate("MainWindow", "You have 0 Private Keys connected", None))
        self.Refresh.setToolTip(self._translate("MainWindow", "Refresh", None))
        self.History_Title.setText(self._translate("MainWindow", "Account History", None))
        self.ExplainHistory.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainHistory.setText(self._translate("MainWindow", "?", None))
        self.FullHistory.setSortingEnabled(False)
        item = self.FullHistory.horizontalHeaderItem(0)
        item.setText(self._translate("MainWindow", "Label", None))
        item = self.FullHistory.horizontalHeaderItem(1)
        item.setText(self._translate("MainWindow", "Type", None))
        item = self.FullHistory.horizontalHeaderItem(2)
        item.setText(self._translate("MainWindow", "Amount", None))
        item = self.FullHistory.horizontalHeaderItem(3)
        item.setText(self._translate("MainWindow", "Details", None))
        __sortingEnabled = self.FullHistory.isSortingEnabled()
        self.FullHistory.setSortingEnabled(False)
        self.FullHistory.setSortingEnabled(__sortingEnabled)
        self.ExportToCSV.setToolTip(self._translate("MainWindow", "Export to CSV", None))
        self.ExportToCSV.setText(self._translate("MainWindow", "Export To CSV", None))
        self.ClearHistory.setToolTip(self._translate("MainWindow", "Clear History", None))
        self.ClearHistory.setText(self._translate("MainWindow", "Clear History", None))
        self.ExplainContracts.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainContracts.setText(self._translate("MainWindow", "?", None))
        self.SendLabel_3.setText(self._translate("MainWindow", "Description:", None))
        self.SendLabel_4.setText(self._translate("MainWindow", "Image:", None))
        self.AttachImage.setToolTip(self._translate("MainWindow", "Attach an Image to your contract", None))
        self.AttachImage.setText(self._translate("MainWindow", "Attach an Image", None))
        self.SendLabel.setText(self._translate("MainWindow", "Send Contract to:", None))
        self.ContractAmountLabel.setText(self._translate("MainWindow", "Amount:", None))
        self.WhoPays.setItemText(0, self._translate("MainWindow", "I pay this amount", None))
        self.WhoPays.setItemText(1, self._translate("MainWindow", "The other party pays this amount", None))
        self.ContractFeeLabel.setText(self._translate("MainWindow", "Fee:", None))
        #self.ContractFee.setText(self._translate("MainWindow", "0.0002", None))
        self.DepositLabel.setText(self._translate("MainWindow", "You Deposit:", None))
        self.TheDepositLabel.setText(self._translate("MainWindow", "They Deposit:", None))
        self.TimeToCompleteLabel.setText(self._translate("MainWindow", "Time to Complete:", None))
        self.DaysMultiplier.setItemText(0, self._translate("MainWindow", "Days", None))
        self.DaysMultiplier.setItemText(1, self._translate("MainWindow", "Hours", None))
        self.AutoBackupLabel_2.setText(self._translate("MainWindow", "Auto Backup", None))
        self.ExplainAutoBackupOffer.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainAutoBackupOffer.setText(self._translate("MainWindow", "?", None))
        self.TxBackupPath.setPlaceholderText(self._translate("MainWindow", "Path to flash drive or backup folder.", None))
        self.BrowseTxBackup.setToolTip(self._translate("MainWindow", "Create path to Backup Folder", None))
        self.InstantRefundLabel.setText(self._translate("MainWindow", "Instant Refund", None))
        self.instantexplain.setToolTip(self._translate("MainWindow", "Help", None))
        self.instantexplain.setText(self._translate("MainWindow", "?", None))
        self.InstantAmountLabel.setText(self._translate("MainWindow", "Amount:", None))
        self.InstantWhoPays.setItemText(0, self._translate("MainWindow", "I am depositing this/broadcasting", None))
        self.InstantWhoPays.setItemText(1, self._translate("MainWindow", "They are depositing this/broadcasting", None))
        self.SendContract.setToolTip(self._translate("MainWindow", "Create Contract", None))
        self.SendContract.setText(self._translate("MainWindow", "Create Contract", None))
        self.checkBox.setText(self._translate("MainWindow", "Disable Notifications", None))
        self.FilterCustom.setText(self._translate("MainWindow", "Filter Non-Market Offers", None))
        self.DisableSpamFilter.setText(self._translate("MainWindow", "Disable spam filter", None))
        self.ExplainPending.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainPending.setText(self._translate("MainWindow", "?", None))
        self.ExplainOpen.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainOpen.setText(self._translate("MainWindow", "?", None))
        self.ShowWhat.setItemText(0, self._translate("MainWindow", "  Show all contracts", None))
        self.ShowWhat.setItemText(1, self._translate("MainWindow", "  Selling Coins", None))
        self.ShowWhat.setItemText(2, self._translate("MainWindow", "  Buying Coins", None))
        self.ShowWhat.setItemText(3, self._translate("MainWindow", "  Selling Items", None))
        self.ShowWhat.setItemText(4, self._translate("MainWindow", "  Buying Items", None))
        self.ShowWhat.setItemText(5, self._translate("MainWindow", "  Auctions", None))
        self.ShowWhat.setItemText(6, self._translate("MainWindow", "  Reverse Auctions", None))
        self.ShowWhat.setItemText(7, self._translate("MainWindow", "  Job Offers", None))
        self.ShowWhat.setItemText(8, self._translate("MainWindow", "  Employee Search", None))
        self.ShowWhat.setItemText(9, self._translate("MainWindow", "  Barter", None))
        self.ShowWhat.setItemText(10, self._translate("MainWindow", "  Misc", None))
        self.ShowWhat.setItemText(11, self._translate("MainWindow", "  Python Contracts", None))
        self.SearchEdit.setPlaceholderText(self._translate("MainWindow", "Type here to search", None))
        self.Search.setToolTip(self._translate("MainWindow", "Search", None))
        self.Search.setText(self._translate("MainWindow", "Go", None))
        self.ExplainMarket.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainMarket.setText(self._translate("MainWindow", "?", None))
        #item = self.OfferTable.horizontalHeaderItem(0)
        #item.setText(self._translate("MainWindow", "Images", None))
        #item = self.OfferTable.horizontalHeaderItem(1)
        #item.setText(self._translate("MainWindow", "Type", None))
        #item = self.OfferTable.horizontalHeaderItem(2)
        #item.setText(self._translate("MainWindow", "Description", None))
        #item = self.OfferTable.horizontalHeaderItem(3)
        #item.setText(self._translate("MainWindow", "Price", None))
        #item = self.OfferTable.horizontalHeaderItem(4)
        #item.setText(self._translate("MainWindow", "Payment", None))
        #item = self.OfferTable.horizontalHeaderItem(5)
        #item.setText(self._translate("MainWindow", "Contact", None))
        #item = self.OfferTable.horizontalHeaderItem(6)
        #item.setText(self._translate("MainWindow", "Deposits", None))
        #item = self.OfferTable.horizontalHeaderItem(7)
        #item.setText(self._translate("MainWindow", "Duration", None))
        #item = self.OfferTable.horizontalHeaderItem(8)
        #item.setText(self._translate("MainWindow", "Escrow", None))
        #item = self.OfferTable.horizontalHeaderItem(9)
        #item.setText(self._translate("MainWindow", "Date", None))
        self.MarketBox.setItemText(0, "ALL")
        self.OfferBox.setItemText(0, self._translate("MainWindow", "  Select Offer Type", None))
        self.OfferBox.setItemText(1, self._translate("MainWindow", "  Buy Coins With Cash", None))
        self.OfferBox.setItemText(2, self._translate("MainWindow", "  Sell Coins For Cash", None))
        self.OfferBox.setItemText(3, self._translate("MainWindow", "  Sell Something", None))
        self.OfferBox.setItemText(4, self._translate("MainWindow", "  Buy Something", None))
        self.OfferBox.setItemText(5, self._translate("MainWindow", "  Employ Someone", None))
        self.OfferBox.setItemText(6, self._translate("MainWindow", "  Find A Job", None))
        self.OfferBox.setItemText(7, self._translate("MainWindow", "  Barter Items/Services", None))
        self.OfferBox.setItemText(8, self._translate("MainWindow", "  Custom Offer", None))
        self.PostToMarket.setToolTip(self._translate("MainWindow", "Post Offer", None))
        self.PostToMarket.setText(self._translate("MainWindow", "Post Offer", None))
        self.SettingsMarket.setToolTip(self._translate("MainWindow", "Settings / Personal Info", None))
        self.SettingsMarket.setText(self._translate("MainWindow", "Settings/Personal Info", None))
        self.JoinChan.setToolTip(self._translate("MainWindow", "Add / Join Market", None))
        self.JoinChan.setText(self._translate("MainWindow", "Add/Join Market", None))
        self.LeaveChan.setToolTip(self._translate("MainWindow", "Leave Current Market", None))
        self.LeaveChan.setText(self._translate("MainWindow", "Leave Current Market", None))
        self.NewContact.setToolTip(self._translate("MainWindow", "Add New Contact", None))
        self.NewContact.setText(self._translate("MainWindow", "Add New Contact", None))
        self.BackupContacts.setToolTip(self._translate("MainWindow", "Backup-up Contacts", None))
        self.BackupContacts.setText(self._translate("MainWindow", "Back-up Contacts", None))
        self.menuFile.setTitle(self._translate("MainWindow", "File", None))
        self.menuSettings.setTitle(self._translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(self._translate("MainWindow", "Help", None))
        self.menuDonate.setTitle(self._translate("MainWindow", "Donate", None))
        self.actionNew_Wallet.setText(self._translate("MainWindow", "New Wallet", None))
        self.actionOpen_Wallet.setText(self._translate("MainWindow", "Open Wallet", None))
        self.actionSave_Copy.setText(self._translate("MainWindow", "Backup Wallet", None))
        self.actionEncrypt_Keyfile.setText(self._translate("MainWindow", "Encrypt Keyfile", None))
        self.actionEncrypt_Decrypt.setText(self._translate("MainWindow", "Encrypt/Decrypt", None))
        self.actionSign_Verify.setText(self._translate("MainWindow", "Sign/Verify", None))
        self.actionExit.setText(self._translate("MainWindow", "Exit", None))
        self.actionAbout.setText(self._translate("MainWindow", "About", None))
        self.actionDocumentation_2.setText(self._translate("MainWindow", "Documentation", None))
        self.actionOfficial_Website.setText(self._translate("MainWindow", "Official Website", None))
        self.actionDynamic_Peg_Info.setText(self._translate("MainWindow", "Dynamic Peg Info", None))
        self.actionLanguage.setText(self._translate("MainWindow", "Language", None))
        self.actionGeneral_Settings.setText(self._translate("MainWindow", "General Settings", None))
        self.actionAdvanced_Sending.setText(self._translate("MainWindow", "Advanced Sending", None))
        self.actionTranslation_Editor.setText(self._translate("MainWindow", "Translation Editor", None))
        self.actionAPI.setText(self._translate("MainWindow", "Activate API", None))
        self.DConsole.setText(self._translate("MainWindow", "Debug Console", None))
        self.actionBuy_me_a_beer.setText(self._translate("MainWindow", "Buy us a beer", None))
        self.actionKey_To_Image.setText(self._translate("MainWindow", "Key To Image", None))
        self.actionUnlock_Wallet.setText(self._translate("MainWindow", "Unlock Wallet", None))

    def setBitBayStyle(self):
        from styles import bay as bay_style
        self.style = bay_style

    def BayHalo(self, main_window):
        styles.bay.apply(self, main_window)

    def BitHalo(self, main_window):
        styles.btc.apply(self, main_window)

    def BLKHalo(self, main_window):
        styles.blk.apply(self, main_window)

if __name__ == "__main__":
    import sys
    import os
    import styles.bay_rc

    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.adjustSize = lambda :""
    ui.ApplicationPath = os.path.abspath(os.path.dirname(__file__))+"/."
    main_window.ApplicationPath = ui.ApplicationPath
    ui.language = "en"
    ui.translations = {}
    ui.setBitBayStyle()

    NewCoin1 = {}
    NewCoin1['daemon']="bitbayd"
    NewCoin1['datadir']="bitbaydata"
    NewCoin1['config']="bitbay"
    NewCoin1['rpcuser']="bitbayrpc"
    NewCoin1['rpcpassword']="32w54er56t7y89j8h34w5e6t7y8u9ik34sAs4"
    NewCoin1['rpcport']="19915"
    NewCoin1['port']="19914"
    NewCoin1['blocktime']="64"
    NewCoin1['6aLength']=248
    NewCoin1['pegging']=True
    NewCoin1['checksequenceverify']=False
    NewCoin1['staking']=True
    NewCoin1['stakeconfirmations']=120
    NewCoin1['logo']="/images/BitBay.png"
    NewCoin1['name']="BitBay"
    NewCoin1['website']="http://bitbaymarket.net/"#"http://www.thebitbay.org/"  and bitbaymarket is also under Bitbays control
    NewCoin1['videolibrary']="https://www.youtube.com/watch?v=CIU4s2G8jU8&list=PL4MGGKJn4DizGw7oBXwzETMVLNCZ6G2_t"
    NewCoin1['updatewindows']="https://bithalo.github.io/bithalo/downloads/BitBayUpdateWin.html"
    NewCoin1['TabText']="rgb(255, 255, 255)"
    NewCoin1['splash']="LoadingBitBay.png"
    NewCoin1['HaloName']="BitBay"
    NewCoin1['Background']="#70aee7"
    NewCoin1['LabelText']="rgb(251, 251, 251)"
    NewCoin1['TabSelected']="#acb6c6"
    NewCoin1['QTabBackground']="rgba(0, 0, 34, 250)"
    NewCoin1['QFrameColor']="#00000"
    NewCoin1['Symbol']="BAY"
    NewCoin1['CommandLinkColor']="#fbfbfb"
    NewCoin1['ProgressBarColor']="#a5d1e4"#545d6d
    NewCoin1['TabGradient']="qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #009ee3, stop: 0.4 rgba(0, 90, 177, 250), stop:1 rgba(0, 50, 100, 250))"
    NewCoin1['NavBarIcon']="/images/navbar_arrow_bay.png"
    NewCoin1['default market']="BitBay"
    NewCoin1['IRC']="https://kiwiirc.com/client/irc.kiwiirc.com/#BitHalo,#BitBay" #http://webchat.freenode.net?channels=BitHalo,#BitBay&amp;uio=OT10cnVlJjExPTIzNg6b"
    NewCoin1['links']=("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Arial\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px; font-weight:600;\">Links/Misc</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://bitbay.market/\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">http://bitbay.market/</span></a><span style=\" font-size:15px;\">  The official BitBay website</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://bitbaymarket.net/\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">http://bitbaymarket.net/</span></a><span style=\" font-size:15px;\">  BitBay mirror websites</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.reddit.com/r/bitbay/\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">http://www.reddit.com/r/bitbay/</span></a><span style=\" font-size:15px;\">  BitBay community subreddit</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/bitbaymarket/bitbay-bootstrap/releases\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">bitbaybootstrap.zip</span></a><span style=\" font-size:15px;\">  Download BitBay bootstrap.zip.</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.Blackhalo.info\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">www.Blackhalo.info</span></a><span style=\" font-size:15px;\">  BlackHalo, the worlds first contracting software</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.BitHalo.org\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">www.BitHalo.org</span></a><span style=\" font-size:15px;\">  The original BitHalo Website</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.NightTrader.org\"><span style=\" font-size:15px; text-decoration: underline; color:#0000ff;\">www.NightTrader.org</span></a><span style=\" font-size:15px;\">  NightTrader decentralized exchange</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:15px;\"><br /></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">If you have any feedback or questions please contact us through the official website. Thank you.</span></p></body></html>")
    NewCoin1['Moderator']=0

    ui.NewCoin = NewCoin1
    ui.setupUi(main_window)

    main_window.show()

    #ui.retranslateUi2(MainWindow)
    sys.exit(app.exec())
