# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ANewBitHalo.ui'
#
# Created: Wed Nov 12 19:50:27 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

import ast
import traceback

from yandex_translate import YandexTranslate
from PyQt6 import QtCore, QtGui, QtWebEngineWidgets, QtWidgets


def _fromUtf8(s):
    return s


ytrans = YandexTranslate("trnsl.1.1.20170227T075822Z.710cc070687ef49d.4773b96b2fa3e9cea7df423e9ab798c58d504036")


def compareFont(Label1, Label2):
    try:
        f = Label1.font()
        f2 = Label2.font()
        s = f.pixelSize()
        s2 = f2.pixelSize()
        if s == -1:
            s = f.pointSize()
            s2 = f2.pointSize()
        if s > s2:
            Label1.setFont(Label2.font())
        else:
            Label2.setFont(Label1.font())
    except Exception:
        traceback.print_exc()
    return True


class myQLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kargs):
        super(myQLabel, self).__init__(*args, **kargs)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored))

        self.setMinSize(6)

    def setMinSize(self, minfs):

        f = self.font()
        f.setPixelSize(minfs)
        f.setFamily(_fromUtf8("Arial"))
        br = QtGui.QFontMetrics(f).boundingRect(self.text())

        self.setMinimumSize(br.width(), br.height())

    def resizeEvent(self, event):
        super(myQLabel, self).resizeEvent(event)

        if not self.text():
            return

        # --- fetch current parameters ----

        f = self.font()
        cr = self.contentsRect()

        # --- find the font size that fits the contentsRect ---

        fs = 1
        while True:

            f.setPixelSize(fs)
            br = QtGui.QFontMetrics(f).boundingRect(self.text())

            if br.height() <= cr.height() and br.width() <= cr.width():
                fs += 1
            else:
                f.setPixelSize(max(fs - 1, 1))  # backtrack
                break

        # --- update font size ---

        self.setFont(f)


class Ui_MainWindow(object):
    ApplicationPath = ""

    def _translate(self, context, text, disambig):
        if self.language != "DEFAULT" and self.language != "en":
            if self.language not in self.translations:
                self.translations[self.language] = {}
            if text not in self.translations[self.language]:
                if text == "":
                    return ""
                self.translist.append(text)
            else:
                try:
                    translateThis = ast.literal_eval(self.translations[self.language][text])
                    return translateThis
                except Exception:
                    return ""
        return QtCore.QCoreApplication.translate(context, text, disambig)

    def GTranslate(self):
        try:
            if self.translist == []:
                return False
            if self.language == "en" or self.language == "DEFAULT":
                self.translist = []
                return False
            if self.yandexAPI == "":  # For now google translate is too slow without API access although this can be expanded upon
                print("Yandex API key not available")
                return False
            else:
                ytrans = YandexTranslate(self.yandexAPI)
            # The Yandex site has a 10K text size limit, so we do multiple requests
            xpos = 0
            numby = 0
            posy = 1
            listoflists = []
            testlist = ast.literal_eval(str(self.translist))
            endoflist = len(testlist)
            for trans in testlist:
                numby += len(trans)
                if numby > 7000:
                    listoflists.append(testlist[xpos:posy])
                    numby = 0
                    xpos = posy
                else:
                    if posy == endoflist:
                        listoflists.append(testlist[xpos:posy])
                posy += 1
            resp = []
            for mytranslist in listoflists:
                resp1 = ytrans.translate(mytranslist, self.language)
                resp1 = resp1["text"]
                for respy in resp1:
                    resp.append(respy)
            resp = ytrans.translate(ast.literal_eval(str(self.translist)), self.language)
            resp = resp["text"]
            pos = 0
            for trans in resp:
                langtext = QtWidgets.QLabel()
                langtext.setText(trans)
                x = langtext.text()
                st = repr(x)
                ast.literal_eval(st)
                self.translations[self.language][self.translist[pos]] = st
                pos += 1
            self.translist = []
            return True
        except Exception:
            traceback.print_exc()
            return False

    def setupUi(self, MainWindow):
        self.NewCoin = {}
        # self.translations={}
        self.translist = []
        self.NewCoin["logo"] = "/images/BitBay.png"
        self.NewCoin["name"] = "BitBay"
        self.NewCoin["TabText"] = "rgb(255, 255, 255)"
        self.NewCoin["HaloName"] = "Halo"
        self.NewCoin["Background"] = "#70aee7"
        self.NewCoin["LabelText"] = "rgb(251, 251, 251)"
        self.NewCoin["BackgroundImage"] = "/images/bg_bitbay.png"
        self.NewCoin["BackgroundImage2"] = "/images/bg_bitbay_2.png"
        self.NewCoin["TabSelected"] = "#acb6c6"
        self.NewCoin["QTabBackground"] = "rgba(0, 0, 34, 250)"
        self.NewCoin["QFrameColor"] = "#00000"
        self.NewCoin["FrameGradient"] = "qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #2f3339, stop: 0.4 rgba(0, 0, 34, 250), stop:0 rgba(50, 50, 50, 250)"
        self.NewCoin["Symbol"] = "BAY"
        self.NewCoin["CommandLinkColor"] = "#fbfbfb"
        self.NewCoin["ProgressBarColor"] = "#545d6d"
        self.NewCoin["TabGradient"] = "qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #009ee3, stop: 0.4 rgba(0, 90, 177, 250), stop:1 rgba(0, 50, 100, 250))"
        self.NewCoin["NavBarIcon"] = "/images/navbar_arrow_bay.png"
        self.NewCoin["IRC"] = "http://webchat.freenode.net?channels=BitHalo,#Blackcoin&amp;uio=OT10cnVlJjExPTIzNg6b"
        # self.ApplicationPath="C:\\Users\\David\\Desktop\\BlackHalo\Halo\\"
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(981, 724)
        MainWindow.setMinimumSize(QtCore.QSize(991, 724))
        # self.ApplicationPath.replace("\\","/")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/BitHalo.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Tabs.sizePolicy().hasHeightForWidth())
        self.Tabs.setSizePolicy(sizePolicy)
        # self.Tabs.setUsesScrollButtons(False)
        # self.Tabs.setMinimumSize(QtCore.QSize(981, 620))
        self.Tabs.setSizeIncrement(QtCore.QSize(100, 98))
        self.Tabs.setStyleSheet(
            _fromUtf8(
                "QTabWidget::pane { /* The tab widget frame */\n"
                "border-top: 6px solid #d27e16;\n"
                "border-right: 2px solid #d27e16;\n"
                "border-left: 2px solid #d27e16;\n"
                "border-bottom: 6px solid #d27e16;\n"
                "margin-top:0px;\n"
                "background-color:#ececec;\n"
                "background: qlineargradient(x1:0, y1:1, x2:1, y2:0, stop:0 #c0c0c0, stop: 0.4 rgba(236, 236, 236, 200), stop:1 rgba(236, 236, 236, 200));\n"
                "\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}\n"
                "QTabWidget::tab-bar {\n"
                "left: 0px; /* move to the right by 5px */\n"
                "\n"
                "}\n"
                "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
                "QTabBar::tab {\n"
                "color: #FFF;\n"
                "opacity: 0.6;\n"
                "text-align: center;\n"
                "background-color: #222222;\n"
                "\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #2b3034, stop: 0.4 rgba(34, 34, 34, 250), stop:1 rgba(34, 34, 34, 250));\n"
                "\n"
                "padding: 20px 5px 20px 5px;\n"
                "/*padding: 40px 10px 10px 10px; */\n"
                "border-right: 1px dotted #C2C7CB;\n"
                "}\n"
                "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                "color: #f7931a;\n"
                "}\n"
                "QTabBar::tab:selected {\n"
                "background: #d27e16;\n"
                "color: #000;\n"
                "opacity: 1;\n"
                "}\n"
                "QTabBar::tab:!selected {\n"
                "margin-top: 0px; /* make non-selected tabs look smaller */\n"
                "\n"
                "}\n"
                ""
            )
        )
        self.Tabs.setIconSize(QtCore.QSize(18, 18))
        self.Tabs.setDocumentMode(False)
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPixelSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.frame_2.setFont(font)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_2 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}"
            )
        )
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_3.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_3.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.commandLinkButton = QtWidgets.QPushButton(self.frame_2)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
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
                " }"
            )
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_attention_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton.setDefault(False)
        self.commandLinkButton.setFlat(False)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.horizontalLayout_2.addWidget(self.commandLinkButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_2)
        self.gridLayout_7.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(40, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_5 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_5.setMaximumSize(QtCore.QSize(16666, 40))
        self.frame_5.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_5 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.MyAddress_7 = QtWidgets.QLabel(self.frame_5)
        self.MyAddress_7.setGeometry(QtCore.QRect(10, 10, 561, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyAddress_7.setFont(font)
        self.MyAddress_7.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))
        self.MyAddress_7.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyAddress_7.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.MyAddress_7.setObjectName(_fromUtf8("MyAddress_7"))
        self.horizontalLayout.addWidget(self.frame_5)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CopyAddressToClipboard_3 = QtWidgets.QPushButton(self.tab)
        self.CopyAddressToClipboard_3.setMinimumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard_3.setMaximumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CopyAddressToClipboard_3.setStyleSheet(
            _fromUtf8(
                "QPushButton#CopyAddressToClipboard_3 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#CopyAddressToClipboard_3:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.CopyAddressToClipboard_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_copypaste_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.CopyAddressToClipboard_3.setIcon(icon2)
        self.CopyAddressToClipboard_3.setIconSize(QtCore.QSize(20, 20))
        self.CopyAddressToClipboard_3.setFlat(False)
        self.CopyAddressToClipboard_3.setObjectName(_fromUtf8("CopyAddressToClipboard_3"))
        self.horizontalLayout.addWidget(self.CopyAddressToClipboard_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setMinimumSize(QtCore.QSize(520, 81))
        self.frame_4.setMaximumSize(QtCore.QSize(520, 81))
        self.frame_4.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_4 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.WelcomeActualBalance = myQLabel(self.frame_4)
        self.WelcomeActualBalance.setGeometry(QtCore.QRect(0, 10, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        # self.WelcomeActualBalance.setFont(font)
        self.WelcomeActualBalance.setStyleSheet(_fromUtf8("color: rgb(104, 104, 104);\n" "font: Bold;"))  # 16px \"Arial\";
        # self.WelcomeActualBalance.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.WelcomeActualBalance.setObjectName(_fromUtf8("WelcomeActualBalance"))
        self.WelcomeAvailableBalance = myQLabel(self.frame_4)
        self.WelcomeAvailableBalance.setGeometry(QtCore.QRect(0, 50, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        # self.WelcomeAvailableBalance.setFont(font)
        self.WelcomeAvailableBalance.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.WelcomeAvailableBalance.setStyleSheet(_fromUtf8("color: rgb(104, 104, 104);\n" "font: bold;"))
        # self.WelcomeAvailableBalance.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.WelcomeAvailableBalance.setObjectName(_fromUtf8("WelcomeAvailableBalance"))
        self.line_6 = QtWidgets.QFrame(self.frame_4)
        self.line_6.setGeometry(QtCore.QRect(10, 40, 471, 20))
        self.line_6.setStyleSheet(_fromUtf8("border: 1px dotted #000000; \n" "border-style: dotted none none; \n" "color: #fff;"))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.Symbol_1 = myQLabel(self.frame_4)
        self.Symbol_1.setGeometry(QtCore.QRect(430, 10, 36, 21))
        self.Symbol_1.setStyleSheet(_fromUtf8('font: bold "Arial";\n' "color: #24282C;"))
        self.Symbol_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Symbol_1.setObjectName(_fromUtf8("Symbol_1"))
        self.Symbol_2 = myQLabel(self.frame_4)
        self.Symbol_2.setGeometry(QtCore.QRect(430, 50, 41, 21))
        self.Symbol_2.setStyleSheet(_fromUtf8('font: bold "Arial";\n' "color: #24282C;"))
        self.Symbol_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Symbol_2.setObjectName(_fromUtf8("Symbol_2"))
        self.MyBalance_4 = QtWidgets.QLabel(self.frame_4)
        self.MyBalance_4.setGeometry(QtCore.QRect(170, 50, 251, 20))
        self.MyBalance_4.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.MyBalance_4.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyBalance_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MyBalance_4.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.MyBalance_4.setObjectName(_fromUtf8("MyBalance_4"))
        self.MyBalance_3 = QtWidgets.QLabel(self.frame_4)
        self.MyBalance_3.setGeometry(QtCore.QRect(170, 10, 251, 20))
        self.MyBalance_3.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.MyBalance_3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyBalance_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MyBalance_3.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.MyBalance_3.setObjectName(_fromUtf8("MyBalance_3"))
        self.verticalLayout_2.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.Conversion = QtWidgets.QPushButton(self.frame_4)
        self.Conversion.setMinimumSize(QtCore.QSize(31, 31))
        self.Conversion.setMaximumSize(QtCore.QSize(31, 31))
        self.Conversion.setGeometry(QtCore.QRect(484, 7, 31, 31))
        self.Conversion.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Conversion.setToolTip(_fromUtf8("Open Account"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setItalic(False)
        font.setWeight(50)
        self.Conversion.setFont(font)
        self.Conversion.setText("$")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.OpenAccount = QtWidgets.QPushButton(self.tab)
        self.OpenAccount.setMinimumSize(QtCore.QSize(281, 71))
        self.OpenAccount.setMaximumSize(QtCore.QSize(281, 71))
        self.OpenAccount.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.OpenAccount.setToolTip(_fromUtf8("Open Account"))
        self.OpenAccount.setStyleSheet(
            _fromUtf8(
                "QPushButton#OpenAccount {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#OpenAccount:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_openaccount_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.OpenAccount.setIcon(icon3)
        self.OpenAccount.setIconSize(QtCore.QSize(20, 20))
        self.OpenAccount.setObjectName(_fromUtf8("OpenAccount"))
        self.horizontalLayout_4.addWidget(self.OpenAccount)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.JointAccount = QtWidgets.QPushButton(self.tab)
        self.JointAccount.setMinimumSize(QtCore.QSize(281, 71))
        self.JointAccount.setMaximumSize(QtCore.QSize(281, 71))
        self.JointAccount.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.JointAccount.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.JointAccount.setStyleSheet(
            _fromUtf8(
                "QPushButton#JointAccount {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#JointAccount:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_jointaccount_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.JointAccount.setIcon(icon4)
        self.JointAccount.setIconSize(QtCore.QSize(20, 20))
        self.JointAccount.setObjectName(_fromUtf8("JointAccount"))
        self.horizontalLayout_4.addWidget(self.JointAccount)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.LineBalance_3 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_3.sizePolicy().hasHeightForWidth())
        self.LineBalance_3.setSizePolicy(sizePolicy)
        self.LineBalance_3.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_3.setObjectName(_fromUtf8("LineBalance_3"))
        self.horizontalLayout_5.addWidget(self.LineBalance_3)
        self.MyBalance_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyBalance_5.setFont(font)
        self.MyBalance_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.MyBalance_5.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.MyBalance_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MyBalance_5.setObjectName(_fromUtf8("MyBalance_5"))
        self.horizontalLayout_5.addWidget(self.MyBalance_5)
        self.LineBalance_2 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_2.sizePolicy().hasHeightForWidth())
        self.LineBalance_2.setSizePolicy(sizePolicy)
        self.LineBalance_2.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_2.setObjectName(_fromUtf8("LineBalance_2"))
        self.horizontalLayout_5.addWidget(self.LineBalance_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 6, -1, 0)
        self.gridLayout_2.setVerticalSpacing(22)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.HireSomeone = QtWidgets.QPushButton(self.tab)
        self.HireSomeone.setMinimumSize(QtCore.QSize(181, 71))
        self.HireSomeone.setMaximumSize(QtCore.QSize(250, 71))
        self.HireSomeone.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.HireSomeone.setStyleSheet(
            _fromUtf8(
                "QPushButton#HireSomeone {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#HireSomeone:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_hire_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.HireSomeone.setIcon(icon5)
        self.HireSomeone.setIconSize(QtCore.QSize(20, 20))
        self.HireSomeone.setObjectName(_fromUtf8("HireSomeone"))
        self.gridLayout_2.addWidget(self.HireSomeone, 1, 2, 1, 1)
        self.Barter = QtWidgets.QPushButton(self.tab)
        self.Barter.setMinimumSize(QtCore.QSize(181, 71))
        self.Barter.setMaximumSize(QtCore.QSize(250, 71))
        self.Barter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Barter.setStyleSheet(
            _fromUtf8(
                "QPushButton#Barter {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#Barter:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_trade_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.Barter.setIcon(icon6)
        self.Barter.setIconSize(QtCore.QSize(25, 25))
        self.Barter.setObjectName(_fromUtf8("Barter"))
        self.gridLayout_2.addWidget(self.Barter, 0, 4, 1, 1)
        self.Custom = QtWidgets.QPushButton(self.tab)
        self.Custom.setMinimumSize(QtCore.QSize(181, 71))
        self.Custom.setMaximumSize(QtCore.QSize(250, 71))
        self.Custom.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Custom.setStyleSheet(
            _fromUtf8(
                "QPushButton#Custom {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#Custom:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contract_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.Custom.setIcon(icon7)
        self.Custom.setIconSize(QtCore.QSize(20, 20))
        self.Custom.setObjectName(_fromUtf8("Custom"))
        self.gridLayout_2.addWidget(self.Custom, 1, 4, 1, 1)
        self.FindJob = QtWidgets.QPushButton(self.tab)
        self.FindJob.setMinimumSize(QtCore.QSize(181, 71))
        self.FindJob.setMaximumSize(QtCore.QSize(250, 71))
        self.FindJob.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.FindJob.setStyleSheet(
            _fromUtf8(
                "QPushButton#FindJob {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#FindJob:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_findjob_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.FindJob.setIcon(icon8)
        self.FindJob.setIconSize(QtCore.QSize(20, 20))
        self.FindJob.setObjectName(_fromUtf8("FindJob"))
        self.gridLayout_2.addWidget(self.FindJob, 0, 2, 1, 1)
        self.BuyAnything = QtWidgets.QPushButton(self.tab)
        self.BuyAnything.setMinimumSize(QtCore.QSize(181, 71))
        self.BuyAnything.setMaximumSize(QtCore.QSize(250, 71))
        self.BuyAnything.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BuyAnything.setStyleSheet(
            _fromUtf8(
                "QPushButton#BuyAnything{\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color:rgba(251, 251, 251, 100%);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#BuyAnything:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_buysell_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.BuyAnything.setIcon(icon9)
        self.BuyAnything.setIconSize(QtCore.QSize(20, 20))
        self.BuyAnything.setObjectName(_fromUtf8("BuyAnything"))
        self.gridLayout_2.addWidget(self.BuyAnything, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        self.BuyCoins = QtWidgets.QPushButton(self.tab)
        self.BuyCoins.setMinimumSize(QtCore.QSize(181, 71))
        self.BuyCoins.setMaximumSize(QtCore.QSize(250, 71))
        self.BuyCoins.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BuyCoins.setStyleSheet(
            _fromUtf8(
                "QPushButton#BuyCoins {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#BuyCoins:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_buycoins_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.BuyCoins.setIcon(icon10)
        self.BuyCoins.setIconSize(QtCore.QSize(20, 20))
        self.BuyCoins.setObjectName(_fromUtf8("BuyCoins"))
        self.gridLayout_2.addWidget(self.BuyCoins, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 3, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.line = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 400))
        self.line.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: none  solid none none;"))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_9.addWidget(self.line)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(25, -1, 30, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.HaloContactsIcon_2 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HaloContactsIcon_2.sizePolicy().hasHeightForWidth())
        self.HaloContactsIcon_2.setSizePolicy(sizePolicy)
        self.HaloContactsIcon_2.setMinimumSize(QtCore.QSize(221, 211))
        self.HaloContactsIcon_2.setMaximumSize(QtCore.QSize(221, 211))
        self.HaloContactsIcon_2.setStyleSheet(
            _fromUtf8(
                "QPushButton#HaloContactsIcon_2 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "\n"
                "     \n"
                "}\n"
                " QPushButton#HaloContactsIcon_2:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                " }"
            )
        )
        self.HaloContactsIcon_2.setText(_fromUtf8(""))
        self.HaloContactsIcon_2.setIcon(icon)
        self.HaloContactsIcon_2.setIconSize(QtCore.QSize(211, 211))
        self.HaloContactsIcon_2.setFlat(True)
        self.HaloContactsIcon_2.setObjectName(_fromUtf8("HaloContactsIcon_2"))
        self.verticalLayout_3.addWidget(self.HaloContactsIcon_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.switchcoin = QtWidgets.QPushButton(self.tab)
        self.switchcoin.setMinimumSize(QtCore.QSize(221, 71))
        self.switchcoin.setMaximumSize(QtCore.QSize(221, 71))
        self.switchcoin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.switchcoin.setStyleSheet(
            _fromUtf8(
                "QPushButton#switchcoin {\n"
                "    \n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "    \n"
                "    \n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_blackhalo_03.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                "     \n"
                "}\n"
                " QPushButton#switchcoin:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_blackhalo_04.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                " }"
            )
        )
        self.switchcoin.setText(_fromUtf8(""))
        self.switchcoin.setIconSize(QtCore.QSize(20, 20))
        self.switchcoin.setObjectName(_fromUtf8("switchcoin"))
        self.verticalLayout_3.addWidget(self.switchcoin)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 12)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.LineBalance_6 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_6.sizePolicy().hasHeightForWidth())
        self.LineBalance_6.setSizePolicy(sizePolicy)
        self.LineBalance_6.setMinimumSize(QtCore.QSize(10, 0))
        self.LineBalance_6.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_6.setObjectName(_fromUtf8("LineBalance_6"))
        self.horizontalLayout_7.addWidget(self.LineBalance_6)
        self.MyBalance_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyBalance_6.setFont(font)
        self.MyBalance_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.MyBalance_6.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.MyBalance_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MyBalance_6.setObjectName(_fromUtf8("MyBalance_6"))
        self.horizontalLayout_7.addWidget(self.MyBalance_6)
        self.LineBalance_4 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_4.sizePolicy().hasHeightForWidth())
        self.LineBalance_4.setSizePolicy(sizePolicy)
        self.LineBalance_4.setMinimumSize(QtCore.QSize(10, 0))
        self.LineBalance_4.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_4.setObjectName(_fromUtf8("LineBalance_4"))
        self.horizontalLayout_7.addWidget(self.LineBalance_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.VideoLibrary = QtWidgets.QPushButton(self.tab)
        self.VideoLibrary.setMinimumSize(QtCore.QSize(221, 71))
        self.VideoLibrary.setMaximumSize(QtCore.QSize(221, 71))
        self.VideoLibrary.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.VideoLibrary.setStyleSheet(
            _fromUtf8(
                "QPushButton#VideoLibrary {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#VideoLibrary:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_video_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.VideoLibrary.setIcon(icon11)
        self.VideoLibrary.setIconSize(QtCore.QSize(20, 20))
        self.VideoLibrary.setObjectName(_fromUtf8("VideoLibrary"))
        self.verticalLayout_3.addWidget(self.VideoLibrary)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.LineBalance_5 = QtWidgets.QFrame(self.tab)
        self.LineBalance_5.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_5.setObjectName(_fromUtf8("LineBalance_5"))
        self.verticalLayout_5.addWidget(self.LineBalance_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.labelProgress = QtWidgets.QLabel(self.tab)
        self.labelProgress.setMinimumSize(QtCore.QSize(0, 0))
        self.labelProgress.setMaximumSize(QtCore.QSize(16777215, 19))
        self.labelProgress.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: 13px "Arial";'))
        self.labelProgress.setObjectName(_fromUtf8("labelProgress"))
        self.horizontalLayout_6.addWidget(self.labelProgress)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(671, 21))
        self.progressBar.setMaximumSize(QtCore.QSize(672, 21))
        self.progressBar.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: #f7931a;\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.Rescan = QtWidgets.QPushButton(self.tab)
        self.Rescan.setMinimumSize(QtCore.QSize(75, 23))
        self.Rescan.setMaximumSize(QtCore.QSize(150, 23))
        self.Rescan.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Rescan.setStyleSheet(
            _fromUtf8(
                "QPushButton#Rescan {\n"
                '    font: bold 12px "Arial";\n'
                "color: #24282C;\n"
                "background-color: #fbfbfb;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "     \n"
                "}\n"
                " QPushButton#Rescan:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                " }"
            )
        )
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_rescan_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.Rescan.setIcon(icon12)
        self.Rescan.setObjectName(_fromUtf8("Rescan"))
        self.horizontalLayout_6.addWidget(self.Rescan)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout_7.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(0, icon13)

        self.Tabs.addTab(self.tab, icon13, _fromUtf8(""))
        self.SendBitcoins = QtWidgets.QWidget()
        self.SendBitcoins.setEnabled(True)
        self.SendBitcoins.setObjectName(_fromUtf8("SendBitcoins"))
        self.gridLayout_11 = QtWidgets.QGridLayout(self.SendBitcoins)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.frame = QtWidgets.QFrame(self.SendBitcoins)
        self.frame.setMinimumSize(QtCore.QSize(600, 70))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setStyleSheet(
            _fromUtf8(
                "QFrame#frame {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_7.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_7.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayout_11.addWidget(self.frame_7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.commandLinkButton_3 = QtWidgets.QPushButton(self.frame)
        self.commandLinkButton_3.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_3.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_3.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_3 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_3:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.horizontalLayout_11.addWidget(self.commandLinkButton_3)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_11)
        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(40, 10, 0, -1)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.PayToLabel = QtWidgets.QLabel(self.SendBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PayToLabel.setFont(font)
        self.PayToLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.PayToLabel.setObjectName(_fromUtf8("PayToLabel"))
        self.gridLayout_3.addWidget(self.PayToLabel, 2, 0, 1, 1)
        self.BitPayTo = QtWidgets.QLineEdit(self.SendBitcoins)
        self.BitPayTo.setMinimumSize(QtCore.QSize(600, 40))
        self.BitPayTo.setMaximumSize(QtCore.QSize(600, 40))
        self.BitPayTo.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                ""
            )
        )
        self.BitPayTo.setObjectName(_fromUtf8("BitPayTo"))
        self.gridLayout_3.addWidget(self.BitPayTo, 2, 1, 1, 1)
        self.AmountLabel = QtWidgets.QLabel(self.SendBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.AmountLabel.setFont(font)
        self.AmountLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.AmountLabel.setObjectName(_fromUtf8("AmountLabel"))
        self.gridLayout_3.addWidget(self.AmountLabel, 3, 0, 1, 1)
        self.BitAmount = QtWidgets.QLineEdit(self.SendBitcoins)
        self.BitAmount.setMinimumSize(QtCore.QSize(300, 40))
        self.BitAmount.setMaximumSize(QtCore.QSize(300, 40))
        self.BitAmount.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                ""
            )
        )
        self.BitAmount.setObjectName(_fromUtf8("BitAmount"))
        self.gridLayout_3.addWidget(self.BitAmount, 3, 1, 1, 1)
        self.BitFee = QtWidgets.QLineEdit(self.SendBitcoins)
        self.BitFee.setMinimumSize(QtCore.QSize(300, 40))
        self.BitFee.setMaximumSize(QtCore.QSize(300, 40))
        self.BitFee.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                ""
            )
        )
        # self.BitFee.setReadOnly(True)
        self.BitFee.setObjectName(_fromUtf8("BitFee"))
        self.gridLayout_3.addWidget(self.BitFee, 4, 1, 1, 1)
        self.FeeLabel = QtWidgets.QLabel(self.SendBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.FeeLabel.setFont(font)
        self.FeeLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.FeeLabel.setObjectName(_fromUtf8("FeeLabel"))
        self.gridLayout_3.addWidget(self.FeeLabel, 4, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.SendBitcoins)
        self.frame_6.setMinimumSize(QtCore.QSize(500, 81))
        self.frame_6.setMaximumSize(QtCore.QSize(500, 81))
        self.frame_6.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_6 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 10px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.SendActualBalance = myQLabel(self.frame_6)
        self.SendActualBalance.setGeometry(QtCore.QRect(0, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        # font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendActualBalance.setFont(font)
        self.SendActualBalance.setStyleSheet(_fromUtf8("color: rgb(104, 104, 104);\n" 'font: Bold "Arial";'))
        self.SendActualBalance.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.SendActualBalance.setObjectName(_fromUtf8("SendActualBalance"))
        self.SendAvailableBalance = myQLabel(self.frame_6)
        self.SendAvailableBalance.setGeometry(QtCore.QRect(0, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        # font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendAvailableBalance.setFont(font)
        self.SendAvailableBalance.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SendAvailableBalance.setStyleSheet(_fromUtf8("color: rgb(104, 104, 104);\n" 'font: bold "Arial";'))
        self.SendAvailableBalance.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.SendAvailableBalance.setObjectName(_fromUtf8("SendAvailableBalance"))
        self.line_7 = QtWidgets.QFrame(self.frame_6)
        self.line_7.setGeometry(QtCore.QRect(10, 40, 471, 20))
        self.line_7.setStyleSheet(_fromUtf8("border: 1px dotted #000000; \n" "border-style: dotted none none; \n" "color: #fff;"))
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.Symbol_3 = QtWidgets.QLabel(self.frame_6)
        self.Symbol_3.setGeometry(QtCore.QRect(430, 10, 46, 21))
        self.Symbol_3.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.Symbol_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Symbol_3.setObjectName(_fromUtf8("Symbol_3"))
        self.Symbol_4 = QtWidgets.QLabel(self.frame_6)
        self.Symbol_4.setGeometry(QtCore.QRect(430, 50, 46, 21))
        self.Symbol_4.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.Symbol_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Symbol_4.setObjectName(_fromUtf8("Symbol_4"))
        self.MyBalance_8 = QtWidgets.QLabel(self.frame_6)
        self.MyBalance_8.setGeometry(QtCore.QRect(170, 50, 251, 20))
        self.MyBalance_8.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.MyBalance_8.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyBalance_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MyBalance_8.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.MyBalance_8.setObjectName(_fromUtf8("MyBalance_8"))
        self.MyBalance_7 = QtWidgets.QLabel(self.frame_6)
        self.MyBalance_7.setGeometry(QtCore.QRect(170, 10, 251, 20))
        self.MyBalance_7.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.MyBalance_7.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyBalance_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MyBalance_7.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.MyBalance_7.setObjectName(_fromUtf8("MyBalance_7"))
        self.gridLayout_3.addWidget(self.frame_6, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem17, 2, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem18)
        self.LineBalance_7 = QtWidgets.QFrame(self.SendBitcoins)
        self.LineBalance_7.setMinimumSize(QtCore.QSize(600, 0))
        self.LineBalance_7.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_7.setObjectName(_fromUtf8("LineBalance_7"))
        self.verticalLayout_8.addWidget(self.LineBalance_7)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem19)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.AdvancedSend = QtWidgets.QPushButton(self.SendBitcoins)
        self.AdvancedSend.setMinimumSize(QtCore.QSize(250, 50))
        self.AdvancedSend.setMaximumSize(QtCore.QSize(250, 50))
        self.AdvancedSend.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AdvancedSend.setStyleSheet(
            _fromUtf8(
                "QPushButton#AdvancedSend {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#AdvancedSend:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_gear_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.AdvancedSend.setIcon(icon14)
        self.AdvancedSend.setObjectName(_fromUtf8("AdvancedSend"))
        self.horizontalLayout_12.addWidget(self.AdvancedSend)
        self.ExplainSpend = QtWidgets.QPushButton(self.SendBitcoins)
        self.ExplainSpend.setMinimumSize(QtCore.QSize(50, 50))
        self.ExplainSpend.setMaximumSize(QtCore.QSize(50, 50))
        self.ExplainSpend.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainSpend.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainSpend {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainSpend:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainSpend.setIconSize(QtCore.QSize(20, 20))
        self.ExplainSpend.setObjectName(_fromUtf8("ExplainSpend"))
        self.horizontalLayout_12.addWidget(self.ExplainSpend)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem21)
        self.SendMyBitcoins = QtWidgets.QPushButton(self.SendBitcoins)
        self.SendMyBitcoins.setMinimumSize(QtCore.QSize(300, 50))
        self.SendMyBitcoins.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(1)  # Changed from -1
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendMyBitcoins.setFont(font)
        self.SendMyBitcoins.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SendMyBitcoins.setStyleSheet(
            _fromUtf8(
                "QPushButton#SendMyBitcoins {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#SendMyBitcoins:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.SendMyBitcoins.setIcon(icon15)
        self.SendMyBitcoins.setIconSize(QtCore.QSize(20, 20))
        self.SendMyBitcoins.setObjectName(_fromUtf8("SendMyBitcoins"))
        self.horizontalLayout_12.addWidget(self.SendMyBitcoins)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem22)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem23)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.LineBalance_8 = QtWidgets.QFrame(self.SendBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_8.sizePolicy().hasHeightForWidth())
        self.LineBalance_8.setSizePolicy(sizePolicy)
        self.LineBalance_8.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_8.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_8.setObjectName(_fromUtf8("LineBalance_8"))
        self.horizontalLayout_13.addWidget(self.LineBalance_8)
        self.MyBalance_9 = QtWidgets.QLabel(self.SendBitcoins)
        self.MyBalance_9.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyBalance_9.setFont(font)
        self.MyBalance_9.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.MyBalance_9.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.MyBalance_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MyBalance_9.setObjectName(_fromUtf8("MyBalance_9"))
        self.horizontalLayout_13.addWidget(self.MyBalance_9)
        self.LineBalance_9 = QtWidgets.QFrame(self.SendBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_9.sizePolicy().hasHeightForWidth())
        self.LineBalance_9.setSizePolicy(sizePolicy)
        self.LineBalance_9.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_9.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_9.setObjectName(_fromUtf8("LineBalance_9"))
        self.horizontalLayout_13.addWidget(self.LineBalance_9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem24)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem25)
        self.LabelStepOne = QtWidgets.QTextBrowser(self.SendBitcoins)
        self.LabelStepOne.setMinimumSize(QtCore.QSize(300, 90))
        self.LabelStepOne.setMaximumSize(QtCore.QSize(300, 90))
        self.LabelStepOne.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.LabelStepOne.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.LabelStepOne.setObjectName(_fromUtf8("LabelStepOne"))
        self.horizontalLayout_14.addWidget(self.LabelStepOne)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem26)
        self.LabelStepTwo = QtWidgets.QTextBrowser(self.SendBitcoins)
        self.LabelStepTwo.setMinimumSize(QtCore.QSize(300, 90))
        self.LabelStepTwo.setMaximumSize(QtCore.QSize(250, 90))
        self.LabelStepTwo.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.LabelStepTwo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.LabelStepTwo.setObjectName(_fromUtf8("LabelStepTwo"))
        self.horizontalLayout_14.addWidget(self.LabelStepTwo)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem27)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem28)
        self.LineBalance_12 = QtWidgets.QFrame(self.SendBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_12.sizePolicy().hasHeightForWidth())
        self.LineBalance_12.setSizePolicy(sizePolicy)
        self.LineBalance_12.setMinimumSize(QtCore.QSize(800, 0))
        self.LineBalance_12.setMaximumSize(QtCore.QSize(800, 16777215))
        self.LineBalance_12.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_12.setObjectName(_fromUtf8("LineBalance_12"))
        self.verticalLayout_8.addWidget(self.LineBalance_12)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem29)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem30)
        self.CreateSignatureOne = QtWidgets.QPushButton(self.SendBitcoins)
        self.CreateSignatureOne.setMinimumSize(QtCore.QSize(300, 50))
        self.CreateSignatureOne.setMaximumSize(QtCore.QSize(300, 50))
        self.CreateSignatureOne.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CreateSignatureOne.setStyleSheet(
            _fromUtf8(
                "QPushButton#CreateSignatureOne {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#CreateSignatureOne:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_add_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.CreateSignatureOne.setIcon(icon16)
        self.CreateSignatureOne.setIconSize(QtCore.QSize(20, 20))
        self.CreateSignatureOne.setObjectName(_fromUtf8("CreateSignatureOne"))
        self.horizontalLayout_15.addWidget(self.CreateSignatureOne)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem31)
        self.OpenBitSignatureAndSend = QtWidgets.QPushButton(self.SendBitcoins)
        self.OpenBitSignatureAndSend.setMinimumSize(QtCore.QSize(300, 50))
        self.OpenBitSignatureAndSend.setMaximumSize(QtCore.QSize(300, 50))
        self.OpenBitSignatureAndSend.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.OpenBitSignatureAndSend.setStyleSheet(
            _fromUtf8(
                "QPushButton#OpenBitSignatureAndSend {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#OpenBitSignatureAndSend:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.OpenBitSignatureAndSend.setIcon(icon7)
        self.OpenBitSignatureAndSend.setIconSize(QtCore.QSize(20, 20))
        self.OpenBitSignatureAndSend.setObjectName(_fromUtf8("OpenBitSignatureAndSend"))
        self.horizontalLayout_15.addWidget(self.OpenBitSignatureAndSend)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem32)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem33)
        self.horizontalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem34)
        self.gridLayout_11.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(1, icon17)

        self.Tabs.addTab(self.SendBitcoins, icon17, _fromUtf8(""))
        self.ReceiveBitcoins = QtWidgets.QWidget()
        self.ReceiveBitcoins.setObjectName(_fromUtf8("ReceiveBitcoins"))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ReceiveBitcoins)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame_8 = QtWidgets.QFrame(self.ReceiveBitcoins)
        self.frame_8.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_8.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_8 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.formLayout_9 = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout_9.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.frame_21 = QtWidgets.QFrame(self.frame_8)
        self.frame_21.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_21.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_21.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName(_fromUtf8("frame_21"))
        self.horizontalLayout_17.addWidget(self.frame_21)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_10.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_8)
        self.label_10.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_17.addLayout(self.verticalLayout_10)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem35)
        self.commandLinkButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.commandLinkButton_4.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_4.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_4.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_4 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_4:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_4.setIcon(icon1)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_4.setObjectName(_fromUtf8("commandLinkButton_4"))
        self.horizontalLayout_17.addWidget(self.commandLinkButton_4)
        self.formLayout_9.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_17)
        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setContentsMargins(40, 10, 10, 10)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setSpacing(20)
        self.horizontalLayout_59.setObjectName(_fromUtf8("horizontalLayout_59"))
        self.LineBalance_24 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_24.sizePolicy().hasHeightForWidth())
        self.LineBalance_24.setSizePolicy(sizePolicy)
        self.LineBalance_24.setMinimumSize(QtCore.QSize(20, 0))
        self.LineBalance_24.setMaximumSize(QtCore.QSize(20, 16777215))
        self.LineBalance_24.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_24.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_24.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_24.setObjectName(_fromUtf8("LineBalance_24"))
        self.horizontalLayout_59.addWidget(self.LineBalance_24)
        self.ContactLabel_2 = QtWidgets.QLabel(self.ReceiveBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ContactLabel_2.setFont(font)
        self.ContactLabel_2.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 21px "Arial";'))
        self.ContactLabel_2.setObjectName(_fromUtf8("ContactLabel_2"))
        self.horizontalLayout_59.addWidget(self.ContactLabel_2)
        self.LineBalance_25 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_25.sizePolicy().hasHeightForWidth())
        self.LineBalance_25.setSizePolicy(sizePolicy)
        self.LineBalance_25.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_25.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_25.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_25.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_25.setObjectName(_fromUtf8("LineBalance_25"))
        self.horizontalLayout_59.addWidget(self.LineBalance_25)
        self.ExplainReceive = QtWidgets.QPushButton(self.ReceiveBitcoins)
        self.ExplainReceive.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainReceive.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainReceive.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainReceive.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainReceive {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainReceive:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainReceive.setIconSize(QtCore.QSize(20, 20))
        self.ExplainReceive.setObjectName(_fromUtf8("ExplainReceive"))
        self.horizontalLayout_59.addWidget(self.ExplainReceive)
        self.verticalLayout_11.addLayout(self.horizontalLayout_59)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem36)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.frame_10 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(2000, 40))
        self.frame_10.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_10 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.MyAddress = QtWidgets.QLabel(self.frame_10)
        self.MyAddress.setSizePolicy(sizePolicy)
        self.MyAddress.setMinimumSize(QtCore.QSize(441, 40))
        self.MyAddress.setMaximumSize(QtCore.QSize(2000, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyAddress.setFont(font)
        self.MyAddress.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))
        self.MyAddress.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyAddress.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.MyAddress.setObjectName(_fromUtf8("MyAddress"))
        self.horizontalLayout_18.addWidget(self.frame_10)
        spacerItem37 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem37)
        self.CopyAddressToClipboard = QtWidgets.QPushButton(self.ReceiveBitcoins)
        self.CopyAddressToClipboard.setMinimumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard.setMaximumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CopyAddressToClipboard.setStyleSheet(
            _fromUtf8(
                "QPushButton#CopyAddressToClipboard {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#CopyAddressToClipboard:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.CopyAddressToClipboard.setText(_fromUtf8(""))
        self.CopyAddressToClipboard.setIcon(icon2)
        self.CopyAddressToClipboard.setIconSize(QtCore.QSize(20, 20))
        self.CopyAddressToClipboard.setFlat(False)
        self.CopyAddressToClipboard.setObjectName(_fromUtf8("CopyAddressToClipboard"))
        self.horizontalLayout_18.addWidget(self.CopyAddressToClipboard)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem38)
        self.LineBalance_13 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_13.sizePolicy().hasHeightForWidth())
        self.LineBalance_13.setSizePolicy(sizePolicy)
        self.LineBalance_13.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_13.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_13.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_13.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_13.setObjectName(_fromUtf8("LineBalance_13"))
        self.verticalLayout_11.addWidget(self.LineBalance_13)
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem39)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.frame_11 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_11.setMaximumSize(QtCore.QSize(2000, 40))
        self.frame_11.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_11 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.MyAddress_3 = QtWidgets.QLabel(self.frame_11)
        self.MyAddress_3.setSizePolicy(sizePolicy)
        self.MyAddress_3.setMinimumSize(QtCore.QSize(441, 40))
        self.MyAddress_3.setMaximumSize(QtCore.QSize(2000, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyAddress_3.setFont(font)
        self.MyAddress_3.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))
        self.MyAddress_3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyAddress_3.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.MyAddress_3.setObjectName(_fromUtf8("MyAddress_3"))
        self.horizontalLayout_19.addWidget(self.frame_11)
        spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem40)
        self.CopyAddressToClipboard_2 = QtWidgets.QPushButton(self.ReceiveBitcoins)
        self.CopyAddressToClipboard_2.setMinimumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard_2.setMaximumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CopyAddressToClipboard_2.setStyleSheet(
            _fromUtf8(
                "QPushButton#CopyAddressToClipboard_2 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#CopyAddressToClipboard_2:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.CopyAddressToClipboard_2.setText(_fromUtf8(""))
        self.CopyAddressToClipboard_2.setIcon(icon2)
        self.CopyAddressToClipboard_2.setIconSize(QtCore.QSize(20, 20))
        self.CopyAddressToClipboard_2.setFlat(False)
        self.CopyAddressToClipboard_2.setObjectName(_fromUtf8("CopyAddressToClipboard_2"))
        self.horizontalLayout_19.addWidget(self.CopyAddressToClipboard_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.BitmessageStatus = QtWidgets.QLabel(self.ReceiveBitcoins)
        self.BitmessageStatus.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.BitmessageStatus.setObjectName(_fromUtf8("BitmessageStatus"))
        self.verticalLayout_12.addWidget(self.BitmessageStatus)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.EnableBitmessage = QtWidgets.QCheckBox(self.ReceiveBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.EnableBitmessage.setFont(font)
        self.EnableBitmessage.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 15px "Arial";'))
        self.EnableBitmessage.setObjectName(_fromUtf8("EnableBitmessage"))
        self.horizontalLayout_20.addWidget(self.EnableBitmessage)
        self.EnableIRC = QtWidgets.QCheckBox(self.ReceiveBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.EnableIRC.setFont(font)
        self.EnableIRC.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 15px "Arial";'))
        self.EnableIRC.setObjectName(_fromUtf8("EnableIRC"))
        self.horizontalLayout_20.addWidget(self.EnableIRC)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem41)
        self.verticalLayout_12.addLayout(self.horizontalLayout_20)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem42)
        self.LineBalance_14 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_14.sizePolicy().hasHeightForWidth())
        self.LineBalance_14.setSizePolicy(sizePolicy)
        self.LineBalance_14.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_14.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_14.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_14.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_14.setObjectName(_fromUtf8("LineBalance_14"))
        self.verticalLayout_11.addWidget(self.LineBalance_14)
        spacerItem43 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem43)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.frame_12 = QtWidgets.QFrame(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_12.setMaximumSize(QtCore.QSize(2000, 40))
        self.frame_12.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_12 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.MyEmail = QtWidgets.QLabel(self.frame_12)
        self.MyEmail.setSizePolicy(sizePolicy)
        self.MyEmail.setMinimumSize(QtCore.QSize(441, 40))
        self.MyEmail.setMaximumSize(QtCore.QSize(2000, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyEmail.setFont(font)
        self.MyEmail.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 16px "Arial";'))
        self.MyEmail.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyEmail.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.MyEmail.setObjectName(_fromUtf8("MyEmail"))
        self.horizontalLayout_21.addWidget(self.frame_12)
        spacerItem44 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem44)
        self.AddEmail_2 = QtWidgets.QPushButton(self.ReceiveBitcoins)
        self.AddEmail_2.setMinimumSize(QtCore.QSize(40, 40))
        self.AddEmail_2.setMaximumSize(QtCore.QSize(40, 40))
        self.AddEmail_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AddEmail_2.setStyleSheet(
            _fromUtf8(
                "QPushButton#AddEmail_2 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#AddEmail_2:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.AddEmail_2.setText(_fromUtf8(""))
        self.AddEmail_2.setIcon(icon2)
        self.AddEmail_2.setIconSize(QtCore.QSize(20, 20))
        self.AddEmail_2.setFlat(False)
        self.AddEmail_2.setObjectName(_fromUtf8("AddEmail_2"))
        self.horizontalLayout_21.addWidget(self.AddEmail_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_21)
        self.EmailStatus = QtWidgets.QLabel(self.ReceiveBitcoins)
        self.EmailStatus.setMinimumSize(QtCore.QSize(0, 20))
        self.EmailStatus.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.EmailStatus.setObjectName(_fromUtf8("EmailStatus"))
        self.verticalLayout_11.addWidget(self.EmailStatus)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.EmailBox = QtWidgets.QLineEdit(self.ReceiveBitcoins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmailBox.sizePolicy().hasHeightForWidth())
        self.EmailBox.setSizePolicy(sizePolicy)
        self.EmailBox.setMinimumSize(QtCore.QSize(0, 40))
        self.EmailBox.setMaximumSize(QtCore.QSize(6000, 40))
        self.EmailBox.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                ""
            )
        )
        self.EmailBox.setInputMask(_fromUtf8(""))
        self.EmailBox.setText(_fromUtf8(""))
        self.EmailBox.setObjectName(_fromUtf8("EmailBox"))
        self.horizontalLayout_22.addWidget(self.EmailBox)
        spacerItem45 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem45)
        self.AddEmail = QtWidgets.QPushButton(self.ReceiveBitcoins)
        self.AddEmail.setMinimumSize(QtCore.QSize(150, 40))
        self.AddEmail.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.AddEmail.setFont(font)
        self.AddEmail.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AddEmail.setStyleSheet(
            _fromUtf8(
                "QPushButton#AddEmail {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#AddEmail:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.AddEmail.setIcon(icon16)
        self.AddEmail.setIconSize(QtCore.QSize(20, 20))
        self.AddEmail.setObjectName(_fromUtf8("AddEmail"))
        self.horizontalLayout_22.addWidget(self.AddEmail)
        spacerItem46 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem46)
        self.verticalLayout_11.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.EnableEmail = QtWidgets.QCheckBox(self.ReceiveBitcoins)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.EnableEmail.setFont(font)
        self.EnableEmail.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 15px "Arial";'))
        self.EnableEmail.setObjectName(_fromUtf8("EnableEmail"))
        self.horizontalLayout_23.addWidget(self.EnableEmail)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem47)
        self.verticalLayout_11.addLayout(self.horizontalLayout_23)
        self.OutboxButton = QtWidgets.QPushButton(self.ReceiveBitcoins)
        self.OutboxButton.setMinimumSize(QtCore.QSize(150, 40))
        self.OutboxButton.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.OutboxButton.setFont(font)
        self.OutboxButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.OutboxButton.setStyleSheet(
            _fromUtf8(
                "QPushButton#OutboxButton {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#OutboxButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.OutboxButton.setObjectName(_fromUtf8("OutboxButton"))
        self.verticalLayout_11.addWidget(self.OutboxButton)

        spacerItem48 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem48)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem49)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        spacerItem50 = QtWidgets.QSpacerItem(343, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem50, 1, 1, 1, 1)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(2, icon18)

        self.Tabs.addTab(self.ReceiveBitcoins, icon18, _fromUtf8(""))
        self.History = QtWidgets.QWidget()
        self.History.setStyleSheet(
            _fromUtf8(
                "QTableView#FullHistory QHeaderView\n"
                "{\n"
                "    /* draw the hole hor top & bottom line for the header */\n"
                "    height: 30px;\n"
                "border-top-color: #ffffff;\n"
                "}\n"
                "\n"
                "QTableView#FullHistory QHeaderView::section:horizontal:first\n"
                "{\n"
                "border-top-color: #ffffff;\n"
                "}\n"
                "\n"
                "QTableView#FullHistory QHeaderView::section:horizontal:last\n"
                "{\n"
                "    border-top-color: #ffffff;\n"
                "}\n"
                "\n"
                "\n"
                "\n"
                "QTableView#FullHistory QHeaderView::section:horizontal\n"
                "{\n"
                "    /* for each section draw ONLY left & right lines */\n"
                "    height: 24px;\n"
                "border-top-color: #ffffff;\n"
                "border-bottom-color: #9c9c9c;\n"
                "border-left-color:#ffffff;\n"
                "border-right-color:#9c9c9c;\n"
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "\n"
                "background-color: #fbfbfb;\n"
                "\n"
                " }\n"
                "QTableView {\n"
                "\n"
                "    background-color: rgba(251, 251, 251, 100%);\n"
                "color: #24282C;\n"
                "\n"
                "\n"
                "}\n"
                "\n"
                "QTableView::item:selected\n"
                "\n"
                "{\n"
                "\n"
                "    color: #24282C;\n"
                "\n"
                "    background-color:rgba(200, 200, 200, 25%);\n"
                "\n"
                "}\n"
                "\n"
                "QTableView::item:focus\n"
                "\n"
                "{\n"
                "\n"
                "color: #24282C;\n"
                "\n"
                "}"
            )
        )
        self.History.setObjectName(_fromUtf8("History"))
        self.gridLayout_5 = QtWidgets.QGridLayout(self.History)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_9 = QtWidgets.QFrame(self.History)
        self.frame_9.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_9.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_9 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.formLayout_10 = QtWidgets.QFormLayout(self.frame_9)
        self.formLayout_10.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.frame_22 = QtWidgets.QFrame(self.frame_9)
        self.frame_22.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_22.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_22.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_22.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_22.setObjectName(_fromUtf8("frame_22"))
        self.horizontalLayout_25.addWidget(self.frame_22)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_14 = QtWidgets.QLabel(self.frame_9)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_13.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_9)
        self.label_15.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_13.addWidget(self.label_15)
        self.horizontalLayout_25.addLayout(self.verticalLayout_13)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem51)
        self.commandLinkButton_5 = QtWidgets.QPushButton(self.frame_9)
        self.commandLinkButton_5.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_5.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_5.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_5 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_5:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_5.setIcon(icon1)
        self.commandLinkButton_5.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        self.horizontalLayout_25.addWidget(self.commandLinkButton_5)
        self.formLayout_10.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_25)
        self.gridLayout_5.addWidget(self.frame_9, 0, 0, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setContentsMargins(0, 0, -1, 20)
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.frame_13 = QtWidgets.QFrame(self.History)
        self.frame_13.setMinimumSize(QtCore.QSize(570, 40))
        self.frame_13.setMaximumSize(QtCore.QSize(570, 40))
        self.frame_13.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_13 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName(_fromUtf8("frame_13"))
        self.MyAddress_2 = QtWidgets.QLabel(self.frame_13)
        self.MyAddress_2.setMinimumSize(QtCore.QSize(570, 40))
        self.MyAddress_2.setMaximumSize(QtCore.QSize(570, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MyAddress_2.setFont(font)
        self.MyAddress_2.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))
        self.MyAddress_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyAddress_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.MyAddress_2.setObjectName(_fromUtf8("MyAddress_2"))
        self.horizontalLayout_27.addWidget(self.frame_13)
        self.CopyAddressToClipboard_5 = QtWidgets.QPushButton(self.History)
        self.CopyAddressToClipboard_5.setMinimumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard_5.setMaximumSize(QtCore.QSize(40, 40))
        self.CopyAddressToClipboard_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CopyAddressToClipboard_5.setStyleSheet(
            _fromUtf8(
                "QPushButton#CopyAddressToClipboard_5 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#CopyAddressToClipboard_5:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.CopyAddressToClipboard_5.setText(_fromUtf8(""))
        self.CopyAddressToClipboard_5.setIcon(icon2)
        self.CopyAddressToClipboard_5.setIconSize(QtCore.QSize(20, 20))
        self.CopyAddressToClipboard_5.setFlat(False)
        self.CopyAddressToClipboard_5.setObjectName(_fromUtf8("CopyAddressToClipboard_5"))
        self.horizontalLayout_27.addWidget(self.CopyAddressToClipboard_5)
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem52)
        self.verticalLayout_14.addLayout(self.horizontalLayout_27)
        self.verticalLayout_17.addLayout(self.verticalLayout_14)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.frame_14 = QtWidgets.QFrame(self.History)
        self.frame_14.setMinimumSize(QtCore.QSize(500, 40))
        self.frame_14.setMaximumSize(QtCore.QSize(500, 40))
        self.frame_14.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_14 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_14.setObjectName(_fromUtf8("frame_14"))
        self.HistoryBalance = QtWidgets.QLabel(self.frame_14)
        self.HistoryBalance.setGeometry(QtCore.QRect(0, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.HistoryBalance.setFont(font)
        self.HistoryBalance.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.HistoryBalance.setStyleSheet(_fromUtf8("color: rgb(104, 104, 104);\n" 'font: bold 16px "Arial";'))
        self.HistoryBalance.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.HistoryBalance.setObjectName(_fromUtf8("MyBalance"))
        self.Symbol_5 = QtWidgets.QLabel(self.frame_14)
        self.Symbol_5.setGeometry(QtCore.QRect(430, 10, 41, 21))
        self.Symbol_5.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.Symbol_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Symbol_5.setObjectName(_fromUtf8("Symbol_5"))
        self.MyBalance = QtWidgets.QLabel(self.frame_14)
        self.MyBalance.setGeometry(QtCore.QRect(170, 10, 251, 20))
        self.MyBalance.setStyleSheet(_fromUtf8('font: bold 16px "Arial";\n' "color: #24282C;"))
        self.MyBalance.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.MyBalance.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MyBalance.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.MyBalance.setObjectName(_fromUtf8("MyBalance"))
        self.horizontalLayout_26.addWidget(self.frame_14)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem53)
        self.verticalLayout_17.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.TitleRecent = QtWidgets.QLabel(self.History)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleRecent.sizePolicy().hasHeightForWidth())
        self.TitleRecent.setSizePolicy(sizePolicy)
        self.TitleRecent.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TitleRecent.setFont(font)
        self.TitleRecent.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.TitleRecent.setObjectName(_fromUtf8("TitleRecent"))
        self.horizontalLayout_28.addWidget(self.TitleRecent)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem54)
        self.KeysConnected = QtWidgets.QLineEdit(self.History)
        self.KeysConnected.setMinimumSize(QtCore.QSize(300, 40))
        self.KeysConnected.setMaximumSize(QtCore.QSize(16777215, 40))
        self.KeysConnected.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.KeysConnected.setReadOnly(True)
        self.KeysConnected.setObjectName(_fromUtf8("KeysConnected"))
        self.horizontalLayout_28.addWidget(self.KeysConnected)
        self.Refresh = QtWidgets.QPushButton(self.History)
        self.Refresh.setMinimumSize(QtCore.QSize(40, 40))
        self.Refresh.setMaximumSize(QtCore.QSize(40, 40))
        self.Refresh.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Refresh.setStyleSheet(
            _fromUtf8(
                "QPushButton#Refresh {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#Refresh:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.Refresh.setText(_fromUtf8(""))
        self.Refresh.setIcon(icon12)
        self.Refresh.setIconSize(QtCore.QSize(20, 20))
        self.Refresh.setObjectName(_fromUtf8("Refresh"))
        self.horizontalLayout_28.addWidget(self.Refresh)
        self.verticalLayout_15.addLayout(self.horizontalLayout_28)
        self.HistorylistWidget = QtWidgets.QListWidget(self.History)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.HistorylistWidget.sizePolicy().hasHeightForWidth())
        self.HistorylistWidget.setSizePolicy(sizePolicy)
        self.HistorylistWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.HistorylistWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.HistorylistWidget.setStyleSheet(
            _fromUtf8(
                'font: 16px "Courier";\n'
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.HistorylistWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.HistorylistWidget.setObjectName(_fromUtf8("HistorylistWidget"))
        self.verticalLayout_15.addWidget(self.HistorylistWidget)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setContentsMargins(0, 20, -1, 7)
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        spacerItem55 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem55)
        self.labelProgress2 = QtWidgets.QLabel(self.History)
        self.labelProgress2.setMinimumSize(QtCore.QSize(0, 0))
        self.labelProgress2.setMaximumSize(QtCore.QSize(16777215, 19))
        self.labelProgress2.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: 13px "Arial";'))
        self.labelProgress2.setObjectName(_fromUtf8("labelProgress2"))
        self.horizontalLayout_31.addWidget(self.labelProgress2)
        self.progressBar2 = QtWidgets.QProgressBar(self.History)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar2.sizePolicy().hasHeightForWidth())
        self.progressBar2.setSizePolicy(sizePolicy)
        self.progressBar2.setMinimumSize(QtCore.QSize(0, 21))
        self.progressBar2.setMaximumSize(QtCore.QSize(100000, 21))
        self.progressBar2.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: #f7931a;\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setObjectName(_fromUtf8("progressBar2"))
        self.horizontalLayout_31.addWidget(self.progressBar2)
        self.Rescan2 = QtWidgets.QPushButton(self.History)
        self.Rescan2.setMinimumSize(QtCore.QSize(75, 23))
        self.Rescan2.setMaximumSize(QtCore.QSize(150, 23))
        self.Rescan2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Rescan2.setStyleSheet(
            _fromUtf8(
                "QPushButton#Rescan2 {\n"
                '    font: bold 12px "Arial";\n'
                "color: #24282C;\n"
                "background-color: #fbfbfb;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "     \n"
                "}\n"
                " QPushButton#Rescan2:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                " }"
            )
        )
        self.Rescan2.setIcon(icon12)
        self.Rescan2.setObjectName(_fromUtf8("Rescan2"))
        self.horizontalLayout_31.addWidget(self.Rescan2)
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem56)
        self.verticalLayout_15.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_30.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.History_Title = QtWidgets.QLabel(self.History)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.History_Title.setFont(font)
        self.History_Title.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.History_Title.setObjectName(_fromUtf8("History_Title"))
        self.horizontalLayout_29.addWidget(self.History_Title)
        self.ExplainHistory = QtWidgets.QPushButton(self.History)
        self.ExplainHistory.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainHistory.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainHistory.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainHistory.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainHistory {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainHistory:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainHistory.setIconSize(QtCore.QSize(20, 20))
        self.ExplainHistory.setObjectName(_fromUtf8("ExplainHistory"))
        self.horizontalLayout_29.addWidget(self.ExplainHistory)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        self.FullHistory = QtWidgets.QTableWidget(self.History)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.FullHistory.sizePolicy().hasHeightForWidth())
        self.FullHistory.setSizePolicy(sizePolicy)
        self.FullHistory.setMinimumSize(QtCore.QSize(0, 300))
        self.FullHistory.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FullHistory.setSizeIncrement(QtCore.QSize(0, 0))
        self.FullHistory.setBaseSize(QtCore.QSize(0, 0))
        self.FullHistory.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "\n"
                "border-radius: 8px;\n"
                "border-width: 1px;\n"
                " border-style: inset;\n"
                "border-color: lightgrey;\n"
                "background-color:rgba(251, 251, 251, 80%);"
            )
        )
        self.FullHistory.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.FullHistory.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.FullHistory.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.FullHistory.setObjectName(_fromUtf8("FullHistory"))
        self.FullHistory.setColumnCount(4)
        self.FullHistory.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.FullHistory.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FullHistory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FullHistory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FullHistory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FullHistory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsSelectable
            | QtCore.Qt.ItemFlag.ItemIsEditable
            | QtCore.Qt.ItemFlag.ItemIsDragEnabled
            | QtCore.Qt.ItemFlag.ItemIsUserCheckable
            | QtCore.Qt.ItemFlag.ItemIsEnabled
        )
        self.FullHistory.setItem(0, 0, item)
        self.FullHistory.horizontalHeader().setStretchLastSection(True)
        self.FullHistory.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_16.addWidget(self.FullHistory)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem57)
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem58)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem59)
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem60)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem61)
        spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem62)
        self.ExportToCSV = QtWidgets.QPushButton(self.History)
        self.ExportToCSV.setMinimumSize(QtCore.QSize(150, 40))
        self.ExportToCSV.setMaximumSize(QtCore.QSize(150, 40))
        self.ExportToCSV.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExportToCSV.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExportToCSV {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExportToCSV:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        icon19 = QtGui.QIcon()
        icon19.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_export_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.ExportToCSV.setIcon(icon19)
        self.ExportToCSV.setIconSize(QtCore.QSize(20, 20))
        self.ExportToCSV.setObjectName(_fromUtf8("ExportToCSV"))
        self.horizontalLayout_32.addWidget(self.ExportToCSV)
        spacerItem63 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem63)
        self.ClearHistory = QtWidgets.QPushButton(self.History)
        self.ClearHistory.setMinimumSize(QtCore.QSize(150, 40))
        self.ClearHistory.setMaximumSize(QtCore.QSize(150, 40))
        self.ClearHistory.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ClearHistory.setStyleSheet(
            _fromUtf8(
                "QPushButton#ClearHistory {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ClearHistory:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        icon20 = QtGui.QIcon()
        icon20.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_trash_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.ClearHistory.setIcon(icon20)
        self.ClearHistory.setIconSize(QtCore.QSize(20, 20))
        self.ClearHistory.setObjectName(_fromUtf8("ClearHistory"))
        self.horizontalLayout_32.addWidget(self.ClearHistory)
        self.verticalLayout_16.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_30.addLayout(self.verticalLayout_16)
        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_30)
        self.gridLayout_5.addLayout(self.verticalLayout_17, 1, 0, 1, 1)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(3, icon21)

        self.Tabs.addTab(self.History, icon21, _fromUtf8(""))
        self.Chat = QtWidgets.QWidget()
        self.Chat.setObjectName(_fromUtf8("Chat"))
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Chat)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.frame_15 = QtWidgets.QFrame(self.Chat)
        self.frame_15.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_15.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_15 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName(_fromUtf8("frame_15"))
        self.formLayout_11 = QtWidgets.QFormLayout(self.frame_15)
        self.formLayout_11.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_11.setObjectName(_fromUtf8("formLayout_11"))
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.frame_23 = QtWidgets.QFrame(self.frame_15)
        self.frame_23.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_23.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_23.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_23.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_23.setObjectName(_fromUtf8("frame_23"))
        self.horizontalLayout_33.addWidget(self.frame_23)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.label_16 = QtWidgets.QLabel(self.frame_15)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_18.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame_15)
        self.label_17.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_18.addWidget(self.label_17)
        self.horizontalLayout_33.addLayout(self.verticalLayout_18)
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem64)
        self.commandLinkButton_6 = QtWidgets.QPushButton(self.frame_15)
        self.commandLinkButton_6.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_6.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_6.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_6 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_6:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_6.setIcon(icon1)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_6.setObjectName(_fromUtf8("commandLinkButton_6"))
        self.horizontalLayout_33.addWidget(self.commandLinkButton_6)
        self.formLayout_11.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_33)
        self.gridLayout_8.addWidget(self.frame_15, 0, 0, 1, 1)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_7.setContentsMargins(10, 10, 10, 10)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.webView = QtWebEngineWidgets.QWebEngineView(self.Chat)
        self.webView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.webView.setFont(font)
        self.webView.setAccessibleName(_fromUtf8(""))
        self.webView.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color: rgb(251, 251, 251);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        # self.webView.setUrl(QtCore.QUrl(_fromUtf8("'<b>Hello World</b>'")))
        self.webView.setHtml(_fromUtf8("<iframe src=" + self.NewCoin["IRC"] + " width='100%' height='500'></iframe></div></div></div>"))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.webView)
        self.gridLayout_8.addLayout(self.formLayout_7, 1, 0, 1, 1)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(4, icon22)

        self.Tabs.addTab(self.Chat, icon22, _fromUtf8(""))
        self.MakeAnOffer = QtWidgets.QWidget()
        self.MakeAnOffer.setObjectName(_fromUtf8("MakeAnOffer"))
        self.gridLayout_12 = QtWidgets.QGridLayout(self.MakeAnOffer)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.frame_16 = QtWidgets.QFrame(self.MakeAnOffer)
        self.frame_16.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_16.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_16 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName(_fromUtf8("frame_16"))
        self.formLayout_12 = QtWidgets.QFormLayout(self.frame_16)
        self.formLayout_12.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_12.setObjectName(_fromUtf8("formLayout_12"))
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.frame_24 = QtWidgets.QFrame(self.frame_16)
        self.frame_24.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_24.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_24.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_24.setObjectName(_fromUtf8("frame_24"))
        self.horizontalLayout_34.addWidget(self.frame_24)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.label_18 = QtWidgets.QLabel(self.frame_16)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_19.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.frame_16)
        self.label_19.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_19.addWidget(self.label_19)
        self.horizontalLayout_34.addLayout(self.verticalLayout_19)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem65)
        self.commandLinkButton_7 = QtWidgets.QPushButton(self.frame_16)
        self.commandLinkButton_7.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_7.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_7.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_7 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_7:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_7.setIcon(icon1)
        self.commandLinkButton_7.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_7.setObjectName(_fromUtf8("commandLinkButton_7"))
        self.horizontalLayout_34.addWidget(self.commandLinkButton_7)
        self.formLayout_12.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_34)
        self.gridLayout_12.addWidget(self.frame_16, 0, 0, 1, 1)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setSpacing(6)
        self.horizontalLayout_41.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_41.setObjectName(_fromUtf8("horizontalLayout_41"))
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName(_fromUtf8("verticalLayout_27"))
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setSpacing(20)
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        self.LineBalance_17 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_17.sizePolicy().hasHeightForWidth())
        self.LineBalance_17.setSizePolicy(sizePolicy)
        self.LineBalance_17.setMinimumSize(QtCore.QSize(20, 0))
        self.LineBalance_17.setMaximumSize(QtCore.QSize(20, 16777215))
        self.LineBalance_17.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_17.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_17.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_17.setObjectName(_fromUtf8("LineBalance_17"))
        self.horizontalLayout_40.addWidget(self.LineBalance_17)
        self.SmartContractLabel = QtWidgets.QLabel(self.MakeAnOffer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SmartContractLabel.setFont(font)
        self.SmartContractLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 21px "Arial";'))
        self.SmartContractLabel.setObjectName(_fromUtf8("SmartContractLabel"))
        self.horizontalLayout_40.addWidget(self.SmartContractLabel)
        self.LineBalance_16 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_16.sizePolicy().hasHeightForWidth())
        self.LineBalance_16.setSizePolicy(sizePolicy)
        self.LineBalance_16.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_16.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_16.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_16.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_16.setObjectName(_fromUtf8("LineBalance_16"))
        self.horizontalLayout_40.addWidget(self.LineBalance_16)
        self.ExplainContracts = QtWidgets.QPushButton(self.MakeAnOffer)
        self.ExplainContracts.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainContracts.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainContracts.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainContracts.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainContracts {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainContracts:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainContracts.setObjectName(_fromUtf8("ExplainContracts"))
        self.horizontalLayout_40.addWidget(self.ExplainContracts)
        self.verticalLayout_27.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setSpacing(10)
        self.horizontalLayout_54.setObjectName(_fromUtf8("horizontalLayout_54"))
        self.SendLabel_3 = QtWidgets.QLabel(self.MakeAnOffer)
        self.SendLabel_3.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendLabel_3.setFont(font)
        self.SendLabel_3.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.SendLabel_3.setObjectName(_fromUtf8("SendLabel_3"))
        self.horizontalLayout_54.addWidget(self.SendLabel_3)
        self.DescriptionBox = QtWidgets.QTextEdit(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DescriptionBox.sizePolicy().hasHeightForWidth())
        self.DescriptionBox.setSizePolicy(sizePolicy)
        self.DescriptionBox.setMinimumSize(QtCore.QSize(0, 89))
        self.DescriptionBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.DescriptionBox.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.DescriptionBox.setObjectName(_fromUtf8("DescriptionBox"))
        self.horizontalLayout_54.addWidget(self.DescriptionBox)
        self.verticalLayout_27.addLayout(self.horizontalLayout_54)
        spacerItem66 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem66)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName(_fromUtf8("horizontalLayout_42"))
        self.SendLabel_4 = QtWidgets.QLabel(self.MakeAnOffer)
        self.SendLabel_4.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendLabel_4.setFont(font)
        self.SendLabel_4.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.SendLabel_4.setObjectName(_fromUtf8("SendLabel_4"))
        self.horizontalLayout_42.addWidget(self.SendLabel_4)
        self.ImageBox = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.ImageBox.setMinimumSize(QtCore.QSize(0, 40))
        self.ImageBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ImageBox.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.ImageBox.setObjectName(_fromUtf8("ImageBox"))
        self.horizontalLayout_42.addWidget(self.ImageBox)
        self.AttachImage = QtWidgets.QPushButton(self.MakeAnOffer)
        self.AttachImage.setMinimumSize(QtCore.QSize(150, 40))
        self.AttachImage.setMaximumSize(QtCore.QSize(16777215, 40))
        self.AttachImage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AttachImage.setStyleSheet(
            _fromUtf8(
                "QPushButton#AttachImage {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#AttachImage:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.AttachImage.setIcon(icon3)
        self.AttachImage.setIconSize(QtCore.QSize(20, 20))
        self.AttachImage.setObjectName(_fromUtf8("AttachImage"))
        self.horizontalLayout_42.addWidget(self.AttachImage)
        self.verticalLayout_27.addLayout(self.horizontalLayout_42)
        spacerItem67 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem67)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName(_fromUtf8("horizontalLayout_43"))
        self.SendLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.SendLabel.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendLabel.setFont(font)
        self.SendLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.SendLabel.setObjectName(_fromUtf8("SendLabel"))
        self.horizontalLayout_43.addWidget(self.SendLabel)
        self.ContractTo = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.ContractTo.setMinimumSize(QtCore.QSize(0, 40))
        self.ContractTo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ContractTo.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.ContractTo.setObjectName(_fromUtf8("ContractTo"))
        self.horizontalLayout_43.addWidget(self.ContractTo)
        self.verticalLayout_27.addLayout(self.horizontalLayout_43)
        spacerItem68 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem68)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName(_fromUtf8("horizontalLayout_44"))
        self.ContractAmountLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.ContractAmountLabel.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ContractAmountLabel.setFont(font)
        self.ContractAmountLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.ContractAmountLabel.setObjectName(_fromUtf8("ContractAmountLabel"))
        self.horizontalLayout_44.addWidget(self.ContractAmountLabel)
        self.ContractAmount = QtWidgets.QLineEdit(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContractAmount.sizePolicy().hasHeightForWidth())
        self.ContractAmount.setSizePolicy(sizePolicy)
        self.ContractAmount.setMinimumSize(QtCore.QSize(210, 40))
        self.ContractAmount.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ContractAmount.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.ContractAmount.setObjectName(_fromUtf8("ContractAmount"))
        self.horizontalLayout_44.addWidget(self.ContractAmount)
        spacerItem69 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem69)
        self.WhoPays = QtWidgets.QComboBox(self.MakeAnOffer)
        self.WhoPays.setMinimumSize(QtCore.QSize(0, 40))
        self.WhoPays.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WhoPays.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.WhoPays.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.WhoPays.setObjectName(_fromUtf8("WhoPays"))
        self.WhoPays.addItem(_fromUtf8(""))
        self.WhoPays.addItem(_fromUtf8(""))
        self.horizontalLayout_44.addWidget(self.WhoPays)
        self.verticalLayout_27.addLayout(self.horizontalLayout_44)
        spacerItem70 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem70)
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName(_fromUtf8("horizontalLayout_45"))
        self.ContractFeeLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.ContractFeeLabel.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ContractFeeLabel.setFont(font)
        self.ContractFeeLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.ContractFeeLabel.setObjectName(_fromUtf8("ContractFeeLabel"))
        self.horizontalLayout_45.addWidget(self.ContractFeeLabel)
        self.ContractFee = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.ContractFee.setMinimumSize(QtCore.QSize(210, 40))
        self.ContractFee.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ContractFee.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        # self.ContractFee.setReadOnly(True)
        self.ContractFee.setObjectName(_fromUtf8("ContractFee"))
        self.horizontalLayout_45.addWidget(self.ContractFee)
        self.verticalLayout_27.addLayout(self.horizontalLayout_45)
        spacerItem71 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem71)
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName(_fromUtf8("horizontalLayout_46"))
        self.DepositLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.DepositLabel.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DepositLabel.setFont(font)
        self.DepositLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.DepositLabel.setObjectName(_fromUtf8("DepositLabel"))
        self.horizontalLayout_46.addWidget(self.DepositLabel)
        self.YouDeposit = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.YouDeposit.setMinimumSize(QtCore.QSize(0, 40))
        self.YouDeposit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.YouDeposit.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.YouDeposit.setObjectName(_fromUtf8("YouDeposit"))
        self.horizontalLayout_46.addWidget(self.YouDeposit)
        self.verticalLayout_27.addLayout(self.horizontalLayout_46)
        spacerItem72 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem72)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName(_fromUtf8("horizontalLayout_47"))
        self.TheDepositLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.TheDepositLabel.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TheDepositLabel.setFont(font)
        self.TheDepositLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.TheDepositLabel.setObjectName(_fromUtf8("TheDepositLabel"))
        self.horizontalLayout_47.addWidget(self.TheDepositLabel)
        self.TheyDeposit = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.TheyDeposit.setMinimumSize(QtCore.QSize(210, 40))
        self.TheyDeposit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.TheyDeposit.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.TheyDeposit.setObjectName(_fromUtf8("TheyDeposit"))
        self.horizontalLayout_47.addWidget(self.TheyDeposit)
        self.verticalLayout_27.addLayout(self.horizontalLayout_47)
        spacerItem73 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem73)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName(_fromUtf8("horizontalLayout_48"))
        self.TimeToCompleteLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.TimeToCompleteLabel.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TimeToCompleteLabel.setFont(font)
        self.TimeToCompleteLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.TimeToCompleteLabel.setObjectName(_fromUtf8("TimeToCompleteLabel"))
        self.horizontalLayout_48.addWidget(self.TimeToCompleteLabel)
        self.ContractTime = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.ContractTime.setMinimumSize(QtCore.QSize(210, 40))
        self.ContractTime.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ContractTime.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.ContractTime.setObjectName(_fromUtf8("ContractTime"))
        self.horizontalLayout_48.addWidget(self.ContractTime)
        self.DaysMultiplier = QtWidgets.QComboBox(self.MakeAnOffer)
        self.DaysMultiplier.setMinimumSize(QtCore.QSize(80, 40))
        self.DaysMultiplier.setMaximumSize(QtCore.QSize(80, 40))
        self.DaysMultiplier.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DaysMultiplier.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.DaysMultiplier.setObjectName(_fromUtf8("DaysMultiplier"))
        self.DaysMultiplier.addItem(_fromUtf8(""))
        self.DaysMultiplier.addItem(_fromUtf8(""))
        self.horizontalLayout_48.addWidget(self.DaysMultiplier)
        self.verticalLayout_27.addLayout(self.horizontalLayout_48)
        spacerItem74 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_27.addItem(spacerItem74)
        self.horizontalLayout_41.addLayout(self.verticalLayout_27)
        spacerItem75 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem75)
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_53.setObjectName(_fromUtf8("horizontalLayout_53"))
        self.line_2 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(0, 500))
        self.line_2.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: none  solid none none;"))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_53.addWidget(self.line_2)
        self.horizontalLayout_41.addLayout(self.horizontalLayout_53)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_28.setObjectName(_fromUtf8("verticalLayout_28"))
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setSpacing(20)
        self.horizontalLayout_55.setObjectName(_fromUtf8("horizontalLayout_55"))
        self.LineBalance_19 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_19.sizePolicy().hasHeightForWidth())
        self.LineBalance_19.setSizePolicy(sizePolicy)
        self.LineBalance_19.setMinimumSize(QtCore.QSize(20, 0))
        self.LineBalance_19.setMaximumSize(QtCore.QSize(20, 16777215))
        self.LineBalance_19.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_19.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_19.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_19.setObjectName(_fromUtf8("LineBalance_19"))
        self.horizontalLayout_55.addWidget(self.LineBalance_19)
        self.AutoBackupLabel_2 = QtWidgets.QLabel(self.MakeAnOffer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.AutoBackupLabel_2.setFont(font)
        self.AutoBackupLabel_2.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 21px "Arial";'))
        self.AutoBackupLabel_2.setObjectName(_fromUtf8("AutoBackupLabel_2"))
        self.horizontalLayout_55.addWidget(self.AutoBackupLabel_2)
        self.LineBalance_18 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_18.sizePolicy().hasHeightForWidth())
        self.LineBalance_18.setSizePolicy(sizePolicy)
        self.LineBalance_18.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_18.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_18.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_18.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_18.setObjectName(_fromUtf8("LineBalance_18"))
        self.horizontalLayout_55.addWidget(self.LineBalance_18)
        self.ExplainAutoBackupOffer = QtWidgets.QPushButton(self.MakeAnOffer)
        self.ExplainAutoBackupOffer.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainAutoBackupOffer.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainAutoBackupOffer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainAutoBackupOffer.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainAutoBackupOffer {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainAutoBackupOffer:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainAutoBackupOffer.setObjectName(_fromUtf8("ExplainAutoBackupOffer"))
        self.horizontalLayout_55.addWidget(self.ExplainAutoBackupOffer)
        self.verticalLayout_28.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName(_fromUtf8("horizontalLayout_52"))
        self.TxBackupPath = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.TxBackupPath.setMinimumSize(QtCore.QSize(0, 40))
        self.TxBackupPath.setMaximumSize(QtCore.QSize(16777215, 40))
        self.TxBackupPath.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.TxBackupPath.setObjectName(_fromUtf8("TxBackupPath"))
        self.horizontalLayout_52.addWidget(self.TxBackupPath)
        self.BrowseTxBackup = QtWidgets.QPushButton(self.MakeAnOffer)
        self.BrowseTxBackup.setMinimumSize(QtCore.QSize(40, 40))
        self.BrowseTxBackup.setMaximumSize(QtCore.QSize(40, 40))
        self.BrowseTxBackup.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BrowseTxBackup.setStyleSheet(
            _fromUtf8(
                "QPushButton#BrowseTxBackup {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#BrowseTxBackup:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.BrowseTxBackup.setText(_fromUtf8(""))
        self.BrowseTxBackup.setIcon(icon3)
        self.BrowseTxBackup.setIconSize(QtCore.QSize(20, 20))
        self.BrowseTxBackup.setObjectName(_fromUtf8("BrowseTxBackup"))
        self.horizontalLayout_52.addWidget(self.BrowseTxBackup)
        self.verticalLayout_28.addLayout(self.horizontalLayout_52)
        self.AutoBackupLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.AutoBackupLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 13px "Arial";'))
        self.AutoBackupLabel.setObjectName(_fromUtf8("AutoBackupLabel"))
        self.verticalLayout_28.addWidget(self.AutoBackupLabel)
        spacerItem76 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_28.addItem(spacerItem76)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName(_fromUtf8("verticalLayout_29"))
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setSpacing(20)
        self.horizontalLayout_50.setObjectName(_fromUtf8("horizontalLayout_50"))
        self.LineBalance_21 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_21.sizePolicy().hasHeightForWidth())
        self.LineBalance_21.setSizePolicy(sizePolicy)
        self.LineBalance_21.setMinimumSize(QtCore.QSize(20, 0))
        self.LineBalance_21.setMaximumSize(QtCore.QSize(20, 16777215))
        self.LineBalance_21.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_21.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_21.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_21.setObjectName(_fromUtf8("LineBalance_21"))
        self.horizontalLayout_50.addWidget(self.LineBalance_21)
        self.InstantRefundLabel = QtWidgets.QLabel(self.MakeAnOffer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.InstantRefundLabel.setFont(font)
        self.InstantRefundLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 21px "Arial";'))
        self.InstantRefundLabel.setObjectName(_fromUtf8("InstantRefundLabel"))
        self.horizontalLayout_50.addWidget(self.InstantRefundLabel)
        self.LineBalance_20 = QtWidgets.QFrame(self.MakeAnOffer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_20.sizePolicy().hasHeightForWidth())
        self.LineBalance_20.setSizePolicy(sizePolicy)
        self.LineBalance_20.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_20.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_20.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_20.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_20.setObjectName(_fromUtf8("LineBalance_20"))
        self.horizontalLayout_50.addWidget(self.LineBalance_20)
        self.instantexplain = QtWidgets.QPushButton(self.MakeAnOffer)
        self.instantexplain.setMinimumSize(QtCore.QSize(40, 40))
        self.instantexplain.setMaximumSize(QtCore.QSize(40, 40))
        self.instantexplain.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.instantexplain.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain{\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#instantexplain:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.instantexplain.setObjectName(_fromUtf8("instantexplain"))
        self.horizontalLayout_50.addWidget(self.instantexplain)
        self.verticalLayout_29.addLayout(self.horizontalLayout_50)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName(_fromUtf8("horizontalLayout_51"))
        self.InstantAmountLabel = QtWidgets.QLabel(self.MakeAnOffer)
        self.InstantAmountLabel.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.InstantAmountLabel.setFont(font)
        self.InstantAmountLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 16px "Arial";'))
        self.InstantAmountLabel.setObjectName(_fromUtf8("InstantAmountLabel"))
        self.horizontalLayout_51.addWidget(self.InstantAmountLabel)
        self.InstantAmount = QtWidgets.QLineEdit(self.MakeAnOffer)
        self.InstantAmount.setMinimumSize(QtCore.QSize(210, 40))
        self.InstantAmount.setMaximumSize(QtCore.QSize(16777215, 40))
        self.InstantAmount.setStyleSheet(
            _fromUtf8(
                'font: 19px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.InstantAmount.setObjectName(_fromUtf8("InstantAmount"))
        self.horizontalLayout_51.addWidget(self.InstantAmount)
        self.verticalLayout_29.addLayout(self.horizontalLayout_51)
        self.verticalLayout_28.addLayout(self.verticalLayout_29)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName(_fromUtf8("horizontalLayout_56"))
        spacerItem77 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem77)
        self.InstantWhoPays = QtWidgets.QComboBox(self.MakeAnOffer)
        self.InstantWhoPays.setMinimumSize(QtCore.QSize(0, 40))
        self.InstantWhoPays.setMaximumSize(QtCore.QSize(16777215, 40))
        self.InstantWhoPays.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.InstantWhoPays.setObjectName(_fromUtf8("InstantWhoPays"))
        self.InstantWhoPays.addItem(_fromUtf8(""))
        self.InstantWhoPays.addItem(_fromUtf8(""))
        self.horizontalLayout_56.addWidget(self.InstantWhoPays)
        self.verticalLayout_28.addLayout(self.horizontalLayout_56)
        spacerItem78 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_28.addItem(spacerItem78)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName(_fromUtf8("horizontalLayout_49"))
        spacerItem79 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem79)
        self.SendContract = QtWidgets.QPushButton(self.MakeAnOffer)
        self.SendContract.setMinimumSize(QtCore.QSize(281, 71))
        self.SendContract.setMaximumSize(QtCore.QSize(281, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SendContract.setFont(font)
        self.SendContract.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SendContract.setStyleSheet(
            _fromUtf8(
                "QPushButton#SendContract{\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#SendContract:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.SendContract.setIcon(icon7)
        self.SendContract.setIconSize(QtCore.QSize(20, 20))
        self.SendContract.setObjectName(_fromUtf8("SendContract"))
        self.horizontalLayout_49.addWidget(self.SendContract)
        spacerItem80 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem80)
        self.verticalLayout_28.addLayout(self.horizontalLayout_49)
        spacerItem81 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_28.addItem(spacerItem81)
        self.horizontalLayout_41.addLayout(self.verticalLayout_28)
        self.gridLayout_12.addLayout(self.horizontalLayout_41, 1, 0, 1, 1)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(5, icon23)

        self.Tabs.addTab(self.MakeAnOffer, icon23, _fromUtf8(""))
        self.PendingOffers = QtWidgets.QWidget()
        self.PendingOffers.setObjectName(_fromUtf8("PendingOffers"))
        self.gridLayout_9 = QtWidgets.QGridLayout(self.PendingOffers)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.frame_18 = QtWidgets.QFrame(self.PendingOffers)
        self.frame_18.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_18.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_18 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName(_fromUtf8("frame_18"))
        self.formLayout_16 = QtWidgets.QFormLayout(self.frame_18)
        self.formLayout_16.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_16.setObjectName(_fromUtf8("formLayout_16"))
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.frame_26 = QtWidgets.QFrame(self.frame_18)
        self.frame_26.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_26.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_26.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_26.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_26.setObjectName(_fromUtf8("frame_26"))
        self.horizontalLayout_36.addWidget(self.frame_26)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.label_22 = QtWidgets.QLabel(self.frame_18)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_21.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_18)
        self.label_23.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_21.addWidget(self.label_23)
        self.horizontalLayout_36.addLayout(self.verticalLayout_21)
        spacerItem82 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem82)
        self.commandLinkButton_9 = QtWidgets.QPushButton(self.frame_18)
        self.commandLinkButton_9.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_9.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_9.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_9 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_9:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_9.setIcon(icon1)
        self.commandLinkButton_9.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_9.setObjectName(_fromUtf8("commandLinkButton_9"))
        self.horizontalLayout_36.addWidget(self.commandLinkButton_9)
        self.formLayout_16.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_36)
        self.gridLayout_9.addWidget(self.frame_18, 0, 0, 1, 1)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.checkBox = QtWidgets.QCheckBox(self.PendingOffers)
        self.checkBox.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 15px "Arial";'))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_8.addWidget(self.checkBox)
        spacerItem83 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem83)
        self.FilterCustom = QtWidgets.QCheckBox(self.PendingOffers)
        self.FilterCustom.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 15px "Arial";'))
        self.FilterCustom.setObjectName(_fromUtf8("FilterCustom"))
        self.horizontalLayout_8.addWidget(self.FilterCustom)
        spacerItem84 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem84)
        self.DisableSpamFilter = QtWidgets.QCheckBox(self.PendingOffers)
        self.DisableSpamFilter.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 15px "Arial";'))
        self.DisableSpamFilter.setObjectName(_fromUtf8("DisableSpamFilter"))
        self.horizontalLayout_8.addWidget(self.DisableSpamFilter)
        spacerItem85 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem85)
        self.ExplainPending = QtWidgets.QPushButton(self.PendingOffers)
        self.ExplainPending.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainPending.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainPending.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainPending.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainPending {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainPending:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainPending.setObjectName(_fromUtf8("ExplainPending"))
        self.horizontalLayout_8.addWidget(self.ExplainPending)
        self.verticalLayout_22.addLayout(self.horizontalLayout_8)
        self.MyPendingOffers = QtWidgets.QListWidget(self.PendingOffers)
        self.MyPendingOffers.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.MyPendingOffers.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed
            | QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked
            | QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed
            | QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked
        )
        self.MyPendingOffers.setObjectName(_fromUtf8("MyPendingOffers"))
        self.verticalLayout_22.addWidget(self.MyPendingOffers)
        self.gridLayout_9.addLayout(self.verticalLayout_22, 1, 0, 1, 1)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(6, icon24)

        self.Tabs.addTab(self.PendingOffers, icon24, _fromUtf8(""))
        self.OpenContracts = QtWidgets.QWidget()
        self.OpenContracts.setObjectName(_fromUtf8("OpenContracts"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.OpenContracts)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame_17 = QtWidgets.QFrame(self.OpenContracts)
        self.frame_17.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_17.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_17 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName(_fromUtf8("frame_17"))
        self.formLayout_15 = QtWidgets.QFormLayout(self.frame_17)
        self.formLayout_15.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_15.setObjectName(_fromUtf8("formLayout_15"))
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.frame_25 = QtWidgets.QFrame(self.frame_17)
        self.frame_25.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_25.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_25.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_25.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_25.setObjectName(_fromUtf8("frame_25"))
        self.horizontalLayout_35.addWidget(self.frame_25)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.label_20 = QtWidgets.QLabel(self.frame_17)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_20.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.frame_17)
        self.label_21.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_20.addWidget(self.label_21)
        self.horizontalLayout_35.addLayout(self.verticalLayout_20)
        spacerItem86 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem86)
        self.commandLinkButton_8 = QtWidgets.QPushButton(self.frame_17)
        self.commandLinkButton_8.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_8.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_8.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_8 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_8:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_8.setIcon(icon1)
        self.commandLinkButton_8.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_8.setObjectName(_fromUtf8("commandLinkButton_8"))
        self.horizontalLayout_35.addWidget(self.commandLinkButton_8)
        self.formLayout_15.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_35)
        self.gridLayout_4.addWidget(self.frame_17, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setSpacing(20)
        self.horizontalLayout_61.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_61.setObjectName(_fromUtf8("horizontalLayout_61"))
        self.LineBalance_26 = QtWidgets.QFrame(self.OpenContracts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_26.sizePolicy().hasHeightForWidth())
        self.LineBalance_26.setSizePolicy(sizePolicy)
        self.LineBalance_26.setMinimumSize(QtCore.QSize(20, 0))
        self.LineBalance_26.setMaximumSize(QtCore.QSize(20, 16777215))
        self.LineBalance_26.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_26.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_26.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_26.setObjectName(_fromUtf8("LineBalance_26"))
        self.horizontalLayout_61.addWidget(self.LineBalance_26)
        self.SmartContractLabel_2 = QtWidgets.QLabel(self.OpenContracts)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SmartContractLabel_2.setFont(font)
        self.SmartContractLabel_2.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 21px "Arial";'))
        self.SmartContractLabel_2.setObjectName(_fromUtf8("SmartContractLabel_2"))
        self.horizontalLayout_61.addWidget(self.SmartContractLabel_2)
        self.LineBalance_27 = QtWidgets.QFrame(self.OpenContracts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_27.sizePolicy().hasHeightForWidth())
        self.LineBalance_27.setSizePolicy(sizePolicy)
        self.LineBalance_27.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_27.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_27.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_27.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_27.setObjectName(_fromUtf8("LineBalance_27"))
        self.horizontalLayout_61.addWidget(self.LineBalance_27)
        self.ExplainOpen = QtWidgets.QPushButton(self.OpenContracts)
        self.ExplainOpen.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainOpen.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainOpen.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainOpen.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainOpen {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainOpen:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainOpen.setObjectName(_fromUtf8("ExplainOpen"))
        self.horizontalLayout_61.addWidget(self.ExplainOpen)
        self.verticalLayout_6.addLayout(self.horizontalLayout_61)
        self.MyOpenContracts = QtWidgets.QListWidget(self.OpenContracts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MyOpenContracts.sizePolicy().hasHeightForWidth())
        self.MyOpenContracts.setSizePolicy(sizePolicy)
        self.MyOpenContracts.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.MyOpenContracts.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed
            | QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked
            | QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed
            | QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked
        )
        self.MyOpenContracts.setObjectName(_fromUtf8("MyOpenContracts"))
        self.verticalLayout_6.addWidget(self.MyOpenContracts)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(7, icon25)

        self.Tabs.addTab(self.OpenContracts, icon25, _fromUtf8(""))
        self.Market = QtWidgets.QWidget()
        self.Market.setStyleSheet(
            _fromUtf8(
                "QTableView#OfferTable QHeaderView\n"
                "{\n"
                "    /* draw the hole hor top & bottom line for the header */\n"
                "    height: 30px;\n"
                "border-top-color: #ffffff;\n"
                "}\n"
                "\n"
                "QTableView#OfferTable QHeaderView::section:horizontal:first\n"
                "{\n"
                "border-top-color: #ffffff;\n"
                "}\n"
                "\n"
                "QTableView#OfferTable QHeaderView::section:horizontal:last\n"
                "{\n"
                "    border-top-color: #ffffff;\n"
                "}\n"
                "\n"
                "\n"
                "\n"
                "QTableView#OfferTable QHeaderView::section:horizontal\n"
                "{\n"
                "    /* for each section draw ONLY left & right lines */\n"
                "    height: 24px;\n"
                "border-top-color: #ffffff;\n"
                "border-bottom-color: #9c9c9c;\n"
                "border-left-color:#ffffff;\n"
                "border-right-color:#9c9c9c;\n"
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "\n"
                "background-color: #fbfbfb;\n"
                "\n"
                " }\n"
                "QTableView {\n"
                "\n"
                "    background-color: rgba(251, 251, 251, 100%);\n"
                "color: #24282C;\n"
                "\n"
                "\n"
                "}\n"
                "\n"
                "QTableView::item:selected\n"
                "\n"
                "{\n"
                "\n"
                "    color: #24282C;\n"
                "\n"
                "    background-color:rgba(200, 200, 200, 25%);\n"
                "\n"
                "}\n"
                "\n"
                "QTableView::item:focus\n"
                "\n"
                "{\n"
                "\n"
                "color: #24282C;\n"
                "\n"
                "}"
            )
        )
        self.Market.setObjectName(_fromUtf8("Market"))
        self.gridLayout_13 = QtWidgets.QGridLayout(self.Market)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.frame_19 = QtWidgets.QFrame(self.Market)
        self.frame_19.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_19.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_19 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName(_fromUtf8("frame_19"))
        self.formLayout_17 = QtWidgets.QFormLayout(self.frame_19)
        self.formLayout_17.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_17.setObjectName(_fromUtf8("formLayout_17"))
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.frame_27 = QtWidgets.QFrame(self.frame_19)
        self.frame_27.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_27.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_27.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_27.setObjectName(_fromUtf8("frame_27"))
        self.horizontalLayout_37.addWidget(self.frame_27)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.label_24 = QtWidgets.QLabel(self.frame_19)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_23.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.frame_19)
        self.label_25.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_23.addWidget(self.label_25)
        self.horizontalLayout_37.addLayout(self.verticalLayout_23)
        spacerItem87 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem87)
        self.commandLinkButton_10 = QtWidgets.QPushButton(self.frame_19)
        self.commandLinkButton_10.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_10.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_10.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_10 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_10:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_10.setIcon(icon1)
        self.commandLinkButton_10.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_10.setObjectName(_fromUtf8("commandLinkButton_10"))
        self.horizontalLayout_37.addWidget(self.commandLinkButton_10)
        self.formLayout_17.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_37)
        self.gridLayout_13.addWidget(self.frame_19, 0, 0, 1, 1)
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_57.setObjectName(_fromUtf8("horizontalLayout_57"))
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName(_fromUtf8("verticalLayout_31"))
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.ShowWhat = QtWidgets.QComboBox(self.Market)
        self.ShowWhat.setMinimumSize(QtCore.QSize(200, 40))
        self.ShowWhat.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ShowWhat.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.ShowWhat.setObjectName(_fromUtf8("ShowWhat"))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.addItem(_fromUtf8(""))
        self.ShowWhat.setMaxVisibleItems(12)
        self.horizontalLayout_24.addWidget(self.ShowWhat)
        self.SearchEdit = QtWidgets.QLineEdit(self.Market)
        self.SearchEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.SearchEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SearchEdit.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                ""
            )
        )
        self.SearchEdit.setObjectName(_fromUtf8("SearchEdit"))
        self.horizontalLayout_24.addWidget(self.SearchEdit)
        self.Search = QtWidgets.QPushButton(self.Market)
        self.Search.setMinimumSize(QtCore.QSize(150, 40))
        self.Search.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Search.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Search.setStyleSheet(
            _fromUtf8(
                "QPushButton#Search {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#Search:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        icon26 = QtGui.QIcon()
        icon26.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_search_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.Search.setIcon(icon26)
        self.Search.setIconSize(QtCore.QSize(20, 20))
        self.Search.setObjectName(_fromUtf8("Search"))
        self.horizontalLayout_24.addWidget(self.Search)
        self.ExplainMarket = QtWidgets.QPushButton(self.Market)
        self.ExplainMarket.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainMarket.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainMarket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainMarket.setStyleSheet(
            _fromUtf8(
                "QPushButton#ExplainMarket {\n"
                '    font: bold 18px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#ExplainMarket:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainMarket.setIconSize(QtCore.QSize(20, 20))
        self.ExplainMarket.setObjectName(_fromUtf8("ExplainMarket"))
        self.horizontalLayout_24.addWidget(self.ExplainMarket)
        self.verticalLayout_31.addLayout(self.horizontalLayout_24)
        self.OfferTable = QtWidgets.QTableWidget(self.Market)
        self.OfferTable.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.OfferTable.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.OfferTable.setAutoFillBackground(False)
        self.OfferTable.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "\n"
                "border-radius: 8px;\n"
                "border-width: 1px;\n"
                " border-style: inset;\n"
                "border-color: lightgrey;\n"
                "background-color:rgba(251, 251, 251, 80%);"
            )
        )
        self.OfferTable.setObjectName(_fromUtf8("OfferTable"))
        self.OfferTable.setColumnCount(10)
        self.OfferTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.OfferTable.setHorizontalHeaderItem(9, item)
        self.OfferTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_31.addWidget(self.OfferTable)
        self.horizontalLayout_57.addLayout(self.verticalLayout_31)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setSpacing(15)
        self.verticalLayout_30.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_30.setObjectName(_fromUtf8("verticalLayout_30"))
        self.MarketBox = QtWidgets.QComboBox(self.Market)
        self.MarketBox.setMinimumSize(QtCore.QSize(200, 40))
        self.MarketBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MarketBox.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.MarketBox.setObjectName(_fromUtf8("MarketBox"))
        self.MarketBox.addItem(_fromUtf8(""))
        self.verticalLayout_30.addWidget(self.MarketBox)
        spacerItem88 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem88)
        self.OfferBox = QtWidgets.QComboBox(self.Market)
        self.OfferBox.setMinimumSize(QtCore.QSize(200, 40))
        self.OfferBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.OfferBox.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.OfferBox.setObjectName(_fromUtf8("OfferBox"))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.OfferBox.addItem(_fromUtf8(""))
        self.verticalLayout_30.addWidget(self.OfferBox)
        self.PostToMarket = QtWidgets.QPushButton(self.Market)
        self.PostToMarket.setMinimumSize(QtCore.QSize(0, 40))
        self.PostToMarket.setMaximumSize(QtCore.QSize(16777215, 40))
        self.PostToMarket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.PostToMarket.setStyleSheet(
            _fromUtf8(
                "QPushButton#PostToMarket {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#PostToMarket:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.PostToMarket.setIcon(icon15)
        self.PostToMarket.setIconSize(QtCore.QSize(20, 20))
        self.PostToMarket.setObjectName(_fromUtf8("PostToMarket"))
        self.verticalLayout_30.addWidget(self.PostToMarket)
        spacerItem89 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem89)
        self.SettingsMarket = QtWidgets.QPushButton(self.Market)
        self.SettingsMarket.setMinimumSize(QtCore.QSize(0, 40))
        self.SettingsMarket.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SettingsMarket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SettingsMarket.setStyleSheet(
            _fromUtf8(
                "QPushButton#SettingsMarket {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#SettingsMarket:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.SettingsMarket.setIcon(icon14)
        self.SettingsMarket.setIconSize(QtCore.QSize(20, 20))
        self.SettingsMarket.setObjectName(_fromUtf8("SettingsMarket"))
        self.verticalLayout_30.addWidget(self.SettingsMarket)
        spacerItem90 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem90)
        self.JoinChan = QtWidgets.QPushButton(self.Market)
        self.JoinChan.setMinimumSize(QtCore.QSize(0, 40))
        self.JoinChan.setMaximumSize(QtCore.QSize(16777215, 40))
        self.JoinChan.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.JoinChan.setStyleSheet(
            _fromUtf8(
                "QPushButton#JoinChan {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#JoinChan:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        icon27 = QtGui.QIcon()
        icon27.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_join_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.JoinChan.setIcon(icon27)
        self.JoinChan.setIconSize(QtCore.QSize(20, 20))
        self.JoinChan.setObjectName(_fromUtf8("JoinChan"))
        self.verticalLayout_30.addWidget(self.JoinChan)
        self.LeaveChan = QtWidgets.QPushButton(self.Market)
        self.LeaveChan.setMinimumSize(QtCore.QSize(0, 40))
        self.LeaveChan.setMaximumSize(QtCore.QSize(16777215, 40))
        self.LeaveChan.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LeaveChan.setStyleSheet(
            _fromUtf8(
                "QPushButton#LeaveChan {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 5px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#LeaveChan:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.LeaveChan.setIcon(icon19)
        self.LeaveChan.setIconSize(QtCore.QSize(20, 20))
        self.LeaveChan.setObjectName(_fromUtf8("LeaveChan"))
        self.verticalLayout_30.addWidget(self.LeaveChan)
        spacerItem91 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem91)
        self.horizontalLayout_57.addLayout(self.verticalLayout_30)
        self.gridLayout_13.addLayout(self.horizontalLayout_57, 1, 0, 1, 1)
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setContentsMargins(10, 0, 10, 10)
        self.horizontalLayout_58.setObjectName(_fromUtf8("horizontalLayout_58"))
        self.MarketRules = QtWidgets.QTextBrowser(self.Market)
        self.MarketRules.setMinimumSize(QtCore.QSize(0, 55))
        self.MarketRules.setMaximumSize(QtCore.QSize(300000, 55))
        self.MarketRules.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.MarketRules.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.MarketRules.setObjectName(_fromUtf8("MarketRules"))
        self.horizontalLayout_58.addWidget(self.MarketRules)
        self.gridLayout_13.addLayout(self.horizontalLayout_58, 2, 0, 1, 1)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(8, icon28)

        self.Tabs.addTab(self.Market, icon28, _fromUtf8(""))
        self.Contacts = QtWidgets.QWidget()
        self.Contacts.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Contacts.setObjectName(_fromUtf8("Contacts"))
        self.gridLayout_10 = QtWidgets.QGridLayout(self.Contacts)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.frame_20 = QtWidgets.QFrame(self.Contacts)
        self.frame_20.setMinimumSize(QtCore.QSize(600, 70))
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_20.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_20 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_20.setObjectName(_fromUtf8("frame_20"))
        self.formLayout_18 = QtWidgets.QFormLayout(self.frame_20)
        self.formLayout_18.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_18.setObjectName(_fromUtf8("formLayout_18"))
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setContentsMargins(-1, 0, 30, -1)
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.frame_28 = QtWidgets.QFrame(self.frame_20)
        self.frame_28.setMinimumSize(QtCore.QSize(37, 37))
        self.frame_28.setMaximumSize(QtCore.QSize(37, 37))
        self.frame_28.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_28.setObjectName(_fromUtf8("frame_28"))
        self.horizontalLayout_38.addWidget(self.frame_28)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.label_26 = QtWidgets.QLabel(self.frame_20)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout_24.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.frame_20)
        self.label_27.setStyleSheet(_fromUtf8('font: bold 15px "Arial";\n' "color: rgb(251, 251, 251);"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.verticalLayout_24.addWidget(self.label_27)
        self.horizontalLayout_38.addLayout(self.verticalLayout_24)
        spacerItem56B = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem56B)
        self.commandLinkButton_11 = QtWidgets.QPushButton(self.frame_20)
        self.commandLinkButton_11.setMinimumSize(QtCore.QSize(220, 40))
        self.commandLinkButton_11.setMaximumSize(QtCore.QSize(180, 40))
        self.commandLinkButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton_11.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_11 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_11:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.commandLinkButton_11.setIcon(icon1)
        self.commandLinkButton_11.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton_11.setObjectName(_fromUtf8("commandLinkButton_11"))
        self.horizontalLayout_38.addWidget(self.commandLinkButton_11)
        self.formLayout_18.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_38)
        self.gridLayout_10.addWidget(self.frame_20, 0, 0, 1, 1)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_34.setObjectName(_fromUtf8("verticalLayout_34"))
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.LineBalance_23 = QtWidgets.QFrame(self.Contacts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_23.sizePolicy().hasHeightForWidth())
        self.LineBalance_23.setSizePolicy(sizePolicy)
        self.LineBalance_23.setMinimumSize(QtCore.QSize(20, 0))
        self.LineBalance_23.setMaximumSize(QtCore.QSize(20, 16777215))
        self.LineBalance_23.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_23.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_23.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_23.setObjectName(_fromUtf8("LineBalance_23"))
        self.horizontalLayout_16.addWidget(self.LineBalance_23)
        self.ContactLabel = QtWidgets.QLabel(self.Contacts)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPixelSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ContactLabel.setFont(font)
        self.ContactLabel.setStyleSheet(_fromUtf8("color:#24282C;\n" 'font: bold 21px "Arial";'))
        self.ContactLabel.setObjectName(_fromUtf8("ContactLabel"))
        self.horizontalLayout_16.addWidget(self.ContactLabel)
        self.LineBalance_22 = QtWidgets.QFrame(self.Contacts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineBalance_22.sizePolicy().hasHeightForWidth())
        self.LineBalance_22.setSizePolicy(sizePolicy)
        self.LineBalance_22.setMinimumSize(QtCore.QSize(0, 0))
        self.LineBalance_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineBalance_22.setStyleSheet(_fromUtf8("border: 1px #b9b9b9;\n" "\n" "border-style: solid none none none;"))
        self.LineBalance_22.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.LineBalance_22.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.LineBalance_22.setObjectName(_fromUtf8("LineBalance_22"))
        self.horizontalLayout_16.addWidget(self.LineBalance_22)
        self.verticalLayout_25.addLayout(self.horizontalLayout_16)
        self.ContactTable = QtWidgets.QListWidget(self.Contacts)
        self.ContactTable.setMinimumSize(QtCore.QSize(700, 0))
        self.ContactTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ContactTable.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;"
            )
        )
        self.ContactTable.setObjectName(_fromUtf8("ContactTable"))
        self.verticalLayout_25.addWidget(self.ContactTable)
        self.horizontalLayout_39.addLayout(self.verticalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setSpacing(20)
        self.verticalLayout_26.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_32.setObjectName(_fromUtf8("verticalLayout_32"))
        self.verticalLayout_26.addLayout(self.verticalLayout_32)
        self.NewContact = QtWidgets.QPushButton(self.Contacts)
        self.NewContact.setMinimumSize(QtCore.QSize(0, 40))
        self.NewContact.setMaximumSize(QtCore.QSize(16777215, 40))
        self.NewContact.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.NewContact.setStyleSheet(
            _fromUtf8(
                "QPushButton#NewContact {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#NewContact:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon29 = QtGui.QIcon()
        icon29.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_addcontact_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.NewContact.setIcon(icon29)
        self.NewContact.setIconSize(QtCore.QSize(20, 20))
        self.NewContact.setObjectName(_fromUtf8("NewContact"))
        self.verticalLayout_26.addWidget(self.NewContact)
        self.BackupContacts = QtWidgets.QPushButton(self.Contacts)
        self.BackupContacts.setMinimumSize(QtCore.QSize(0, 40))
        self.BackupContacts.setMaximumSize(QtCore.QSize(16777215, 40))
        self.BackupContacts.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BackupContacts.setStyleSheet(
            _fromUtf8(
                "QPushButton#BackupContacts {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "     \n"
                "}\n"
                " QPushButton#BackupContacts:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        icon30 = QtGui.QIcon()
        icon30.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_backup_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.BackupContacts.setIcon(icon30)
        self.BackupContacts.setIconSize(QtCore.QSize(20, 20))
        self.BackupContacts.setObjectName(_fromUtf8("BackupContacts"))
        self.verticalLayout_26.addWidget(self.BackupContacts)
        spacerItem92 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_26.addItem(spacerItem92)
        self.HaloContactsIcon = QtWidgets.QPushButton(self.Contacts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HaloContactsIcon.sizePolicy().hasHeightForWidth())
        self.HaloContactsIcon.setSizePolicy(sizePolicy)
        self.HaloContactsIcon.setMinimumSize(QtCore.QSize(221, 211))
        self.HaloContactsIcon.setMaximumSize(QtCore.QSize(221, 211))
        self.HaloContactsIcon.setStyleSheet(
            _fromUtf8(
                "QPushButton#HaloContactsIcon {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "\n"
                "     \n"
                "}\n"
                " QPushButton#HaloContactsIcon:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                " }"
            )
        )
        self.HaloContactsIcon.setText(_fromUtf8(""))
        self.HaloContactsIcon.setIcon(icon)
        self.HaloContactsIcon.setIconSize(QtCore.QSize(211, 211))
        self.HaloContactsIcon.setFlat(True)
        self.HaloContactsIcon.setObjectName(_fromUtf8("HaloContactsIcon"))
        self.verticalLayout_26.addWidget(self.HaloContactsIcon)
        spacerItem93 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_26.addItem(spacerItem93)
        self.horizontalLayout_39.addLayout(self.verticalLayout_26)
        self.verticalLayout_34.addLayout(self.horizontalLayout_39)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_33.setObjectName(_fromUtf8("verticalLayout_33"))
        self.textBrowser = QtWidgets.QTextBrowser(self.Contacts)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 160))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 160))
        self.textBrowser.setStyleSheet(
            _fromUtf8(
                'font: 16px "Arial";\n'
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "     border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "background-image: url(" + self.ApplicationPath + "/images/Night_300px.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;"
            )
        )
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_33.addWidget(self.textBrowser)
        self.verticalLayout_34.addLayout(self.verticalLayout_33)
        self.gridLayout_10.addLayout(self.verticalLayout_34, 1, 0, 1, 1)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(9, icon31)

        self.Tabs.addTab(self.Contacts, icon31, _fromUtf8(""))
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuDonate = QtWidgets.QMenu(self.menubar)
        self.menuDonate.setObjectName(_fromUtf8("menuDonate"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Wallet = QtGui.QAction(MainWindow)
        self.actionNew_Wallet.setObjectName(_fromUtf8("actionNew_Wallet"))
        self.actionOpen_Wallet = QtGui.QAction(MainWindow)
        self.actionOpen_Wallet.setObjectName(_fromUtf8("actionOpen_Wallet"))
        self.actionSave_Copy = QtGui.QAction(MainWindow)
        self.actionSave_Copy.setObjectName(_fromUtf8("actionSave_Copy"))
        self.actionEncrypt_Keyfile = QtGui.QAction(MainWindow)
        self.actionEncrypt_Keyfile.setObjectName(_fromUtf8("actionEncrypt_Keyfile"))
        self.actionEncrypt_Decrypt = QtGui.QAction(MainWindow)
        self.actionEncrypt_Decrypt.setObjectName(_fromUtf8("actionEcrypt_Decrypt"))
        self.actionSign_Verify = QtGui.QAction(MainWindow)
        self.actionSign_Verify.setObjectName(_fromUtf8("actionSign_Verify"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionDocumentation_2 = QtGui.QAction(MainWindow)
        self.actionDocumentation_2.setObjectName(_fromUtf8("actionDocumentation_2"))
        self.actionOfficial_Website = QtGui.QAction(MainWindow)
        self.actionOfficial_Website.setObjectName(_fromUtf8("actionOfficial_Website"))
        self.actionBuy_me_a_beer = QtGui.QAction(MainWindow)
        self.actionBuy_me_a_beer.setObjectName(_fromUtf8("actionBuy_me_a_beer"))
        self.actionKey_To_Image = QtGui.QAction(MainWindow)
        self.actionKey_To_Image.setObjectName(_fromUtf8("actionKey_To_Image"))
        self.actionUnlock_Wallet = QtGui.QAction(MainWindow)
        self.actionUnlock_Wallet.setObjectName(_fromUtf8("Unlock_Wallet"))
        self.actionLanguage = QtGui.QAction(MainWindow)
        self.actionLanguage.setObjectName(_fromUtf8("Language"))
        self.actionGeneral_Settings = QtGui.QAction(MainWindow)
        self.actionGeneral_Settings.setObjectName(_fromUtf8("General_Settings"))
        self.actionAdvanced_Sending = QtGui.QAction(MainWindow)
        self.actionAdvanced_Sending.setObjectName(_fromUtf8("Advanced_Sending"))
        self.actionTranslation_Editor = QtGui.QAction(MainWindow)
        self.actionTranslation_Editor.setObjectName(_fromUtf8("Translation_Editor"))
        self.actionAPI = QtGui.QAction(MainWindow)
        self.actionAPI.setObjectName(_fromUtf8("Activate_API"))
        self.DConsole = QtGui.QAction(MainWindow)
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
        self.menuDonate.addAction(self.actionBuy_me_a_beer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuDonate.menuAction())
        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.retranslateUi2(MainWindow)
        res = self.GTranslate()  # Check to see if we have translations
        if res:
            self.retranslateUi2(MainWindow)
        # self.resize(self.Tabs.minimumSizeHint())
        self.adjustSize()

    def retranslateUi2(self, MainWindow):
        # m = self._translate("MainWindow", "Not connected to internet!", None)
        MainWindow.setWindowTitle(self._translate("MainWindow", "BitHalo", None))
        self.label_2.setText(self._translate("MainWindow", "Welcome to BitHalo", None))
        self.label_3.setText(self._translate("MainWindow", "Multi-Signature Wallet, Decentralized Smart Contracting & Exchange", None))
        self.commandLinkButton.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.MyAddress_7.setText(self._translate("MainWindow", "Your Bitcoin Address:", None))
        self.CopyAddressToClipboard_3.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.WelcomeActualBalance.setText(self._translate("MainWindow", "Actual Balance:", None))
        self.WelcomeAvailableBalance.setText(self._translate("MainWindow", "Available Balance:", None))
        compareFont(self.WelcomeAvailableBalance, self.WelcomeActualBalance)
        self.Symbol_1.setText(self._translate("MainWindow", "BTC", None))
        self.Symbol_2.setText(self._translate("MainWindow", "BTC", None))
        self.MyBalance_4.setText(self._translate("MainWindow", "", None))
        self.MyBalance_3.setText(self._translate("MainWindow", "4", None))
        self.OpenAccount.setText(self._translate("MainWindow", "Open Account", None))
        self.JointAccount.setToolTip(self._translate("MainWindow", "New Account", None))
        self.JointAccount.setText(self._translate("MainWindow", "New Account", None))
        self.MyBalance_5.setText(self._translate("MainWindow", "Smart Contracts", None))
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
        self.switchcoin.setToolTip(self._translate("MainWindow", "Switch to BlackHalo", None))
        self.MyBalance_6.setText(self._translate("MainWindow", "Learn more about Halo", None))
        self.VideoLibrary.setToolTip(self._translate("MainWindow", "Video Library", None))
        self.VideoLibrary.setText(self._translate("MainWindow", "Video Library", None))
        self.labelProgress.setText(self._translate("MainWindow", "Synchronizing...", None))
        self.Rescan.setToolTip(self._translate("MainWindow", "Rescan", None))
        self.Rescan.setText(self._translate("MainWindow", "Rescan", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), self._translate("MainWindow", "Home", None))
        self.label_7.setText(self._translate("MainWindow", "Send Bitcoins", None))
        self.label_8.setText(self._translate("MainWindow", 'Send Bitcoins using "Two Step" - multisignature security.', None))
        self.commandLinkButton_3.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_3.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.PayToLabel.setText(self._translate("MainWindow", "Pay To:", None))
        self.AmountLabel.setText(self._translate("MainWindow", "Amount:", None))
        # self.BitFee.setText(self._translate("MainWindow", "0.0002", None))
        self.FeeLabel.setText(self._translate("MainWindow", "Fee:", None))
        self.SendActualBalance.setText(self._translate("MainWindow", "Actual Balance:", None))
        self.SendAvailableBalance.setText(self._translate("MainWindow", "Available Balance:", None))
        self.Symbol_3.setText(self._translate("MainWindow", "BTC", None))
        self.Symbol_4.setText(self._translate("MainWindow", "BTC", None))
        self.MyBalance_8.setText(self._translate("MainWindow", "", None))
        self.MyBalance_7.setText(self._translate("MainWindow", "", None))
        self.AdvancedSend.setToolTip(self._translate("MainWindow", "Advanced Sending", None))
        self.AdvancedSend.setText(self._translate("MainWindow", "Advanced Sending", None))
        self.ExplainSpend.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainSpend.setText(self._translate("MainWindow", "?", None))
        self.SendMyBitcoins.setToolTip(self._translate("MainWindow", "Send", None))
        self.SendMyBitcoins.setText(self._translate("MainWindow", "Send", None))
        self.MyBalance_9.setText(self._translate("MainWindow", "Two Step Send", None))
        self.LabelStepOne.setHtml(
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
            '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Step 1:</span>'
            + self._translate(
                "MainWindow",
                " Fill out the payment form above. Then open your first private key file and email/send the signature it creates to your 2nd location/party.",
                None,
            )
            + "</p></body></html>"
        )
        self.LabelStepTwo.setHtml(
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
            '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Step 2:</span>'
            + self._translate(
                "MainWindow",
                " Open the other parties signature file, sign and review the payment details. If everything looks good, send it.",
                None,
            )
            + "</p></body></html>"
        )
        self.CreateSignatureOne.setToolTip(self._translate("MainWindow", "Create Signature File", None))
        self.CreateSignatureOne.setText(self._translate("MainWindow", "Create Signature File", None))
        self.OpenBitSignatureAndSend.setToolTip(self._translate("MainWindow", "Open Signature File, Sign and Send", None))
        self.OpenBitSignatureAndSend.setText(self._translate("MainWindow", "Open Signature File, Sign and Send", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.SendBitcoins), self._translate("MainWindow", "Send Bitcoins", None))
        self.label_9.setText(self._translate("MainWindow", "Receive Bitcoins", None))
        self.commandLinkButton_4.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_4.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.ContactLabel_2.setText(self._translate("MainWindow", "Your Accounts", None))
        self.ExplainReceive.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainReceive.setText(self._translate("MainWindow", "?", None))
        self.MyAddress.setText(self._translate("MainWindow", "Your Bitcoin Address:", None))
        self.CopyAddressToClipboard.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.MyAddress_3.setText(self._translate("MainWindow", "Your BitMessage Address: ", None))
        self.CopyAddressToClipboard_2.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.BitmessageStatus.setText(self._translate("MainWindow", "Status:", None))
        self.EnableBitmessage.setText(self._translate("MainWindow", "Enable Bitmessage", None))
        self.EnableIRC.setText(self._translate("MainWindow", "Enable IRC contracting", None))
        self.MyEmail.setText(self._translate("MainWindow", "Your Email Address: ", None))
        self.AddEmail_2.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.EmailStatus.setText(self._translate("MainWindow", "Status:", None))
        self.EmailBox.setPlaceholderText(self._translate("MainWindow", 'Enter your Email here and then click the"Add/Change" button...', None))
        self.AddEmail.setToolTip(self._translate("MainWindow", "Add / Change Email", None))
        self.AddEmail.setText(self._translate("MainWindow", "Add/Change", None))
        self.EnableEmail.setText(self._translate("MainWindow", "Enable Email (Encrypted)", None))
        self.OutboxButton.setToolTip(self._translate("MainWindow", "Outbox", None))
        self.OutboxButton.setText(self._translate("MainWindow", "Outbox", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.ReceiveBitcoins), self._translate("MainWindow", "Receive Bitcoins", None))
        self.label_14.setText(self._translate("MainWindow", "History", None))
        self.label_15.setText(self._translate("MainWindow", "Bitcoin Transfer History", None))
        self.commandLinkButton_5.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_5.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.MyAddress_2.setText(self._translate("MainWindow", "Your Bitcoin Address:  ", None))
        self.CopyAddressToClipboard_5.setToolTip(self._translate("MainWindow", "Copy Address to Clipboard", None))
        self.HistoryBalance.setText(self._translate("MainWindow", "Balance:", None))
        self.Symbol_5.setText(self._translate("MainWindow", "BTC", None))
        self.MyBalance.setText(self._translate("MainWindow", "", None))
        self.TitleRecent.setText(self._translate("MainWindow", "Account Details", None))
        self.KeysConnected.setText(self._translate("MainWindow", "You have 0 Private Keys connected", None))
        self.Refresh.setToolTip(self._translate("MainWindow", "Refresh", None))
        self.labelProgress2.setText(self._translate("MainWindow", "Synchronizing...", None))
        self.Rescan2.setToolTip(self._translate("MainWindow", "Rescan", None))
        self.Rescan2.setText(self._translate("MainWindow", "Rescan", None))
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
        self.Tabs.setTabText(self.Tabs.indexOf(self.History), self._translate("MainWindow", "History", None))
        self.label_16.setText(self._translate("MainWindow", "Chat", None))
        self.label_17.setText(self._translate("MainWindow", "Use IRC to find people to make smart contracts with", None))
        self.commandLinkButton_6.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_6.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Chat), self._translate("MainWindow", "Chat", None))
        self.label_18.setText(self._translate("MainWindow", "Make an Offer", None))
        self.label_19.setText(self._translate("MainWindow", "Create a Smart Contract", None))
        self.commandLinkButton_7.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_7.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.SmartContractLabel.setText(self._translate("MainWindow", "Create a Smart Contract", None))
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
        # self.ContractFee.setText(self._translate("MainWindow", "0.0002", None))
        self.DepositLabel.setText(self._translate("MainWindow", "You Deposit:", None))
        self.TheDepositLabel.setText(self._translate("MainWindow", "They Deposit:", None))
        self.TimeToCompleteLabel.setText(self._translate("MainWindow", "Time to Complete:", None))
        self.DaysMultiplier.setItemText(0, self._translate("MainWindow", "Days", None))
        self.DaysMultiplier.setItemText(1, self._translate("MainWindow", "Hours", None))
        self.AutoBackupLabel_2.setText(self._translate("MainWindow", "Auto Backup", None))
        self.ExplainAutoBackupOffer.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainAutoBackupOffer.setText(self._translate("MainWindow", "?", None))
        self.TxBackupPath.setPlaceholderText(self._translate("MainWindow", "Path to flash drive or backup folder..", None))
        self.BrowseTxBackup.setToolTip(self._translate("MainWindow", "Create path to Backup Folder", None))
        self.AutoBackupLabel.setText(self._translate("MainWindow", "This auto-backup is for contracts only!", None))
        self.InstantRefundLabel.setText(self._translate("MainWindow", "Instant Refund", None))
        self.instantexplain.setToolTip(self._translate("MainWindow", "Help", None))
        self.instantexplain.setText(self._translate("MainWindow", "?", None))
        self.InstantAmountLabel.setText(self._translate("MainWindow", "Amount:", None))
        self.InstantWhoPays.setItemText(0, self._translate("MainWindow", "I am depositing this/broadcasting", None))
        self.InstantWhoPays.setItemText(1, self._translate("MainWindow", "They are depositing this/broadcasting", None))
        self.SendContract.setToolTip(self._translate("MainWindow", "Create Contract", None))
        self.SendContract.setText(self._translate("MainWindow", "Create Contract", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.MakeAnOffer), self._translate("MainWindow", "Make an Offer", None))
        self.label_22.setText(self._translate("MainWindow", "Pending Offers", None))
        self.label_23.setText(self._translate("MainWindow", "List of offers you have sent and received", None))
        self.commandLinkButton_9.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_9.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.checkBox.setText(self._translate("MainWindow", "Disable Notifications", None))
        self.FilterCustom.setText(self._translate("MainWindow", "Filter Non-Market Offers", None))
        self.DisableSpamFilter.setText(self._translate("MainWindow", "Disable spam filter", None))
        self.ExplainPending.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainPending.setText(self._translate("MainWindow", "?", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.PendingOffers), self._translate("MainWindow", "Pending Offers", None))
        self.label_20.setText(self._translate("MainWindow", "Open Contracts", None))
        self.label_21.setText(self._translate("MainWindow", "Listed Smart Contract Negotiations", None))
        self.commandLinkButton_8.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_8.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.SmartContractLabel_2.setText(self._translate("MainWindow", "Open Contracts", None))
        self.ExplainOpen.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainOpen.setText(self._translate("MainWindow", "?", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.OpenContracts), self._translate("MainWindow", "Open Contracts", None))
        self.label_24.setText(self._translate("MainWindow", "Market", None))
        self.label_25.setText(self._translate("MainWindow", "Welcome to the Halo Marketplace", None))
        self.commandLinkButton_10.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_10.setText(self._translate("MainWindow", "New Pending Offer!", None))
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
        self.Search.setText(self._translate("MainWindow", "Search", None))
        self.ExplainMarket.setToolTip(self._translate("MainWindow", "Help", None))
        self.ExplainMarket.setText(self._translate("MainWindow", "?", None))
        # item = self.OfferTable.horizontalHeaderItem(0)
        # item.setText(self._translate("MainWindow", "Images", None))
        # item = self.OfferTable.horizontalHeaderItem(1)
        # item.setText(self._translate("MainWindow", "Type", None))
        # item = self.OfferTable.horizontalHeaderItem(2)
        # item.setText(self._translate("MainWindow", "Description", None))
        # item = self.OfferTable.horizontalHeaderItem(3)
        # item.setText(self._translate("MainWindow", "Price", None))
        # item = self.OfferTable.horizontalHeaderItem(4)
        # item.setText(self._translate("MainWindow", "Payment", None))
        # item = self.OfferTable.horizontalHeaderItem(5)
        # item.setText(self._translate("MainWindow", "Contact", None))
        # item = self.OfferTable.horizontalHeaderItem(6)
        # item.setText(self._translate("MainWindow", "Deposits", None))
        # item = self.OfferTable.horizontalHeaderItem(7)
        # item.setText(self._translate("MainWindow", "Duration", None))
        # item = self.OfferTable.horizontalHeaderItem(8)
        # item.setText(self._translate("MainWindow", "Escrow", None))
        # item = self.OfferTable.horizontalHeaderItem(9)
        # item.setText(self._translate("MainWindow", "Date", None))
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
        self.MarketRules.setHtml(
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
            '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
            + self._translate("MainWindow", "These markets are decentralized. However volunteers may moderate.", None)
            + '<span style=" font-weight:600;">'
            + self._translate("MainWindow", "Do not post illegal content to the markets or you may get blocked.", None)
            + "</span>"
            + self._translate("MainWindow", " These revolutionary markets are a way of connecting to people worldwide.", None)
            + "</p></body></html>"
        )
        self.Tabs.setTabText(self.Tabs.indexOf(self.Market), self._translate("MainWindow", "Market", None))
        self.label_26.setText(self._translate("MainWindow", "Contacts", None))
        self.label_27.setText(self._translate("MainWindow", "Add contacts to your Bitcoin Address Book", None))
        self.commandLinkButton_11.setToolTip(self._translate("MainWindow", "New Pending Offer", None))
        self.commandLinkButton_11.setText(self._translate("MainWindow", "New Pending Offer!", None))
        self.ContactLabel.setText(self._translate("MainWindow", "Contacts", None))
        self.NewContact.setToolTip(self._translate("MainWindow", "Add New Contact", None))
        self.NewContact.setText(self._translate("MainWindow", "Add New Contact", None))
        self.BackupContacts.setToolTip(self._translate("MainWindow", "Backup-up Contacts", None))
        self.BackupContacts.setText(self._translate("MainWindow", "Back-up Contacts", None))
        self.textBrowser.setHtml(
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
            '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            '<p style=" margin-top:0px; margin-bottom:0px; '
            'margin-left:0px; margin-right:0px; -qt-block-indent:0; '
            'text-indent:0px;"><span style=" font-size:15px; '
            'font-weight:600;">Links/Misc</span></p>\n'
            '<p style=" margin-top:0px; margin-bottom:0px; '
            'margin-left:0px; margin-right:0px; -qt-block-indent:0; '
            'text-indent:0px;"><a href="www.Blackhalo.info">'
            '<span style=" font-size:15px; text-decoration: underline; '
            'color:#0000ff;">www.Blackhalo.info</span></a>'
            '<span style=" font-size:15px;">  '
            + self._translate("MainWindow", "BlackHalo, the worlds first contracting software", None)
            + "</span></p>\n"
            '<p style=" margin-top:0px; margin-bottom:0px; '
            'margin-left:0px; margin-right:0px; -qt-block-indent:0; '
            'text-indent:0px;"><a href="www.BitHalo.org"><span style=" '
            'font-size:15px; text-decoration: underline; '
            'color:#0000ff;">www.BitHalo.org</span></a>'
            '<span style=" font-size:15px;">  '
            + self._translate("MainWindow", "The original BitHalo Website", None)
            + "</span></p>\n"
            '<p style=" margin-top:0px; margin-bottom:0px; '
            'margin-left:0px; margin-right:0px; -qt-block-indent:0; '
            'text-indent:0px;"><a href="www.NightTrader.org"><span style=" '
            'font-size:15px; text-decoration: underline; '
            'color:#0000ff;">www.NightTrader.org</span></a>'
            '<span style=" font-size:15px;">  '
            + self._translate("MainWindow", "NightTrader decentralized exchange", None)
            + "</span></p>\n"
            '<p style=" margin-top:0px; margin-bottom:0px; '
            'margin-left:0px; margin-right:0px; -qt-block-indent:0; '
            'text-indent:0px;"><a href="http://www.reddit.com/r/blackcoin/">'
            '<span style=" font-size:15px; text-decoration: underline; '
            'color:#0000ff;">http://www.reddit.com/r/blackcoin/</span></a>'
            '<span style=" font-size:15px;">  '
            + self._translate("MainWindow", "Blackcoin community subreddit", None)
            + "</span></p>\n"
            '<p style="-qt-paragraph-type:empty; margin-top:0px; '
            'margin-bottom:0px; margin-left:0px; margin-right:0px; '
            '-qt-block-indent:0; text-indent:0px; font-size:15px;"><br /></p>\n'
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:15px;"><br />'
            + self._translate(
                "MainWindow",
                "If you have any feedback or questions please contact us through the BitHalo/BlackHalo website. Thank you.",
                None,
            )
            + "</span></p></body></html>"
        )
        self.Tabs.setTabText(self.Tabs.indexOf(self.Contacts), self._translate("MainWindow", "Contacts", None))
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
        self.actionLanguage.setText(self._translate("MainWindow", "Language", None))
        self.actionGeneral_Settings.setText(self._translate("MainWindow", "General Settings", None))
        self.actionAdvanced_Sending.setText(self._translate("MainWindow", "Advanced Sending", None))
        self.actionTranslation_Editor.setText(self._translate("MainWindow", "Translation Editor", None))
        self.actionAPI.setText(self._translate("MainWindow", "Activate API", None))
        self.DConsole.setText(self._translate("MainWindow", "Debug Console", None))
        self.actionBuy_me_a_beer.setText(self._translate("MainWindow", "Buy us a beer", None))
        self.actionKey_To_Image.setText(self._translate("MainWindow", "Key To Image", None))
        self.actionUnlock_Wallet.setText(self._translate("MainWindow", "Unlock Wallet", None))

    def BitHalo(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(981, 724)
        # MainWindow.setMinimumSize(QtCore.QSize(981, 724))
        # self.ApplicationPath.replace("\\","/")
        # self.MarketBox.setItemText(0, self._translate("MainWindow", self.NewCoin['default market'], None))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/BitHalo.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        if self.NewCoin["Moderator"] == 1:
            self.label_25.setText(self._translate("MainWindow", "Welcome to the Halo Marketplace: Moderator version", None))
        MainWindow.setWindowIcon(icon)
        self.webView.setHtml(_fromUtf8("<iframe src=" + self.NewCoin["IRC"] + " width='100%' height='500'></iframe></div></div></div>"))
        self.label_7.setText(self._translate("MainWindow", "Send Bitcoins", None))
        self.label_9.setText(self._translate("MainWindow", "Receive Bitcoins", None))
        self.label_8.setText(self._translate("MainWindow", 'Send Bitcoins using "Two Step" - multisignature security.', None))
        self.label_10.setText(self._translate("MainWindow", "Receive contracts with your Bitcoin Address, BitMessage Address or Email", None))
        self.Tabs.setStyleSheet(
            _fromUtf8(
                "QTabWidget::pane { /* The tab widget frame */\n"
                "border-top: 6px solid #d27e16;\n"
                "border-right: 2px solid #d27e16;\n"
                "border-left: 2px solid #d27e16;\n"
                "border-bottom: 6px solid #d27e16;\n"
                "margin-top:0px;\n"
                "background-color:#ececec;\n"
                "background: qlineargradient(x1:0, y1:1, x2:1, y2:0, stop:0 #c0c0c0, stop: 0.4 rgba(236, 236, 236, 200), stop:1 rgba(236, 236, 236, 200));\n"
                "\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}\n"
                "QTabWidget::tab-bar {\n"
                "left: 0px; /* move to the right by 5px */\n"
                "\n"
                "}\n"
                "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
                "QTabBar::tab {\n"
                "color: #FFF;\n"
                "opacity: 0.6;\n"
                "text-align: center;\n"
                "background-color: #222222;\n"
                "\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #2b3034, stop: 0.4 rgba(34, 34, 34, 250), stop:1 rgba(34, 34, 34, 250));\n"
                "\n"
                "padding: 20px 5px 20px 5px;\n"
                "/*padding: 40px 10px 10px 10px; */\n"
                "border-right: 1px dotted #C2C7CB;\n"
                "}\n"
                "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                "color: #f7931a;\n"
                "}\n"
                "QTabBar::tab:selected {\n"
                "background: #d27e16;\n"
                "color: #000;\n"
                "opacity: 1;\n"
                "}\n"
                "QTabBar::tab:!selected {\n"
                "margin-top: 0px; /* make non-selected tabs look smaller */\n"
                "\n"
                "}\n"
                ""
            )
        )
        self.Tabs.setIconSize(QtCore.QSize(18, 18))

        self.frame_2.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_2 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}"
            )
        )

        self.frame_3.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_2.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.commandLinkButton.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
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
                " }"
            )
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_attention_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_4.setIcon(icon1)
        self.commandLinkButton_5.setIcon(icon1)
        self.commandLinkButton_6.setIcon(icon1)
        self.commandLinkButton_7.setIcon(icon1)
        self.commandLinkButton_8.setIcon(icon1)
        self.commandLinkButton_9.setIcon(icon1)
        self.commandLinkButton_10.setIcon(icon1)
        self.commandLinkButton_11.setIcon(icon1)

        self.frame_5.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_5 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )

        self.switchcoin.setStyleSheet(
            _fromUtf8(
                "QPushButton#switchcoin {\n"
                "    \n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "    \n"
                "    \n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_blackhalo_03.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                "     \n"
                "}\n"
                " QPushButton#switchcoin:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_blackhalo_04.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                " }"
            )
        )

        self.progressBar.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: #f7931a;\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(0, icon13)

        self.frame.setStyleSheet(
            _fromUtf8(
                "QFrame#frame {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_7.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.label_7.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.commandLinkButton_3.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_3 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_3:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(1, icon17)

        self.frame_8.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_8 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_21.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_9.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))

        self.commandLinkButton_4.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_4 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_4:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(2, icon18)

        self.frame_9.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_9 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_22.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))
        self.label_14.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.commandLinkButton_5.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_5 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_5:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.MyAddress_2.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))

        self.progressBar2.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: #f7931a;\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )

        icon21 = QtGui.QIcon()
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(3, icon21)

        self.frame_15.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_15 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_23.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_16.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.commandLinkButton_6.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_6 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_6:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon22 = QtGui.QIcon()
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(4, icon22)

        self.frame_16.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_16 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_24.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_18.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))

        self.commandLinkButton_7.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_7 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_7:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon23 = QtGui.QIcon()
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(5, icon23)

        self.frame_18.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_18 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_26.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_22.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))
        self.commandLinkButton_9.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_9 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_9:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon24 = QtGui.QIcon()
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(6, icon24)

        self.frame_17.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_17 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_25.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_20.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))

        self.commandLinkButton_8.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_8 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_8:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon25 = QtGui.QIcon()
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(7, icon25)

        self.frame_19.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_19 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_27.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_24.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))

        self.commandLinkButton_10.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_10 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_10:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(8, icon28)

        self.frame_20.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_20 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #f9a921, stop: 0.4 rgba(247, 147, 26, 250), stop:0 rgba(249, 169, 33, 250));\n"
                " background-image: url(" + self.ApplicationPath + "/images/bg_bithalo_2.png); \n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_28.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow.png);"))

        self.label_26.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #604004;\n" "\n" ""))

        self.commandLinkButton_11.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_11 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_11:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon31 = QtGui.QIcon()
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(9, icon31)

        ##################################################

        MainWindow.setWindowTitle(self._translate("MainWindow", "BitHalo", None))
        self.label_2.setText(self._translate("MainWindow", "Welcome to BitHalo", None))

        self.MyAddress_7.setText(self._translate("MainWindow", "Your Bitcoin Address:", None))

        self.Symbol_1.setText(self._translate("MainWindow", "BTC", None))
        self.Symbol_2.setText(self._translate("MainWindow", "", None))
        self.label_8.setText(self._translate("MainWindow", 'Send Bitcoins using "Two Step" - multisignature security.', None))

        self.Symbol_3.setText(self._translate("MainWindow", "BTC", None))
        self.Symbol_4.setText(self._translate("MainWindow", "BTC", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.SendBitcoins), self._translate("MainWindow", "Send Bitcoins", None))

        # self.label_10.setText(self._translate("MainWindow", "Receive payments with your Bitcoin Address, BitMessage Address or Email", None))

        self.MyAddress.setText(self._translate("MainWindow", "Your Bitcoin Address:", None))

        self.Tabs.setTabText(self.Tabs.indexOf(self.ReceiveBitcoins), self._translate("MainWindow", "Receive Bitcoins", None))

        self.label_15.setText(self._translate("MainWindow", "Bitcoin Transfer History", None))

        self.MyAddress_2.setText(self._translate("MainWindow", "Your Bitcoin Address:  ", None))

        self.Symbol_5.setText(self._translate("MainWindow", "BTC", None))

        self.label_27.setText(self._translate("MainWindow", "Add contacts to your Bitcoin Address Book", None))

    def BLKHalo(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(991, 724)
        # MainWindow.setMinimumSize(QtCore.QSize(991, 724))
        # self.ApplicationPath.replace("\\","/")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/BlackHalo.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        MainWindow.setWindowIcon(icon)
        if self.NewCoin["Moderator"] == 1:
            self.label_25.setText(self._translate("MainWindow", "Welcome to the Halo Marketplace: Moderator version", None))
        self.webView.setHtml(_fromUtf8("<iframe src=" + self.NewCoin["IRC"] + " width='100%' height='500'></iframe></div></div></div>"))
        # self.Tabs.setTabPosition(QtWidgets.QTabWidget.West)
        # self.MarketBox.setItemText(0, self._translate("MainWindow", self.NewCoin['default market'], None))
        self.ContactLabel_2.setText(self._translate("MainWindow", "Your Accounts", None))
        self.label_7.setText(self._translate("MainWindow", "Send Blackcoins", None))
        self.label_9.setText(self._translate("MainWindow", "Receive Blackcoins", None))
        self.label_8.setText(self._translate("MainWindow", 'Send Blackcoins using "Two Step" - multisignature security.', None))
        self.label_10.setText(self._translate("MainWindow", "Receive contracts with your Blackcoin Address, BitMessage Address or Email", None))
        self.Tabs.setStyleSheet(
            _fromUtf8(
                "QTabWidget::pane { /* The tab widget frame */\n"
                "border-top: 6px solid #000000;\n"
                "border-right: 2px solid #000000;\n"
                "border-left: 2px solid #000000;\n"
                "border-bottom: 6px solid #000000;\n"
                "margin-top:0px;\n"
                "background-color:#ececec;\n"
                "background: qlineargradient(x1:0, y1:1, x2:1, y2:0, stop:0 #c0c0c0, stop: 0.4 rgba(236, 236, 236, 200), stop:1 rgba(236, 236, 236, 200));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}\n"
                "QTabWidget::tab-bar {\n"
                "left: 0px; /* move to the right by 5px */\n"
                "\n"
                "}\n"
                "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
                "QTabBar::tab {\n"
                "color: #222222;\n"
                "opacity: 0.6;\n"
                "text-align: center;\n"
                "background-color: #e8b100;\n"
                "\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #ffc300, stop: 0.4 rgba(232, 177, 0, 250), stop:1 rgba(232, 177, 0, 250));\n"
                "\n"
                "padding: 20px 5px 20px 5px;\n"
                "/*padding: 40px 10px 10px 10px; */\n"
                "border-right: 1px dotted #222222;\n"
                "}\n"
                "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                "color: #fbfbfb;\n"
                "}\n"
                "QTabBar::tab:selected {\n"
                "background: #000000;\n"
                "color: #fbfbfb;\n"
                "opacity: 1;\n"
                "}\n"
                "QTabBar::tab:!selected {\n"
                "margin-top: 0px; /* make non-selected tabs look smaller */\n"
                "\n"
                "}"
            )
        )
        self.Tabs.setIconSize(QtCore.QSize(18, 18))

        self.frame_2.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_2 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}"
            )
        )

        self.frame_3.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_2.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))

        self.commandLinkButton.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
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
                " }"
            )
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_attention_inactive.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_4.setIcon(icon1)
        self.commandLinkButton_5.setIcon(icon1)
        self.commandLinkButton_6.setIcon(icon1)
        self.commandLinkButton_7.setIcon(icon1)
        self.commandLinkButton_8.setIcon(icon1)
        self.commandLinkButton_9.setIcon(icon1)
        self.commandLinkButton_10.setIcon(icon1)
        self.commandLinkButton_11.setIcon(icon1)
        self.frame_5.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_5 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )

        self.switchcoin.setStyleSheet(
            _fromUtf8(
                "QPushButton#switchcoin {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "    \n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_bithalo_01.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                "     \n"
                "}\n"
                " QPushButton#switchcoin:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                "    \n"
                "    \n"
                "    \n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_bithalo_02.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                " }"
            )
        )

        self.progressBar.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: #e8b100;\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(0, icon13)
        self.frame.setStyleSheet(
            _fromUtf8(
                "QFrame#frame {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_7.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))
        self.label_7.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))
        self.commandLinkButton_3.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_3 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_3:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(1, icon17)

        self.frame_8.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_8 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_21.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_9.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))

        self.commandLinkButton_4.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_4 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_4:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(2, icon18)

        self.frame_9.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_9 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_22.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))
        self.label_14.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))
        self.commandLinkButton_5.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_5 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_5:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.MyAddress_2.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))

        self.progressBar2.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: #e8b100;\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )

        icon21 = QtGui.QIcon()
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(3, icon21)

        self.frame_15.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_15 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_23.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_16.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))
        self.commandLinkButton_6.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_6 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_6:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon22 = QtGui.QIcon()
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(4, icon22)

        self.frame_16.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_16 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_24.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_18.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))

        self.commandLinkButton_7.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_7 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_7:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon23 = QtGui.QIcon()
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(5, icon23)

        self.frame_18.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_18 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_26.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_22.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))
        self.commandLinkButton_9.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_9 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_9:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon24 = QtGui.QIcon()
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(6, icon24)

        self.frame_17.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_17 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_25.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_20.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))

        self.commandLinkButton_8.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_8 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_8:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon25 = QtGui.QIcon()
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(7, icon25)

        self.frame_19.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_19 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_27.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_24.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))

        self.commandLinkButton_10.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_10 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_10:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(8, icon28)

        self.frame_20.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_20 {\n"
                "/*your qss properties here*/\n"
                "background: qlineargradient(x1:1, y1:1, x2:0, y2:1, stop:0 #202020, stop: 0.4 rgba(34, 34, 34, 250), stop:0 rgba(50, 50, 50, 250));\n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_blackhalo_2.png);\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_28.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + "/images/navbar_arrow_bc.png);"))

        self.label_26.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: #e8b100;\n" "\n" ""))

        self.commandLinkButton_11.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_11 {\n"
                '    font: bold 14px "Arial";\n'
                "color: #fbfbfb;\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_11:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon31 = QtGui.QIcon()
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(9, icon31)

        ##################################################

        MainWindow.setWindowTitle(self._translate("MainWindow", "BlackHalo", None))
        self.label_2.setText(self._translate("MainWindow", "Welcome to BlackHalo", None))

        self.MyAddress_7.setText(self._translate("MainWindow", "Your Blackcoin Address:", None))

        self.Symbol_1.setText(self._translate("MainWindow", "BC", None))
        self.Symbol_2.setText(self._translate("MainWindow", "BC", None))
        self.label_8.setText(self._translate("MainWindow", 'Send Blackcoins using "Two Step" - multisignature security.', None))

        self.Symbol_4.setText(self._translate("MainWindow", "BC", None))
        self.Symbol_3.setText(self._translate("MainWindow", "BC", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.SendBitcoins), self._translate("MainWindow", "Send Blackcoins", None))

        self.MyAddress.setText(self._translate("MainWindow", "Your Blackcoin Address:", None))

        self.Tabs.setTabText(self.Tabs.indexOf(self.ReceiveBitcoins), self._translate("MainWindow", "Receive Blackcoins", None))

        self.label_15.setText(self._translate("MainWindow", "Blackcoin Transfer History", None))

        self.MyAddress_2.setText(self._translate("MainWindow", "Your Blackcoin Address:", None))

        self.Symbol_5.setText(self._translate("MainWindow", "BC", None))

        self.label_27.setText(self._translate("MainWindow", "Add contacts to your Blackcoin Address Book", None))

    def OtherCoin(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(991, 724)
        # MainWindow.setMinimumSize(QtCore.QSize(991, 724))
        # self.ApplicationPath.replace("\\","/")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + self.NewCoin["logo"])),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        MainWindow.setWindowIcon(icon)
        # self.Tabs.setTabPosition(QtWidgets.QTabWidget.West)
        # self.MarketBox.setItemText(0, self._translate("MainWindow", self.NewCoin['default market'], None))
        self.webView.setHtml(_fromUtf8("<iframe src=" + self.NewCoin["IRC"] + " width='100%' height='500'></iframe></div></div></div>"))
        if self.NewCoin["name"] == "BitBay":
            if self.NewCoin["Moderator"] == 1:
                self.label_25.setText(self._translate("MainWindow", "Welcome to the BitBay Marketplace: Moderator version", None))
            self.textBrowser.setHtml(self.NewCoin["links"])
        self.ContactLabel_2.setText(self._translate("MainWindow", "Your Accounts", None))
        self.label_7.setText(self._translate("MainWindow", "Send " + self.NewCoin["name"], None))
        self.label_9.setText(self._translate("MainWindow", "Receive " + self.NewCoin["name"], None))
        self.label_8.setText(self._translate("MainWindow", "Send " + self.NewCoin["name"] + ' using "Two Step" - multisignature security.', None))
        self.label_10.setText(
            self._translate(
                "MainWindow",
                "Receive contracts with your " + self.NewCoin["name"] + " Address, BitMessage Address or Email",
                None,
            )
        )
        self.Tabs.setStyleSheet(
            _fromUtf8(
                "QTabWidget::pane { /* The tab widget frame */\n"
                "border-top: 6px solid #000000;\n"
                "border-right: 2px solid #000000;\n"
                "border-left: 2px solid #000000;\n"
                "border-bottom: 6px solid #000000;\n"
                "margin-top:0px;\n"
                "background-color:#ececec;\n"
                "background: qlineargradient(x1:0, y1:1, x2:1, y2:0, stop:0 #c0c0c0, stop: 0.4 rgba(236, 236, 236, 200), stop:1 rgba(236, 236, 236, 200));\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}\n"
                "QTabWidget::tab-bar {\n"
                "left: 0px; /* move to the right by 5px */\n"
                "\n"
                "}\n"
                "/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
                "QTabBar::tab {\n"
                "color: " + self.NewCoin["TabText"] + ";\n"
                "opacity: 0.6;\n"
                "text-align: center;\n"
                "background-color: " + self.NewCoin["Background"] + ";\n"
                "\n"
                "background: " + self.NewCoin["TabGradient"] + ";\n"
                "\n"
                "padding: 20px 5px 20px 5px;\n"
                "/*padding: 40px 10px 10px 10px; */\n"
                "border-right: 1px dotted #222222;\n"
                "}\n"
                "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                "color: " + self.NewCoin["TabSelected"] + ";\n"
                "}\n"
                "QTabBar::tab:selected {\n"
                "background: " + self.NewCoin["QTabBackground"] + ";\n"
                "color: " + self.NewCoin["TabSelected"] + ";\n"
                "opacity: 1;\n"
                "}\n"
                "QTabBar::tab:!selected {\n"
                "margin-top: 0px; /* make non-selected tabs look smaller */\n"
                "\n"
                "}"
            )
        )
        self.Tabs.setIconSize(QtCore.QSize(18, 18))

        self.frame_2.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_2 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "\n"
                "}"
            )
        )

        self.frame_3.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_2.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))

        self.commandLinkButton.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
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
                " }"
            )
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_attention_inactive.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_4.setIcon(icon1)
        self.commandLinkButton_5.setIcon(icon1)
        self.commandLinkButton_6.setIcon(icon1)
        self.commandLinkButton_7.setIcon(icon1)
        self.commandLinkButton_8.setIcon(icon1)
        self.commandLinkButton_9.setIcon(icon1)
        self.commandLinkButton_10.setIcon(icon1)
        self.commandLinkButton_11.setIcon(icon1)
        self.frame_5.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_5 {\n"
                "/*your qss properties here*/\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 8px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "}"
            )
        )

        self.switchcoin.setStyleSheet(
            _fromUtf8(
                "QPushButton#switchcoin {\n"
                '    font: bold 14px "Arial";\n'
                "color: #24282C;\n"
                "    border-style: outset;\n"
                "     border-width: 2px;\n"
                "     border-radius: 8px;\n"
                "     border-color: lightgrey;\n"
                "background-color: #fbfbfb;\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:0, stop:0 #f5f5f5, stop: 0.4 rgba(251, 251, 251, 250), stop:1 rgba(251, 251, 251, 250));\n"
                "    \n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_bithalo_01.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                "     \n"
                "}\n"
                " QPushButton#switchcoin:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                "    \n"
                "    \n"
                "    \n"
                "    \n"
                "    background-image: url(" + self.ApplicationPath + "/images/bg_switch_to_bithalo_02.png);\n"
                "  background-position: top middle;\n"
                "  background-repeat: no-repeat;\n"
                " }"
            )
        )

        self.progressBar.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: " + self.NewCoin["ProgressBarColor"] + ";\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon13.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_home_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(0, icon13)
        self.frame.setStyleSheet(
            _fromUtf8(
                "QFrame#frame {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_7.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))
        self.label_7.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))
        self.commandLinkButton_3.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_3 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_3:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon17.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_send_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(1, icon17)

        self.frame_8.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_8 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_21.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_9.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))

        self.commandLinkButton_4.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_4 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_4:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon18.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_recieve_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(2, icon18)

        self.frame_9.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_9 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_22.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))
        self.label_14.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))
        self.commandLinkButton_5.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_5 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_5:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        self.MyAddress_2.setStyleSheet(_fromUtf8("color: #24282C;\n" 'font: bold 15px "Arial";'))

        self.progressBar2.setStyleSheet(
            _fromUtf8(
                "QProgressBar {\n"
                "color: #24282C;\n"
                "background-color:rgba(251, 251, 251, 80%);\n"
                "border-radius: 5px;\n"
                "border-style: inset;\n"
                "border-width: 2px;\n"
                "border-color: lightgrey;\n"
                "     text-align: center;\n"
                " }\n"
                "QProgressBar::chunk {\n"
                "background-color: " + self.NewCoin["ProgressBarColor"] + ";\n"
                "     width: 10px;\n"
                "     margin: 0.5px;\n"
                "\n"
                " }"
            )
        )

        icon21 = QtGui.QIcon()
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon21.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_history_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(3, icon21)

        self.frame_15.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_15 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_23.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_16.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))
        self.commandLinkButton_6.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_6 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_6:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon22 = QtGui.QIcon()
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon22.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_chat_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(4, icon22)

        self.frame_16.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_16 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_24.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_18.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))

        self.commandLinkButton_7.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_7 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_7:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon23 = QtGui.QIcon()
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon23.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_makeoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(5, icon23)

        self.frame_18.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_18 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_26.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_22.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))
        self.commandLinkButton_9.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_9 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_9:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon24 = QtGui.QIcon()
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon24.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_pendingoffer_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(6, icon24)

        self.frame_17.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_17 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_25.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_20.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))

        self.commandLinkButton_8.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_8 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_8:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon25 = QtGui.QIcon()
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon25.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_orders_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(7, icon25)

        self.frame_19.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_19 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )
        self.frame_27.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_24.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))

        self.commandLinkButton_10.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_10 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_10:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon28.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_owl_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(8, icon28)

        self.frame_20.setStyleSheet(
            _fromUtf8(
                "QFrame#frame_20 {\n"
                "/*your qss properties here*/\n"
                "background: " + self.NewCoin["FrameGradient"] + ");\n"
                "    background-image: url(" + self.ApplicationPath + self.NewCoin["BackgroundImage2"] + ");\n"
                "  background-position: top right;\n"
                "  background-repeat: no-repeat;\n"
                "}"
            )
        )

        self.frame_28.setStyleSheet(_fromUtf8("background-image: url(" + self.ApplicationPath + self.NewCoin["NavBarIcon"] + ");"))

        self.label_26.setStyleSheet(_fromUtf8('font: bold 24px "Arial";\n' "color: " + self.NewCoin["LabelText"] + ";\n" "\n" ""))

        self.commandLinkButton_11.setStyleSheet(
            _fromUtf8(
                "QPushButton#commandLinkButton_11 {\n"
                '    font: bold 14px "Arial";\n'
                "color: " + self.NewCoin["CommandLinkColor"] + ";\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "     \n"
                "}\n"
                " QPushButton#commandLinkButton_11:pressed {\n"
                "    background-color: Transparent;\n"
                "    background-repeat:no-repeat;\n"
                "    border: none;\n"
                "    outline:none;\n"
                "\n"
                " }"
            )
        )

        icon31 = QtGui.QIcon()
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_inactive.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.On,
        )
        icon31.addPixmap(
            QtGui.QPixmap(_fromUtf8(self.ApplicationPath + "/images/icon_contacts_active.png")),
            QtGui.QIcon.Mode.Active,
            QtGui.QIcon.State.Off,
        )
        self.Tabs.setTabIcon(9, icon31)

        ##################################################

        MainWindow.setWindowTitle(self._translate("MainWindow", self.NewCoin["HaloName"], None))
        self.label_2.setText(self._translate("MainWindow", "Welcome to " + self.NewCoin["HaloName"], None))

        self.MyAddress_7.setText(self._translate("MainWindow", "Your " + self.NewCoin["name"] + " Address:", None))

        self.Symbol_1.setText(self._translate("MainWindow", self.NewCoin["Symbol"], None))
        self.Symbol_2.setText(self._translate("MainWindow", self.NewCoin["Symbol"], None))

        self.Symbol_4.setText(self._translate("MainWindow", self.NewCoin["Symbol"], None))
        self.Symbol_3.setText(self._translate("MainWindow", self.NewCoin["Symbol"], None))
        self.Tabs.setTabText(
            self.Tabs.indexOf(self.SendBitcoins),
            self._translate("MainWindow", "Send " + self.NewCoin["name"] + "", None),
        )  # There used to be an "s" at the end of it,

        self.MyAddress.setText(self._translate("MainWindow", "Your " + self.NewCoin["name"] + " Address:", None))

        self.Tabs.setTabText(
            self.Tabs.indexOf(self.ReceiveBitcoins),
            self._translate("MainWindow", "Receive " + self.NewCoin["name"], None),
        )

        self.label_15.setText(self._translate("MainWindow", "" + self.NewCoin["name"] + " Transfer History", None))

        self.MyAddress_2.setText(self._translate("MainWindow", "Your " + self.NewCoin["name"] + " Address:", None))

        self.Symbol_5.setText(self._translate("MainWindow", self.NewCoin["Symbol"], None))

        self.label_27.setText(self._translate("MainWindow", "Add contacts to your " + self.NewCoin["name"] + " Address Book", None))


if __name__ == "__main__":
    import sys

    import os
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle('cleanlooks')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.ApplicationPath = os.path.abspath(os.path.dirname(__file__))
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
