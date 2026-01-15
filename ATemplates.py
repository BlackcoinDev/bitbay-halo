# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATemplates.ui'
#
# Created: Tue Jun 16 23:20:35 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWebEngineCore, QtWebEngineWidgets, QtWidgets


def _fromUtf8(s):
    return s


def _translate(context, text, disambig):
    return QtCore.QCoreApplication.translate(context, text, disambig)


# All automatically generated Labels are now redefined so fonts are cross platform and fit the boxes
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

    def setText(self, text):
        QtWidgets.QLabel.setText(self, text)
        self.resizeText()

    def resizeEvent(self, event):
        super(myQLabel, self).resizeEvent(event)
        self.resizeText()

    def resizeText(self):
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


# All automatically generated check boxes are now redefined so fonts are cross platform and fit the boxes
class myQCheckBox(QtWidgets.QCheckBox):
    def __init__(self, *args, **kargs):
        super(QtWidgets.QCheckBox, self).__init__(*args, **kargs)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored))

        self.setMinSize(6)

    def setMinSize(self, minfs):

        f = self.font()
        f.setPixelSize(minfs)
        f.setFamily(_fromUtf8("Arial"))
        br = QtGui.QFontMetrics(f).boundingRect(self.text())

        self.setMinimumSize(br.width(), br.height())

    def resizeEvent(self, event):
        super(QtWidgets.QCheckBox, self).resizeEvent(event)

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
        if fs > 4:
            fs -= 3  # Accomodate for the check box itself
        f.setPixelSize(fs)
        self.setFont(f)


class MyForm(QtWidgets.QDialog):
    def setupUi(self, Form):
        appfont = QtGui.QFont()
        appfont.setPixelSize(11)
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(715, 705)
        Form.setFont(appfont)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Pages = QtWidgets.QStackedWidget(Form)
        self.Pages.setObjectName(_fromUtf8("Pages"))
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.RateBox = QtWidgets.QComboBox(self.page1)
        self.RateBox.setGeometry(QtCore.QRect(0, 50, 161, 31))
        self.RateBox.setStyleSheet(_fromUtf8("font: 16px"))
        self.RateBox.setObjectName(_fromUtf8("RateBox"))
        self.RateBox.addItem(_fromUtf8(""))
        self.RateBox.addItem(_fromUtf8(""))
        self.SellCoinsForCashTitle = myQLabel(self.page1)
        self.SellCoinsForCashTitle.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.SellCoinsForCashTitle.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.SellCoinsForCashTitle.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.SellCoinsForCashTitle.setObjectName(_fromUtf8("SellCoinsForCashTitle"))
        self.Price = myQLabel(self.page1)
        self.Price.setGeometry(QtCore.QRect(0, 100, 61, 31))
        # self.Price.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Price.setObjectName(_fromUtf8("Price"))
        self.PriceBox = QtWidgets.QLineEdit(self.page1)
        self.PriceBox.setGeometry(QtCore.QRect(90, 100, 211, 31))
        self.PriceBox.setStyleSheet(
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
        self.PriceBox.setText(_fromUtf8(""))
        self.PriceBox.setObjectName(_fromUtf8("PriceBox"))
        self.AmountBox = QtWidgets.QLineEdit(self.page1)
        self.AmountBox.setGeometry(QtCore.QRect(90, 140, 211, 31))
        self.AmountBox.setStyleSheet(
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
        self.AmountBox.setText(_fromUtf8(""))
        self.AmountBox.setObjectName(_fromUtf8("AmountBox"))
        self.Amount = myQLabel(self.page1)
        self.Amount.setGeometry(QtCore.QRect(0, 140, 71, 31))
        # self.Amount.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Amount.setObjectName(_fromUtf8("Amount"))
        self.AmountUSD = QtWidgets.QComboBox(self.page1)
        self.AmountUSD.setGeometry(QtCore.QRect(310, 140, 51, 31))
        self.AmountUSD.setObjectName(_fromUtf8("AmountUSD"))
        self.AmountUSD.addItem(_fromUtf8(""))
        self.AmountUSD.addItem(_fromUtf8(""))
        self.PriceTrackingTitle = myQLabel(self.page1)
        self.PriceTrackingTitle.setGeometry(QtCore.QRect(400, 50, 211, 31))
        # self.PriceTrackingTitle.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PriceTrackingTitle.setObjectName(_fromUtf8("PriceTrackingTitle"))
        self.ServiceChargeText = myQLabel(self.page1)
        self.ServiceChargeText.setGeometry(QtCore.QRect(0, 190, 141, 31))
        # self.ServiceChargeText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.ServiceChargeText.setObjectName(_fromUtf8("ServiceChargeText"))
        self.ServiceCharge = QtWidgets.QComboBox(self.page1)
        self.ServiceCharge.setGeometry(QtCore.QRect(140, 190, 81, 31))
        self.ServiceCharge.setObjectName(_fromUtf8("ServiceCharge"))
        self.ServiceCharge.addItem(_fromUtf8(""))
        self.ServiceCharge.addItem(_fromUtf8(""))
        self.ServiceCharge.addItem(_fromUtf8(""))
        self.ServiceCharge.addItem(_fromUtf8(""))
        self.ServiceCharge.addItem(_fromUtf8(""))
        self.ServiceCharge.addItem(_fromUtf8(""))
        self.MaxIncreaseSell = QtWidgets.QComboBox(self.page1)
        self.MaxIncreaseSell.setGeometry(QtCore.QRect(400, 90, 161, 31))
        self.MaxIncreaseSell.setObjectName(_fromUtf8("MaxIncreaseSell"))
        self.MaxIncreaseSell.addItem(_fromUtf8(""))
        self.MaxIncreaseSell.addItem(_fromUtf8(""))
        self.MaxIncreaseSell.addItem(_fromUtf8(""))
        self.MaxDecreaseSell = QtWidgets.QComboBox(self.page1)
        self.MaxDecreaseSell.setGeometry(QtCore.QRect(400, 130, 161, 31))
        self.MaxDecreaseSell.setObjectName(_fromUtf8("MaxDecreaseSell"))
        self.MaxDecreaseSell.addItem(_fromUtf8(""))
        self.MaxDecreaseSell.addItem(_fromUtf8(""))
        self.MaxDecreaseSell.addItem(_fromUtf8(""))
        self.MaxDecreaseSell.addItem(_fromUtf8(""))
        self.ServiceChargeBox = QtWidgets.QLineEdit(self.page1)
        self.ServiceChargeBox.setGeometry(QtCore.QRect(230, 190, 71, 31))
        self.ServiceChargeBox.setStyleSheet(
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
        self.ServiceChargeBox.setObjectName(_fromUtf8("ServiceChargeBox"))
        self.MaxIncreaseSellBox = QtWidgets.QLineEdit(self.page1)
        self.MaxIncreaseSellBox.setGeometry(QtCore.QRect(570, 90, 71, 31))
        self.MaxIncreaseSellBox.setStyleSheet(
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
        self.MaxIncreaseSellBox.setObjectName(_fromUtf8("MaxIncreaseSellBox"))
        self.MaxDecreaseSellBox = QtWidgets.QLineEdit(self.page1)
        self.MaxDecreaseSellBox.setGeometry(QtCore.QRect(570, 130, 71, 31))
        self.MaxDecreaseSellBox.setStyleSheet(
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
        self.MaxDecreaseSellBox.setObjectName(_fromUtf8("MaxDecreaseSellBox"))
        self.perc1 = myQLabel(self.page1)
        self.perc1.setGeometry(QtCore.QRect(650, 90, 21, 31))
        # self.perc1.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc1.setObjectName(_fromUtf8("perc1"))
        self.perc5 = myQLabel(self.page1)
        self.perc5.setGeometry(QtCore.QRect(310, 190, 21, 31))
        # self.perc5.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc5.setObjectName(_fromUtf8("perc5"))
        self.perc2 = myQLabel(self.page1)
        self.perc2.setGeometry(QtCore.QRect(650, 130, 21, 31))
        # self.perc2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc2.setObjectName(_fromUtf8("perc2"))
        self.DepositSettings = QtWidgets.QComboBox(self.page1)
        self.DepositSettings.setGeometry(QtCore.QRect(0, 290, 211, 31))
        self.DepositSettings.setObjectName(_fromUtf8("DepositSettings"))
        self.DepositSettings.addItem(_fromUtf8(""))
        self.DepositSettings.addItem(_fromUtf8(""))
        self.DepositSettings.addItem(_fromUtf8(""))
        self.TimeLimitBox = QtWidgets.QLineEdit(self.page1)
        self.TimeLimitBox.setGeometry(QtCore.QRect(510, 340, 101, 31))
        self.TimeLimitBox.setStyleSheet(
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
        self.TimeLimitBox.setObjectName(_fromUtf8("TimeLimitBox"))
        self.TimeLimitText = myQLabel(self.page1)
        self.TimeLimitText.setGeometry(QtCore.QRect(400, 340, 101, 31))
        # self.TimeLimitText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText.setObjectName(_fromUtf8("TimeLimitText"))
        self.TimeLimitDays = QtWidgets.QComboBox(self.page1)
        self.TimeLimitDays.setGeometry(QtCore.QRect(620, 340, 51, 31))
        self.TimeLimitDays.setObjectName(_fromUtf8("TimeLimitDays"))
        self.TimeLimitDays.addItem(_fromUtf8(""))
        self.TimeLimitDays.addItem(_fromUtf8(""))
        self.TheirDepositText = myQLabel(self.page1)
        self.TheirDepositText.setGeometry(QtCore.QRect(0, 380, 131, 31))
        # self.TheirDepositText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText.setObjectName(_fromUtf8("TheirDepositText"))
        self.MyDepositBox = QtWidgets.QLineEdit(self.page1)
        self.MyDepositBox.setGeometry(QtCore.QRect(140, 340, 161, 31))
        self.MyDepositBox.setStyleSheet(
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
        self.MyDepositBox.setText(_fromUtf8(""))
        self.MyDepositBox.setObjectName(_fromUtf8("MyDepositBox"))
        self.MyDepositText = myQLabel(self.page1)
        self.MyDepositText.setGeometry(QtCore.QRect(0, 340, 101, 31))
        # self.MyDepositText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText.setObjectName(_fromUtf8("MyDepositText"))
        self.TheirDepositBox = QtWidgets.QLineEdit(self.page1)
        self.TheirDepositBox.setGeometry(QtCore.QRect(140, 380, 161, 31))
        self.TheirDepositBox.setStyleSheet(
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
        self.TheirDepositBox.setText(_fromUtf8(""))
        self.TheirDepositBox.setObjectName(_fromUtf8("TheirDepositBox"))
        self.line = QtWidgets.QFrame(self.page1)
        self.line.setGeometry(QtCore.QRect(10, 420, 671, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.PaymentOptions = myQLabel(self.page1)
        self.PaymentOptions.setGeometry(QtCore.QRect(0, 440, 151, 31))
        # self.PaymentOptions.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PaymentOptions.setObjectName(_fromUtf8("PaymentOptions"))
        self.agreelabel = myQLabel(self.page1)
        self.agreelabel.setGeometry(QtCore.QRect(0, 470, 331, 16))
        self.agreelabel.setObjectName(_fromUtf8("agreelabel"))
        self.NotesText1 = myQLabel(self.page1)
        self.NotesText1.setGeometry(QtCore.QRect(400, 440, 281, 31))
        # self.NotesText1.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.NotesText1.setObjectName(_fromUtf8("NotesText1"))
        self.NotesBox1 = QtWidgets.QTextEdit(self.page1)
        self.NotesBox1.setGeometry(QtCore.QRect(400, 470, 271, 125))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox1.sizePolicy().hasHeightForWidth())
        self.NotesBox1.setSizePolicy(sizePolicy)
        self.NotesBox1.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox1.setMaximumSize(QtCore.QSize(16777215, 125))
        self.NotesBox1.setStyleSheet(
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
        self.NotesBox1.setObjectName(_fromUtf8("NotesBox1"))
        self.BankWireCheck = myQCheckBox(self.page1)
        self.BankWireCheck.setGeometry(QtCore.QRect(0, 500, 141, 17))
        self.BankWireCheck.setObjectName(_fromUtf8("BankWireCheck"))
        self.WUCheck = myQCheckBox(self.page1)
        self.WUCheck.setGeometry(QtCore.QRect(160, 500, 141, 17))
        self.WUCheck.setObjectName(_fromUtf8("WUCheck"))
        self.MoneyGramCheck = myQCheckBox(self.page1)
        self.MoneyGramCheck.setGeometry(QtCore.QRect(0, 530, 131, 17))
        self.MoneyGramCheck.setObjectName(_fromUtf8("MoneyGramCheck"))
        self.DebitCheck = myQCheckBox(self.page1)
        self.DebitCheck.setGeometry(QtCore.QRect(160, 530, 131, 17))
        self.DebitCheck.setObjectName(_fromUtf8("DebitCheck"))
        self.CashMailCheck = myQCheckBox(self.page1)
        self.CashMailCheck.setGeometry(QtCore.QRect(0, 560, 131, 17))
        self.CashMailCheck.setObjectName(_fromUtf8("CashMailCheck"))
        self.OtherCheck = myQCheckBox(self.page1)
        self.OtherCheck.setGeometry(QtCore.QRect(160, 560, 131, 17))
        self.OtherCheck.setObjectName(_fromUtf8("OtherCheck"))
        self.MinOrderSellBox = QtWidgets.QLineEdit(self.page1)
        self.MinOrderSellBox.setGeometry(QtCore.QRect(570, 240, 71, 31))
        self.MinOrderSellBox.setStyleSheet(
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
        self.MinOrderSellBox.setObjectName(_fromUtf8("MinOrderSellBox"))
        self.perc3 = myQLabel(self.page1)
        self.perc3.setGeometry(QtCore.QRect(650, 240, 21, 31))
        # self.perc3.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc3.setObjectName(_fromUtf8("perc3"))
        self.MinOrderSell = QtWidgets.QComboBox(self.page1)
        self.MinOrderSell.setGeometry(QtCore.QRect(400, 240, 161, 31))
        self.MinOrderSell.setObjectName(_fromUtf8("MinOrderSell"))
        self.MinOrderSell.addItem(_fromUtf8(""))
        self.MinOrderSell.addItem(_fromUtf8(""))
        self.MinOrderSell.addItem(_fromUtf8(""))
        self.MinOrderSell.addItem(_fromUtf8(""))
        self.MaxOrderSellBox = QtWidgets.QLineEdit(self.page1)
        self.MaxOrderSellBox.setGeometry(QtCore.QRect(570, 280, 71, 31))
        self.MaxOrderSellBox.setStyleSheet(
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
        self.MaxOrderSellBox.setObjectName(_fromUtf8("MaxOrderSellBox"))
        self.MaxOrderSell = QtWidgets.QComboBox(self.page1)
        self.MaxOrderSell.setGeometry(QtCore.QRect(400, 280, 161, 31))
        self.MaxOrderSell.setObjectName(_fromUtf8("MaxOrderSell"))
        self.MaxOrderSell.addItem(_fromUtf8(""))
        self.MaxOrderSell.addItem(_fromUtf8(""))
        self.MaxOrderSell.addItem(_fromUtf8(""))
        self.MaxOrderSell.addItem(_fromUtf8(""))
        self.perc4 = myQLabel(self.page1)
        self.perc4.setGeometry(QtCore.QRect(650, 280, 21, 31))
        # self.perc4.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc4.setObjectName(_fromUtf8("perc4"))
        self.line_2 = QtWidgets.QFrame(self.page1)
        self.line_2.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.SaveContinue1 = QtWidgets.QPushButton(self.page1)
        self.SaveContinue1.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue1.setObjectName(_fromUtf8("SaveContinue1"))
        self.ShowAdvancedCash = myQCheckBox(self.page1)
        self.ShowAdvancedCash.setGeometry(QtCore.QRect(400, 10, 271, 31))
        self.ShowAdvancedCash.setStyleSheet(_fromUtf8('font: 22px "Arial";'))
        self.ShowAdvancedCash.setObjectName(_fromUtf8("ShowAdvancedCash"))
        self.LimitOrderText1 = myQLabel(self.page1)
        self.LimitOrderText1.setGeometry(QtCore.QRect(400, 190, 211, 31))
        # self.LimitOrderText1.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.LimitOrderText1.setObjectName(_fromUtf8("LimitOrderText1"))
        self.ExchangeRate = myQLabel(self.page1)
        self.ExchangeRate.setGeometry(QtCore.QRect(180, 50, 201, 31))
        # self.ExchangeRate.setStyleSheet(_fromUtf8("font: 15px \"Arial\";"))
        self.ExchangeRate.setObjectName(_fromUtf8("ExchangeRate"))
        self.ExplainSellCash = QtWidgets.QPushButton(self.page1)
        self.ExplainSellCash.setGeometry(QtCore.QRect(330, 10, 40, 40))
        self.ExplainSellCash.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainSellCash.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainSellCash.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainSellCash.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainSellCash.setIconSize(QtCore.QSize(20, 20))
        self.ExplainSellCash.setObjectName(_fromUtf8("ExplainSellCash"))
        self.SupplyAdditional1 = myQCheckBox(self.page1)
        self.SupplyAdditional1.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional1.setObjectName(_fromUtf8("SupplyAdditional1"))
        self.SaveFuture1 = myQCheckBox(self.page1)
        self.SaveFuture1.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture1.setObjectName(_fromUtf8("SaveFuture1"))
        self.ClearForm1 = QtWidgets.QPushButton(self.page1)
        self.ClearForm1.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm1.setObjectName(_fromUtf8("ClearForm1"))
        self.PriceUSD = QtWidgets.QComboBox(self.page1)
        self.PriceUSD.setGeometry(QtCore.QRect(310, 100, 51, 31))
        self.PriceUSD.setObjectName(_fromUtf8("PriceUSD"))
        self.PriceUSD.addItem(_fromUtf8(""))
        self.MyDepositUSD = QtWidgets.QComboBox(self.page1)
        self.MyDepositUSD.setGeometry(QtCore.QRect(310, 340, 51, 31))
        self.MyDepositUSD.setObjectName(_fromUtf8("MyDepositUSD"))
        self.MyDepositUSD.addItem(_fromUtf8(""))
        self.MyDepositUSD.addItem(_fromUtf8(""))
        self.TheirDepositUSD = QtWidgets.QComboBox(self.page1)
        self.TheirDepositUSD.setGeometry(QtCore.QRect(310, 380, 51, 31))
        self.TheirDepositUSD.setObjectName(_fromUtf8("TheirDepositUSD"))
        self.TheirDepositUSD.addItem(_fromUtf8(""))
        self.TheirDepositUSD.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName(_fromUtf8("page2"))
        self.WireText = myQLabel(self.page2)
        self.WireText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.WireText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.WireText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.WireText.setObjectName(_fromUtf8("WireText"))
        self.WireBrowser = QtWidgets.QTextBrowser(self.page2)
        self.WireBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.WireBrowser.setObjectName(_fromUtf8("WireBrowser"))
        self.WireSelect = QtWidgets.QComboBox(self.page2)
        self.WireSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.WireSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.WireSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WireSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.WireSelect.setStyleSheet(
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
        self.WireSelect.setObjectName(_fromUtf8("WireSelect"))
        self.AccountName = myQLabel(self.page2)
        self.AccountName.setGeometry(QtCore.QRect(0, 230, 501, 31))
        # self.AccountName.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AccountName.setObjectName(_fromUtf8("AccountName"))
        self.BankBox = QtWidgets.QLineEdit(self.page2)
        self.BankBox.setGeometry(QtCore.QRect(0, 190, 501, 31))
        self.BankBox.setStyleSheet(
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
        self.BankBox.setText(_fromUtf8(""))
        self.BankBox.setObjectName(_fromUtf8("BankBox"))
        self.BankName = myQLabel(self.page2)
        self.BankName.setGeometry(QtCore.QRect(0, 160, 501, 31))
        # self.BankName.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.BankName.setObjectName(_fromUtf8("BankName"))
        self.NameBox = QtWidgets.QLineEdit(self.page2)
        self.NameBox.setGeometry(QtCore.QRect(0, 400, 501, 31))
        self.NameBox.setStyleSheet(
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
        self.NameBox.setText(_fromUtf8(""))
        self.NameBox.setObjectName(_fromUtf8("NameBox"))
        self.NameAct = myQLabel(self.page2)
        self.NameAct.setGeometry(QtCore.QRect(0, 370, 501, 31))
        # self.NameAct.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.NameAct.setObjectName(_fromUtf8("NameAct"))
        self.AccountBox = QtWidgets.QLineEdit(self.page2)
        self.AccountBox.setGeometry(QtCore.QRect(0, 260, 501, 31))
        self.AccountBox.setStyleSheet(
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
        self.AccountBox.setText(_fromUtf8(""))
        self.AccountBox.setObjectName(_fromUtf8("AccountBox"))
        self.Routing = myQLabel(self.page2)
        self.Routing.setGeometry(QtCore.QRect(0, 300, 501, 31))
        # self.Routing.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.Routing.setObjectName(_fromUtf8("Routing"))
        self.RoutingBox = QtWidgets.QLineEdit(self.page2)
        self.RoutingBox.setGeometry(QtCore.QRect(0, 330, 501, 31))
        self.RoutingBox.setStyleSheet(
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
        self.RoutingBox.setText(_fromUtf8(""))
        self.RoutingBox.setObjectName(_fromUtf8("RoutingBox"))
        self.OtherInfo = myQLabel(self.page2)
        self.OtherInfo.setGeometry(QtCore.QRect(0, 440, 501, 31))
        # self.OtherInfo.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherInfo.setObjectName(_fromUtf8("OtherInfo"))
        self.OtherBox = QtWidgets.QTextEdit(self.page2)
        self.OtherBox.setGeometry(QtCore.QRect(0, 470, 501, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherBox.sizePolicy().hasHeightForWidth())
        self.OtherBox.setSizePolicy(sizePolicy)
        self.OtherBox.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.OtherBox.setStyleSheet(
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
        self.OtherBox.setObjectName(_fromUtf8("OtherBox"))
        self.line_5 = QtWidgets.QFrame(self.page2)
        self.line_5.setGeometry(QtCore.QRect(0, 580, 501, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.Save1 = QtWidgets.QPushButton(self.page2)
        self.Save1.setGeometry(QtCore.QRect(0, 620, 151, 41))
        self.Save1.setObjectName(_fromUtf8("Save1"))
        self.Remove1 = QtWidgets.QPushButton(self.page2)
        self.Remove1.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove1.setObjectName(_fromUtf8("Remove1"))
        self.Create1 = QtWidgets.QPushButton(self.page2)
        self.Create1.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create1.setObjectName(_fromUtf8("Create1"))
        self.Update1 = QtWidgets.QPushButton(self.page2)
        self.Update1.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update1.setObjectName(_fromUtf8("Update1"))
        self.Pages.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName(_fromUtf8("page3"))
        self.line_9 = QtWidgets.QFrame(self.page3)
        self.line_9.setGeometry(QtCore.QRect(0, 600, 501, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.WUText = myQLabel(self.page3)
        self.WUText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.WUText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.WUText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.WUText.setObjectName(_fromUtf8("WUText"))
        self.OtherInfo2 = myQLabel(self.page3)
        self.OtherInfo2.setGeometry(QtCore.QRect(0, 480, 501, 31))
        # self.OtherInfo2.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherInfo2.setObjectName(_fromUtf8("OtherInfo2"))
        self.PhoneBox1 = QtWidgets.QLineEdit(self.page3)
        self.PhoneBox1.setGeometry(QtCore.QRect(0, 260, 501, 31))
        self.PhoneBox1.setStyleSheet(
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
        self.PhoneBox1.setText(_fromUtf8(""))
        self.PhoneBox1.setObjectName(_fromUtf8("PhoneBox1"))
        self.Save2 = QtWidgets.QPushButton(self.page3)
        self.Save2.setGeometry(QtCore.QRect(0, 620, 151, 41))
        self.Save2.setObjectName(_fromUtf8("Save2"))
        self.Remove2 = QtWidgets.QPushButton(self.page3)
        self.Remove2.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove2.setObjectName(_fromUtf8("Remove2"))
        self.CountryBox1 = QtWidgets.QLineEdit(self.page3)
        self.CountryBox1.setGeometry(QtCore.QRect(0, 330, 501, 31))
        self.CountryBox1.setStyleSheet(
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
        self.CountryBox1.setText(_fromUtf8(""))
        self.CountryBox1.setObjectName(_fromUtf8("CountryBox1"))
        self.Update2 = QtWidgets.QPushButton(self.page3)
        self.Update2.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update2.setObjectName(_fromUtf8("Update2"))
        self.PhoneText1 = myQLabel(self.page3)
        self.PhoneText1.setGeometry(QtCore.QRect(0, 230, 501, 31))
        # self.PhoneText1.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.PhoneText1.setObjectName(_fromUtf8("PhoneText1"))
        self.OtherBox2 = QtWidgets.QTextEdit(self.page3)
        self.OtherBox2.setGeometry(QtCore.QRect(0, 510, 501, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherBox2.sizePolicy().hasHeightForWidth())
        self.OtherBox2.setSizePolicy(sizePolicy)
        self.OtherBox2.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherBox2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.OtherBox2.setStyleSheet(
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
        self.OtherBox2.setObjectName(_fromUtf8("OtherBox2"))
        self.CountryText1 = myQLabel(self.page3)
        self.CountryText1.setGeometry(QtCore.QRect(0, 300, 501, 31))
        # self.CountryText1.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CountryText1.setObjectName(_fromUtf8("CountryText1"))
        self.Pickup1 = QtWidgets.QLineEdit(self.page3)
        self.Pickup1.setGeometry(QtCore.QRect(0, 400, 501, 31))
        self.Pickup1.setStyleSheet(
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
        self.Pickup1.setText(_fromUtf8(""))
        self.Pickup1.setObjectName(_fromUtf8("Pickup1"))
        self.CityPickup1 = myQLabel(self.page3)
        self.CityPickup1.setGeometry(QtCore.QRect(0, 370, 501, 31))
        # self.CityPickup1.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CityPickup1.setObjectName(_fromUtf8("CityPickup1"))
        self.FullName1 = myQLabel(self.page3)
        self.FullName1.setGeometry(QtCore.QRect(0, 160, 501, 31))
        # self.FullName1.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.FullName1.setObjectName(_fromUtf8("FullName1"))
        self.NameBox1 = QtWidgets.QLineEdit(self.page3)
        self.NameBox1.setGeometry(QtCore.QRect(0, 190, 501, 31))
        self.NameBox1.setStyleSheet(
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
        self.NameBox1.setText(_fromUtf8(""))
        self.NameBox1.setObjectName(_fromUtf8("NameBox1"))
        self.Create2 = QtWidgets.QPushButton(self.page3)
        self.Create2.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create2.setObjectName(_fromUtf8("Create2"))
        self.WUSelect = QtWidgets.QComboBox(self.page3)
        self.WUSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.WUSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.WUSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WUSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.WUSelect.setStyleSheet(
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
        self.WUSelect.setObjectName(_fromUtf8("WUSelect"))
        self.WUBrowser = QtWidgets.QTextBrowser(self.page3)
        self.WUBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.WUBrowser.setObjectName(_fromUtf8("WUBrowser"))
        self.Secret1 = myQCheckBox(self.page3)
        self.Secret1.setGeometry(QtCore.QRect(0, 440, 421, 31))
        # self.Secret1.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.Secret1.setObjectName(_fromUtf8("Secret1"))
        self.Pages.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName(_fromUtf8("page4"))
        self.FullNameText2 = myQLabel(self.page4)
        self.FullNameText2.setGeometry(QtCore.QRect(0, 160, 361, 31))
        # self.FullNameText2.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.FullNameText2.setObjectName(_fromUtf8("FullNameText2"))
        self.CountryText2 = myQLabel(self.page4)
        self.CountryText2.setGeometry(QtCore.QRect(0, 300, 261, 31))
        # self.CountryText2.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CountryText2.setObjectName(_fromUtf8("CountryText2"))
        self.MGText = myQLabel(self.page4)
        self.MGText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.MGText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.MGText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.MGText.setObjectName(_fromUtf8("MGText"))
        self.NameBox2 = QtWidgets.QLineEdit(self.page4)
        self.NameBox2.setGeometry(QtCore.QRect(0, 190, 501, 31))
        self.NameBox2.setStyleSheet(
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
        self.NameBox2.setText(_fromUtf8(""))
        self.NameBox2.setObjectName(_fromUtf8("NameBox2"))
        self.MGSelect = QtWidgets.QComboBox(self.page4)
        self.MGSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.MGSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.MGSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MGSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MGSelect.setStyleSheet(
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
        self.MGSelect.setObjectName(_fromUtf8("MGSelect"))
        self.Remove3 = QtWidgets.QPushButton(self.page4)
        self.Remove3.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove3.setObjectName(_fromUtf8("Remove3"))
        self.Save3 = QtWidgets.QPushButton(self.page4)
        self.Save3.setGeometry(QtCore.QRect(0, 620, 151, 41))
        self.Save3.setObjectName(_fromUtf8("Save3"))
        self.CountryBox2 = QtWidgets.QLineEdit(self.page4)
        self.CountryBox2.setGeometry(QtCore.QRect(0, 330, 501, 31))
        self.CountryBox2.setStyleSheet(
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
        self.CountryBox2.setText(_fromUtf8(""))
        self.CountryBox2.setObjectName(_fromUtf8("CountryBox2"))
        self.OtherInfo3 = myQLabel(self.page4)
        self.OtherInfo3.setGeometry(QtCore.QRect(0, 480, 501, 31))
        # self.OtherInfo3.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherInfo3.setObjectName(_fromUtf8("OtherInfo3"))
        self.FundsPickup2 = QtWidgets.QLineEdit(self.page4)
        self.FundsPickup2.setGeometry(QtCore.QRect(0, 400, 501, 31))
        self.FundsPickup2.setStyleSheet(
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
        self.FundsPickup2.setText(_fromUtf8(""))
        self.FundsPickup2.setObjectName(_fromUtf8("FundsPickup2"))
        self.Update3 = QtWidgets.QPushButton(self.page4)
        self.Update3.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update3.setObjectName(_fromUtf8("Update3"))
        self.MGBrowser = QtWidgets.QTextBrowser(self.page4)
        self.MGBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.MGBrowser.setObjectName(_fromUtf8("MGBrowser"))
        self.PhoneBox2 = QtWidgets.QLineEdit(self.page4)
        self.PhoneBox2.setGeometry(QtCore.QRect(0, 260, 501, 31))
        self.PhoneBox2.setStyleSheet(
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
        self.PhoneBox2.setText(_fromUtf8(""))
        self.PhoneBox2.setObjectName(_fromUtf8("PhoneBox2"))
        self.PhoneText2 = myQLabel(self.page4)
        self.PhoneText2.setGeometry(QtCore.QRect(0, 230, 501, 31))
        # self.PhoneText2.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.PhoneText2.setObjectName(_fromUtf8("PhoneText2"))
        self.Secret2 = myQCheckBox(self.page4)
        self.Secret2.setGeometry(QtCore.QRect(0, 440, 421, 31))
        # self.Secret2.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.Secret2.setObjectName(_fromUtf8("Secret2"))
        self.OtherBox3 = QtWidgets.QTextEdit(self.page4)
        self.OtherBox3.setGeometry(QtCore.QRect(0, 510, 501, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherBox3.sizePolicy().hasHeightForWidth())
        self.OtherBox3.setSizePolicy(sizePolicy)
        self.OtherBox3.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherBox3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.OtherBox3.setStyleSheet(
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
        self.OtherBox3.setObjectName(_fromUtf8("OtherBox3"))
        self.CityFunds2 = myQLabel(self.page4)
        self.CityFunds2.setGeometry(QtCore.QRect(0, 370, 501, 31))
        # self.CityFunds2.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CityFunds2.setObjectName(_fromUtf8("CityFunds2"))
        self.Create3 = QtWidgets.QPushButton(self.page4)
        self.Create3.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create3.setObjectName(_fromUtf8("Create3"))
        self.line_10 = QtWidgets.QFrame(self.page4)
        self.line_10.setGeometry(QtCore.QRect(0, 600, 501, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.Pages.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName(_fromUtf8("page5"))
        self.Remove4 = QtWidgets.QPushButton(self.page5)
        self.Remove4.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove4.setObjectName(_fromUtf8("Remove4"))
        self.line_11 = QtWidgets.QFrame(self.page5)
        self.line_11.setGeometry(QtCore.QRect(0, 400, 501, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.Update4 = QtWidgets.QPushButton(self.page5)
        self.Update4.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update4.setObjectName(_fromUtf8("Update4"))
        self.DebitBox = QtWidgets.QTextEdit(self.page5)
        self.DebitBox.setGeometry(QtCore.QRect(0, 190, 501, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DebitBox.sizePolicy().hasHeightForWidth())
        self.DebitBox.setSizePolicy(sizePolicy)
        self.DebitBox.setMinimumSize(QtCore.QSize(0, 89))
        self.DebitBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.DebitBox.setStyleSheet(
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
        self.DebitBox.setObjectName(_fromUtf8("DebitBox"))
        self.Create4 = QtWidgets.QPushButton(self.page5)
        self.Create4.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create4.setObjectName(_fromUtf8("Create4"))
        self.Save4 = QtWidgets.QPushButton(self.page5)
        self.Save4.setGeometry(QtCore.QRect(0, 420, 151, 41))
        self.Save4.setObjectName(_fromUtf8("Save4"))
        self.DebitText = myQLabel(self.page5)
        self.DebitText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.DebitText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.DebitText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.DebitText.setObjectName(_fromUtf8("DebitText"))
        self.DebitSelect = QtWidgets.QComboBox(self.page5)
        self.DebitSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.DebitSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.DebitSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.DebitSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DebitSelect.setStyleSheet(
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
        self.DebitSelect.setObjectName(_fromUtf8("DebitSelect"))
        self.DebitInfoText = myQLabel(self.page5)
        self.DebitInfoText.setGeometry(QtCore.QRect(0, 160, 501, 31))
        # self.DebitInfoText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.DebitInfoText.setObjectName(_fromUtf8("DebitInfoText"))
        self.DebitBrowser = QtWidgets.QTextBrowser(self.page5)
        self.DebitBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.DebitBrowser.setObjectName(_fromUtf8("DebitBrowser"))
        self.Pages.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName(_fromUtf8("page6"))
        self.Save5 = QtWidgets.QPushButton(self.page6)
        self.Save5.setGeometry(QtCore.QRect(0, 420, 151, 41))
        self.Save5.setObjectName(_fromUtf8("Save5"))
        self.OtherFundText = myQLabel(self.page6)
        self.OtherFundText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.OtherFundText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.OtherFundText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.OtherFundText.setObjectName(_fromUtf8("OtherFundText"))
        self.Create5 = QtWidgets.QPushButton(self.page6)
        self.Create5.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create5.setObjectName(_fromUtf8("Create5"))
        self.OtherFundSelect = QtWidgets.QComboBox(self.page6)
        self.OtherFundSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.OtherFundSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.OtherFundSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.OtherFundSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.OtherFundSelect.setStyleSheet(
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
        self.OtherFundSelect.setObjectName(_fromUtf8("OtherFundSelect"))
        self.OtherFundBrowser = QtWidgets.QTextBrowser(self.page6)
        self.OtherFundBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.OtherFundBrowser.setObjectName(_fromUtf8("OtherFundBrowser"))
        self.OtherFundBox = QtWidgets.QTextEdit(self.page6)
        self.OtherFundBox.setGeometry(QtCore.QRect(0, 190, 501, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherFundBox.sizePolicy().hasHeightForWidth())
        self.OtherFundBox.setSizePolicy(sizePolicy)
        self.OtherFundBox.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherFundBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.OtherFundBox.setStyleSheet(
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
        self.OtherFundBox.setObjectName(_fromUtf8("OtherFundBox"))
        self.Update5 = QtWidgets.QPushButton(self.page6)
        self.Update5.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update5.setObjectName(_fromUtf8("Update5"))
        self.line_12 = QtWidgets.QFrame(self.page6)
        self.line_12.setGeometry(QtCore.QRect(0, 400, 501, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.Remove5 = QtWidgets.QPushButton(self.page6)
        self.Remove5.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove5.setObjectName(_fromUtf8("Remove5"))
        self.AltText = myQLabel(self.page6)
        self.AltText.setGeometry(QtCore.QRect(0, 160, 501, 31))
        # self.AltText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AltText.setObjectName(_fromUtf8("AltText"))
        self.Pages.addWidget(self.page6)
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName(_fromUtf8("page7"))
        self.NameCashText = myQLabel(self.page7)
        self.NameCashText.setGeometry(QtCore.QRect(0, 160, 361, 31))
        # self.NameCashText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.NameCashText.setObjectName(_fromUtf8("NameCashText"))
        self.CountryCashText = myQLabel(self.page7)
        self.CountryCashText.setGeometry(QtCore.QRect(0, 240, 61, 31))
        # self.CountryCashText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CountryCashText.setObjectName(_fromUtf8("CountryCashText"))
        self.CashMailText = myQLabel(self.page7)
        self.CashMailText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.CashMailText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.CashMailText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.CashMailText.setObjectName(_fromUtf8("CashMailText"))
        self.NameCashBox = QtWidgets.QLineEdit(self.page7)
        self.NameCashBox.setGeometry(QtCore.QRect(0, 190, 501, 31))
        self.NameCashBox.setStyleSheet(
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
        self.NameCashBox.setText(_fromUtf8(""))
        self.NameCashBox.setObjectName(_fromUtf8("NameCashBox"))
        self.CashMailSelect = QtWidgets.QComboBox(self.page7)
        self.CashMailSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.CashMailSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.CashMailSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.CashMailSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CashMailSelect.setStyleSheet(
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
        self.CashMailSelect.setObjectName(_fromUtf8("CashMailSelect"))
        self.Remove6 = QtWidgets.QPushButton(self.page7)
        self.Remove6.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove6.setObjectName(_fromUtf8("Remove6"))
        self.Save6 = QtWidgets.QPushButton(self.page7)
        self.Save6.setGeometry(QtCore.QRect(0, 620, 151, 41))
        self.Save6.setObjectName(_fromUtf8("Save6"))
        self.CityCashBox = QtWidgets.QLineEdit(self.page7)
        self.CityCashBox.setGeometry(QtCore.QRect(220, 270, 221, 31))
        self.CityCashBox.setStyleSheet(
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
        self.CityCashBox.setText(_fromUtf8(""))
        self.CityCashBox.setObjectName(_fromUtf8("CityCashBox"))
        self.OtherInfoCash = myQLabel(self.page7)
        self.OtherInfoCash.setGeometry(QtCore.QRect(0, 480, 501, 31))
        # self.OtherInfoCash.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherInfoCash.setObjectName(_fromUtf8("OtherInfoCash"))
        self.StateCashBox = QtWidgets.QLineEdit(self.page7)
        self.StateCashBox.setGeometry(QtCore.QRect(460, 270, 201, 31))
        self.StateCashBox.setStyleSheet(
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
        self.StateCashBox.setText(_fromUtf8(""))
        self.StateCashBox.setObjectName(_fromUtf8("StateCashBox"))
        self.Update6 = QtWidgets.QPushButton(self.page7)
        self.Update6.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update6.setObjectName(_fromUtf8("Update6"))
        self.CashMailBrowser = QtWidgets.QTextBrowser(self.page7)
        self.CashMailBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.CashMailBrowser.setObjectName(_fromUtf8("CashMailBrowser"))
        self.CountryCashBox = QtWidgets.QLineEdit(self.page7)
        self.CountryCashBox.setGeometry(QtCore.QRect(0, 270, 201, 31))
        self.CountryCashBox.setStyleSheet(
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
        self.CountryCashBox.setText(_fromUtf8(""))
        self.CountryCashBox.setObjectName(_fromUtf8("CountryCashBox"))
        self.PhoneCashText = myQLabel(self.page7)
        self.PhoneCashText.setGeometry(QtCore.QRect(230, 310, 261, 31))
        # self.PhoneCashText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.PhoneCashText.setObjectName(_fromUtf8("PhoneCashText"))
        self.InsuranceCheckCash = myQCheckBox(self.page7)
        self.InsuranceCheckCash.setGeometry(QtCore.QRect(470, 340, 191, 31))
        self.InsuranceCheckCash.setStyleSheet(_fromUtf8('font: 16px "Arial";'))
        self.InsuranceCheckCash.setObjectName(_fromUtf8("InsuranceCheckCash"))
        self.OtherInfoCashBox = QtWidgets.QTextEdit(self.page7)
        self.OtherInfoCashBox.setGeometry(QtCore.QRect(0, 510, 501, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherInfoCashBox.sizePolicy().hasHeightForWidth())
        self.OtherInfoCashBox.setSizePolicy(sizePolicy)
        self.OtherInfoCashBox.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherInfoCashBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.OtherInfoCashBox.setStyleSheet(
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
        self.OtherInfoCashBox.setObjectName(_fromUtf8("OtherInfoCashBox"))
        self.CityCashText = myQLabel(self.page7)
        self.CityCashText.setGeometry(QtCore.QRect(230, 240, 101, 31))
        # self.CityCashText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CityCashText.setObjectName(_fromUtf8("CityCashText"))
        self.Create6 = QtWidgets.QPushButton(self.page7)
        self.Create6.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create6.setObjectName(_fromUtf8("Create6"))
        self.line_13 = QtWidgets.QFrame(self.page7)
        self.line_13.setGeometry(QtCore.QRect(0, 600, 501, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.StateCashText = myQLabel(self.page7)
        self.StateCashText.setGeometry(QtCore.QRect(460, 240, 41, 31))
        # self.StateCashText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.StateCashText.setObjectName(_fromUtf8("StateCashText"))
        self.AddressTextCash = myQLabel(self.page7)
        self.AddressTextCash.setGeometry(QtCore.QRect(0, 380, 71, 31))
        # self.AddressTextCash.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AddressTextCash.setObjectName(_fromUtf8("AddressTextCash"))
        self.AddressCashBox = QtWidgets.QTextEdit(self.page7)
        self.AddressCashBox.setGeometry(QtCore.QRect(0, 410, 661, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.AddressCashBox.sizePolicy().hasHeightForWidth())
        self.AddressCashBox.setSizePolicy(sizePolicy)
        self.AddressCashBox.setMinimumSize(QtCore.QSize(100, 30))
        self.AddressCashBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.AddressCashBox.setStyleSheet(
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
        self.AddressCashBox.setObjectName(_fromUtf8("AddressCashBox"))
        self.ZipCashBox = QtWidgets.QLineEdit(self.page7)
        self.ZipCashBox.setGeometry(QtCore.QRect(0, 340, 201, 31))
        self.ZipCashBox.setStyleSheet(
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
        self.ZipCashBox.setText(_fromUtf8(""))
        self.ZipCashBox.setObjectName(_fromUtf8("ZipCashBox"))
        self.PhoneCashBox = QtWidgets.QLineEdit(self.page7)
        self.PhoneCashBox.setGeometry(QtCore.QRect(220, 340, 221, 31))
        self.PhoneCashBox.setStyleSheet(
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
        self.PhoneCashBox.setText(_fromUtf8(""))
        self.PhoneCashBox.setObjectName(_fromUtf8("PhoneCashBox"))
        self.ZipCashText = myQLabel(self.page7)
        self.ZipCashText.setGeometry(QtCore.QRect(0, 310, 81, 31))
        # self.ZipCashText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.ZipCashText.setObjectName(_fromUtf8("ZipCashText"))
        self.Pages.addWidget(self.page7)
        self.page8 = QtWidgets.QWidget()
        self.page8.setObjectName(_fromUtf8("page8"))
        self.Remove7 = QtWidgets.QPushButton(self.page8)
        self.Remove7.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove7.setObjectName(_fromUtf8("Remove7"))
        self.OtherMailBox = QtWidgets.QTextEdit(self.page8)
        self.OtherMailBox.setGeometry(QtCore.QRect(0, 510, 501, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherMailBox.sizePolicy().hasHeightForWidth())
        self.OtherMailBox.setSizePolicy(sizePolicy)
        self.OtherMailBox.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherMailBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.OtherMailBox.setStyleSheet(
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
        self.OtherMailBox.setObjectName(_fromUtf8("OtherMailBox"))
        self.CountryMailBox = QtWidgets.QLineEdit(self.page8)
        self.CountryMailBox.setGeometry(QtCore.QRect(0, 270, 201, 31))
        self.CountryMailBox.setStyleSheet(
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
        self.CountryMailBox.setText(_fromUtf8(""))
        self.CountryMailBox.setObjectName(_fromUtf8("CountryMailBox"))
        self.NameMailBox = QtWidgets.QLineEdit(self.page8)
        self.NameMailBox.setGeometry(QtCore.QRect(0, 190, 501, 31))
        self.NameMailBox.setStyleSheet(
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
        self.NameMailBox.setText(_fromUtf8(""))
        self.NameMailBox.setObjectName(_fromUtf8("NameMailBox"))
        self.OtherMailText = myQLabel(self.page8)
        self.OtherMailText.setGeometry(QtCore.QRect(0, 480, 501, 31))
        # self.OtherMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherMailText.setObjectName(_fromUtf8("OtherMailText"))
        self.AddressMailBox = QtWidgets.QTextEdit(self.page8)
        self.AddressMailBox.setGeometry(QtCore.QRect(0, 410, 661, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.AddressMailBox.sizePolicy().hasHeightForWidth())
        self.AddressMailBox.setSizePolicy(sizePolicy)
        self.AddressMailBox.setMinimumSize(QtCore.QSize(100, 30))
        self.AddressMailBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.AddressMailBox.setStyleSheet(
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
        self.AddressMailBox.setObjectName(_fromUtf8("AddressMailBox"))
        self.Update7 = QtWidgets.QPushButton(self.page8)
        self.Update7.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update7.setObjectName(_fromUtf8("Update7"))
        self.InsuranceMailCheck = myQCheckBox(self.page8)
        self.InsuranceMailCheck.setGeometry(QtCore.QRect(470, 340, 191, 31))
        self.InsuranceMailCheck.setStyleSheet(_fromUtf8('font: 16px "Arial";'))
        self.InsuranceMailCheck.setObjectName(_fromUtf8("InsuranceMailCheck"))
        self.Save7 = QtWidgets.QPushButton(self.page8)
        self.Save7.setGeometry(QtCore.QRect(0, 620, 151, 41))
        self.Save7.setObjectName(_fromUtf8("Save7"))
        self.StateMailBox = QtWidgets.QLineEdit(self.page8)
        self.StateMailBox.setGeometry(QtCore.QRect(460, 270, 201, 31))
        self.StateMailBox.setStyleSheet(
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
        self.StateMailBox.setText(_fromUtf8(""))
        self.StateMailBox.setObjectName(_fromUtf8("StateMailBox"))
        self.StateMailText = myQLabel(self.page8)
        self.StateMailText.setGeometry(QtCore.QRect(460, 240, 41, 31))
        # self.StateMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.StateMailText.setObjectName(_fromUtf8("StateMailText"))
        self.CityMailBox = QtWidgets.QLineEdit(self.page8)
        self.CityMailBox.setGeometry(QtCore.QRect(220, 270, 221, 31))
        self.CityMailBox.setStyleSheet(
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
        self.CityMailBox.setText(_fromUtf8(""))
        self.CityMailBox.setObjectName(_fromUtf8("CityMailBox"))
        self.MailingText = myQLabel(self.page8)
        self.MailingText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.MailingText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.MailingText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.MailingText.setObjectName(_fromUtf8("MailingText"))
        self.MailingBrowser = QtWidgets.QTextBrowser(self.page8)
        self.MailingBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.MailingBrowser.setObjectName(_fromUtf8("MailingBrowser"))
        self.ZipMailBox = QtWidgets.QLineEdit(self.page8)
        self.ZipMailBox.setGeometry(QtCore.QRect(0, 340, 201, 31))
        self.ZipMailBox.setStyleSheet(
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
        self.ZipMailBox.setText(_fromUtf8(""))
        self.ZipMailBox.setObjectName(_fromUtf8("ZipMailBox"))
        self.CityMailText = myQLabel(self.page8)
        self.CityMailText.setGeometry(QtCore.QRect(230, 240, 101, 31))
        # self.CityMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CityMailText.setObjectName(_fromUtf8("CityMailText"))
        self.NameTextMail = myQLabel(self.page8)
        self.NameTextMail.setGeometry(QtCore.QRect(0, 160, 361, 31))
        # self.NameTextMail.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.NameTextMail.setObjectName(_fromUtf8("NameTextMail"))
        self.Create7 = QtWidgets.QPushButton(self.page8)
        self.Create7.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create7.setObjectName(_fromUtf8("Create7"))
        self.AddressMailText = myQLabel(self.page8)
        self.AddressMailText.setGeometry(QtCore.QRect(0, 380, 71, 31))
        # self.AddressMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AddressMailText.setObjectName(_fromUtf8("AddressMailText"))
        self.PhoneMailBox = QtWidgets.QLineEdit(self.page8)
        self.PhoneMailBox.setGeometry(QtCore.QRect(220, 340, 221, 31))
        self.PhoneMailBox.setStyleSheet(
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
        self.PhoneMailBox.setText(_fromUtf8(""))
        self.PhoneMailBox.setObjectName(_fromUtf8("PhoneMailBox"))
        self.ZipMailText = myQLabel(self.page8)
        self.ZipMailText.setGeometry(QtCore.QRect(0, 310, 81, 31))
        # self.ZipMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.ZipMailText.setObjectName(_fromUtf8("ZipMailText"))
        self.PhoneMailText = myQLabel(self.page8)
        self.PhoneMailText.setGeometry(QtCore.QRect(230, 310, 261, 31))
        # self.PhoneMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.PhoneMailText.setObjectName(_fromUtf8("PhoneMailText"))
        self.line_14 = QtWidgets.QFrame(self.page8)
        self.line_14.setGeometry(QtCore.QRect(0, 600, 501, 20))
        self.line_14.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.MailingSelect = QtWidgets.QComboBox(self.page8)
        self.MailingSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.MailingSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.MailingSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MailingSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MailingSelect.setStyleSheet(
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
        self.MailingSelect.setObjectName(_fromUtf8("MailingSelect"))
        self.CountryMailText = myQLabel(self.page8)
        self.CountryMailText.setGeometry(QtCore.QRect(0, 240, 61, 31))
        # self.CountryMailText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.CountryMailText.setObjectName(_fromUtf8("CountryMailText"))
        self.Pages.addWidget(self.page8)
        self.page9 = QtWidgets.QWidget()
        self.page9.setObjectName(_fromUtf8("page9"))
        self.ContactBrowser = QtWidgets.QTextBrowser(self.page9)
        self.ContactBrowser.setGeometry(QtCore.QRect(0, 40, 501, 71))
        self.ContactBrowser.setObjectName(_fromUtf8("ContactBrowser"))
        self.PhoneContactText = myQLabel(self.page9)
        self.PhoneContactText.setGeometry(QtCore.QRect(0, 230, 261, 31))
        # self.PhoneContactText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.PhoneContactText.setObjectName(_fromUtf8("PhoneContactText"))
        self.line_15 = QtWidgets.QFrame(self.page9)
        self.line_15.setGeometry(QtCore.QRect(0, 600, 501, 20))
        self.line_15.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.IRCContactText = myQLabel(self.page9)
        self.IRCContactText.setGeometry(QtCore.QRect(0, 300, 261, 31))
        # self.IRCContactText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.IRCContactText.setObjectName(_fromUtf8("IRCContactText"))
        self.Remove8 = QtWidgets.QPushButton(self.page9)
        self.Remove8.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.Remove8.setObjectName(_fromUtf8("Remove8"))
        self.PhoneContactBox = QtWidgets.QLineEdit(self.page9)
        self.PhoneContactBox.setGeometry(QtCore.QRect(0, 260, 501, 31))
        self.PhoneContactBox.setStyleSheet(
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
        self.PhoneContactBox.setText(_fromUtf8(""))
        self.PhoneContactBox.setObjectName(_fromUtf8("PhoneContactBox"))
        self.OtherContactBox = QtWidgets.QTextEdit(self.page9)
        self.OtherContactBox.setGeometry(QtCore.QRect(0, 510, 501, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OtherContactBox.sizePolicy().hasHeightForWidth())
        self.OtherContactBox.setSizePolicy(sizePolicy)
        self.OtherContactBox.setMinimumSize(QtCore.QSize(0, 89))
        self.OtherContactBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.OtherContactBox.setStyleSheet(
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
        self.OtherContactBox.setObjectName(_fromUtf8("OtherContactBox"))
        self.Update8 = QtWidgets.QPushButton(self.page9)
        self.Update8.setGeometry(QtCore.QRect(510, 150, 151, 41))
        self.Update8.setObjectName(_fromUtf8("Update8"))
        self.ToxContactText = myQLabel(self.page9)
        self.ToxContactText.setGeometry(QtCore.QRect(0, 370, 261, 31))
        # self.ToxContactText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.ToxContactText.setObjectName(_fromUtf8("ToxContactText"))
        self.ContactText = myQLabel(self.page9)
        self.ContactText.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.ContactText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.ContactText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.ContactText.setObjectName(_fromUtf8("ContactText"))
        self.ToxContactBox = QtWidgets.QLineEdit(self.page9)
        self.ToxContactBox.setGeometry(QtCore.QRect(0, 400, 501, 31))
        self.ToxContactBox.setStyleSheet(
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
        self.ToxContactBox.setText(_fromUtf8(""))
        self.ToxContactBox.setObjectName(_fromUtf8("ToxContactBox"))
        self.OtherContactText = myQLabel(self.page9)
        self.OtherContactText.setGeometry(QtCore.QRect(0, 480, 501, 31))
        # self.OtherContactText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherContactText.setObjectName(_fromUtf8("OtherContactText"))
        self.EmailContactBox = QtWidgets.QLineEdit(self.page9)
        self.EmailContactBox.setGeometry(QtCore.QRect(0, 190, 501, 31))
        self.EmailContactBox.setStyleSheet(
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
        self.EmailContactBox.setText(_fromUtf8(""))
        self.EmailContactBox.setObjectName(_fromUtf8("EmailContactBox"))
        self.IRCContactBox = QtWidgets.QLineEdit(self.page9)
        self.IRCContactBox.setGeometry(QtCore.QRect(0, 330, 501, 31))
        self.IRCContactBox.setStyleSheet(
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
        self.IRCContactBox.setText(_fromUtf8(""))
        self.IRCContactBox.setObjectName(_fromUtf8("IRCContactBox"))
        self.EmailContactText = myQLabel(self.page9)
        self.EmailContactText.setGeometry(QtCore.QRect(0, 160, 361, 31))
        # self.EmailContactText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.EmailContactText.setObjectName(_fromUtf8("EmailContactText"))
        self.Create8 = QtWidgets.QPushButton(self.page9)
        self.Create8.setGeometry(QtCore.QRect(510, 110, 151, 41))
        self.Create8.setObjectName(_fromUtf8("Create8"))
        self.Save8 = QtWidgets.QPushButton(self.page9)
        self.Save8.setGeometry(QtCore.QRect(0, 620, 151, 41))
        self.Save8.setObjectName(_fromUtf8("Save8"))
        self.ContactSelect = QtWidgets.QComboBox(self.page9)
        self.ContactSelect.setGeometry(QtCore.QRect(0, 110, 501, 40))
        self.ContactSelect.setMinimumSize(QtCore.QSize(0, 40))
        self.ContactSelect.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ContactSelect.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ContactSelect.setStyleSheet(
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
        self.ContactSelect.setObjectName(_fromUtf8("ContactSelect"))
        self.Pages.addWidget(self.page9)
        self.page10 = QtWidgets.QWidget()
        self.page10.setObjectName(_fromUtf8("page10"))
        self.MaxIncreaseBuy = QtWidgets.QComboBox(self.page10)
        self.MaxIncreaseBuy.setGeometry(QtCore.QRect(400, 90, 161, 31))
        self.MaxIncreaseBuy.setObjectName(_fromUtf8("MaxIncreaseBuy"))
        self.MaxIncreaseBuy.addItem(_fromUtf8(""))
        self.MaxIncreaseBuy.addItem(_fromUtf8(""))
        self.line_16 = QtWidgets.QFrame(self.page10)
        self.line_16.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.perc6 = myQLabel(self.page10)
        self.perc6.setGeometry(QtCore.QRect(650, 90, 21, 31))
        # self.perc6.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc6.setObjectName(_fromUtf8("perc6"))
        self.AmountText2 = myQLabel(self.page10)
        self.AmountText2.setGeometry(QtCore.QRect(0, 140, 71, 31))
        # self.AmountText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AmountText2.setObjectName(_fromUtf8("AmountText2"))
        self.MaxDecreaseBuyBox = QtWidgets.QLineEdit(self.page10)
        self.MaxDecreaseBuyBox.setGeometry(QtCore.QRect(570, 130, 71, 31))
        self.MaxDecreaseBuyBox.setStyleSheet(
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
        self.MaxDecreaseBuyBox.setObjectName(_fromUtf8("MaxDecreaseBuyBox"))
        self.MyDepositBox2 = QtWidgets.QLineEdit(self.page10)
        self.MyDepositBox2.setGeometry(QtCore.QRect(140, 340, 161, 31))
        self.MyDepositBox2.setStyleSheet(
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
        self.MyDepositBox2.setText(_fromUtf8(""))
        self.MyDepositBox2.setObjectName(_fromUtf8("MyDepositBox2"))
        self.MaxDecreaseBuy = QtWidgets.QComboBox(self.page10)
        self.MaxDecreaseBuy.setGeometry(QtCore.QRect(400, 130, 161, 31))
        self.MaxDecreaseBuy.setObjectName(_fromUtf8("MaxDecreaseBuy"))
        self.MaxDecreaseBuy.addItem(_fromUtf8(""))
        self.MaxDecreaseBuy.addItem(_fromUtf8(""))
        self.MaxDecreaseBuy.addItem(_fromUtf8(""))
        self.DebitCheck2 = myQCheckBox(self.page10)
        self.DebitCheck2.setGeometry(QtCore.QRect(160, 530, 131, 17))
        self.DebitCheck2.setObjectName(_fromUtf8("DebitCheck2"))
        self.perc9 = myQLabel(self.page10)
        self.perc9.setGeometry(QtCore.QRect(650, 280, 21, 31))
        # self.perc9.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc9.setObjectName(_fromUtf8("perc9"))
        self.TimeLimitDays2 = QtWidgets.QComboBox(self.page10)
        self.TimeLimitDays2.setGeometry(QtCore.QRect(620, 340, 51, 31))
        self.TimeLimitDays2.setObjectName(_fromUtf8("TimeLimitDays2"))
        self.TimeLimitDays2.addItem(_fromUtf8(""))
        self.TimeLimitDays2.addItem(_fromUtf8(""))
        self.NotesText2 = myQLabel(self.page10)
        self.NotesText2.setGeometry(QtCore.QRect(400, 440, 281, 31))
        # self.NotesText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.NotesText2.setObjectName(_fromUtf8("NotesText2"))
        self.ServiceCharge2 = QtWidgets.QComboBox(self.page10)
        self.ServiceCharge2.setGeometry(QtCore.QRect(230, 190, 71, 31))
        self.ServiceCharge2.setObjectName(_fromUtf8("ServiceCharge2"))
        self.ServiceCharge2.addItem(_fromUtf8(""))
        self.ServiceCharge2.addItem(_fromUtf8(""))
        self.ServiceCharge2.addItem(_fromUtf8(""))
        self.ServiceCharge2.addItem(_fromUtf8(""))
        self.ServiceCharge2.addItem(_fromUtf8(""))
        self.MyDepositText2 = myQLabel(self.page10)
        self.MyDepositText2.setGeometry(QtCore.QRect(0, 340, 101, 31))
        # self.MyDepositText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText2.setObjectName(_fromUtf8("MyDepositText2"))
        self.perc7 = myQLabel(self.page10)
        self.perc7.setGeometry(QtCore.QRect(650, 130, 21, 31))
        # self.perc7.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc7.setObjectName(_fromUtf8("perc7"))
        self.BankWireCheck2 = myQCheckBox(self.page10)
        self.BankWireCheck2.setGeometry(QtCore.QRect(0, 500, 141, 17))
        self.BankWireCheck2.setObjectName(_fromUtf8("BankWireCheck2"))
        self.CashMail2 = myQCheckBox(self.page10)
        self.CashMail2.setGeometry(QtCore.QRect(0, 560, 131, 17))
        self.CashMail2.setObjectName(_fromUtf8("CashMail2"))
        self.MaxService2 = myQLabel(self.page10)
        self.MaxService2.setGeometry(QtCore.QRect(0, 190, 231, 31))
        # self.MaxService2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MaxService2.setObjectName(_fromUtf8("MaxService2"))
        self.ExchangeRate2 = myQLabel(self.page10)
        self.ExchangeRate2.setGeometry(QtCore.QRect(180, 50, 201, 31))
        # self.ExchangeRate2.setStyleSheet(_fromUtf8("font: 15px \"Arial\";"))
        self.ExchangeRate2.setObjectName(_fromUtf8("ExchangeRate2"))
        self.PayMentOptions2 = myQLabel(self.page10)
        self.PayMentOptions2.setGeometry(QtCore.QRect(0, 440, 151, 31))
        # self.PayMentOptions2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PayMentOptions2.setObjectName(_fromUtf8("PayMentOptions2"))
        self.CoinsForCashBuy = myQLabel(self.page10)
        self.CoinsForCashBuy.setGeometry(QtCore.QRect(0, 0, 281, 51))
        self.CoinsForCashBuy.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.CoinsForCashBuy.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.CoinsForCashBuy.setObjectName(_fromUtf8("CoinsForCashBuy"))
        self.AmountBox2 = QtWidgets.QLineEdit(self.page10)
        self.AmountBox2.setGeometry(QtCore.QRect(90, 140, 211, 31))
        self.AmountBox2.setStyleSheet(
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
        self.AmountBox2.setText(_fromUtf8(""))
        self.AmountBox2.setObjectName(_fromUtf8("AmountBox2"))
        self.PriceTrackingTitle2 = myQLabel(self.page10)
        self.PriceTrackingTitle2.setGeometry(QtCore.QRect(400, 50, 211, 31))
        # self.PriceTrackingTitle2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PriceTrackingTitle2.setObjectName(_fromUtf8("PriceTrackingTitle2"))
        self.MaxOrderBuy = QtWidgets.QComboBox(self.page10)
        self.MaxOrderBuy.setGeometry(QtCore.QRect(400, 280, 161, 31))
        self.MaxOrderBuy.setObjectName(_fromUtf8("MaxOrderBuy"))
        self.MaxOrderBuy.addItem(_fromUtf8(""))
        self.MaxOrderBuy.addItem(_fromUtf8(""))
        self.MaxOrderBuy.addItem(_fromUtf8(""))
        self.MaxOrderBuy.addItem(_fromUtf8(""))
        self.perc8 = myQLabel(self.page10)
        self.perc8.setGeometry(QtCore.QRect(650, 240, 21, 31))
        # self.perc8.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc8.setObjectName(_fromUtf8("perc8"))
        self.OtherCheck2 = myQCheckBox(self.page10)
        self.OtherCheck2.setGeometry(QtCore.QRect(160, 560, 131, 17))
        self.OtherCheck2.setObjectName(_fromUtf8("OtherCheck2"))
        self.TheirDepositBox2 = QtWidgets.QLineEdit(self.page10)
        self.TheirDepositBox2.setGeometry(QtCore.QRect(140, 380, 161, 31))
        self.TheirDepositBox2.setStyleSheet(
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
        self.TheirDepositBox2.setText(_fromUtf8(""))
        self.TheirDepositBox2.setObjectName(_fromUtf8("TheirDepositBox2"))
        self.RateBox2 = QtWidgets.QComboBox(self.page10)
        self.RateBox2.setGeometry(QtCore.QRect(0, 50, 161, 31))
        self.RateBox2.setStyleSheet(_fromUtf8("font: 16px"))
        self.RateBox2.setObjectName(_fromUtf8("RateBox2"))
        self.RateBox2.addItem(_fromUtf8(""))
        self.RateBox2.addItem(_fromUtf8(""))
        self.AmountUSD2 = QtWidgets.QComboBox(self.page10)
        self.AmountUSD2.setGeometry(QtCore.QRect(310, 140, 51, 31))
        self.AmountUSD2.setObjectName(_fromUtf8("AmountUSD2"))
        self.AmountUSD2.addItem(_fromUtf8(""))
        self.AmountUSD2.addItem(_fromUtf8(""))
        self.TimeLimitText2 = myQLabel(self.page10)
        self.TimeLimitText2.setGeometry(QtCore.QRect(400, 340, 101, 31))
        # self.TimeLimitText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText2.setObjectName(_fromUtf8("TimeLimitText2"))
        self.SaveContinue2 = QtWidgets.QPushButton(self.page10)
        self.SaveContinue2.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue2.setObjectName(_fromUtf8("SaveContinue2"))
        self.PriceText2 = myQLabel(self.page10)
        self.PriceText2.setGeometry(QtCore.QRect(0, 100, 61, 31))
        # self.PriceText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PriceText2.setObjectName(_fromUtf8("PriceText2"))
        self.DepositSettings2 = QtWidgets.QComboBox(self.page10)
        self.DepositSettings2.setGeometry(QtCore.QRect(0, 290, 211, 31))
        self.DepositSettings2.setObjectName(_fromUtf8("DepositSettings2"))
        self.DepositSettings2.addItem(_fromUtf8(""))
        self.DepositSettings2.addItem(_fromUtf8(""))
        self.DepositSettings2.addItem(_fromUtf8(""))
        self.TimeLimitBox2 = QtWidgets.QLineEdit(self.page10)
        self.TimeLimitBox2.setGeometry(QtCore.QRect(510, 340, 101, 31))
        self.TimeLimitBox2.setStyleSheet(
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
        self.TimeLimitBox2.setObjectName(_fromUtf8("TimeLimitBox2"))
        self.MinOrderBuy = QtWidgets.QComboBox(self.page10)
        self.MinOrderBuy.setGeometry(QtCore.QRect(400, 240, 161, 31))
        self.MinOrderBuy.setObjectName(_fromUtf8("MinOrderBuy"))
        self.MinOrderBuy.addItem(_fromUtf8(""))
        self.MinOrderBuy.addItem(_fromUtf8(""))
        self.MinOrderBuy.addItem(_fromUtf8(""))
        self.MinOrderBuy.addItem(_fromUtf8(""))
        self.MaxIncreaseBuyBox = QtWidgets.QLineEdit(self.page10)
        self.MaxIncreaseBuyBox.setGeometry(QtCore.QRect(570, 90, 71, 31))
        self.MaxIncreaseBuyBox.setStyleSheet(
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
        self.MaxIncreaseBuyBox.setObjectName(_fromUtf8("MaxIncreaseBuyBox"))
        self.ShowAdvancedCashBuy = myQCheckBox(self.page10)
        self.ShowAdvancedCashBuy.setGeometry(QtCore.QRect(400, 10, 271, 31))
        self.ShowAdvancedCashBuy.setStyleSheet(_fromUtf8('font: 22px "Arial";'))
        self.ShowAdvancedCashBuy.setObjectName(_fromUtf8("ShowAdvancedCashBuy"))
        self.LimitOrderText2 = myQLabel(self.page10)
        self.LimitOrderText2.setGeometry(QtCore.QRect(400, 190, 211, 31))
        # self.LimitOrderText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.LimitOrderText2.setObjectName(_fromUtf8("LimitOrderText2"))
        self.AgreeFund2 = myQLabel(self.page10)
        self.AgreeFund2.setGeometry(QtCore.QRect(0, 470, 331, 16))
        self.AgreeFund2.setObjectName(_fromUtf8("AgreeFund2"))
        self.TheirDepositText2 = myQLabel(self.page10)
        self.TheirDepositText2.setGeometry(QtCore.QRect(0, 380, 131, 31))
        # self.TheirDepositText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText2.setObjectName(_fromUtf8("TheirDepositText2"))
        self.MoneyGramCheck2 = myQCheckBox(self.page10)
        self.MoneyGramCheck2.setGeometry(QtCore.QRect(0, 530, 131, 17))
        self.MoneyGramCheck2.setObjectName(_fromUtf8("MoneyGramCheck2"))
        self.WUCheck2 = myQCheckBox(self.page10)
        self.WUCheck2.setGeometry(QtCore.QRect(160, 500, 141, 17))
        self.WUCheck2.setObjectName(_fromUtf8("WUCheck2"))
        self.MaxOrderBuyBox = QtWidgets.QLineEdit(self.page10)
        self.MaxOrderBuyBox.setGeometry(QtCore.QRect(570, 280, 71, 31))
        self.MaxOrderBuyBox.setStyleSheet(
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
        self.MaxOrderBuyBox.setObjectName(_fromUtf8("MaxOrderBuyBox"))
        self.MinOrderBuyBox = QtWidgets.QLineEdit(self.page10)
        self.MinOrderBuyBox.setGeometry(QtCore.QRect(570, 240, 71, 31))
        self.MinOrderBuyBox.setStyleSheet(
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
        self.MinOrderBuyBox.setObjectName(_fromUtf8("MinOrderBuyBox"))
        self.PriceBox2 = QtWidgets.QLineEdit(self.page10)
        self.PriceBox2.setGeometry(QtCore.QRect(90, 100, 211, 31))
        self.PriceBox2.setStyleSheet(
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
        self.PriceBox2.setText(_fromUtf8(""))
        self.PriceBox2.setObjectName(_fromUtf8("PriceBox2"))
        self.NotesBox2 = QtWidgets.QTextEdit(self.page10)
        self.NotesBox2.setGeometry(QtCore.QRect(400, 470, 271, 125))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox2.sizePolicy().hasHeightForWidth())
        self.NotesBox2.setSizePolicy(sizePolicy)
        self.NotesBox2.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox2.setMaximumSize(QtCore.QSize(16777215, 125))
        self.NotesBox2.setStyleSheet(
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
        self.NotesBox2.setObjectName(_fromUtf8("NotesBox2"))
        self.line_17 = QtWidgets.QFrame(self.page10)
        self.line_17.setGeometry(QtCore.QRect(10, 420, 671, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.ExplainCashBuy = QtWidgets.QPushButton(self.page10)
        self.ExplainCashBuy.setGeometry(QtCore.QRect(320, 10, 40, 40))
        self.ExplainCashBuy.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainCashBuy.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainCashBuy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainCashBuy.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainCashBuy.setIconSize(QtCore.QSize(20, 20))
        self.ExplainCashBuy.setObjectName(_fromUtf8("ExplainCashBuy"))
        self.SupplyAdditional2 = myQCheckBox(self.page10)
        self.SupplyAdditional2.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional2.setObjectName(_fromUtf8("SupplyAdditional2"))
        self.SaveFuture2 = myQCheckBox(self.page10)
        self.SaveFuture2.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture2.setObjectName(_fromUtf8("SaveFuture2"))
        self.ClearForm2 = QtWidgets.QPushButton(self.page10)
        self.ClearForm2.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm2.setObjectName(_fromUtf8("ClearForm2"))
        self.MyDepositUSD2 = QtWidgets.QComboBox(self.page10)
        self.MyDepositUSD2.setGeometry(QtCore.QRect(310, 340, 51, 31))
        self.MyDepositUSD2.setObjectName(_fromUtf8("MyDepositUSD2"))
        self.MyDepositUSD2.addItem(_fromUtf8(""))
        self.MyDepositUSD2.addItem(_fromUtf8(""))
        self.TheirDepositUSD2 = QtWidgets.QComboBox(self.page10)
        self.TheirDepositUSD2.setGeometry(QtCore.QRect(310, 380, 51, 31))
        self.TheirDepositUSD2.setObjectName(_fromUtf8("TheirDepositUSD2"))
        self.TheirDepositUSD2.addItem(_fromUtf8(""))
        self.TheirDepositUSD2.addItem(_fromUtf8(""))
        self.PriceUSD2 = QtWidgets.QComboBox(self.page10)
        self.PriceUSD2.setGeometry(QtCore.QRect(310, 100, 51, 31))
        self.PriceUSD2.setObjectName(_fromUtf8("PriceUSD2"))
        self.PriceUSD2.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page10)
        self.page11 = QtWidgets.QWidget()
        self.page11.setObjectName(_fromUtf8("page11"))
        self.Description1 = myQLabel(self.page11)
        self.Description1.setGeometry(QtCore.QRect(0, 90, 101, 31))
        # self.Description1.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Description1.setObjectName(_fromUtf8("Description1"))
        self.NotesBox3 = QtWidgets.QTextEdit(self.page11)
        self.NotesBox3.setGeometry(QtCore.QRect(400, 519, 271, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox3.sizePolicy().hasHeightForWidth())
        self.NotesBox3.setSizePolicy(sizePolicy)
        self.NotesBox3.setMinimumSize(QtCore.QSize(0, 50))
        self.NotesBox3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox3.setStyleSheet(
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
        self.NotesBox3.setObjectName(_fromUtf8("NotesBox3"))
        self.JobTitleBox1 = QtWidgets.QLineEdit(self.page11)
        self.JobTitleBox1.setGeometry(QtCore.QRect(90, 50, 581, 31))
        self.JobTitleBox1.setStyleSheet(
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
        self.JobTitleBox1.setText(_fromUtf8(""))
        self.JobTitleBox1.setObjectName(_fromUtf8("JobTitleBox1"))
        self.HireSomeoneText = myQLabel(self.page11)
        self.HireSomeoneText.setGeometry(QtCore.QRect(0, 0, 191, 51))
        self.HireSomeoneText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.HireSomeoneText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.HireSomeoneText.setObjectName(_fromUtf8("HireSomeoneText"))
        self.NotesText3 = myQLabel(self.page11)
        self.NotesText3.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.NotesText3.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.NotesText3.setObjectName(_fromUtf8("NotesText3"))
        self.JobSelect1 = QtWidgets.QComboBox(self.page11)
        self.JobSelect1.setGeometry(QtCore.QRect(0, 230, 201, 31))
        self.JobSelect1.setObjectName(_fromUtf8("JobSelect1"))
        self.JobSelect1.addItem(_fromUtf8(""))
        self.JobSelect1.addItem(_fromUtf8(""))
        self.JobSelect1.addItem(_fromUtf8(""))
        self.line_4 = QtWidgets.QFrame(self.page11)
        self.line_4.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.SaveContinue3 = QtWidgets.QPushButton(self.page11)
        self.SaveContinue3.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue3.setObjectName(_fromUtf8("SaveContinue3"))
        self.JobTitle1 = myQLabel(self.page11)
        self.JobTitle1.setGeometry(QtCore.QRect(0, 50, 81, 31))
        # self.JobTitle1.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.JobTitle1.setObjectName(_fromUtf8("JobTitle1"))
        self.DescriptionBox2 = QtWidgets.QTextEdit(self.page11)
        self.DescriptionBox2.setGeometry(QtCore.QRect(0, 120, 671, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DescriptionBox2.sizePolicy().hasHeightForWidth())
        self.DescriptionBox2.setSizePolicy(sizePolicy)
        self.DescriptionBox2.setMinimumSize(QtCore.QSize(0, 89))
        self.DescriptionBox2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.DescriptionBox2.setStyleSheet(
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
        self.DescriptionBox2.setObjectName(_fromUtf8("DescriptionBox2"))
        self.JobAmount1 = QtWidgets.QLineEdit(self.page11)
        self.JobAmount1.setGeometry(QtCore.QRect(0, 280, 201, 31))
        self.JobAmount1.setStyleSheet(
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
        self.JobAmount1.setText(_fromUtf8(""))
        self.JobAmount1.setObjectName(_fromUtf8("JobAmount1"))
        self.RateSelect1 = QtWidgets.QComboBox(self.page11)
        self.RateSelect1.setGeometry(QtCore.QRect(210, 230, 151, 31))
        self.RateSelect1.setObjectName(_fromUtf8("RateSelect1"))
        self.RateSelect1.addItem(_fromUtf8(""))
        self.RateSelect1.addItem(_fromUtf8(""))
        self.RateSelect1.addItem(_fromUtf8(""))
        self.RateSelect1.addItem(_fromUtf8(""))
        self.JobRate = QtWidgets.QComboBox(self.page11)
        self.JobRate.setGeometry(QtCore.QRect(270, 280, 91, 31))
        self.JobRate.setObjectName(_fromUtf8("JobRate"))
        self.JobRate.addItem(_fromUtf8(""))
        self.JobRate.addItem(_fromUtf8(""))
        self.JobRate.addItem(_fromUtf8(""))
        self.JobRate.addItem(_fromUtf8(""))
        self.JobRate.hide()
        self.JobUSD = QtWidgets.QComboBox(self.page11)
        self.JobUSD.setGeometry(QtCore.QRect(210, 280, 51, 31))
        self.JobUSD.setObjectName(_fromUtf8("JobUSD"))
        self.JobUSD.addItem(_fromUtf8(""))
        self.JobUSD.addItem(_fromUtf8(""))
        self.EnableAutoPayCheck = myQCheckBox(self.page11)
        self.EnableAutoPayCheck.setGeometry(QtCore.QRect(400, 230, 261, 31))
        # self.EnableAutoPayCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.EnableAutoPayCheck.setObjectName(_fromUtf8("EnableAutoPayCheck"))
        self.RequireReportCheck = myQCheckBox(self.page11)
        self.RequireReportCheck.setGeometry(QtCore.QRect(400, 270, 261, 31))
        # self.RequireReportCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.RequireReportCheck.setObjectName(_fromUtf8("RequireReportCheck"))
        self.ExplainHire = QtWidgets.QPushButton(self.page11)
        self.ExplainHire.setGeometry(QtCore.QRect(630, 10, 40, 40))
        self.ExplainHire.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainHire.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainHire.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainHire.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainHire.setIconSize(QtCore.QSize(20, 20))
        self.ExplainHire.setObjectName(_fromUtf8("ExplainHire"))
        self.SupplyAdditional3 = myQCheckBox(self.page11)
        self.SupplyAdditional3.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional3.setObjectName(_fromUtf8("SupplyAdditional3"))
        self.SaveFuture3 = myQCheckBox(self.page11)
        self.SaveFuture3.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture3.setObjectName(_fromUtf8("SaveFuture3"))
        self.ClearForm3 = QtWidgets.QPushButton(self.page11)
        self.ClearForm3.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm3.setObjectName(_fromUtf8("ClearForm3"))
        self.TheirDepositText3 = myQLabel(self.page11)
        self.TheirDepositText3.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText3.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText3.setObjectName(_fromUtf8("TheirDepositText3"))
        self.TimeLimitBox3 = QtWidgets.QLineEdit(self.page11)
        self.TimeLimitBox3.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox3.setStyleSheet(
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
        self.TimeLimitBox3.setObjectName(_fromUtf8("TimeLimitBox3"))
        self.MyDepositUSD3 = QtWidgets.QComboBox(self.page11)
        self.MyDepositUSD3.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD3.setObjectName(_fromUtf8("MyDepositUSD3"))
        self.MyDepositUSD3.addItem(_fromUtf8(""))
        self.MyDepositUSD3.addItem(_fromUtf8(""))
        self.DepositSettings3 = QtWidgets.QComboBox(self.page11)
        self.DepositSettings3.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings3.setObjectName(_fromUtf8("DepositSettings3"))
        self.DepositSettings3.addItem(_fromUtf8(""))
        self.DepositSettings3.addItem(_fromUtf8(""))
        self.DepositSettings3.addItem(_fromUtf8(""))
        self.TimeLimitDays3 = QtWidgets.QComboBox(self.page11)
        self.TimeLimitDays3.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays3.setObjectName(_fromUtf8("TimeLimitDays3"))
        self.TimeLimitDays3.addItem(_fromUtf8(""))
        self.TimeLimitDays3.addItem(_fromUtf8(""))
        self.TheirDepositUSD3 = QtWidgets.QComboBox(self.page11)
        self.TheirDepositUSD3.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD3.setObjectName(_fromUtf8("TheirDepositUSD3"))
        self.TheirDepositUSD3.addItem(_fromUtf8(""))
        self.TheirDepositUSD3.addItem(_fromUtf8(""))
        self.TheirDepositBox3 = QtWidgets.QLineEdit(self.page11)
        self.TheirDepositBox3.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox3.setStyleSheet(
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
        self.TheirDepositBox3.setText(_fromUtf8(""))
        self.TheirDepositBox3.setObjectName(_fromUtf8("TheirDepositBox3"))
        self.MyDepositBox3 = QtWidgets.QLineEdit(self.page11)
        self.MyDepositBox3.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox3.setStyleSheet(
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
        self.MyDepositBox3.setText(_fromUtf8(""))
        self.MyDepositBox3.setObjectName(_fromUtf8("MyDepositBox3"))
        self.MyDepositText3 = myQLabel(self.page11)
        self.MyDepositText3.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText3.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText3.setObjectName(_fromUtf8("MyDepositText3"))
        self.TimeLimitText3 = myQLabel(self.page11)
        self.TimeLimitText3.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText3.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText3.setObjectName(_fromUtf8("TimeLimitText3"))
        self.RequestInterviewCheck = myQCheckBox(self.page11)
        self.RequestInterviewCheck.setGeometry(QtCore.QRect(0, 370, 261, 31))
        # self.RequestInterviewCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.RequestInterviewCheck.setObjectName(_fromUtf8("RequestInterviewCheck"))
        self.RequireResumeCheck = myQCheckBox(self.page11)
        self.RequireResumeCheck.setGeometry(QtCore.QRect(0, 330, 261, 31))
        # self.RequireResumeCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.RequireResumeCheck.setObjectName(_fromUtf8("RequireResumeCheck"))
        self.Pages.addWidget(self.page11)
        self.page12 = QtWidgets.QWidget()
        self.page12.setObjectName(_fromUtf8("page12"))
        self.AcceptOneCheck = myQCheckBox(self.page12)
        self.AcceptOneCheck.setGeometry(QtCore.QRect(400, 230, 280, 31))
        # self.AcceptOneCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AcceptOneCheck.setObjectName(_fromUtf8("AcceptOneCheck"))
        self.FindJobText = myQLabel(self.page12)
        self.FindJobText.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.FindJobText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.FindJobText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.FindJobText.setObjectName(_fromUtf8("FindJobText"))
        self.line_6 = QtWidgets.QFrame(self.page12)
        self.line_6.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.SaveContinue4 = QtWidgets.QPushButton(self.page12)
        self.SaveContinue4.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue4.setObjectName(_fromUtf8("SaveContinue4"))
        self.LinkResumeText = myQLabel(self.page12)
        self.LinkResumeText.setGeometry(QtCore.QRect(0, 290, 151, 31))
        # self.LinkResumeText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.LinkResumeText.setObjectName(_fromUtf8("LinkResumeText"))
        self.AcceptTempCheck = myQCheckBox(self.page12)
        self.AcceptTempCheck.setGeometry(QtCore.QRect(400, 270, 280, 31))
        # self.AcceptTempCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AcceptTempCheck.setObjectName(_fromUtf8("AcceptTempCheck"))
        self.Notes4 = myQLabel(self.page12)
        self.Notes4.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.Notes4.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Notes4.setObjectName(_fromUtf8("Notes4"))
        self.DescriptionBox2_2 = QtWidgets.QTextEdit(self.page12)
        self.DescriptionBox2_2.setGeometry(QtCore.QRect(0, 120, 671, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DescriptionBox2_2.sizePolicy().hasHeightForWidth())
        self.DescriptionBox2_2.setSizePolicy(sizePolicy)
        self.DescriptionBox2_2.setMinimumSize(QtCore.QSize(0, 89))
        self.DescriptionBox2_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.DescriptionBox2_2.setStyleSheet(
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
        self.DescriptionBox2_2.setObjectName(_fromUtf8("DescriptionBox2_2"))
        self.DepositSettings4 = QtWidgets.QComboBox(self.page12)
        self.DepositSettings4.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings4.setObjectName(_fromUtf8("DepositSettings4"))
        self.DepositSettings4.addItem(_fromUtf8(""))
        self.DepositSettings4.addItem(_fromUtf8(""))
        self.DepositSettings4.addItem(_fromUtf8(""))
        self.ExplainFind = QtWidgets.QPushButton(self.page12)
        self.ExplainFind.setGeometry(QtCore.QRect(630, 10, 40, 40))
        self.ExplainFind.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainFind.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainFind.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainFind.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.ExplainFind.setIconSize(QtCore.QSize(20, 20))
        self.ExplainFind.setObjectName(_fromUtf8("ExplainFind"))
        self.LinkResumeBox = QtWidgets.QLineEdit(self.page12)
        self.LinkResumeBox.setGeometry(QtCore.QRect(150, 290, 211, 31))
        self.LinkResumeBox.setStyleSheet(
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
        self.LinkResumeBox.setText(_fromUtf8(""))
        self.LinkResumeBox.setObjectName(_fromUtf8("LinkResumeBox"))
        self.NotesBox4 = QtWidgets.QTextEdit(self.page12)
        self.NotesBox4.setGeometry(QtCore.QRect(400, 519, 271, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox4.sizePolicy().hasHeightForWidth())
        self.NotesBox4.setSizePolicy(sizePolicy)
        self.NotesBox4.setMinimumSize(QtCore.QSize(0, 50))
        self.NotesBox4.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox4.setStyleSheet(
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
        self.NotesBox4.setObjectName(_fromUtf8("NotesBox4"))
        self.JobTitleBox2 = QtWidgets.QLineEdit(self.page12)
        self.JobTitleBox2.setGeometry(QtCore.QRect(90, 50, 581, 31))
        self.JobTitleBox2.setStyleSheet(
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
        self.JobTitleBox2.setText(_fromUtf8(""))
        self.JobTitleBox2.setObjectName(_fromUtf8("JobTitleBox2"))
        self.JobTitle2 = myQLabel(self.page12)
        self.JobTitle2.setGeometry(QtCore.QRect(0, 50, 81, 31))
        # self.JobTitle2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.JobTitle2.setObjectName(_fromUtf8("JobTitle2"))
        self.Description2 = myQLabel(self.page12)
        self.Description2.setGeometry(QtCore.QRect(0, 90, 191, 31))
        # self.Description2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Description2.setObjectName(_fromUtf8("Description2"))
        self.AcceptFullCheck = myQCheckBox(self.page12)
        self.AcceptFullCheck.setGeometry(QtCore.QRect(400, 310, 280, 31))
        # self.AcceptFullCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AcceptFullCheck.setObjectName(_fromUtf8("AcceptFullCheck"))
        self.AcceptInterviewCheck = myQCheckBox(self.page12)
        self.AcceptInterviewCheck.setGeometry(QtCore.QRect(400, 350, 280, 31))
        # self.AcceptInterviewCheck.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AcceptInterviewCheck.setObjectName(_fromUtf8("AcceptInterviewCheck"))
        self.uploadfree = myQLabel(self.page12)
        self.uploadfree.setGeometry(QtCore.QRect(0, 330, 131, 21))
        self.uploadfree.setObjectName(_fromUtf8("uploadfree"))
        self.sendspacelink = QtWidgets.QPushButton(self.page12)
        self.sendspacelink.setGeometry(QtCore.QRect(130, 330, 111, 21))
        self.sendspacelink.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.sendspacelink.setObjectName(_fromUtf8("sendspacelink"))
        sendspacefont = QtGui.QFont()
        sendspacefont.setPixelSize(11)
        self.sendspacelink.setFont(sendspacefont)
        self.SupplyAdditional4 = myQCheckBox(self.page12)
        self.SupplyAdditional4.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional4.setObjectName(_fromUtf8("SupplyAdditional4"))
        self.SaveFuture4 = myQCheckBox(self.page12)
        self.SaveFuture4.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture4.setObjectName(_fromUtf8("SaveFuture4"))
        self.ClearForm4 = QtWidgets.QPushButton(self.page12)
        self.ClearForm4.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm4.setObjectName(_fromUtf8("ClearForm4"))
        self.MyDepositText4 = myQLabel(self.page12)
        self.MyDepositText4.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText4.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText4.setObjectName(_fromUtf8("MyDepositText4"))
        self.MyDepositUSD4 = QtWidgets.QComboBox(self.page12)
        self.MyDepositUSD4.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD4.setObjectName(_fromUtf8("MyDepositUSD4"))
        self.MyDepositUSD4.addItem(_fromUtf8(""))
        self.MyDepositUSD4.addItem(_fromUtf8(""))
        self.TimeLimitBox4 = QtWidgets.QLineEdit(self.page12)
        self.TimeLimitBox4.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox4.setStyleSheet(
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
        self.TimeLimitBox4.setObjectName(_fromUtf8("TimeLimitBox4"))
        self.TimeLimitText4 = myQLabel(self.page12)
        self.TimeLimitText4.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText4.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText4.setObjectName(_fromUtf8("TimeLimitText4"))
        self.MyDepositBox4 = QtWidgets.QLineEdit(self.page12)
        self.MyDepositBox4.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox4.setStyleSheet(
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
        self.MyDepositBox4.setText(_fromUtf8(""))
        self.MyDepositBox4.setObjectName(_fromUtf8("MyDepositBox4"))
        self.TimeLimitDays4 = QtWidgets.QComboBox(self.page12)
        self.TimeLimitDays4.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays4.setObjectName(_fromUtf8("TimeLimitDays4"))
        self.TimeLimitDays4.addItem(_fromUtf8(""))
        self.TimeLimitDays4.addItem(_fromUtf8(""))
        self.TheirDepositBox4 = QtWidgets.QLineEdit(self.page12)
        self.TheirDepositBox4.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox4.setStyleSheet(
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
        self.TheirDepositBox4.setText(_fromUtf8(""))
        self.TheirDepositBox4.setObjectName(_fromUtf8("TheirDepositBox4"))
        self.TheirDepositText4 = myQLabel(self.page12)
        self.TheirDepositText4.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText4.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText4.setObjectName(_fromUtf8("TheirDepositText4"))
        self.TheirDepositUSD4 = QtWidgets.QComboBox(self.page12)
        self.TheirDepositUSD4.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD4.setObjectName(_fromUtf8("TheirDepositUSD4"))
        self.TheirDepositUSD4.addItem(_fromUtf8(""))
        self.TheirDepositUSD4.addItem(_fromUtf8(""))
        self.FindRate = QtWidgets.QComboBox(self.page12)
        self.FindRate.setGeometry(QtCore.QRect(270, 240, 91, 31))
        self.FindRate.setObjectName(_fromUtf8("FindRate"))
        self.FindRate.addItem(_fromUtf8(""))
        self.FindRate.addItem(_fromUtf8(""))
        self.FindRate.addItem(_fromUtf8(""))
        self.FindRate.addItem(_fromUtf8(""))
        self.FindAmount = QtWidgets.QLineEdit(self.page12)
        self.FindAmount.setGeometry(QtCore.QRect(0, 240, 201, 31))
        self.FindAmount.setStyleSheet(
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
        self.FindAmount.setText(_fromUtf8(""))
        self.FindAmount.setObjectName(_fromUtf8("FindAmount"))
        self.FindUSD = QtWidgets.QComboBox(self.page12)
        self.FindUSD.setGeometry(QtCore.QRect(210, 240, 51, 31))
        self.FindUSD.setObjectName(_fromUtf8("FindUSD"))
        self.FindUSD.addItem(_fromUtf8(""))
        self.FindUSD.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page12)
        self.page13 = QtWidgets.QWidget()
        self.page13.setObjectName(_fromUtf8("page13"))
        self.SellImageText = myQLabel(self.page13)
        self.SellImageText.setGeometry(QtCore.QRect(0, 180, 71, 31))
        # self.SellImageText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.SellImageText.setObjectName(_fromUtf8("SellImageText"))
        self.NotesBox5 = QtWidgets.QTextEdit(self.page13)
        self.NotesBox5.setGeometry(QtCore.QRect(400, 510, 271, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox5.sizePolicy().hasHeightForWidth())
        self.NotesBox5.setSizePolicy(sizePolicy)
        self.NotesBox5.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox5.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox5.setStyleSheet(
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
        self.NotesBox5.setObjectName(_fromUtf8("NotesBox5"))
        self.CountrySellSelect = QtWidgets.QComboBox(self.page13)
        self.CountrySellSelect.setGeometry(QtCore.QRect(400, 220, 271, 31))
        self.CountrySellSelect.setObjectName(_fromUtf8("CountrySellSelect"))
        self.CountrySellSelect.addItem(_fromUtf8(""))
        self.CountrySellSelect.addItem(_fromUtf8(""))
        self.SellSomethingText = myQLabel(self.page13)
        self.SellSomethingText.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.SellSomethingText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.SellSomethingText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.SellSomethingText.setObjectName(_fromUtf8("SellSomethingText"))
        self.TheirDepositText5 = myQLabel(self.page13)
        self.TheirDepositText5.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText5.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText5.setObjectName(_fromUtf8("TheirDepositText5"))
        self.ExplainSell = QtWidgets.QPushButton(self.page13)
        self.ExplainSell.setGeometry(QtCore.QRect(330, 10, 40, 40))
        self.ExplainSell.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainSell.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainSell.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainSell.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainSell.setIconSize(QtCore.QSize(20, 20))
        self.ExplainSell.setObjectName(_fromUtf8("ExplainSell"))
        self.ShippingSellSelect = QtWidgets.QComboBox(self.page13)
        self.ShippingSellSelect.setGeometry(QtCore.QRect(490, 50, 181, 31))
        self.ShippingSellSelect.setObjectName(_fromUtf8("ShippingSellSelect"))
        self.ShippingSellSelect.addItem(_fromUtf8(""))
        self.ShippingSellSelect.addItem(_fromUtf8(""))
        self.ShippingSellSelect.addItem(_fromUtf8(""))
        self.ShippingSellSelect.addItem(_fromUtf8(""))
        self.ShippingSellSelect.addItem(_fromUtf8(""))
        self.SellImageBox = QtWidgets.QLineEdit(self.page13)
        self.SellImageBox.setGeometry(QtCore.QRect(80, 180, 141, 31))
        self.SellImageBox.setStyleSheet(
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
        self.SellImageBox.setText(_fromUtf8(""))
        self.SellImageBox.setObjectName(_fromUtf8("SellImageBox"))
        self.ShipToTextSell = myQLabel(self.page13)
        self.ShipToTextSell.setGeometry(QtCore.QRect(400, 260, 111, 31))
        # self.ShipToTextSell.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.ShipToTextSell.setObjectName(_fromUtf8("ShipToTextSell"))
        self.TimeLimitBox5 = QtWidgets.QLineEdit(self.page13)
        self.TimeLimitBox5.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox5.setStyleSheet(
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
        self.TimeLimitBox5.setObjectName(_fromUtf8("TimeLimitBox5"))
        self.Notes5 = myQLabel(self.page13)
        self.Notes5.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.Notes5.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Notes5.setObjectName(_fromUtf8("Notes5"))
        self.MyDepositText5 = myQLabel(self.page13)
        self.MyDepositText5.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText5.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText5.setObjectName(_fromUtf8("MyDepositText5"))
        self.DepositSettings5 = QtWidgets.QComboBox(self.page13)
        self.DepositSettings5.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings5.setObjectName(_fromUtf8("DepositSettings5"))
        self.DepositSettings5.addItem(_fromUtf8(""))
        self.DepositSettings5.addItem(_fromUtf8(""))
        self.DepositSettings5.addItem(_fromUtf8(""))
        self.line_8 = QtWidgets.QFrame(self.page13)
        self.line_8.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.TheirDepositBox5 = QtWidgets.QLineEdit(self.page13)
        self.TheirDepositBox5.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox5.setStyleSheet(
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
        self.TheirDepositBox5.setText(_fromUtf8(""))
        self.TheirDepositBox5.setObjectName(_fromUtf8("TheirDepositBox5"))
        self.SaveContinue5 = QtWidgets.QPushButton(self.page13)
        self.SaveContinue5.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue5.setObjectName(_fromUtf8("SaveContinue5"))
        self.MyDepositBox5 = QtWidgets.QLineEdit(self.page13)
        self.MyDepositBox5.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox5.setStyleSheet(
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
        self.MyDepositBox5.setText(_fromUtf8(""))
        self.MyDepositBox5.setObjectName(_fromUtf8("MyDepositBox5"))
        self.TimeLimitText5 = myQLabel(self.page13)
        self.TimeLimitText5.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText5.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText5.setObjectName(_fromUtf8("TimeLimitText5"))
        self.TimeLimitDays5 = QtWidgets.QComboBox(self.page13)
        self.TimeLimitDays5.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays5.setObjectName(_fromUtf8("TimeLimitDays5"))
        self.TimeLimitDays5.addItem(_fromUtf8(""))
        self.TimeLimitDays5.addItem(_fromUtf8(""))
        self.ShipToSellBox = QtWidgets.QLineEdit(self.page13)
        self.ShipToSellBox.setGeometry(QtCore.QRect(510, 260, 161, 31))
        self.ShipToSellBox.setStyleSheet(
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
        self.ShipToSellBox.setObjectName(_fromUtf8("ShipToSellBox"))
        self.ShippingSellText = myQLabel(self.page13)
        self.ShippingSellText.setGeometry(QtCore.QRect(400, 50, 91, 31))
        # self.ShippingSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.ShippingSellText.setObjectName(_fromUtf8("ShippingSellText"))
        self.SellAttachImage = QtWidgets.QPushButton(self.page13)
        self.SellAttachImage.setGeometry(QtCore.QRect(230, 180, 131, 31))
        self.SellAttachImage.setMinimumSize(QtCore.QSize(100, 20))
        self.SellAttachImage.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SellAttachImage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SellAttachImage.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/Images/images/icon_openaccount_active.png")),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.SellAttachImage.setIcon(icon)
        self.SellAttachImage.setIconSize(QtCore.QSize(20, 20))
        self.SellAttachImage.setObjectName(_fromUtf8("SellAttachImage"))
        self.DescriptionSellText = myQLabel(self.page13)
        self.DescriptionSellText.setGeometry(QtCore.QRect(0, 50, 101, 31))
        # self.DescriptionSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.DescriptionSellText.setObjectName(_fromUtf8("DescriptionSellText"))
        self.DescriptionSellBox = QtWidgets.QTextEdit(self.page13)
        self.DescriptionSellBox.setGeometry(QtCore.QRect(0, 80, 361, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DescriptionSellBox.sizePolicy().hasHeightForWidth())
        self.DescriptionSellBox.setSizePolicy(sizePolicy)
        self.DescriptionSellBox.setMinimumSize(QtCore.QSize(0, 89))
        self.DescriptionSellBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.DescriptionSellBox.setStyleSheet(
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
        self.DescriptionSellBox.setObjectName(_fromUtf8("DescriptionSellBox"))
        self.SellQuantity = myQLabel(self.page13)
        self.SellQuantity.setGeometry(QtCore.QRect(150, 220, 71, 31))
        # self.SellQuantity.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.SellQuantity.setObjectName(_fromUtf8("SellQuantity"))
        self.SellQuantityBox = QtWidgets.QLineEdit(self.page13)
        self.SellQuantityBox.setGeometry(QtCore.QRect(230, 220, 131, 31))
        self.SellQuantityBox.setStyleSheet(
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
        self.SellQuantityBox.setText(_fromUtf8(""))
        self.SellQuantityBox.setObjectName(_fromUtf8("SellQuantityBox"))
        self.SellSelect = QtWidgets.QComboBox(self.page13)
        self.SellSelect.setGeometry(QtCore.QRect(0, 220, 131, 31))
        self.SellSelect.setObjectName(_fromUtf8("SellSelect"))
        self.SellSelect.addItem(_fromUtf8(""))
        self.SellSelect.addItem(_fromUtf8(""))
        self.BuyoutSellBox = QtWidgets.QLineEdit(self.page13)
        self.BuyoutSellBox.setGeometry(QtCore.QRect(120, 260, 171, 31))
        self.BuyoutSellBox.setStyleSheet(
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
        self.BuyoutSellBox.setText(_fromUtf8(""))
        self.BuyoutSellBox.setObjectName(_fromUtf8("BuyoutSellBox"))
        self.BuyoutSellText = myQLabel(self.page13)
        self.BuyoutSellText.setGeometry(QtCore.QRect(0, 260, 111, 31))
        # self.BuyoutSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.BuyoutSellText.setObjectName(_fromUtf8("BuyoutSellText"))
        self.BuyoutSellUSD = QtWidgets.QComboBox(self.page13)
        self.BuyoutSellUSD.setGeometry(QtCore.QRect(310, 260, 51, 31))
        self.BuyoutSellUSD.setObjectName(_fromUtf8("BuyoutSellUSD"))
        self.BuyoutSellUSD.addItem(_fromUtf8(""))
        self.BuyoutSellUSD.addItem(_fromUtf8(""))
        self.BidSellBox = QtWidgets.QLineEdit(self.page13)
        self.BidSellBox.setGeometry(QtCore.QRect(120, 310, 171, 31))
        self.BidSellBox.setStyleSheet(
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
        self.BidSellBox.setText(_fromUtf8(""))
        self.BidSellBox.setObjectName(_fromUtf8("BidSellBox"))
        self.BidSellUSD = QtWidgets.QComboBox(self.page13)
        self.BidSellUSD.setGeometry(QtCore.QRect(310, 310, 51, 31))
        self.BidSellUSD.setObjectName(_fromUtf8("BidSellUSD"))
        self.BidSellUSD.addItem(_fromUtf8(""))
        self.BidSellUSD.addItem(_fromUtf8(""))
        self.BidSellText = myQLabel(self.page13)
        self.BidSellText.setGeometry(QtCore.QRect(0, 310, 101, 31))
        # self.BidSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.BidSellText.setObjectName(_fromUtf8("BidSellText"))
        self.DurationSellDays = QtWidgets.QComboBox(self.page13)
        self.DurationSellDays.setGeometry(QtCore.QRect(310, 360, 51, 31))
        self.DurationSellDays.setObjectName(_fromUtf8("DurationSellDays"))
        self.DurationSellDays.addItem(_fromUtf8(""))
        self.DurationSellBox = QtWidgets.QLineEdit(self.page13)
        self.DurationSellBox.setGeometry(QtCore.QRect(120, 360, 171, 31))
        self.DurationSellBox.setStyleSheet(
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
        self.DurationSellBox.setText(_fromUtf8(""))
        self.DurationSellBox.setObjectName(_fromUtf8("DurationSellBox"))
        self.DurationSellText = myQLabel(self.page13)
        self.DurationSellText.setGeometry(QtCore.QRect(0, 360, 101, 31))
        # self.DurationSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.DurationSellText.setObjectName(_fromUtf8("DurationSellText"))
        self.RateSellBox2 = QtWidgets.QLineEdit(self.page13)
        self.RateSellBox2.setGeometry(QtCore.QRect(460, 100, 141, 31))
        self.RateSellBox2.setStyleSheet(
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
        self.RateSellBox2.setText(_fromUtf8(""))
        self.RateSellBox2.setObjectName(_fromUtf8("RateSellBox2"))
        self.RateSellUSD = QtWidgets.QComboBox(self.page13)
        self.RateSellUSD.setGeometry(QtCore.QRect(620, 100, 51, 31))
        self.RateSellUSD.setObjectName(_fromUtf8("RateSellUSD"))
        self.RateSellUSD.addItem(_fromUtf8(""))
        self.RateSellUSD.addItem(_fromUtf8(""))
        self.RateSellText = myQLabel(self.page13)
        self.RateSellText.setGeometry(QtCore.QRect(400, 100, 51, 31))
        # self.RateSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.RateSellText.setObjectName(_fromUtf8("RateSellText"))
        self.WeightSellBox = QtWidgets.QLineEdit(self.page13)
        self.WeightSellBox.setGeometry(QtCore.QRect(480, 150, 101, 31))
        self.WeightSellBox.setStyleSheet(
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
        self.WeightSellBox.setText(_fromUtf8(""))
        self.WeightSellBox.setObjectName(_fromUtf8("WeightSellBox"))
        self.WeightSellText = myQLabel(self.page13)
        self.WeightSellText.setGeometry(QtCore.QRect(400, 150, 71, 31))
        # self.WeightSellText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.WeightSellText.setObjectName(_fromUtf8("WeightSellText"))
        self.WeightSellSelect = QtWidgets.QComboBox(self.page13)
        self.WeightSellSelect.setGeometry(QtCore.QRect(600, 150, 71, 31))
        self.WeightSellSelect.setObjectName(_fromUtf8("WeightSellSelect"))
        self.WeightSellSelect.addItem(_fromUtf8(""))
        self.WeightSellSelect.addItem(_fromUtf8(""))
        self.SupplyAdditional5 = myQCheckBox(self.page13)
        self.SupplyAdditional5.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional5.setObjectName(_fromUtf8("SupplyAdditional5"))
        self.SaveFuture5 = myQCheckBox(self.page13)
        self.SaveFuture5.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture5.setObjectName(_fromUtf8("SaveFuture5"))
        self.ClearForm5 = QtWidgets.QPushButton(self.page13)
        self.ClearForm5.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm5.setObjectName(_fromUtf8("ClearForm5"))
        self.MyDepositUSD5 = QtWidgets.QComboBox(self.page13)
        self.MyDepositUSD5.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD5.setObjectName(_fromUtf8("MyDepositUSD5"))
        self.MyDepositUSD5.addItem(_fromUtf8(""))
        self.MyDepositUSD5.addItem(_fromUtf8(""))
        self.TheirDepositUSD5 = QtWidgets.QComboBox(self.page13)
        self.TheirDepositUSD5.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD5.setObjectName(_fromUtf8("TheirDepositUSD5"))
        self.TheirDepositUSD5.addItem(_fromUtf8(""))
        self.TheirDepositUSD5.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page13)
        self.page14 = QtWidgets.QWidget()
        self.page14.setObjectName(_fromUtf8("page14"))
        self.ShippingBuyText = myQLabel(self.page14)
        self.ShippingBuyText.setGeometry(QtCore.QRect(400, 50, 91, 31))
        # self.ShippingBuyText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.ShippingBuyText.setObjectName(_fromUtf8("ShippingBuyText"))
        self.SaveContinue6 = QtWidgets.QPushButton(self.page14)
        self.SaveContinue6.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue6.setObjectName(_fromUtf8("SaveContinue6"))
        self.DurationBuyDays = QtWidgets.QComboBox(self.page14)
        self.DurationBuyDays.setGeometry(QtCore.QRect(310, 360, 51, 31))
        self.DurationBuyDays.setObjectName(_fromUtf8("DurationBuyDays"))
        self.DurationBuyDays.addItem(_fromUtf8(""))
        self.TheirDepositBox6 = QtWidgets.QLineEdit(self.page14)
        self.TheirDepositBox6.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox6.setStyleSheet(
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
        self.TheirDepositBox6.setText(_fromUtf8(""))
        self.TheirDepositBox6.setObjectName(_fromUtf8("TheirDepositBox6"))
        self.BuySelect = QtWidgets.QComboBox(self.page14)
        self.BuySelect.setGeometry(QtCore.QRect(0, 220, 131, 31))
        self.BuySelect.setObjectName(_fromUtf8("BuySelect"))
        self.BuySelect.addItem(_fromUtf8(""))
        self.BuySelect.addItem(_fromUtf8(""))
        self.MyDepositBox6 = QtWidgets.QLineEdit(self.page14)
        self.MyDepositBox6.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox6.setStyleSheet(
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
        self.MyDepositBox6.setText(_fromUtf8(""))
        self.MyDepositBox6.setObjectName(_fromUtf8("MyDepositBox6"))
        self.TimeLimitBox6 = QtWidgets.QLineEdit(self.page14)
        self.TimeLimitBox6.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox6.setStyleSheet(
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
        self.TimeLimitBox6.setObjectName(_fromUtf8("TimeLimitBox6"))
        self.BidBuyText = myQLabel(self.page14)
        self.BidBuyText.setGeometry(QtCore.QRect(0, 310, 101, 31))
        # self.BidBuyText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.BidBuyText.setObjectName(_fromUtf8("BidBuyText"))
        self.DescriptionBuyBox = QtWidgets.QTextEdit(self.page14)
        self.DescriptionBuyBox.setGeometry(QtCore.QRect(0, 80, 361, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DescriptionBuyBox.sizePolicy().hasHeightForWidth())
        self.DescriptionBuyBox.setSizePolicy(sizePolicy)
        self.DescriptionBuyBox.setMinimumSize(QtCore.QSize(0, 89))
        self.DescriptionBuyBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.DescriptionBuyBox.setStyleSheet(
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
        self.DescriptionBuyBox.setObjectName(_fromUtf8("DescriptionBuyBox"))
        self.BidBuyBox = QtWidgets.QLineEdit(self.page14)
        self.BidBuyBox.setGeometry(QtCore.QRect(120, 310, 171, 31))
        self.BidBuyBox.setStyleSheet(
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
        self.BidBuyBox.setText(_fromUtf8(""))
        self.BidBuyBox.setObjectName(_fromUtf8("BidBuyBox"))
        self.BuyImageText = myQLabel(self.page14)
        self.BuyImageText.setGeometry(QtCore.QRect(0, 180, 71, 31))
        # self.BuyImageText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.BuyImageText.setObjectName(_fromUtf8("BuyImageText"))
        self.BuyText = myQLabel(self.page14)
        self.BuyText.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.BuyText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.BuyText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.BuyText.setObjectName(_fromUtf8("BuyText"))
        self.ShipToBuyBox = QtWidgets.QLineEdit(self.page14)
        self.ShipToBuyBox.setGeometry(QtCore.QRect(540, 260, 131, 31))
        self.ShipToBuyBox.setStyleSheet(
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
        self.ShipToBuyBox.setObjectName(_fromUtf8("ShipToBuyBox"))
        self.DescriptionBuy = myQLabel(self.page14)
        self.DescriptionBuy.setGeometry(QtCore.QRect(0, 50, 101, 31))
        # self.DescriptionBuy.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.DescriptionBuy.setObjectName(_fromUtf8("DescriptionBuy"))
        self.BuyAttachImage = QtWidgets.QPushButton(self.page14)
        self.BuyAttachImage.setGeometry(QtCore.QRect(230, 180, 131, 31))
        self.BuyAttachImage.setMinimumSize(QtCore.QSize(100, 20))
        self.BuyAttachImage.setMaximumSize(QtCore.QSize(16777215, 40))
        self.BuyAttachImage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BuyAttachImage.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.BuyAttachImage.setIcon(icon)
        self.BuyAttachImage.setIconSize(QtCore.QSize(20, 20))
        self.BuyAttachImage.setObjectName(_fromUtf8("BuyAttachImage"))
        self.NotesBox6 = QtWidgets.QTextEdit(self.page14)
        self.NotesBox6.setGeometry(QtCore.QRect(400, 510, 271, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox6.sizePolicy().hasHeightForWidth())
        self.NotesBox6.setSizePolicy(sizePolicy)
        self.NotesBox6.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox6.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox6.setStyleSheet(
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
        self.NotesBox6.setObjectName(_fromUtf8("NotesBox6"))
        self.DurationBuyBox = QtWidgets.QLineEdit(self.page14)
        self.DurationBuyBox.setGeometry(QtCore.QRect(120, 360, 171, 31))
        self.DurationBuyBox.setStyleSheet(
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
        self.DurationBuyBox.setText(_fromUtf8(""))
        self.DurationBuyBox.setObjectName(_fromUtf8("DurationBuyBox"))
        self.MyDepositText6 = myQLabel(self.page14)
        self.MyDepositText6.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText6.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText6.setObjectName(_fromUtf8("MyDepositText6"))
        self.line_19 = QtWidgets.QFrame(self.page14)
        self.line_19.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.ExplainBuy = QtWidgets.QPushButton(self.page14)
        self.ExplainBuy.setGeometry(QtCore.QRect(330, 10, 40, 40))
        self.ExplainBuy.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainBuy.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainBuy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainBuy.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainBuy.setIconSize(QtCore.QSize(20, 20))
        self.ExplainBuy.setObjectName(_fromUtf8("ExplainBuy"))
        self.TimeLimitText6 = myQLabel(self.page14)
        self.TimeLimitText6.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText6.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText6.setObjectName(_fromUtf8("TimeLimitText6"))
        self.BuyoutBuyBox = QtWidgets.QLineEdit(self.page14)
        self.BuyoutBuyBox.setGeometry(QtCore.QRect(120, 260, 171, 31))
        self.BuyoutBuyBox.setStyleSheet(
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
        self.BuyoutBuyBox.setText(_fromUtf8(""))
        self.BuyoutBuyBox.setObjectName(_fromUtf8("BuyoutBuyBox"))
        self.TimeLimitDays6 = QtWidgets.QComboBox(self.page14)
        self.TimeLimitDays6.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays6.setObjectName(_fromUtf8("TimeLimitDays6"))
        self.TimeLimitDays6.addItem(_fromUtf8(""))
        self.TimeLimitDays6.addItem(_fromUtf8(""))
        self.ShipCountryBuy = QtWidgets.QComboBox(self.page14)
        self.ShipCountryBuy.setGeometry(QtCore.QRect(400, 220, 271, 31))
        self.ShipCountryBuy.setObjectName(_fromUtf8("ShipCountryBuy"))
        self.ShipCountryBuy.addItem(_fromUtf8(""))
        self.ShipCountryBuy.addItem(_fromUtf8(""))
        self.TheirDepositText6 = myQLabel(self.page14)
        self.TheirDepositText6.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText6.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText6.setObjectName(_fromUtf8("TheirDepositText6"))
        self.BuyoutBuyUSD = QtWidgets.QComboBox(self.page14)
        self.BuyoutBuyUSD.setGeometry(QtCore.QRect(310, 260, 51, 31))
        self.BuyoutBuyUSD.setObjectName(_fromUtf8("BuyoutBuyUSD"))
        self.BuyoutBuyUSD.addItem(_fromUtf8(""))
        self.BuyoutBuyUSD.addItem(_fromUtf8(""))
        self.DurationBuyText = myQLabel(self.page14)
        self.DurationBuyText.setGeometry(QtCore.QRect(0, 360, 101, 31))
        # self.DurationBuyText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.DurationBuyText.setObjectName(_fromUtf8("DurationBuyText"))
        self.BidBuyUSD = QtWidgets.QComboBox(self.page14)
        self.BidBuyUSD.setGeometry(QtCore.QRect(310, 310, 51, 31))
        self.BidBuyUSD.setObjectName(_fromUtf8("BidBuyUSD"))
        self.BidBuyUSD.addItem(_fromUtf8(""))
        self.BidBuyUSD.addItem(_fromUtf8(""))
        self.BuyoutBuyText = myQLabel(self.page14)
        self.BuyoutBuyText.setGeometry(QtCore.QRect(0, 260, 111, 31))
        # self.BuyoutBuyText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.BuyoutBuyText.setObjectName(_fromUtf8("BuyoutBuyText"))
        self.BuyImageBox = QtWidgets.QLineEdit(self.page14)
        self.BuyImageBox.setGeometry(QtCore.QRect(80, 180, 141, 31))
        self.BuyImageBox.setStyleSheet(
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
        self.BuyImageBox.setText(_fromUtf8(""))
        self.BuyImageBox.setObjectName(_fromUtf8("BuyImageBox"))
        self.Notes6 = myQLabel(self.page14)
        self.Notes6.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.Notes6.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Notes6.setObjectName(_fromUtf8("Notes6"))
        self.DepositSettings6 = QtWidgets.QComboBox(self.page14)
        self.DepositSettings6.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings6.setObjectName(_fromUtf8("DepositSettings6"))
        self.DepositSettings6.addItem(_fromUtf8(""))
        self.DepositSettings6.addItem(_fromUtf8(""))
        self.DepositSettings6.addItem(_fromUtf8(""))
        self.DepositSettings6.addItem(_fromUtf8(""))
        self.ShipToBuyText = myQLabel(self.page14)
        self.ShipToBuyText.setGeometry(QtCore.QRect(400, 260, 141, 31))
        # self.ShipToBuyText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.ShipToBuyText.setObjectName(_fromUtf8("ShipToBuyText"))
        self.LocalPickupBuy = myQCheckBox(self.page14)
        self.LocalPickupBuy.setGeometry(QtCore.QRect(400, 90, 271, 17))
        self.LocalPickupBuy.setObjectName(_fromUtf8("LocalPickupBuy"))
        self.ShippingCityBuy = myQCheckBox(self.page14)
        self.ShippingCityBuy.setGeometry(QtCore.QRect(400, 120, 271, 17))
        self.ShippingCityBuy.setObjectName(_fromUtf8("ShippingCityBuy"))
        self.ShippingCityBuy.hide()
        self.SupplyAdditional6 = myQCheckBox(self.page14)
        self.SupplyAdditional6.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional6.setObjectName(_fromUtf8("SupplyAdditional6"))
        self.SaveFuture6 = myQCheckBox(self.page14)
        self.SaveFuture6.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture6.setObjectName(_fromUtf8("SaveFuture6"))
        self.ClearForm6 = QtWidgets.QPushButton(self.page14)
        self.ClearForm6.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm6.setObjectName(_fromUtf8("ClearForm6"))
        self.MyDepositUSD6 = QtWidgets.QComboBox(self.page14)
        self.MyDepositUSD6.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD6.setObjectName(_fromUtf8("MyDepositUSD6"))
        self.MyDepositUSD6.addItem(_fromUtf8(""))
        self.MyDepositUSD6.addItem(_fromUtf8(""))
        self.TheirDepositUSD6 = QtWidgets.QComboBox(self.page14)
        self.TheirDepositUSD6.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD6.setObjectName(_fromUtf8("TheirDepositUSD6"))
        self.TheirDepositUSD6.addItem(_fromUtf8(""))
        self.TheirDepositUSD6.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page14)
        self.page15 = QtWidgets.QWidget()
        self.page15.setObjectName(_fromUtf8("page15"))
        self.TimeLimitDays7 = QtWidgets.QComboBox(self.page15)
        self.TimeLimitDays7.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays7.setObjectName(_fromUtf8("TimeLimitDays7"))
        self.TimeLimitDays7.addItem(_fromUtf8(""))
        self.TimeLimitDays7.addItem(_fromUtf8(""))
        self.MyDepositBox7 = QtWidgets.QLineEdit(self.page15)
        self.MyDepositBox7.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox7.setStyleSheet(
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
        self.MyDepositBox7.setText(_fromUtf8(""))
        self.MyDepositBox7.setObjectName(_fromUtf8("MyDepositBox7"))
        self.SupplyText = myQLabel(self.page15)
        self.SupplyText.setGeometry(QtCore.QRect(0, 50, 331, 31))
        # self.SupplyText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.SupplyText.setObjectName(_fromUtf8("SupplyText"))
        self.SaveContinue7 = QtWidgets.QPushButton(self.page15)
        self.SaveContinue7.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue7.setObjectName(_fromUtf8("SaveContinue7"))
        self.MyDepositText7 = myQLabel(self.page15)
        self.MyDepositText7.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText7.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText7.setObjectName(_fromUtf8("MyDepositText7"))
        self.BarterText = myQLabel(self.page15)
        self.BarterText.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.BarterText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.BarterText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.BarterText.setObjectName(_fromUtf8("BarterText"))
        self.TheirDepositText7 = myQLabel(self.page15)
        self.TheirDepositText7.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText7.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText7.setObjectName(_fromUtf8("TheirDepositText7"))
        self.TheirDepositBox7 = QtWidgets.QLineEdit(self.page15)
        self.TheirDepositBox7.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox7.setStyleSheet(
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
        self.TheirDepositBox7.setText(_fromUtf8(""))
        self.TheirDepositBox7.setObjectName(_fromUtf8("TheirDepositBox7"))
        self.ExplainBarter = QtWidgets.QPushButton(self.page15)
        self.ExplainBarter.setGeometry(QtCore.QRect(290, 10, 40, 40))
        self.ExplainBarter.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainBarter.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainBarter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainBarter.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainBarter.setIconSize(QtCore.QSize(20, 20))
        self.ExplainBarter.setObjectName(_fromUtf8("ExplainBarter"))
        self.TimeLimitText7 = myQLabel(self.page15)
        self.TimeLimitText7.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText7.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText7.setObjectName(_fromUtf8("TimeLimitText7"))
        self.NotesBox7 = QtWidgets.QTextEdit(self.page15)
        self.NotesBox7.setGeometry(QtCore.QRect(400, 510, 271, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox7.sizePolicy().hasHeightForWidth())
        self.NotesBox7.setSizePolicy(sizePolicy)
        self.NotesBox7.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox7.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox7.setStyleSheet(
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
        self.NotesBox7.setObjectName(_fromUtf8("NotesBox7"))
        self.line_20 = QtWidgets.QFrame(self.page15)
        self.line_20.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_20.setObjectName(_fromUtf8("line_20"))
        self.DepositSettings7 = QtWidgets.QComboBox(self.page15)
        self.DepositSettings7.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings7.setObjectName(_fromUtf8("DepositSettings7"))
        self.DepositSettings7.addItem(_fromUtf8(""))
        self.DepositSettings7.addItem(_fromUtf8(""))
        self.Notes7 = myQLabel(self.page15)
        self.Notes7.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.Notes7.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Notes7.setObjectName(_fromUtf8("Notes7"))
        self.TimeLimitBox7 = QtWidgets.QLineEdit(self.page15)
        self.TimeLimitBox7.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox7.setStyleSheet(
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
        self.TimeLimitBox7.setObjectName(_fromUtf8("TimeLimitBox7"))
        self.DemandText = myQLabel(self.page15)
        self.DemandText.setGeometry(QtCore.QRect(340, 50, 331, 31))
        # self.DemandText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.DemandText.setObjectName(_fromUtf8("DemandText"))
        self.SupplyBox = QtWidgets.QListWidget(self.page15)
        self.SupplyBox.setGeometry(QtCore.QRect(0, 80, 331, 231))
        self.SupplyBox.setObjectName(_fromUtf8("SupplyBox"))
        self.DemandBox = QtWidgets.QListWidget(self.page15)
        self.DemandBox.setGeometry(QtCore.QRect(340, 80, 331, 231))
        self.DemandBox.setObjectName(_fromUtf8("DemandBox"))
        self.AddItemSupply = QtWidgets.QPushButton(self.page15)
        self.AddItemSupply.setGeometry(QtCore.QRect(0, 310, 71, 31))
        self.AddItemSupply.setObjectName(_fromUtf8("AddItemSupply"))
        self.AddItemDemand = QtWidgets.QPushButton(self.page15)
        self.AddItemDemand.setGeometry(QtCore.QRect(340, 310, 71, 31))
        self.AddItemDemand.setObjectName(_fromUtf8("AddItemDemand"))
        self.SupplyAdditional7 = myQCheckBox(self.page15)
        self.SupplyAdditional7.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional7.setObjectName(_fromUtf8("SupplyAdditional7"))
        self.ClearForm7 = QtWidgets.QPushButton(self.page15)
        self.ClearForm7.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm7.setObjectName(_fromUtf8("ClearForm7"))
        self.SaveFuture7 = myQCheckBox(self.page15)
        self.SaveFuture7.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture7.setObjectName(_fromUtf8("SaveFuture7"))
        self.OfferNotInList = myQCheckBox(self.page15)
        self.OfferNotInList.setGeometry(QtCore.QRect(420, 320, 221, 17))
        self.OfferNotInList.setObjectName(_fromUtf8("OfferNotInList"))
        self.BuyMultiple = myQCheckBox(self.page15)
        self.BuyMultiple.setGeometry(QtCore.QRect(80, 320, 211, 17))
        self.BuyMultiple.setObjectName(_fromUtf8("BuyMultiple"))
        self.RequestAll = QtWidgets.QComboBox(self.page15)
        self.RequestAll.setGeometry(QtCore.QRect(0, 360, 211, 31))
        self.RequestAll.setObjectName(_fromUtf8("RequestAll"))
        self.RequestAll.addItem(_fromUtf8(""))
        self.RequestAll.addItem(_fromUtf8(""))
        self.MaxItemsBox = QtWidgets.QLineEdit(self.page15)
        self.MaxItemsBox.setGeometry(QtCore.QRect(460, 360, 71, 31))
        self.MaxItemsBox.setStyleSheet(
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
        self.MaxItemsBox.setText(_fromUtf8(""))
        self.MaxItemsBox.setObjectName(_fromUtf8("MaxItemsBox"))
        self.MaxItems = myQLabel(self.page15)
        self.MaxItems.setGeometry(QtCore.QRect(220, 360, 241, 31))
        # self.MaxItems.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MaxItems.setObjectName(_fromUtf8("MaxItems"))
        self.MaxItems.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MyDepositUSD7 = QtWidgets.QComboBox(self.page15)
        self.MyDepositUSD7.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD7.setObjectName(_fromUtf8("MyDepositUSD7"))
        self.MyDepositUSD7.addItem(_fromUtf8(""))
        self.MyDepositUSD7.addItem(_fromUtf8(""))
        self.TheirDepositUSD7 = QtWidgets.QComboBox(self.page15)
        self.TheirDepositUSD7.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD7.setObjectName(_fromUtf8("TheirDepositUSD7"))
        self.TheirDepositUSD7.addItem(_fromUtf8(""))
        self.TheirDepositUSD7.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page15)
        self.page16 = QtWidgets.QWidget()
        self.page16.setObjectName(_fromUtf8("page16"))
        self.AddLinkImagesBox = QtWidgets.QLineEdit(self.page16)
        self.AddLinkImagesBox.setGeometry(QtCore.QRect(190, 320, 201, 31))
        self.AddLinkImagesBox.setStyleSheet(
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
        self.AddLinkImagesBox.setText(_fromUtf8(""))
        self.AddLinkImagesBox.setObjectName(_fromUtf8("AddLinkImagesBox"))
        self.EstValueText = myQLabel(self.page16)
        self.EstValueText.setGeometry(QtCore.QRect(0, 380, 391, 31))
        # self.EstValueText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.EstValueText.setObjectName(_fromUtf8("EstValueText"))
        self.AddBrowserText = QtWidgets.QTextBrowser(self.page16)
        self.AddBrowserText.setGeometry(QtCore.QRect(0, 240, 391, 71))
        self.AddBrowserText.setObjectName(_fromUtf8("AddBrowserText"))
        self.EstValueUSD = QtWidgets.QComboBox(self.page16)
        self.EstValueUSD.setGeometry(QtCore.QRect(220, 410, 51, 31))
        self.EstValueUSD.setObjectName(_fromUtf8("EstValueUSD"))
        self.EstValueUSD.addItem(_fromUtf8(""))
        self.EstValueUSD.addItem(_fromUtf8(""))
        self.AddDescriptionBox = QtWidgets.QTextEdit(self.page16)
        self.AddDescriptionBox.setGeometry(QtCore.QRect(0, 150, 391, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.AddDescriptionBox.sizePolicy().hasHeightForWidth())
        self.AddDescriptionBox.setSizePolicy(sizePolicy)
        self.AddDescriptionBox.setMinimumSize(QtCore.QSize(0, 89))
        self.AddDescriptionBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.AddDescriptionBox.setStyleSheet(
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
        self.AddDescriptionBox.setObjectName(_fromUtf8("AddDescriptionBox"))
        self.EstValueBox = QtWidgets.QLineEdit(self.page16)
        self.EstValueBox.setGeometry(QtCore.QRect(0, 410, 211, 31))
        self.EstValueBox.setStyleSheet(
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
        self.EstValueBox.setText(_fromUtf8(""))
        self.EstValueBox.setObjectName(_fromUtf8("EstValueBox"))
        self.AddItemToList = QtWidgets.QPushButton(self.page16)
        self.AddItemToList.setGeometry(QtCore.QRect(0, 640, 71, 31))
        self.AddItemToList.setObjectName(_fromUtf8("AddItemToList"))
        self.AddTitleBox = QtWidgets.QLineEdit(self.page16)
        self.AddTitleBox.setGeometry(QtCore.QRect(0, 80, 391, 31))
        self.AddTitleBox.setStyleSheet(
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
        self.AddTitleBox.setText(_fromUtf8(""))
        self.AddTitleBox.setObjectName(_fromUtf8("AddTitleBox"))
        self.AddDescriptionText = myQLabel(self.page16)
        self.AddDescriptionText.setGeometry(QtCore.QRect(0, 120, 101, 31))
        # self.AddDescriptionText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AddDescriptionText.setObjectName(_fromUtf8("AddDescriptionText"))
        self.AddTitleText = myQLabel(self.page16)
        self.AddTitleText.setGeometry(QtCore.QRect(0, 50, 51, 31))
        # self.AddTitleText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AddTitleText.setObjectName(_fromUtf8("AddTitleText"))
        self.imgurlink = QtWidgets.QPushButton(self.page16)
        self.imgurlink.setGeometry(QtCore.QRect(170, 350, 111, 21))
        self.imgurlink.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.imgurlink.setObjectName(_fromUtf8("imgurlink"))
        imgurfont = QtGui.QFont()
        imgurfont.setPixelSize(11)
        self.imgurlink.setFont(imgurfont)
        self.AddLinkimages = myQLabel(self.page16)
        self.AddLinkimages.setGeometry(QtCore.QRect(0, 320, 181, 31))
        # self.AddLinkimages.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AddLinkimages.setObjectName(_fromUtf8("AddLinkimages"))
        self.RemoveItemFromList = QtWidgets.QPushButton(self.page16)
        self.RemoveItemFromList.setGeometry(QtCore.QRect(90, 640, 91, 31))
        self.RemoveItemFromList.setObjectName(_fromUtf8("RemoveItemFromList"))
        self.uploadimages = myQLabel(self.page16)
        self.uploadimages.setGeometry(QtCore.QRect(0, 350, 171, 21))
        self.uploadimages.setObjectName(_fromUtf8("uploadimages"))
        self.AdditemText = myQLabel(self.page16)
        self.AdditemText.setGeometry(QtCore.QRect(0, 10, 221, 31))
        # self.AdditemText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AdditemText.setObjectName(_fromUtf8("AdditemText"))
        self.AddShippingSelect = QtWidgets.QComboBox(self.page16)
        self.AddShippingSelect.setGeometry(QtCore.QRect(410, 150, 271, 31))
        self.AddShippingSelect.setObjectName(_fromUtf8("AddShippingSelect"))
        self.AddShippingSelect.addItem(_fromUtf8(""))
        self.AddShippingSelect.addItem(_fromUtf8(""))
        self.AddShipToBox = QtWidgets.QLineEdit(self.page16)
        self.AddShipToBox.setGeometry(QtCore.QRect(410, 230, 271, 31))
        self.AddShipToBox.setStyleSheet(
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
        self.AddShipToBox.setObjectName(_fromUtf8("AddShipToBox"))
        self.AddMeetupCheck = myQCheckBox(self.page16)
        self.AddMeetupCheck.setGeometry(QtCore.QRect(410, 280, 201, 17))
        self.AddMeetupCheck.setObjectName(_fromUtf8("AddMeetupCheck"))
        self.AddShipToText = myQLabel(self.page16)
        self.AddShipToText.setGeometry(QtCore.QRect(410, 190, 271, 31))
        # self.AddShipToText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AddShipToText.setObjectName(_fromUtf8("AddShipToText"))
        self.AddShippingText = myQLabel(self.page16)
        self.AddShippingText.setGeometry(QtCore.QRect(410, 120, 271, 31))
        # self.AddShippingText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AddShippingText.setObjectName(_fromUtf8("AddShippingText"))
        self.AddMaximumShipText = myQLabel(self.page16)
        self.AddMaximumShipText.setGeometry(QtCore.QRect(410, 310, 271, 31))
        # self.AddMaximumShipText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AddMaximumShipText.setObjectName(_fromUtf8("AddMaximumShipText"))
        self.AddMaxSizeSelect = QtWidgets.QComboBox(self.page16)
        self.AddMaxSizeSelect.setGeometry(QtCore.QRect(410, 340, 271, 31))
        self.AddMaxSizeSelect.setObjectName(_fromUtf8("AddMaxSizeSelect"))
        self.AddMaxSizeSelect.addItem(_fromUtf8(""))
        self.AddMaxSizeSelect.addItem(_fromUtf8(""))
        self.EstValueSelect = QtWidgets.QComboBox(self.page16)
        self.EstValueSelect.setGeometry(QtCore.QRect(280, 410, 111, 31))
        self.EstValueSelect.setObjectName(_fromUtf8("EstValueSelect"))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.EstValueSelect.addItem(_fromUtf8(""))
        self.AddMaxSizeUSD = QtWidgets.QComboBox(self.page16)
        self.AddMaxSizeUSD.setGeometry(QtCore.QRect(570, 380, 111, 31))
        self.AddMaxSizeUSD.setObjectName(_fromUtf8("AddMaxSizeUSD"))
        self.AddMaxSizeUSD.addItem(_fromUtf8(""))
        self.AddMaxSizeUSD.addItem(_fromUtf8(""))
        self.AddMaxSizeUSD.addItem(_fromUtf8(""))
        self.AddMaxSizeUSD.addItem(_fromUtf8(""))
        self.AddMaxSizeBox = QtWidgets.QLineEdit(self.page16)
        self.AddMaxSizeBox.setGeometry(QtCore.QRect(410, 380, 151, 31))
        self.AddMaxSizeBox.setStyleSheet(
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
        self.AddMaxSizeBox.setText(_fromUtf8(""))
        self.AddMaxSizeBox.setObjectName(_fromUtf8("AddMaxSizeBox"))
        self.AddNoteText = myQLabel(self.page16)
        self.AddNoteText.setGeometry(QtCore.QRect(0, 440, 391, 31))
        self.AddNoteText.setObjectName(_fromUtf8("AddNoteText"))
        self.AddQuantityText = myQLabel(self.page16)
        self.AddQuantityText.setGeometry(QtCore.QRect(0, 550, 81, 31))
        # self.AddQuantityText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.AddQuantityText.setObjectName(_fromUtf8("AddQuantityText"))
        self.SetMinBox = QtWidgets.QLineEdit(self.page16)
        self.SetMinBox.setGeometry(QtCore.QRect(150, 470, 121, 31))
        self.SetMinBox.setStyleSheet(
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
        self.SetMinBox.setText(_fromUtf8(""))
        self.SetMinBox.setObjectName(_fromUtf8("SetMinBox"))
        self.QuantitySelect = QtWidgets.QComboBox(self.page16)
        self.QuantitySelect.setGeometry(QtCore.QRect(280, 550, 111, 31))
        self.QuantitySelect.setObjectName(_fromUtf8("QuantitySelect"))
        self.QuantitySelect.addItem(_fromUtf8(""))
        self.QuantitySelect.addItem(_fromUtf8(""))
        self.QuantitySelect.addItem(_fromUtf8(""))
        self.DepositServiceSelect = QtWidgets.QComboBox(self.page16)
        self.DepositServiceSelect.setGeometry(QtCore.QRect(0, 590, 271, 31))
        self.DepositServiceSelect.setObjectName(_fromUtf8("DepositServiceSelect"))
        self.DepositServiceSelect.addItem(_fromUtf8(""))
        self.DepositServiceSelect.addItem(_fromUtf8(""))
        self.DepositServiceBox = QtWidgets.QLineEdit(self.page16)
        self.DepositServiceBox.setGeometry(QtCore.QRect(290, 590, 81, 31))
        self.DepositServiceBox.setStyleSheet(
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
        self.DepositServiceBox.setText(_fromUtf8(""))
        self.DepositServiceBox.setObjectName(_fromUtf8("DepositServiceBox"))
        self.perc10 = myQLabel(self.page16)
        self.perc10.setGeometry(QtCore.QRect(380, 590, 21, 31))
        # self.perc10.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.perc10.setObjectName(_fromUtf8("perc10"))
        self.AddQuantityBox = QtWidgets.QLineEdit(self.page16)
        self.AddQuantityBox.setGeometry(QtCore.QRect(80, 550, 191, 31))
        self.AddQuantityBox.setStyleSheet(
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
        self.AddQuantityBox.setText(_fromUtf8(""))
        self.AddQuantityBox.setObjectName(_fromUtf8("AddQuantityBox"))
        self.SetMaxBox = QtWidgets.QLineEdit(self.page16)
        self.SetMaxBox.setGeometry(QtCore.QRect(150, 510, 121, 31))
        self.SetMaxBox.setStyleSheet(
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
        self.SetMaxBox.setText(_fromUtf8(""))
        self.SetMaxBox.setObjectName(_fromUtf8("SetMaxBox"))
        self.SetMinUSD = QtWidgets.QComboBox(self.page16)
        self.SetMinUSD.setGeometry(QtCore.QRect(280, 470, 111, 31))
        self.SetMinUSD.setObjectName(_fromUtf8("SetMinUSD"))
        self.SetMinUSD.addItem(_fromUtf8(""))
        self.SetMinUSD.addItem(_fromUtf8(""))
        self.SetMinUSD.addItem(_fromUtf8(""))
        self.SetMaxUSD = QtWidgets.QComboBox(self.page16)
        self.SetMaxUSD.setGeometry(QtCore.QRect(280, 510, 111, 31))
        self.SetMaxUSD.setObjectName(_fromUtf8("SetMaxUSD"))
        self.SetMaxUSD.addItem(_fromUtf8(""))
        self.SetMaxUSD.addItem(_fromUtf8(""))
        self.SetMaxUSD.addItem(_fromUtf8(""))
        self.SetMinSelect = QtWidgets.QComboBox(self.page16)
        self.SetMinSelect.setGeometry(QtCore.QRect(0, 470, 141, 31))
        self.SetMinSelect.setObjectName(_fromUtf8("SetMinSelect"))
        self.SetMinSelect.addItem(_fromUtf8(""))
        self.SetMinSelect.addItem(_fromUtf8(""))
        self.SetMaxSelect = QtWidgets.QComboBox(self.page16)
        self.SetMaxSelect.setGeometry(QtCore.QRect(0, 510, 141, 31))
        self.SetMaxSelect.setObjectName(_fromUtf8("SetMaxSelect"))
        self.SetMaxSelect.addItem(_fromUtf8(""))
        self.SetMaxSelect.addItem(_fromUtf8(""))
        self.Pages.addWidget(self.page16)
        self.page17 = QtWidgets.QWidget()
        self.page17.setObjectName(_fromUtf8("page17"))
        self.TheirSupply = myQLabel(self.page17)
        self.TheirSupply.setGeometry(QtCore.QRect(0, 50, 331, 31))
        # self.TheirSupply.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirSupply.setObjectName(_fromUtf8("TheirSupply"))
        self.TheirDemandBox = QtWidgets.QListWidget(self.page17)
        self.TheirDemandBox.setGeometry(QtCore.QRect(340, 80, 331, 131))
        self.TheirDemandBox.setObjectName(_fromUtf8("TheirDemandBox"))
        self.Notes8 = myQLabel(self.page17)
        self.Notes8.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.Notes8.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Notes8.setObjectName(_fromUtf8("Notes8"))
        self.NotesBox8 = QtWidgets.QTextEdit(self.page17)
        self.NotesBox8.setGeometry(QtCore.QRect(400, 510, 271, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox8.sizePolicy().hasHeightForWidth())
        self.NotesBox8.setSizePolicy(sizePolicy)
        self.NotesBox8.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox8.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox8.setStyleSheet(
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
        self.NotesBox8.setObjectName(_fromUtf8("NotesBox8"))
        self.ExplainBarterOffer = QtWidgets.QPushButton(self.page17)
        self.ExplainBarterOffer.setGeometry(QtCore.QRect(290, 10, 40, 40))
        self.ExplainBarterOffer.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainBarterOffer.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainBarterOffer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainBarterOffer.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainBarterOffer.setIconSize(QtCore.QSize(20, 20))
        self.ExplainBarterOffer.setObjectName(_fromUtf8("ExplainBarterOffer"))
        self.MakeOfferBarter = QtWidgets.QPushButton(self.page17)
        self.MakeOfferBarter.setGeometry(QtCore.QRect(10, 630, 101, 41))
        self.MakeOfferBarter.setObjectName(_fromUtf8("MakeOfferBarter"))
        self.TheirDemand = myQLabel(self.page17)
        self.TheirDemand.setGeometry(QtCore.QRect(340, 50, 331, 31))
        # self.TheirDemand.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDemand.setObjectName(_fromUtf8("TheirDemand"))
        self.line_43 = QtWidgets.QFrame(self.page17)
        self.line_43.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_43.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_43.setObjectName(_fromUtf8("line_43"))
        self.BarterOfferText = myQLabel(self.page17)
        self.BarterOfferText.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.BarterOfferText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.BarterOfferText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.BarterOfferText.setObjectName(_fromUtf8("BarterOfferText"))
        self.CancelBarter = QtWidgets.QPushButton(self.page17)
        self.CancelBarter.setGeometry(QtCore.QRect(150, 630, 101, 41))
        self.CancelBarter.setObjectName(_fromUtf8("CancelBarter"))
        self.TheirSupplyBox = QtWidgets.QListWidget(self.page17)
        self.TheirSupplyBox.setGeometry(QtCore.QRect(0, 80, 331, 131))
        self.TheirSupplyBox.setObjectName(_fromUtf8("TheirSupplyBox"))
        self.SupplyAdditional8 = myQCheckBox(self.page17)
        self.SupplyAdditional8.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional8.setObjectName(_fromUtf8("SupplyAdditional8"))
        self.MySupplyBox = QtWidgets.QListWidget(self.page17)
        self.MySupplyBox.setGeometry(QtCore.QRect(340, 280, 331, 131))
        self.MySupplyBox.setObjectName(_fromUtf8("MySupplyBox"))
        self.MyDemandBox = QtWidgets.QListWidget(self.page17)
        self.MyDemandBox.setGeometry(QtCore.QRect(0, 280, 331, 131))
        self.MyDemandBox.setObjectName(_fromUtf8("MyDemandBox"))
        self.MySupply = myQLabel(self.page17)
        self.MySupply.setGeometry(QtCore.QRect(340, 250, 331, 31))
        # self.MySupply.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MySupply.setObjectName(_fromUtf8("MySupply"))
        self.MyDemand = myQLabel(self.page17)
        self.MyDemand.setGeometry(QtCore.QRect(0, 250, 331, 31))
        # self.MyDemand.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDemand.setObjectName(_fromUtf8("MyDemand"))
        self.TheirDepositUSD8 = QtWidgets.QComboBox(self.page17)
        self.TheirDepositUSD8.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD8.setObjectName(_fromUtf8("TheirDepositUSD8"))
        self.TheirDepositUSD8.addItem(_fromUtf8(""))
        self.TheirDepositUSD8.addItem(_fromUtf8(""))
        self.TheirDepositText8 = myQLabel(self.page17)
        self.TheirDepositText8.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText8.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText8.setObjectName(_fromUtf8("TheirDepositText8"))
        self.MyDepositBox8 = QtWidgets.QLineEdit(self.page17)
        self.MyDepositBox8.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox8.setStyleSheet(
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
        self.MyDepositBox8.setText(_fromUtf8(""))
        self.MyDepositBox8.setObjectName(_fromUtf8("MyDepositBox8"))
        self.TimeLimitDays8 = QtWidgets.QComboBox(self.page17)
        self.TimeLimitDays8.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays8.setObjectName(_fromUtf8("TimeLimitDays8"))
        self.TimeLimitDays8.addItem(_fromUtf8(""))
        self.TimeLimitDays8.addItem(_fromUtf8(""))
        self.MyDepositUSD8 = QtWidgets.QComboBox(self.page17)
        self.MyDepositUSD8.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD8.setObjectName(_fromUtf8("MyDepositUSD8"))
        self.MyDepositUSD8.addItem(_fromUtf8(""))
        self.MyDepositUSD8.addItem(_fromUtf8(""))
        self.DepositSettings8 = QtWidgets.QComboBox(self.page17)
        self.DepositSettings8.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings8.setObjectName(_fromUtf8("DepositSettings8"))
        self.DepositSettings8.addItem(_fromUtf8(""))
        self.DepositSettings8.addItem(_fromUtf8(""))
        self.TimeLimitText8 = myQLabel(self.page17)
        self.TimeLimitText8.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText8.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText8.setObjectName(_fromUtf8("TimeLimitText8"))
        self.TimeLimitBox8 = QtWidgets.QLineEdit(self.page17)
        self.TimeLimitBox8.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox8.setStyleSheet(
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
        self.TimeLimitBox8.setObjectName(_fromUtf8("TimeLimitBox8"))
        self.MyDepositText8 = myQLabel(self.page17)
        self.MyDepositText8.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText8.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText8.setObjectName(_fromUtf8("MyDepositText8"))
        self.TheirDepositBox8 = QtWidgets.QLineEdit(self.page17)
        self.TheirDepositBox8.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox8.setStyleSheet(
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
        self.TheirDepositBox8.setText(_fromUtf8(""))
        self.TheirDepositBox8.setObjectName(_fromUtf8("TheirDepositBox8"))
        self.MyOfferNotInList = QtWidgets.QPushButton(self.page17)
        self.MyOfferNotInList.setGeometry(QtCore.QRect(340, 410, 181, 31))
        self.MyOfferNotInList.setObjectName(_fromUtf8("MyOfferNotInList"))
        self.ClickItem = myQLabel(self.page17)
        self.ClickItem.setGeometry(QtCore.QRect(180, 220, 321, 16))
        # self.ClickItem.setStyleSheet(_fromUtf8("font: 13px;"))
        self.ClickItem.setObjectName(_fromUtf8("ClickItem"))
        self.Pages.addWidget(self.page17)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.TheirDepositUSD9 = QtWidgets.QComboBox(self.page)
        self.TheirDepositUSD9.setGeometry(QtCore.QRect(310, 530, 51, 31))
        self.TheirDepositUSD9.setObjectName(_fromUtf8("TheirDepositUSD9"))
        self.TheirDepositUSD9.addItem(_fromUtf8(""))
        self.TheirDepositUSD9.addItem(_fromUtf8(""))
        self.MyDepositBox9 = QtWidgets.QLineEdit(self.page)
        self.MyDepositBox9.setGeometry(QtCore.QRect(140, 490, 161, 31))
        self.MyDepositBox9.setStyleSheet(
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
        self.MyDepositBox9.setText(_fromUtf8(""))
        self.MyDepositBox9.setObjectName(_fromUtf8("MyDepositBox9"))
        self.Notes9 = myQLabel(self.page)
        self.Notes9.setGeometry(QtCore.QRect(400, 480, 281, 31))
        # self.Notes9.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Notes9.setObjectName(_fromUtf8("Notes9"))
        self.PythonText = myQLabel(self.page)
        self.PythonText.setGeometry(QtCore.QRect(0, 0, 311, 51))
        self.PythonText.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.PythonText.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.PythonText.setObjectName(_fromUtf8("PythonText"))
        self.TimeLimitText9 = myQLabel(self.page)
        self.TimeLimitText9.setGeometry(QtCore.QRect(0, 570, 101, 31))
        # self.TimeLimitText9.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText9.setObjectName(_fromUtf8("TimeLimitText9"))
        self.TimeLimitBox9 = QtWidgets.QLineEdit(self.page)
        self.TimeLimitBox9.setGeometry(QtCore.QRect(140, 570, 161, 31))
        self.TimeLimitBox9.setStyleSheet(
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
        self.TimeLimitBox9.setObjectName(_fromUtf8("TimeLimitBox9"))
        self.SaveFuture9 = myQCheckBox(self.page)
        self.SaveFuture9.setGeometry(QtCore.QRect(280, 640, 151, 17))
        self.SaveFuture9.setObjectName(_fromUtf8("SaveFuture9"))
        self.DescriptionPython = myQLabel(self.page)
        self.DescriptionPython.setGeometry(QtCore.QRect(0, 90, 101, 31))
        # self.DescriptionPython.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.DescriptionPython.setObjectName(_fromUtf8("DescriptionPython"))
        self.TimeLimitDays9 = QtWidgets.QComboBox(self.page)
        self.TimeLimitDays9.setGeometry(QtCore.QRect(310, 570, 51, 31))
        self.TimeLimitDays9.setObjectName(_fromUtf8("TimeLimitDays9"))
        self.TimeLimitDays9.addItem(_fromUtf8(""))
        self.TimeLimitDays9.addItem(_fromUtf8(""))
        self.NotesBox9 = QtWidgets.QTextEdit(self.page)
        self.NotesBox9.setGeometry(QtCore.QRect(400, 510, 271, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.NotesBox9.sizePolicy().hasHeightForWidth())
        self.NotesBox9.setSizePolicy(sizePolicy)
        self.NotesBox9.setMinimumSize(QtCore.QSize(0, 89))
        self.NotesBox9.setMaximumSize(QtCore.QSize(16777215, 90))
        self.NotesBox9.setStyleSheet(
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
        self.NotesBox9.setObjectName(_fromUtf8("NotesBox9"))
        self.MyDepositUSD9 = QtWidgets.QComboBox(self.page)
        self.MyDepositUSD9.setGeometry(QtCore.QRect(310, 490, 51, 31))
        self.MyDepositUSD9.setObjectName(_fromUtf8("MyDepositUSD9"))
        self.MyDepositUSD9.addItem(_fromUtf8(""))
        self.MyDepositUSD9.addItem(_fromUtf8(""))
        self.PythonUSD = QtWidgets.QComboBox(self.page)
        self.PythonUSD.setGeometry(QtCore.QRect(310, 390, 51, 31))
        self.PythonUSD.setObjectName(_fromUtf8("PythonUSD"))
        self.PythonUSD.addItem(_fromUtf8(""))
        self.PythonUSD.addItem(_fromUtf8(""))
        self.ExplainPython = QtWidgets.QPushButton(self.page)
        self.ExplainPython.setGeometry(QtCore.QRect(330, 10, 40, 40))
        self.ExplainPython.setMinimumSize(QtCore.QSize(40, 40))
        self.ExplainPython.setMaximumSize(QtCore.QSize(40, 40))
        self.ExplainPython.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExplainPython.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.ExplainPython.setIconSize(QtCore.QSize(20, 20))
        self.ExplainPython.setObjectName(_fromUtf8("ExplainPython"))
        self.TheirDepositText9 = myQLabel(self.page)
        self.TheirDepositText9.setGeometry(QtCore.QRect(0, 530, 131, 31))
        # self.TheirDepositText9.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText9.setObjectName(_fromUtf8("TheirDepositText9"))
        self.TheirDepositBox9 = QtWidgets.QLineEdit(self.page)
        self.TheirDepositBox9.setGeometry(QtCore.QRect(140, 530, 161, 31))
        self.TheirDepositBox9.setStyleSheet(
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
        self.TheirDepositBox9.setText(_fromUtf8(""))
        self.TheirDepositBox9.setObjectName(_fromUtf8("TheirDepositBox9"))
        self.SaveContinue9 = QtWidgets.QPushButton(self.page)
        self.SaveContinue9.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.SaveContinue9.setObjectName(_fromUtf8("SaveContinue9"))
        self.MyDepositText9 = myQLabel(self.page)
        self.MyDepositText9.setGeometry(QtCore.QRect(0, 490, 101, 31))
        # self.MyDepositText9.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText9.setObjectName(_fromUtf8("MyDepositText9"))
        self.ClearForm9 = QtWidgets.QPushButton(self.page)
        self.ClearForm9.setGeometry(QtCore.QRect(190, 630, 81, 41))
        self.ClearForm9.setObjectName(_fromUtf8("ClearForm9"))
        self.DepositSettings9 = QtWidgets.QComboBox(self.page)
        self.DepositSettings9.setGeometry(QtCore.QRect(0, 440, 211, 31))
        self.DepositSettings9.setObjectName(_fromUtf8("DepositSettings9"))
        self.DepositSettings9.addItem(_fromUtf8(""))
        self.DepositSettings9.addItem(_fromUtf8(""))
        self.DepositSettings9.addItem(_fromUtf8(""))
        self.DepositSettings9.addItem(_fromUtf8(""))
        self.DescriptionPythonBox = QtWidgets.QTextEdit(self.page)
        self.DescriptionPythonBox.setGeometry(QtCore.QRect(0, 131, 341, 89))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DescriptionPythonBox.sizePolicy().hasHeightForWidth())
        self.DescriptionPythonBox.setSizePolicy(sizePolicy)
        self.DescriptionPythonBox.setMinimumSize(QtCore.QSize(0, 89))
        self.DescriptionPythonBox.setMaximumSize(QtCore.QSize(16777215, 110))
        self.DescriptionPythonBox.setStyleSheet(
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
        self.DescriptionPythonBox.setObjectName(_fromUtf8("DescriptionPythonBox"))
        self.SupplyAdditional9 = myQCheckBox(self.page)
        self.SupplyAdditional9.setGeometry(QtCore.QRect(460, 640, 211, 17))
        self.SupplyAdditional9.setObjectName(_fromUtf8("SupplyAdditional9"))
        self.line_22 = QtWidgets.QFrame(self.page)
        self.line_22.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_22.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_22.setObjectName(_fromUtf8("line_22"))
        self.PythonSelect = QtWidgets.QComboBox(self.page)
        self.PythonSelect.setGeometry(QtCore.QRect(0, 50, 211, 31))
        self.PythonSelect.setObjectName(_fromUtf8("PythonSelect"))
        self.PythonSelect.addItem(_fromUtf8(""))
        self.PythonSelect.addItem(_fromUtf8(""))
        self.PythonWhoPays = QtWidgets.QComboBox(self.page)
        self.PythonWhoPays.setGeometry(QtCore.QRect(400, 390, 201, 31))
        self.PythonWhoPays.setObjectName(_fromUtf8("PythonWhoPays"))
        self.PythonWhoPays.addItem(_fromUtf8(""))
        self.PythonWhoPays.addItem(_fromUtf8(""))
        self.AttachImagePython = QtWidgets.QPushButton(self.page)
        self.AttachImagePython.setGeometry(QtCore.QRect(540, 90, 131, 31))
        self.AttachImagePython.setMinimumSize(QtCore.QSize(100, 20))
        self.AttachImagePython.setMaximumSize(QtCore.QSize(16777215, 40))
        self.AttachImagePython.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AttachImagePython.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.AttachImagePython.setIcon(icon)
        self.AttachImagePython.setIconSize(QtCore.QSize(20, 20))
        self.AttachImagePython.setObjectName(_fromUtf8("AttachImagePython"))
        self.PythonImageBox = QtWidgets.QLineEdit(self.page)
        self.PythonImageBox.setGeometry(QtCore.QRect(360, 90, 161, 31))
        self.PythonImageBox.setStyleSheet(
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
        self.PythonImageBox.setText(_fromUtf8(""))
        self.PythonImageBox.setObjectName(_fromUtf8("PythonImageBox"))
        self.PythonImage = myQLabel(self.page)
        self.PythonImage.setGeometry(QtCore.QRect(280, 90, 71, 31))
        # self.PythonImage.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PythonImage.setObjectName(_fromUtf8("PythonImage"))
        self.PythonAmountBox = QtWidgets.QLineEdit(self.page)
        self.PythonAmountBox.setGeometry(QtCore.QRect(140, 390, 161, 31))
        self.PythonAmountBox.setStyleSheet(
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
        self.PythonAmountBox.setText(_fromUtf8(""))
        self.PythonAmountBox.setObjectName(_fromUtf8("PythonAmountBox"))
        self.PythonAmount = myQLabel(self.page)
        self.PythonAmount.setGeometry(QtCore.QRect(0, 390, 131, 31))
        # self.PythonAmount.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.PythonAmount.setObjectName(_fromUtf8("PythonAmount"))
        self.LoadFormPython = QtWidgets.QPushButton(self.page)
        self.LoadFormPython.setGeometry(QtCore.QRect(540, 240, 131, 31))
        self.LoadFormPython.setMinimumSize(QtCore.QSize(100, 20))
        self.LoadFormPython.setMaximumSize(QtCore.QSize(16777215, 40))
        self.LoadFormPython.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LoadFormPython.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.LoadFormPython.setIcon(icon)
        self.LoadFormPython.setIconSize(QtCore.QSize(20, 20))
        self.LoadFormPython.setObjectName(_fromUtf8("LoadFormPython"))
        self.CodeOfferFormBox = QtWidgets.QLineEdit(self.page)
        self.CodeOfferFormBox.setGeometry(QtCore.QRect(280, 240, 241, 31))
        self.CodeOfferFormBox.setStyleSheet(
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
        self.CodeOfferFormBox.setText(_fromUtf8(""))
        self.CodeOfferFormBox.setObjectName(_fromUtf8("CodeOfferFormBox"))
        self.CodeFormText = myQLabel(self.page)
        self.CodeFormText.setGeometry(QtCore.QRect(0, 240, 271, 31))
        # self.CodeFormText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.CodeFormText.setObjectName(_fromUtf8("CodeFormText"))
        self.LoadMyPython = QtWidgets.QPushButton(self.page)
        self.LoadMyPython.setGeometry(QtCore.QRect(540, 290, 131, 31))
        self.LoadMyPython.setMinimumSize(QtCore.QSize(100, 20))
        self.LoadMyPython.setMaximumSize(QtCore.QSize(16777215, 40))
        self.LoadMyPython.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LoadMyPython.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.LoadMyPython.setIcon(icon)
        self.LoadMyPython.setIconSize(QtCore.QSize(20, 20))
        self.LoadMyPython.setObjectName(_fromUtf8("LoadMyPython"))
        self.CodeDuringEscrow = QtWidgets.QLineEdit(self.page)
        self.CodeDuringEscrow.setGeometry(QtCore.QRect(280, 290, 241, 31))
        self.CodeDuringEscrow.setStyleSheet(
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
        self.CodeDuringEscrow.setText(_fromUtf8(""))
        self.CodeDuringEscrow.setObjectName(_fromUtf8("CodeDuringEscrow"))
        self.CodeEscrowText = myQLabel(self.page)
        self.CodeEscrowText.setGeometry(QtCore.QRect(0, 290, 271, 31))
        # self.CodeEscrowText.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.CodeEscrowText.setObjectName(_fromUtf8("CodeEscrowText"))
        self.LoadTheirPython = QtWidgets.QPushButton(self.page)
        self.LoadTheirPython.setGeometry(QtCore.QRect(540, 340, 131, 31))
        self.LoadTheirPython.setMinimumSize(QtCore.QSize(100, 20))
        self.LoadTheirPython.setMaximumSize(QtCore.QSize(16777215, 40))
        self.LoadTheirPython.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LoadTheirPython.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.LoadTheirPython.setIcon(icon)
        self.LoadTheirPython.setIconSize(QtCore.QSize(20, 20))
        self.LoadTheirPython.setObjectName(_fromUtf8("LoadTheirPython"))
        self.CodeEscrowWindow = QtWidgets.QLineEdit(self.page)
        self.CodeEscrowWindow.setGeometry(QtCore.QRect(280, 340, 241, 31))
        self.CodeEscrowWindow.setStyleSheet(
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
        self.CodeEscrowWindow.setText(_fromUtf8(""))
        self.CodeEscrowWindow.setObjectName(_fromUtf8("CodeEscrowWindow"))
        self.CodeEscrowText2 = myQLabel(self.page)
        self.CodeEscrowText2.setGeometry(QtCore.QRect(0, 340, 271, 31))
        # self.CodeEscrowText2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.CodeEscrowText2.setObjectName(_fromUtf8("CodeEscrowText2"))
        self.PythonWarning = QtWidgets.QTextBrowser(self.page)
        self.PythonWarning.setGeometry(QtCore.QRect(360, 130, 311, 91))
        self.PythonWarning.setObjectName(_fromUtf8("PythonWarning"))
        self.Pages.addWidget(self.page)
        self.page18 = QtWidgets.QWidget()
        self.page18.setObjectName(_fromUtf8("page18"))
        self.line_21 = QtWidgets.QFrame(self.page18)
        self.line_21.setGeometry(QtCore.QRect(10, 610, 671, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_21.setObjectName(_fromUtf8("line_21"))
        self.ConfirmOrder = QtWidgets.QPushButton(self.page18)
        self.ConfirmOrder.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.ConfirmOrder.setObjectName(_fromUtf8("ConfirmOrder"))
        self.CoinsForCash_16 = myQLabel(self.page18)
        self.CoinsForCash_16.setGeometry(QtCore.QRect(0, 0, 271, 51))
        self.CoinsForCash_16.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.CoinsForCash_16.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.CoinsForCash_16.setObjectName(_fromUtf8("CoinsForCash_16"))
        self.ContactSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.ContactSelectConfirm.setGeometry(QtCore.QRect(420, 140, 211, 40))
        self.ContactSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.ContactSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ContactSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ContactSelectConfirm.setStyleSheet(
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
        self.ContactSelectConfirm.setObjectName(_fromUtf8("ContactSelectConfirm"))
        self.MailingSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.MailingSelectConfirm.setGeometry(QtCore.QRect(420, 210, 211, 40))
        self.MailingSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.MailingSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MailingSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MailingSelectConfirm.setStyleSheet(
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
        self.MailingSelectConfirm.setObjectName(_fromUtf8("MailingSelectConfirm"))
        self.BankSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.BankSelectConfirm.setGeometry(QtCore.QRect(420, 280, 211, 40))
        self.BankSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.BankSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.BankSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BankSelectConfirm.setStyleSheet(
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
        self.BankSelectConfirm.setObjectName(_fromUtf8("BankSelectConfirm"))
        self.WUSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.WUSelectConfirm.setGeometry(QtCore.QRect(420, 350, 211, 40))
        self.WUSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.WUSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WUSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.WUSelectConfirm.setStyleSheet(
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
        self.WUSelectConfirm.setObjectName(_fromUtf8("WUSelectConfirm"))
        self.MGSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.MGSelectConfirm.setGeometry(QtCore.QRect(420, 420, 211, 40))
        self.MGSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.MGSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MGSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MGSelectConfirm.setStyleSheet(
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
        self.MGSelectConfirm.setObjectName(_fromUtf8("MGSelectConfirm"))
        self.DebitSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.DebitSelectConfirm.setGeometry(QtCore.QRect(420, 490, 211, 40))
        self.DebitSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.DebitSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.DebitSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DebitSelectConfirm.setStyleSheet(
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
        self.DebitSelectConfirm.setObjectName(_fromUtf8("DebitSelectConfirm"))
        self.OtherSelectConfirm = QtWidgets.QComboBox(self.page18)
        self.OtherSelectConfirm.setGeometry(QtCore.QRect(420, 560, 211, 40))
        self.OtherSelectConfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.OtherSelectConfirm.setMaximumSize(QtCore.QSize(16777215, 40))
        self.OtherSelectConfirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.OtherSelectConfirm.setStyleSheet(
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
        self.OtherSelectConfirm.setObjectName(_fromUtf8("OtherSelectConfirm"))
        self.ContactConfirm = myQLabel(self.page18)
        self.ContactConfirm.setGeometry(QtCore.QRect(420, 110, 201, 31))
        # self.ContactConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.ContactConfirm.setObjectName(_fromUtf8("ContactConfirm"))
        self.MailingConfirm = myQLabel(self.page18)
        self.MailingConfirm.setGeometry(QtCore.QRect(420, 180, 201, 31))
        # self.MailingConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.MailingConfirm.setObjectName(_fromUtf8("MailingConfirm"))
        self.BankConfirm = myQLabel(self.page18)
        self.BankConfirm.setGeometry(QtCore.QRect(420, 250, 201, 31))
        # self.BankConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.BankConfirm.setObjectName(_fromUtf8("BankConfirm"))
        self.WUConfirm = myQLabel(self.page18)
        self.WUConfirm.setGeometry(QtCore.QRect(420, 320, 201, 31))
        # self.WUConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.WUConfirm.setObjectName(_fromUtf8("WUConfirm"))
        self.MGConfirm = myQLabel(self.page18)
        self.MGConfirm.setGeometry(QtCore.QRect(420, 390, 201, 31))
        # self.MGConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.MGConfirm.setObjectName(_fromUtf8("MGConfirm"))
        self.DebitConfirm = myQLabel(self.page18)
        self.DebitConfirm.setGeometry(QtCore.QRect(420, 460, 201, 31))
        # self.DebitConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.DebitConfirm.setObjectName(_fromUtf8("DebitConfirm"))
        self.OtherConfirm = myQLabel(self.page18)
        self.OtherConfirm.setGeometry(QtCore.QRect(420, 530, 201, 31))
        # self.OtherConfirm.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.OtherConfirm.setObjectName(_fromUtf8("OtherConfirm"))
        self.ContactEdit = QtWidgets.QPushButton(self.page18)
        self.ContactEdit.setGeometry(QtCore.QRect(630, 140, 51, 41))
        self.ContactEdit.setObjectName(_fromUtf8("ContactEdit"))
        self.AddressEdit = QtWidgets.QPushButton(self.page18)
        self.AddressEdit.setGeometry(QtCore.QRect(630, 210, 51, 41))
        self.AddressEdit.setObjectName(_fromUtf8("AddressEdit"))
        self.BankEdit = QtWidgets.QPushButton(self.page18)
        self.BankEdit.setGeometry(QtCore.QRect(630, 280, 51, 41))
        self.BankEdit.setObjectName(_fromUtf8("BankEdit"))
        self.WUEdit = QtWidgets.QPushButton(self.page18)
        self.WUEdit.setGeometry(QtCore.QRect(630, 350, 51, 41))
        self.WUEdit.setObjectName(_fromUtf8("WUEdit"))
        self.DebitEdit = QtWidgets.QPushButton(self.page18)
        self.DebitEdit.setGeometry(QtCore.QRect(630, 490, 51, 41))
        self.DebitEdit.setObjectName(_fromUtf8("DebitEdit"))
        self.MGEdit = QtWidgets.QPushButton(self.page18)
        self.MGEdit.setGeometry(QtCore.QRect(630, 420, 51, 41))
        self.MGEdit.setObjectName(_fromUtf8("MGEdit"))
        self.OtherEdit = QtWidgets.QPushButton(self.page18)
        self.OtherEdit.setGeometry(QtCore.QRect(630, 560, 51, 41))
        self.OtherEdit.setObjectName(_fromUtf8("OtherEdit"))
        self.ConfirmTextEdit = QtWidgets.QTextEdit(self.page18)
        self.ConfirmTextEdit.setGeometry(QtCore.QRect(0, 40, 421, 71))
        self.ConfirmTextEdit.setObjectName(_fromUtf8("ConfirmTextEdit"))
        self.ContractSummary = myQLabel(self.page18)
        self.ContractSummary.setGeometry(QtCore.QRect(10, 110, 361, 31))
        # self.ContractSummary.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.ContractSummary.setObjectName(_fromUtf8("ContractSummary"))
        self.MyDepositSummary = myQLabel(self.page18)
        self.MyDepositSummary.setGeometry(QtCore.QRect(10, 190, 361, 31))
        # self.MyDepositSummary.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.MyDepositSummary.setObjectName(_fromUtf8("MyDepositSummary"))
        self.AmountSummary = myQLabel(self.page18)
        self.AmountSummary.setGeometry(QtCore.QRect(10, 150, 361, 31))
        # self.AmountSummary.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.AmountSummary.setObjectName(_fromUtf8("AmountSummary"))
        self.TheirDepositSummary = myQLabel(self.page18)
        self.TheirDepositSummary.setGeometry(QtCore.QRect(10, 230, 361, 31))
        # self.TheirDepositSummary.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.TheirDepositSummary.setObjectName(_fromUtf8("TheirDepositSummary"))
        self.TimeLimitSummary = myQLabel(self.page18)
        self.TimeLimitSummary.setGeometry(QtCore.QRect(10, 270, 361, 31))
        # self.TimeLimitSummary.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.TimeLimitSummary.setObjectName(_fromUtf8("TimeLimitSummary"))
        self.AutoAcceptValid = myQCheckBox(self.page18)
        self.AutoAcceptValid.setGeometry(QtCore.QRect(10, 400, 211, 17))
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.AutoAcceptValid.setFont(font)
        self.AutoAcceptValid.setObjectName(_fromUtf8("AutoAcceptValid"))
        self.AllowCounters = myQCheckBox(self.page18)
        self.AllowCounters.setGeometry(QtCore.QRect(10, 440, 211, 17))
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.AllowCounters.setFont(font)
        self.AllowCounters.setObjectName(_fromUtf8("AllowCounters"))
        self.AllowChat = myQCheckBox(self.page18)
        self.AllowChat.setGeometry(QtCore.QRect(10, 480, 211, 17))
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.AllowChat.setFont(font)
        self.AllowChat.setObjectName(_fromUtf8("AllowChat"))
        self.AllowPriceTracking = myQCheckBox(self.page18)
        self.AllowPriceTracking.setGeometry(QtCore.QRect(10, 520, 211, 17))
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.AllowPriceTracking.setFont(font)
        self.AllowPriceTracking.setObjectName(_fromUtf8("AllowPriceTracking"))
        self.SendToText = myQLabel(self.page18)
        self.SendToText.setGeometry(QtCore.QRect(10, 310, 91, 31))
        # self.SendToText.setStyleSheet(_fromUtf8("font: 16px \"Arial\";"))
        self.SendToText.setObjectName(_fromUtf8("SendToText"))
        self.SentToSelect = QtWidgets.QComboBox(self.page18)
        self.SentToSelect.setGeometry(QtCore.QRect(120, 310, 221, 31))
        self.SentToSelect.setObjectName(_fromUtf8("SentToSelect"))
        self.SentToSelect.addItem(_fromUtf8(""))
        self.SentToSelect.setItemData(0, 9999999)
        self.SendToAddress = QtWidgets.QLineEdit(self.page18)
        self.SendToAddress.setGeometry(QtCore.QRect(120, 350, 221, 31))
        self.SendToAddress.setStyleSheet(
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
        self.SendToAddress.setText(_fromUtf8(""))
        self.SendToAddress.setObjectName(_fromUtf8("SendToAddress"))
        self.Pages.addWidget(self.page18)
        self.page19 = QtWidgets.QWidget()
        self.page19.setObjectName(_fromUtf8("page19"))
        self.TheirDepositText10 = myQLabel(self.page19)
        self.TheirDepositText10.setGeometry(QtCore.QRect(0, 540, 131, 31))
        # self.TheirDepositText10.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TheirDepositText10.setObjectName(_fromUtf8("TheirDepositText10"))
        self.TextBox1 = QtWidgets.QTextEdit(self.page19)
        self.TextBox1.setGeometry(QtCore.QRect(400, 499, 281, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.TextBox1.sizePolicy().hasHeightForWidth())
        self.TextBox1.setSizePolicy(sizePolicy)
        self.TextBox1.setMinimumSize(QtCore.QSize(0, 89))
        self.TextBox1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.TextBox1.setStyleSheet(
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
        self.TextBox1.setObjectName(_fromUtf8("TextBox1"))
        self.SupplyAdditional10 = myQCheckBox(self.page19)
        self.SupplyAdditional10.setGeometry(QtCore.QRect(430, 620, 211, 17))
        self.SupplyAdditional10.setObjectName(_fromUtf8("SupplyAdditional10"))
        self.TimeLimitBox10 = QtWidgets.QLineEdit(self.page19)
        self.TimeLimitBox10.setGeometry(QtCore.QRect(140, 580, 161, 31))
        self.TimeLimitBox10.setStyleSheet(
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
        self.TimeLimitBox10.setObjectName(_fromUtf8("TimeLimitBox10"))
        self.MarketOrder = myQLabel(self.page19)
        self.MarketOrder.setGeometry(QtCore.QRect(0, 0, 271, 41))
        self.MarketOrder.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.MarketOrder.setStyleSheet(_fromUtf8("font: 29px \"Arial\";"))
        self.MarketOrder.setObjectName(_fromUtf8("MarketOrder"))
        self.SupplyText_2 = myQLabel(self.page19)
        self.SupplyText_2.setGeometry(QtCore.QRect(0, 50, 331, 31))
        # self.SupplyText_2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.SupplyText_2.setText(_fromUtf8(""))
        self.SupplyText_2.setObjectName(_fromUtf8("SupplyText_2"))
        self.TimeLimitDays10 = QtWidgets.QComboBox(self.page19)
        self.TimeLimitDays10.setGeometry(QtCore.QRect(310, 580, 51, 31))
        self.TimeLimitDays10.setObjectName(_fromUtf8("TimeLimitDays10"))
        self.TimeLimitDays10.addItem(_fromUtf8(""))
        self.TimeLimitDays10.addItem(_fromUtf8(""))
        self.MyDepositText10 = myQLabel(self.page19)
        self.MyDepositText10.setGeometry(QtCore.QRect(0, 500, 101, 31))
        # self.MyDepositText10.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.MyDepositText10.setObjectName(_fromUtf8("MyDepositText10"))
        self.DepositSettings10 = QtWidgets.QComboBox(self.page19)
        self.DepositSettings10.setGeometry(QtCore.QRect(0, 460, 211, 31))
        self.DepositSettings10.setObjectName(_fromUtf8("DepositSettings10"))
        self.DepositSettings10.addItem(_fromUtf8(""))
        self.DepositSettings10.addItem(_fromUtf8(""))
        self.Counter = QtWidgets.QPushButton(self.page19)
        self.Counter.setGeometry(QtCore.QRect(140, 630, 121, 41))
        self.Counter.setObjectName(_fromUtf8("Counter"))
        self.Accept = QtWidgets.QPushButton(self.page19)
        self.Accept.setGeometry(QtCore.QRect(0, 630, 121, 41))
        self.Accept.setObjectName(_fromUtf8("Accept"))
        self.Delete = QtWidgets.QPushButton(self.page19)
        self.Delete.setGeometry(QtCore.QRect(280, 630, 121, 41))
        self.Delete.setObjectName(_fromUtf8("Delete"))
        self.SelectContact = QtWidgets.QComboBox(self.page19)
        self.SelectContact.setGeometry(QtCore.QRect(430, 640, 251, 31))
        self.SelectContact.setMinimumSize(QtCore.QSize(0, 31))
        self.SelectContact.setMaximumSize(QtCore.QSize(16777215, 31))
        self.SelectContact.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SelectContact.setStyleSheet(
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
        self.SelectContact.setObjectName(_fromUtf8("SelectContact"))
        self.TheirDepositBox10 = QtWidgets.QLineEdit(self.page19)
        self.TheirDepositBox10.setGeometry(QtCore.QRect(140, 540, 161, 31))
        self.TheirDepositBox10.setStyleSheet(
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
        self.TheirDepositBox10.setText(_fromUtf8(""))
        self.TheirDepositBox10.setObjectName(_fromUtf8("TheirDepositBox10"))
        self.MarketExplanation = QtWidgets.QPushButton(self.page19)
        self.MarketExplanation.setGeometry(QtCore.QRect(290, 0, 40, 40))
        self.MarketExplanation.setMinimumSize(QtCore.QSize(40, 40))
        self.MarketExplanation.setMaximumSize(QtCore.QSize(40, 40))
        self.MarketExplanation.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MarketExplanation.setStyleSheet(
            _fromUtf8(
                "QPushButton {\n"
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
                " QPushButton:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }"
            )
        )
        self.MarketExplanation.setIconSize(QtCore.QSize(20, 20))
        self.MarketExplanation.setObjectName(_fromUtf8("MarketExplanation"))
        self.Text2 = myQLabel(self.page19)
        self.Text2.setGeometry(QtCore.QRect(400, 460, 281, 31))
        # self.Text2.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Text2.setObjectName(_fromUtf8("Text2"))
        self.MyDepositUSD10 = QtWidgets.QComboBox(self.page19)
        self.MyDepositUSD10.setGeometry(QtCore.QRect(310, 500, 51, 31))
        self.MyDepositUSD10.setObjectName(_fromUtf8("MyDepositUSD10"))
        self.MyDepositUSD10.addItem(_fromUtf8(""))
        self.MyDepositUSD10.addItem(_fromUtf8(""))
        self.TimeLimitText10 = myQLabel(self.page19)
        self.TimeLimitText10.setGeometry(QtCore.QRect(0, 580, 101, 31))
        # self.TimeLimitText10.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.TimeLimitText10.setObjectName(_fromUtf8("TimeLimitText10"))
        self.MyDepositBox10 = QtWidgets.QLineEdit(self.page19)
        self.MyDepositBox10.setGeometry(QtCore.QRect(140, 500, 161, 31))
        self.MyDepositBox10.setStyleSheet(
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
        self.MyDepositBox10.setText(_fromUtf8(""))
        self.MyDepositBox10.setObjectName(_fromUtf8("MyDepositBox10"))
        self.Button1 = QtWidgets.QPushButton(self.page19)
        self.Button1.setGeometry(QtCore.QRect(210, 270, 121, 21))
        self.Button1.setObjectName(_fromUtf8("Button1"))
        self.TheirDepositUSD10 = QtWidgets.QComboBox(self.page19)
        self.TheirDepositUSD10.setGeometry(QtCore.QRect(310, 540, 51, 31))
        self.TheirDepositUSD10.setObjectName(_fromUtf8("TheirDepositUSD10"))
        self.TheirDepositUSD10.addItem(_fromUtf8(""))
        self.TheirDepositUSD10.addItem(_fromUtf8(""))
        self.Button2 = QtWidgets.QPushButton(self.page19)
        self.Button2.setGeometry(QtCore.QRect(550, 270, 121, 21))
        self.Button2.setObjectName(_fromUtf8("Button2"))
        self.USD1 = QtWidgets.QComboBox(self.page19)
        self.USD1.setGeometry(QtCore.QRect(220, 330, 51, 31))
        self.USD1.setObjectName(_fromUtf8("USD1"))
        self.USD1.addItem(_fromUtf8(""))
        self.USD1.addItem(_fromUtf8(""))
        self.Box1 = QtWidgets.QLineEdit(self.page19)
        self.Box1.setGeometry(QtCore.QRect(0, 330, 211, 31))
        self.Box1.setStyleSheet(
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
        self.Box1.setText(_fromUtf8(""))
        self.Box1.setObjectName(_fromUtf8("Box1"))
        self.Drop1 = QtWidgets.QComboBox(self.page19)
        self.Drop1.setGeometry(QtCore.QRect(0, 290, 271, 31))
        self.Drop1.setObjectName(_fromUtf8("Drop1"))
        self.Drop1.addItem(_fromUtf8(""))
        self.Drop1.setItemData(0, 0)
        self.Drop1.addItem(_fromUtf8(""))
        self.Drop1.setItemData(1, 1)
        self.Drop3 = QtWidgets.QComboBox(self.page19)
        self.Drop3.setGeometry(QtCore.QRect(0, 370, 161, 31))
        self.Drop3.setObjectName(_fromUtf8("Drop3"))
        self.Drop3.addItem(_fromUtf8(""))
        self.Drop2 = QtWidgets.QComboBox(self.page19)
        self.Drop2.setGeometry(QtCore.QRect(340, 290, 161, 31))
        self.Drop2.setObjectName(_fromUtf8("Drop2"))
        self.Drop2.addItem(_fromUtf8(""))
        self.USD3 = QtWidgets.QComboBox(self.page19)
        self.USD3.setGeometry(QtCore.QRect(220, 410, 51, 31))
        self.USD3.setObjectName(_fromUtf8("USD3"))
        self.USD3.addItem(_fromUtf8(""))
        self.USD3.addItem(_fromUtf8(""))
        self.Box3 = QtWidgets.QLineEdit(self.page19)
        self.Box3.setGeometry(QtCore.QRect(0, 410, 211, 31))
        self.Box3.setStyleSheet(
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
        self.Box3.setText(_fromUtf8(""))
        self.Box3.setObjectName(_fromUtf8("Box3"))
        self.Box2 = QtWidgets.QLineEdit(self.page19)
        self.Box2.setGeometry(QtCore.QRect(340, 330, 221, 31))
        self.Box2.setStyleSheet(
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
        self.Box2.setText(_fromUtf8(""))
        self.Box2.setObjectName(_fromUtf8("Box2"))
        self.USD2 = QtWidgets.QComboBox(self.page19)
        self.USD2.setGeometry(QtCore.QRect(570, 330, 51, 31))
        self.USD2.setObjectName(_fromUtf8("USD2"))
        self.USD2.addItem(_fromUtf8(""))
        self.USD2.addItem(_fromUtf8(""))
        self.Text1 = myQLabel(self.page19)
        self.Text1.setGeometry(QtCore.QRect(340, 370, 161, 31))
        # self.Text1.setStyleSheet(_fromUtf8("font: 19px \"Arial\";"))
        self.Text1.setObjectName(_fromUtf8("Text1"))
        self.Box4 = QtWidgets.QLineEdit(self.page19)
        self.Box4.setGeometry(QtCore.QRect(340, 400, 221, 31))
        self.Box4.setStyleSheet(
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
        self.Box4.setText(_fromUtf8(""))
        self.Box4.setObjectName(_fromUtf8("Box4"))
        self.Link1 = myQLabel(self.page19)
        self.Link1.setGeometry(QtCore.QRect(340, 430, 131, 21))
        self.Link1.setObjectName(_fromUtf8("Link1"))
        self.Link2 = QtWidgets.QPushButton(self.page19)
        self.Link2.setGeometry(QtCore.QRect(470, 430, 111, 21))
        self.Link2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.Link2.setObjectName(_fromUtf8("Link2"))
        sendspacefont = QtGui.QFont()
        sendspacefont.setPixelSize(11)
        self.Link2.setFont(sendspacefont)
        self.Attach = QtWidgets.QPushButton(self.page19)
        self.Attach.setGeometry(QtCore.QRect(570, 400, 111, 31))
        self.Attach.setMinimumSize(QtCore.QSize(100, 20))
        self.Attach.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Attach.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Attach.setStyleSheet(
            _fromUtf8(
                "QPushButton#instantexplain_4 {\n"
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
                " QPushButton#instantexplain_4:pressed {\n"
                "     border-style: inset;\n"
                "background-color: rgba(184, 184, 184, 50);\n"
                "background: qlineargradient(x1:1, y1:1, x2:1, y2:1, stop:0 #eeeeee, stop: 0.4 rgba(224, 224, 224, 250), stop:1 rgba(224, 224, 224, 250));\n"
                " }\n"
                ""
            )
        )
        self.Attach.setIcon(icon)
        self.Attach.setIconSize(QtCore.QSize(20, 20))
        self.Attach.setObjectName(_fromUtf8("Attach"))
        self.Drop4 = QtWidgets.QComboBox(self.page19)
        self.Drop4.setGeometry(QtCore.QRect(170, 370, 101, 31))
        self.Drop4.setObjectName(_fromUtf8("Drop4"))
        self.Drop4.addItem(_fromUtf8(""))
        self.CheckBox1 = myQCheckBox(self.page19)
        self.CheckBox1.setGeometry(QtCore.QRect(230, 460, 151, 21))
        self.CheckBox1.setObjectName(_fromUtf8("CheckBox1"))
        self.Display1 = QtWebEngineWidgets.QWebEngineView(self.page19)
        self.Display1.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebAttribute.JavascriptEnabled, False)

        self.Display1.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebAttribute.PluginsEnabled, False)
        self.Display1.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, False)
        self.Display1.setGeometry(QtCore.QRect(0, 40, 331, 231))
        self.Display1.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.Display1.setObjectName(_fromUtf8("Display1"))
        self.Display2 = QtWebEngineWidgets.QWebEngineView(self.page19)
        self.Display2.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebAttribute.JavascriptEnabled, False)

        self.Display2.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebAttribute.PluginsEnabled, False)
        self.Display2.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, False)
        self.Display2.setGeometry(QtCore.QRect(340, 40, 331, 231))
        self.Display2.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.Display2.setObjectName(_fromUtf8("Display2"))
        self.Pages.addWidget(self.page19)
        self.verticalLayout.addWidget(self.Pages)

        self.retranslateUi(Form)
        self.changeindex = 0
        self.Pages.setCurrentIndex(self.changeindex)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.RateBox.setItemText(0, _translate("Form", "Market Price", None))
        self.RateBox.setItemText(1, _translate("Form", "Price per coin", None))
        self.SellCoinsForCashTitle.setText(_translate("Form", "Sell Coins For Cash", None))
        self.Price.setText(_translate("Form", "Price:", None))
        self.Amount.setText(_translate("Form", "Amount:", None))
        self.AmountUSD.setItemText(0, _translate("Form", "USD", None))
        self.AmountUSD.setItemText(1, _translate("Form", "Coins", None))
        self.PriceTrackingTitle.setText(_translate("Form", "Automatic price tracking:", None))
        self.ServiceChargeText.setText(_translate("Form", "Service Charge:", None))
        self.ServiceCharge.setItemText(0, _translate("Form", "2%", None))
        self.ServiceCharge.setItemText(1, _translate("Form", "5%", None))
        self.ServiceCharge.setItemText(2, _translate("Form", "10%", None))
        self.ServiceCharge.setItemText(3, _translate("Form", "15%", None))
        self.ServiceCharge.setItemText(4, _translate("Form", "20%", None))
        self.ServiceCharge.setItemText(5, _translate("Form", "Custom", None))
        self.MaxIncreaseSell.setItemText(0, _translate("Form", "25% Maximum Increase", None))
        self.MaxIncreaseSell.setItemText(1, _translate("Form", "No Limit", None))
        self.MaxIncreaseSell.setItemText(2, _translate("Form", "Custom Maximum Increase", None))
        self.MaxDecreaseSell.setItemText(0, _translate("Form", "5% Maximum Decrease", None))
        self.MaxDecreaseSell.setItemText(1, _translate("Form", "10% Maximum Decrease", None))
        self.MaxDecreaseSell.setItemText(2, _translate("Form", "15% Maximum Decrease", None))
        self.MaxDecreaseSell.setItemText(3, _translate("Form", "Custom Maximum Decrease", None))
        self.perc1.setText(_translate("Form", "%", None))
        self.perc5.setText(_translate("Form", "%", None))
        self.perc2.setText(_translate("Form", "%", None))
        self.DepositSettings.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings.setItemText(2, _translate("Form", "Make Me A Guarantor", None))
        self.TimeLimitText.setText(_translate("Form", "Time Limit:", None))
        self.TimeLimitDays.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays.setItemText(1, _translate("Form", "Hours", None))
        self.TheirDepositText.setText(_translate("Form", "Their Deposit:", None))
        self.MyDepositText.setText(_translate("Form", "My Deposit:", None))
        self.PaymentOptions.setText(_translate("Form", "Payment Options:", None))
        self.agreelabel.setText(_translate("Form", "You agree to accept any of the marked boxes below as payment", None))
        self.NotesText1.setText(_translate("Form", "Notes/Extra Details:", None))
        self.BankWireCheck.setText(_translate("Form", "Bank Wire/SEPA", None))
        self.WUCheck.setText(_translate("Form", "Western Union", None))
        self.MoneyGramCheck.setText(_translate("Form", "MoneyGram", None))
        self.DebitCheck.setText(_translate("Form", "Prepaid Debit Card", None))
        self.CashMailCheck.setText(_translate("Form", "Cash In The Mail", None))
        self.OtherCheck.setText(_translate("Form", "Other", None))
        self.perc3.setText(_translate("Form", "%", None))
        self.MinOrderSell.setItemText(0, _translate("Form", "25% Minimum Sell Order", None))
        self.MinOrderSell.setItemText(1, _translate("Form", "50% Minimum Sell Order", None))
        self.MinOrderSell.setItemText(2, _translate("Form", "100% Minimum Sell Order", None))
        self.MinOrderSell.setItemText(3, _translate("Form", "Custom Minimum Sell Order", None))
        self.MaxOrderSell.setItemText(0, _translate("Form", "100% Maximum Sell Order", None))
        self.MaxOrderSell.setItemText(1, _translate("Form", "50% Maximum Sell Order", None))
        self.MaxOrderSell.setItemText(2, _translate("Form", "25% Maximum Sell Order", None))
        self.MaxOrderSell.setItemText(3, _translate("Form", "Custom Maximum Sell Order", None))
        self.perc4.setText(_translate("Form", "%", None))
        self.SaveContinue1.setText(_translate("Form", "Save And Continue", None))
        self.ShowAdvancedCash.setText(_translate("Form", "Show Advanced Settings", None))
        self.LimitOrderText1.setText(_translate("Form", "Limit order sizes:", None))
        self.ExchangeRate.setText(_translate("Form", "Exchange Rate:", None))
        self.ExplainSellCash.setToolTip(_translate("Form", "Help", None))
        self.ExplainSellCash.setText(_translate("Form", "?", None))
        self.SupplyAdditional1.setText(_translate("Form", "Supply Contact Information", None))
        self.SaveFuture1.setText(_translate("Form", "Save This Form", None))
        self.ClearForm1.setText(_translate("Form", "Clear Form", None))
        self.PriceUSD.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD.setItemText(1, _translate("Form", "Coins", None))
        self.TheirDepositUSD.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD.setItemText(1, _translate("Form", "Coins", None))
        self.WireText.setText(_translate("Form", "Bank Wire/Sepa/Direct Deposit", None))
        self.WireBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Please fill out the form below. Any bank in the world that accepts international or local wires is supported. '
                "Direct deposit may be an option as well for the buyer. This information is confidential, and not shared with the buyer until the deal funds. "
                "This is one of the most secure and private ways to buy.</span></p>\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11px;">'
                "<br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Please Note:</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Every bank has a different policy. Please check and see what information is needed for international wires, '
                "local wires and direct deposit. If you do large volumes of transactions we recommend checking with your branch about all applicable rules and policies.</span>"
                "</p></body></html>",
                None,
            )
        )
        self.AccountName.setText(_translate("Form", "Account Number (or IBAN):", None))
        self.BankName.setText(_translate("Form", "Bank Name:", None))
        self.NameAct.setText(_translate("Form", "Name on the Account (If applicable):", None))
        self.Routing.setText(_translate("Form", "Routing Number or Swift/BIC (If applicable):", None))
        self.OtherInfo.setText(_translate("Form", "Other information(such as branch address) or instructions:", None))
        self.Save1.setText(_translate("Form", "Save Profile And Continue", None))
        self.Remove1.setText(_translate("Form", "Remove Current Profile", None))
        self.Create1.setText(_translate("Form", "Create New Profile", None))
        self.Update1.setText(_translate("Form", "Update Current Profile", None))
        self.WUText.setText(_translate("Form", "Western Union", None))
        self.OtherInfo2.setText(_translate("Form", "Other Information or special instructions (If applicable):", None))
        self.Save2.setText(_translate("Form", "Save Profile And Continue", None))
        self.Remove2.setText(_translate("Form", "Remove Current Profile", None))
        self.Update2.setText(_translate("Form", "Update Current Profile", None))
        self.PhoneText1.setText(_translate("Form", "Phone Number (If applicable):", None))
        self.CountryText1.setText(_translate("Form", "Country of Residence:", None))
        self.CityPickup1.setText(_translate("Form", "City and State/Province where funds will be picked up:", None))
        self.FullName1.setText(_translate("Form", "Your FULL Name as it shows on your Identification:", None))
        self.Create2.setText(_translate("Form", "Create New Profile", None))
        self.WUBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Please fill out the form below. In order to redeem a Western Union, you should have an office in your '
                "country where you can pick up the cash near you. Please make sure you are familiar with the process and their local policies. "
                "This is the first time in history that Western Union can be sent in exchange for goods securely thanks to double deposit.</span></p></body></html>",
                None,
            )
        )
        self.Secret1.setText(_translate("Form", "Request secret question and answer(optional):", None))
        self.FullNameText2.setText(_translate("Form", "Your FULL Name as it shows on your Identification:", None))
        self.CountryText2.setText(_translate("Form", "Country of Residence:", None))
        self.MGText.setText(_translate("Form", "Money Gram", None))
        self.Remove3.setText(_translate("Form", "Remove Current Profile", None))
        self.Save3.setText(_translate("Form", "Save Profile And Continue", None))
        self.OtherInfo3.setText(_translate("Form", "Other Information or special instructions (If applicable):", None))
        self.Update3.setText(_translate("Form", "Update Current Profile", None))
        self.MGBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Please fill out the form below. In order to redeem a Money Gram, you should have an office in your '
                "country where you can pick up the cash near you. Please make sure you are familiar with the process and their local policies. "
                "Please make sure your name matches exactly what is written on your identification.</span></p></body></html>",
                None,
            )
        )
        self.PhoneText2.setText(_translate("Form", "Phone Number (If applicable):", None))
        self.Secret2.setText(_translate("Form", "Request secret question and answer(optional):", None))
        self.CityFunds2.setText(_translate("Form", "City and State/Province where funds will be picked up:", None))
        self.Create3.setText(_translate("Form", "Create New Profile", None))
        self.Remove4.setText(_translate("Form", "Remove Current Profile", None))
        self.Update4.setText(_translate("Form", "Update Current Profile", None))
        self.Create4.setText(_translate("Form", "Create New Profile", None))
        self.Save4.setText(_translate("Form", "Save Profile And Continue", None))
        self.DebitText.setText(_translate("Form", "Prepaid Debit Card", None))
        self.DebitInfoText.setText(_translate("Form", "Please list all of the funding information for your prepaid card:", None))
        self.DebitBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Every prepaid debit card has different methods of funding. Please explain how this card can be funded '
                "in the box below. Make sure you have as many options to fund as you know to be available such as locations that will fund it, "
                "online services for funding and so forth. Make sure that the funding method carries no risk of chargebacks for your own protection.</span></p></body></html>",
                None,
            )
        )
        self.Save5.setText(_translate("Form", "Save Profile And Continue", None))
        self.OtherFundText.setText(_translate("Form", "Other Funding Methods", None))
        self.Create5.setText(_translate("Form", "Create New Profile", None))
        self.OtherFundBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">There are other methods of funding such as Money Order, Bank Draft, Cashiers Check, PayPal, Payza, '
                "Credit Card Payments and so forth. For your protection we recommend proceeding with extreme caution if you choose to use any of these funding methods. "
                "Double Deposit eliminates a lot of the risk but can not protect you from charge backs after the deal completes, fake checks, or "
                "attempts to reveal personal information. "
                "The trusted methods were recommended because they are secure, protect your privacy and do not allow chargebacks. Your counter-party will "
                "also be warned if they choose this route. "
                "Please make sure you know, prescreen and trust your customer before proceeding.</span></p></body></html>",
                None,
            )
        )
        self.Update5.setText(_translate("Form", "Update Current Profile", None))
        self.Remove5.setText(_translate("Form", "Remove Current Profile", None))
        self.AltText.setText(_translate("Form", "Please list your alternative funding method:", None))
        self.NameCashText.setText(_translate("Form", "Your First and Last Name:", None))
        self.CountryCashText.setText(_translate("Form", "Country:", None))
        self.CashMailText.setText(_translate("Form", "Cash In The Mail", None))
        self.Remove6.setText(_translate("Form", "Remove Current Profile", None))
        self.Save6.setText(_translate("Form", "Save Profile And Continue", None))
        self.OtherInfoCash.setText(_translate("Form", "Other Information, email, contact info or special instructions (Optional):", None))
        self.Update6.setText(_translate("Form", "Update Current Profile", None))
        self.CashMailBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">It is perfectly secure to receive Cash In The Mail thanks to the nature of the double deposits. '
                "However, we highly recommend requiring that your buyers insure any packages. Not every country has a secure mail system and packages "
                "have known to get lost in the mail. "
                "Please consider leaving contact information so the party can contact you in any case.</span></p></body></html>",
                None,
            )
        )
        self.PhoneCashText.setText(_translate("Form", "Phone Number (Optional):", None))
        self.InsuranceCheckCash.setText(_translate("Form", "Require Insurance", None))
        self.CityCashText.setText(_translate("Form", "City/Province:", None))
        self.Create6.setText(_translate("Form", "Create New Profile", None))
        self.StateCashText.setText(_translate("Form", "State:", None))
        self.AddressTextCash.setText(_translate("Form", "Address:", None))
        self.ZipCashText.setText(_translate("Form", "Zip Code:", None))
        self.Remove7.setText(_translate("Form", "Remove Current Profile", None))
        self.OtherMailText.setText(_translate("Form", "Other Information, email, contact info or special instructions (Optional):", None))
        self.Update7.setText(_translate("Form", "Update Current Profile", None))
        self.InsuranceMailCheck.setText(_translate("Form", "Request Insurance", None))
        self.Save7.setText(_translate("Form", "Save Profile And Continue", None))
        self.StateMailText.setText(_translate("Form", "State:", None))
        self.MailingText.setText(_translate("Form", "Mailing Address", None))
        self.MailingBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">The mailing address is only used if you are purchasing items through the mail, receiving packages or '
                "if it is required for a business transaction. All personal information is kept private, and is only stored here on your computer.</span></p></body></html>",
                None,
            )
        )
        self.CityMailText.setText(_translate("Form", "City/Province:", None))
        self.NameTextMail.setText(_translate("Form", "Your First and Last Name:", None))
        self.Create7.setText(_translate("Form", "Create New Profile", None))
        self.AddressMailText.setText(_translate("Form", "Address:", None))
        self.ZipMailText.setText(_translate("Form", "Zip Code:", None))
        self.PhoneMailText.setText(_translate("Form", "Phone Number (Optional):", None))
        self.CountryMailText.setText(_translate("Form", "Country:", None))
        self.ContactBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">In case you need to supply other contact information for your transactions, you can supply all of that here. '
                "This is only shared upon request and if needed for the contract itself. All of this information is optional and it is kept private, "
                "only being saved locally on your computer.</span></p></body></html>",
                None,
            )
        )
        self.PhoneContactText.setText(_translate("Form", "Phone Number:", None))
        self.IRCContactText.setText(_translate("Form", "IRC Name:", None))
        self.Remove8.setText(_translate("Form", "Remove Current Profile", None))
        self.Update8.setText(_translate("Form", "Update Current Profile", None))
        self.ToxContactText.setText(_translate("Form", "Tox:", None))
        self.ContactText.setText(_translate("Form", "Other Contact Information", None))
        self.OtherContactText.setText(_translate("Form", "Other Contact Information:", None))
        self.EmailContactText.setText(_translate("Form", "Email Address:", None))
        self.Create8.setText(_translate("Form", "Create New Profile", None))
        self.Save8.setText(_translate("Form", "Save Profile And Continue", None))
        self.MaxIncreaseBuy.setItemText(0, _translate("Form", "5% Maximum Increase", None))
        self.MaxIncreaseBuy.setItemText(1, _translate("Form", "Custom Maximum Increase", None))
        self.perc6.setText(_translate("Form", "%", None))
        self.AmountText2.setText(_translate("Form", "Amount:", None))
        self.MaxDecreaseBuy.setItemText(0, _translate("Form", "25% Maximum Decrease", None))
        self.MaxDecreaseBuy.setItemText(1, _translate("Form", "No Limit", None))
        self.MaxDecreaseBuy.setItemText(2, _translate("Form", "Custom Maximum Decrease", None))
        self.DebitCheck2.setText(_translate("Form", "Prepaid Debit Card", None))
        self.perc9.setText(_translate("Form", "%", None))
        self.TimeLimitDays2.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays2.setItemText(1, _translate("Form", "Hours", None))
        self.NotesText2.setText(_translate("Form", "Notes/Extra Details:", None))
        self.ServiceCharge2.setItemText(0, _translate("Form", "2%", None))
        self.ServiceCharge2.setItemText(1, _translate("Form", "5%", None))
        self.ServiceCharge2.setItemText(2, _translate("Form", "10%", None))
        self.ServiceCharge2.setItemText(3, _translate("Form", "15%", None))
        self.ServiceCharge2.setItemText(4, _translate("Form", "20%", None))
        self.MyDepositText2.setText(_translate("Form", "My Deposit:", None))
        self.perc7.setText(_translate("Form", "%", None))
        self.BankWireCheck2.setText(_translate("Form", "Bank Wire/SEPA", None))
        self.CashMail2.setText(_translate("Form", "Cash In The Mail", None))
        self.MaxService2.setText(_translate("Form", "Maximum Service Charge:", None))
        self.ExchangeRate2.setText(_translate("Form", "Exchange Rate:", None))
        self.PayMentOptions2.setText(_translate("Form", "Payment Options:", None))
        self.CoinsForCashBuy.setText(_translate("Form", "Buy Coins With Cash", None))
        self.PriceTrackingTitle2.setText(_translate("Form", "Automatic price tracking:", None))
        self.MaxOrderBuy.setItemText(0, _translate("Form", "100% Maximum Buy Order", None))
        self.MaxOrderBuy.setItemText(1, _translate("Form", "50% Maximum Buy Order", None))
        self.MaxOrderBuy.setItemText(2, _translate("Form", "25% Maximum Buy Order", None))
        self.MaxOrderBuy.setItemText(3, _translate("Form", "Custom Maximum Buy Order", None))
        self.perc8.setText(_translate("Form", "%", None))
        self.OtherCheck2.setText(_translate("Form", "Other", None))
        self.RateBox2.setItemText(0, _translate("Form", "Market Price", None))
        self.RateBox2.setItemText(1, _translate("Form", "Price per coin", None))
        self.AmountUSD2.setItemText(0, _translate("Form", "USD", None))
        self.AmountUSD2.setItemText(1, _translate("Form", "Coins", None))
        self.TimeLimitText2.setText(_translate("Form", "Time Limit:", None))
        self.SaveContinue2.setText(_translate("Form", "Save And Continue", None))
        self.PriceText2.setText(_translate("Form", "Price:", None))
        self.DepositSettings2.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings2.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings2.setItemText(2, _translate("Form", "Request A Guarantor", None))
        self.MinOrderBuy.setItemText(0, _translate("Form", "25% Minimum Buy Order", None))
        self.MinOrderBuy.setItemText(1, _translate("Form", "50% Minimum Buy Order", None))
        self.MinOrderBuy.setItemText(2, _translate("Form", "100% Minimum Buy Order", None))
        self.MinOrderBuy.setItemText(3, _translate("Form", "Custom Minimum Buy Order", None))
        self.ShowAdvancedCashBuy.setText(_translate("Form", "Show Advanced Settings", None))
        self.LimitOrderText2.setText(_translate("Form", "Limit order sizes:", None))
        self.AgreeFund2.setText(_translate("Form", "You agree to fund using the selected methods below", None))
        self.TheirDepositText2.setText(_translate("Form", "Their Deposit:", None))
        self.MoneyGramCheck2.setText(_translate("Form", "MoneyGram", None))
        self.WUCheck2.setText(_translate("Form", "Western Union", None))
        self.ExplainCashBuy.setToolTip(_translate("Form", "Help", None))
        self.ExplainCashBuy.setText(_translate("Form", "?", None))
        self.SupplyAdditional2.setText(_translate("Form", "Supply Contact Information", None))
        self.SaveFuture2.setText(_translate("Form", "Save This Form", None))
        self.ClearForm2.setText(_translate("Form", "Clear Form", None))
        self.MyDepositUSD2.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD2.setItemText(1, _translate("Form", "Coins", None))
        self.TheirDepositUSD2.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD2.setItemText(1, _translate("Form", "Coins", None))
        self.PriceUSD2.setItemText(0, _translate("Form", "USD", None))
        self.Description1.setText(_translate("Form", "Description:", None))
        self.HireSomeoneText.setText(_translate("Form", "Hire Someone", None))
        self.NotesText3.setText(_translate("Form", "Notes/Extra Details:", None))
        self.JobSelect1.setItemText(0, _translate("Form", "One Time Job", None))
        self.JobSelect1.setItemText(1, _translate("Form", "Part Time Job", None))
        self.JobSelect1.setItemText(2, _translate("Form", "Full Time Job", None))
        self.SaveContinue3.setText(_translate("Form", "Save And Continue", None))
        self.JobTitle1.setText(_translate("Form", "Job Title:", None))
        self.RateSelect1.setItemText(0, _translate("Form", "Flat Rate", None))
        self.RateSelect1.setItemText(1, _translate("Form", "Pay By The Milestone", None))
        self.RateSelect1.setItemText(2, _translate("Form", "Pay by the Week", None))
        self.RateSelect1.setItemText(3, _translate("Form", "Pay by the Month", None))
        self.JobRate.setItemText(0, _translate("Form", "Flat Rate", None))
        self.JobRate.setItemText(1, _translate("Form", "Per Milestone", None))
        self.JobRate.setItemText(2, _translate("Form", "Per Week", None))
        self.JobRate.setItemText(3, _translate("Form", "Per Month", None))
        self.JobUSD.setItemText(0, _translate("Form", "USD", None))
        self.JobUSD.setItemText(1, _translate("Form", "Coins", None))
        self.EnableAutoPayCheck.setText(_translate("Form", "Enable Automatic Payments", None))
        self.RequireReportCheck.setText(_translate("Form", "Require Report Before Payment", None))
        self.ExplainHire.setToolTip(_translate("Form", "Help", None))
        self.ExplainHire.setText(_translate("Form", "?", None))
        self.SupplyAdditional3.setText(_translate("Form", "Supply Contact Information", None))
        self.SaveFuture3.setText(_translate("Form", "Save This Form", None))
        self.ClearForm3.setText(_translate("Form", "Clear Form", None))
        self.TheirDepositText3.setText(_translate("Form", "Their Deposit:", None))
        self.MyDepositUSD3.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD3.setItemText(1, _translate("Form", "Coins", None))
        self.DepositSettings3.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings3.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings3.setItemText(2, _translate("Form", "Make Me A Guarantor", None))
        self.TimeLimitDays3.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays3.setItemText(1, _translate("Form", "Hours", None))
        self.TheirDepositUSD3.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD3.setItemText(1, _translate("Form", "Coins", None))
        self.MyDepositText3.setText(_translate("Form", "My Deposit:", None))
        self.TimeLimitText3.setText(_translate("Form", "Time Limit:", None))
        self.RequestInterviewCheck.setText(_translate("Form", "Request Interview", None))
        self.RequireResumeCheck.setText(_translate("Form", "Require Resume", None))
        self.AcceptOneCheck.setText(_translate("Form", "Will Accept One Time Jobs", None))
        self.FindJobText.setText(_translate("Form", "Find A Job", None))
        self.SaveContinue4.setText(_translate("Form", "Save And Continue", None))
        self.LinkResumeText.setText(_translate("Form", "Link To Resume:", None))
        self.AcceptTempCheck.setText(_translate("Form", "Will Work Part Time", None))
        self.Notes4.setText(_translate("Form", "Notes/Extra Details:", None))
        self.DepositSettings4.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings4.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings4.setItemText(2, _translate("Form", "Request A Guarantor", None))
        self.ExplainFind.setToolTip(_translate("Form", "Help", None))
        self.ExplainFind.setText(_translate("Form", "?", None))
        self.JobTitle2.setText(_translate("Form", "Job Title:", None))
        self.Description2.setText(_translate("Form", "Description and Skills:", None))
        self.AcceptFullCheck.setText(_translate("Form", "Will Work Full Time ", None))
        self.AcceptInterviewCheck.setText(_translate("Form", "Will Do Interviews", None))
        self.uploadfree.setText(_translate("Form", "You can upload for free at ", None))
        self.sendspacelink.setText(_translate("Form", "www.sendspace.com", None))
        self.SupplyAdditional4.setText(_translate("Form", "Supply Contact Information", None))
        self.SaveFuture4.setText(_translate("Form", "Save This Form", None))
        self.ClearForm4.setText(_translate("Form", "Clear Form", None))
        self.MyDepositText4.setText(_translate("Form", "My Deposit:", None))
        self.MyDepositUSD4.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD4.setItemText(1, _translate("Form", "Coins", None))
        self.TimeLimitText4.setText(_translate("Form", "Time Limit:", None))
        self.TimeLimitDays4.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays4.setItemText(1, _translate("Form", "Hours", None))
        self.TheirDepositText4.setText(_translate("Form", "Their Deposit:", None))
        self.TheirDepositUSD4.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD4.setItemText(1, _translate("Form", "Coins", None))
        self.FindRate.setItemText(0, _translate("Form", "Flat Rate", None))
        self.FindRate.setItemText(1, _translate("Form", "Per Milestone", None))
        self.FindRate.setItemText(2, _translate("Form", "Per Week", None))
        self.FindRate.setItemText(3, _translate("Form", "Per Month", None))
        self.FindUSD.setItemText(0, _translate("Form", "USD", None))
        self.FindUSD.setItemText(1, _translate("Form", "Coins", None))
        self.SellImageText.setText(_translate("Form", "Image:", None))
        self.CountrySellSelect.setItemText(0, _translate("Form", "Will Ship to Any Country", None))
        self.CountrySellSelect.setItemText(1, _translate("Form", "Only Ship To Certain Countries", None))
        self.SellSomethingText.setText(_translate("Form", "Sell Something:", None))
        self.TheirDepositText5.setText(_translate("Form", "Their Deposit:", None))
        self.ExplainSell.setToolTip(_translate("Form", "Help", None))
        self.ExplainSell.setText(_translate("Form", "?", None))
        self.ShippingSellSelect.setItemText(0, _translate("Form", "Free Shipping", None))
        self.ShippingSellSelect.setItemText(1, _translate("Form", "Flat Rate", None))
        self.ShippingSellSelect.setItemText(2, _translate("Form", "Buyer Pays During Escrow", None))
        self.ShippingSellSelect.setItemText(3, _translate("Form", "Buyer Can Calculate Shipping", None))
        self.ShippingSellSelect.setItemText(4, _translate("Form", "No Shipping / Local Delivery", None))
        self.ShipToTextSell.setText(_translate("Form", "Will Ship To:", None))
        self.Notes5.setText(_translate("Form", "Notes/Extra Details:", None))
        self.MyDepositText5.setText(_translate("Form", "My Deposit:", None))
        self.DepositSettings5.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings5.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings5.setItemText(2, _translate("Form", "Make Them A Guarantor", None))
        self.SaveContinue5.setText(_translate("Form", "Save And Continue", None))
        self.TimeLimitText5.setText(_translate("Form", "Time Limit:", None))
        self.TimeLimitDays5.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays5.setItemText(1, _translate("Form", "Hours", None))
        self.ShippingSellText.setText(_translate("Form", "Shipping:", None))
        self.SellAttachImage.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.SellAttachImage.setText(_translate("Form", "Attach an Image", None))
        self.DescriptionSellText.setText(_translate("Form", "Description:", None))
        self.SellQuantity.setText(_translate("Form", "Quantity:", None))
        self.SellSelect.setItemText(0, _translate("Form", "Normal Sale", None))
        self.SellSelect.setItemText(1, _translate("Form", "Auction", None))
        self.BuyoutSellText.setText(_translate("Form", "Buyout Price:", None))
        self.BuyoutSellUSD.setItemText(0, _translate("Form", "USD", None))
        self.BuyoutSellUSD.setItemText(1, _translate("Form", "Coins", None))
        self.BidSellUSD.setItemText(0, _translate("Form", "USD", None))
        self.BidSellUSD.setItemText(1, _translate("Form", "Coins", None))
        self.BidSellText.setText(_translate("Form", "Starting Bid:", None))
        self.DurationSellDays.setItemText(0, _translate("Form", "Days", None))
        self.DurationSellText.setText(_translate("Form", "Duration:", None))
        self.RateSellUSD.setItemText(0, _translate("Form", "USD", None))
        self.RateSellUSD.setItemText(1, _translate("Form", "Coins", None))
        self.RateSellText.setText(_translate("Form", "Rate:", None))
        self.WeightSellText.setText(_translate("Form", "Weight:", None))
        self.WeightSellSelect.setItemText(0, _translate("Form", "Kilograms", None))
        self.WeightSellSelect.setItemText(1, _translate("Form", "Pounds", None))
        self.SupplyAdditional5.setText(_translate("Form", "Supply Contact Information", None))
        self.SaveFuture5.setText(_translate("Form", "Save This Form", None))
        self.ClearForm5.setText(_translate("Form", "Clear Form", None))
        self.MyDepositUSD5.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD5.setItemText(1, _translate("Form", "Coins", None))
        self.TheirDepositUSD5.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD5.setItemText(1, _translate("Form", "Coins", None))
        self.ShippingBuyText.setText(_translate("Form", "Shipping:", None))
        self.SaveContinue6.setText(_translate("Form", "Save And Continue", None))
        self.DurationBuyDays.setItemText(0, _translate("Form", "Days", None))
        self.BuySelect.setItemText(0, _translate("Form", "Normal Sale", None))
        self.BuySelect.setItemText(1, _translate("Form", "Reverse Auction", None))
        self.BidBuyText.setText(_translate("Form", "Starting Bid:", None))
        self.BuyImageText.setText(_translate("Form", "Image:", None))
        self.BuyText.setText(_translate("Form", "Buy Something:", None))
        self.DescriptionBuy.setText(_translate("Form", "Description:", None))
        self.BuyAttachImage.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.BuyAttachImage.setText(_translate("Form", "Attach an Image", None))
        self.MyDepositText6.setText(_translate("Form", "My Deposit:", None))
        self.ExplainBuy.setToolTip(_translate("Form", "Help", None))
        self.ExplainBuy.setText(_translate("Form", "?", None))
        self.TimeLimitText6.setText(_translate("Form", "Time Limit:", None))
        self.TimeLimitDays6.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays6.setItemText(1, _translate("Form", "Hours", None))
        self.ShipCountryBuy.setItemText(0, _translate("Form", "Can Ship From Any Country", None))
        self.ShipCountryBuy.setItemText(1, _translate("Form", "Only Ship From Certain Countries", None))
        self.TheirDepositText6.setText(_translate("Form", "Their Deposit:", None))
        self.BuyoutBuyUSD.setItemText(0, _translate("Form", "USD", None))
        self.BuyoutBuyUSD.setItemText(1, _translate("Form", "Coins", None))
        self.DurationBuyText.setText(_translate("Form", "Duration:", None))
        self.BidBuyUSD.setItemText(0, _translate("Form", "USD", None))
        self.BidBuyUSD.setItemText(1, _translate("Form", "Coins", None))
        self.BuyoutBuyText.setText(_translate("Form", "Buyout Price:", None))
        self.Notes6.setText(_translate("Form", "Notes/Extra Details:", None))
        self.DepositSettings6.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings6.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings6.setItemText(2, _translate("Form", "Make Me A Guarantor", None))
        self.DepositSettings6.setItemText(3, _translate("Form", "Make Them A Guarantor", None))
        self.ShipToBuyText.setText(_translate("Form", "Can Ship From:", None))
        self.ShippingCityBuy.setText(_translate("Form", "Only Supply Shipping City in Advance", None))
        self.LocalPickupBuy.setText(_translate("Form", "Request Local Pickup", None))
        self.SupplyAdditional6.setText(_translate("Form", "Supply Contact Information", None))
        self.SaveFuture6.setText(_translate("Form", "Save This Form", None))
        self.ClearForm6.setText(_translate("Form", "Clear Form", None))
        self.MyDepositUSD6.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD6.setItemText(1, _translate("Form", "Coins", None))
        self.TheirDepositUSD6.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD6.setItemText(1, _translate("Form", "Coins", None))
        self.TimeLimitDays7.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays7.setItemText(1, _translate("Form", "Hours", None))
        self.SupplyText.setText(_translate("Form", "Things I Have / Supply:", None))
        self.SaveContinue7.setText(_translate("Form", "Save And Continue", None))
        self.MyDepositText7.setText(_translate("Form", "My Deposit:", None))
        self.BarterText.setText(_translate("Form", "Barter:", None))
        self.TheirDepositText7.setText(_translate("Form", "Their Deposit:", None))
        self.ExplainBarter.setToolTip(_translate("Form", "Help", None))
        self.ExplainBarter.setText(_translate("Form", "?", None))
        self.TimeLimitText7.setText(_translate("Form", "Time Limit:", None))
        self.DepositSettings7.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings7.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.Notes7.setText(_translate("Form", "Notes/Extra Details:", None))
        self.DemandText.setText(_translate("Form", "Things I Want / Demand:", None))
        self.AddItemSupply.setText(_translate("Form", "Add Item", None))
        self.AddItemDemand.setText(_translate("Form", "Add Item", None))
        self.SupplyAdditional7.setText(_translate("Form", "Supply Contact Information", None))
        self.ClearForm7.setText(_translate("Form", "Clear Form", None))
        self.SaveFuture7.setText(_translate("Form", "Save This Form", None))
        self.OfferNotInList.setText(_translate("Form", "Allow parties to offer things not in my list", None))
        self.BuyMultiple.setText(_translate("Form", "They can buy multiple items in my list", None))
        self.RequestAll.setItemText(0, _translate("Form", "They Can Request All Items In My List", None))
        self.RequestAll.setItemText(1, _translate("Form", "Limit Number Of Items Per Order", None))
        self.MaxItems.setText(_translate("Form", "Maximum Items:", None))
        self.MyDepositUSD7.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD7.setItemText(1, _translate("Form", "Coins", None))
        self.TheirDepositUSD7.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD7.setItemText(1, _translate("Form", "Coins", None))
        self.EstValueText.setText(_translate("Form", "Estimated Value:", None))
        self.AddBrowserText.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">In the description, explain the commodity or service you have to trade. When estimating the value, '
                "please remember to describe how the value was determined. Include possible shipping cost, local or international, service charges or daily rates. "
                "For more help please click the &quot;?&quot; on the previous page.</span></p></body></html>",
                None,
            )
        )
        self.EstValueUSD.setItemText(0, _translate("Form", "USD", None))
        self.EstValueUSD.setItemText(1, _translate("Form", "Coins", None))
        self.AddItemToList.setText(_translate("Form", "Add Item", None))
        self.AddDescriptionText.setText(_translate("Form", "Description:", None))
        self.AddTitleText.setText(_translate("Form", "Title:", None))
        self.imgurlink.setText(_translate("Form", "www.imgur.com", None))
        self.AddLinkimages.setText(_translate("Form", "Link To Images (Optional):", None))
        self.RemoveItemFromList.setText(_translate("Form", "Remove Item", None))
        self.uploadimages.setText(_translate("Form", "You can upload images for free at ", None))
        self.AdditemText.setText(_translate("Form", "Add Item/Service To List:", None))
        self.AddShippingSelect.setItemText(0, _translate("Form", "Will Ship To Any Country", None))
        self.AddShippingSelect.setItemText(1, _translate("Form", "Only Ship To Certain Countries", None))
        self.AddMeetupCheck.setText(_translate("Form", "Can Meet In Person For Local Pickup", None))
        self.AddShipToText.setText(_translate("Form", "Will Ship To:", None))
        self.AddShippingText.setText(_translate("Form", "Shipping:", None))
        self.AddMaximumShipText.setText(_translate("Form", "Maximum Shipment Size:", None))
        self.AddMaxSizeSelect.setItemText(0, _translate("Form", "No Maximum Size", None))
        self.AddMaxSizeSelect.setItemText(1, _translate("Form", "Set Maximum Size/Cost", None))
        self.EstValueSelect.setItemText(0, _translate("Form", "Please Select...", None))
        self.EstValueSelect.setItemText(1, _translate("Form", "Flat Rate", None))
        self.EstValueSelect.setItemText(2, _translate("Form", "Per Kilogram", None))
        self.EstValueSelect.setItemText(3, _translate("Form", "Per Pound", None))
        self.EstValueSelect.setItemText(4, _translate("Form", "Per Day", None))
        self.EstValueSelect.setItemText(5, _translate("Form", "Per Week", None))
        self.EstValueSelect.setItemText(6, _translate("Form", "Per Month", None))
        self.AddMaxSizeUSD.setItemText(0, _translate("Form", "USD", None))
        self.AddMaxSizeUSD.setItemText(1, _translate("Form", "Coins", None))
        self.AddMaxSizeUSD.setItemText(2, _translate("Form", "Kilograms", None))
        self.AddMaxSizeUSD.setItemText(3, _translate("Form", "Pounds", None))
        self.AddNoteText.setText(_translate("Form", "Note: Shipping must be arranged seperately in escrow or is included in value", None))
        self.AddQuantityText.setText(_translate("Form", "Quantity:", None))
        self.DepositServiceSelect.setItemText(0, _translate("Form", "100% Minimum Deposit On Service Charge", None))
        self.DepositServiceSelect.setItemText(1, _translate("Form", "Set Custom Minimum Deposit On Service", None))
        self.QuantitySelect.setItemText(0, _translate("Form", "Kilograms", None))
        self.QuantitySelect.setItemText(1, _translate("Form", "Pounds", None))
        self.QuantitySelect.setItemText(2, _translate("Form", "Items", None))
        self.perc10.setText(_translate("Form", "%", None))
        self.SetMinUSD.setItemText(0, _translate("Form", "USD", None))
        self.SetMinUSD.setItemText(1, _translate("Form", "Coins", None))
        self.SetMinUSD.setItemText(2, _translate("Form", "Quantity", None))
        self.SetMaxUSD.setItemText(0, _translate("Form", "USD", None))
        self.SetMaxUSD.setItemText(1, _translate("Form", "Coins", None))
        self.SetMaxUSD.setItemText(2, _translate("Form", "Quantity", None))
        self.SetMinSelect.setItemText(0, _translate("Form", "No Minimum Order Size", None))
        self.SetMinSelect.setItemText(1, _translate("Form", "Set Minimum Order Size", None))
        self.SetMaxSelect.setItemText(0, _translate("Form", "No Maximum Order Size", None))
        self.SetMaxSelect.setItemText(1, _translate("Form", "Set Maximum Order Size", None))
        self.TheirSupply.setText(_translate("Form", "Things They Have / Supply:", None))
        self.Notes8.setText(_translate("Form", "Notes/Extra Details:", None))
        self.ExplainBarterOffer.setToolTip(_translate("Form", "Help", None))
        self.ExplainBarterOffer.setText(_translate("Form", "?", None))
        self.MakeOfferBarter.setText(_translate("Form", "Make Offer", None))
        self.TheirDemand.setText(_translate("Form", "Things They Want / Demand:", None))
        self.BarterOfferText.setText(_translate("Form", "Barter:", None))
        self.CancelBarter.setText(_translate("Form", "Cancel", None))
        self.SupplyAdditional8.setText(_translate("Form", "Supply Contact Information", None))
        self.MySupply.setText(_translate("Form", "Things I Am Offering:", None))
        self.MyDemand.setText(_translate("Form", "Things I Want:", None))
        self.TheirDepositUSD8.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD8.setItemText(1, _translate("Form", "Coins", None))
        self.TheirDepositText8.setText(_translate("Form", "Their Deposit:", None))
        self.TimeLimitDays8.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays8.setItemText(1, _translate("Form", "Hours", None))
        self.MyDepositUSD8.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD8.setItemText(1, _translate("Form", "Coins", None))
        self.DepositSettings8.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings8.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.TimeLimitText8.setText(_translate("Form", "Time Limit:", None))
        self.MyDepositText8.setText(_translate("Form", "My Deposit:", None))
        self.MyOfferNotInList.setText(_translate("Form", "Add/Offer Item Not In Their List", None))
        self.ClickItem.setText(_translate("Form", "Click on the items to move from one list to the other...", None))
        self.TheirDepositUSD9.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD9.setItemText(1, _translate("Form", "Coins", None))
        self.PythonUSD.setItemText(0, _translate("Form", "USD", None))
        self.PythonUSD.setItemText(1, _translate("Form", "Coins", None))
        self.Notes9.setText(_translate("Form", "Notes/Extra Details:", None))
        self.PythonText.setText(_translate("Form", "Python/Smart Contract:", None))
        self.TimeLimitText9.setText(_translate("Form", "Time Limit:", None))
        self.SaveFuture9.setText(_translate("Form", "Save This Form", None))
        self.DescriptionPython.setText(_translate("Form", "Description:", None))
        self.TimeLimitDays9.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays9.setItemText(1, _translate("Form", "Hours", None))
        self.MyDepositUSD9.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD9.setItemText(1, _translate("Form", "Coins", None))
        self.ExplainPython.setToolTip(_translate("Form", "Help", None))
        self.ExplainPython.setText(_translate("Form", "?", None))
        self.TheirDepositText9.setText(_translate("Form", "Their Deposit:", None))
        self.SaveContinue9.setText(_translate("Form", "Save And Continue", None))
        self.MyDepositText9.setText(_translate("Form", "My Deposit:", None))
        self.ClearForm9.setText(_translate("Form", "Clear Form", None))
        self.DepositSettings9.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings9.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.DepositSettings9.setItemText(2, _translate("Form", "Make Me A Guarantor", None))
        self.DepositSettings9.setItemText(3, _translate("Form", "Make Them A Guarantor", None))
        self.SupplyAdditional9.setText(_translate("Form", "Supply Contact Information", None))
        self.PythonSelect.setItemText(0, _translate("Form", "Select a contract...", None))
        self.PythonSelect.setItemText(1, _translate("Form", "Custom Python Contract", None))
        self.PythonWhoPays.setItemText(0, _translate("Form", "I pay this amount", None))
        self.PythonWhoPays.setItemText(1, _translate("Form", "The other party pays this amount", None))
        self.AttachImagePython.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.AttachImagePython.setText(_translate("Form", "Attach an Image", None))
        self.PythonImage.setText(_translate("Form", "Image:", None))
        self.PythonAmount.setText(_translate("Form", "Amount:", None))
        self.LoadFormPython.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.LoadFormPython.setText(_translate("Form", "Load Python File", None))
        self.CodeFormText.setText(_translate("Form", "Code For Offer Forms:", None))
        self.LoadMyPython.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.LoadMyPython.setText(_translate("Form", "Load Python File", None))
        self.CodeEscrowText.setText(_translate("Form", "Code Run During Escrow:", None))
        self.LoadTheirPython.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.LoadTheirPython.setText(_translate("Form", "Load Python File", None))
        self.CodeEscrowText2.setText(_translate("Form", "Code For Escrow Window:", None))
        self.PythonWarning.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Only approved code will be listed in the contract selection box. If you feel like your code is secure and creative, '
                "you may submit it to the lead developer for approval. Custom contracts are possible for experimentation and fun. Because it uses the internal Python "
                "interpreter in a P2P way, there is absolutely no limit to the amount of control you have with these contracts. Please click the &quot;?&quot; "
                "box for more explanation. "
                "You should have a good understanding of Halo's source code before proceeding.</span></p>\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; '
                'font-size:11px;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">WARNING:</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">Do not create or accept custom contracts unless you have an intimate understanding of programming, '
                "cryptocurrency, Python and Halo. "
                "Custom code can be used to completely control and compromise a computer. Anyone who tries to accept a custom contract will be warned. "
                "If you feel like your code is secure, you can have it reviewed for official approval and inclusion in the client.</span></p>\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; '
                'font-size:11px;"><br /></p></body></html>',
                None,
            )
        )
        self.ConfirmOrder.setText(_translate("Form", "Confirm Order", None))
        self.CoinsForCash_16.setText(_translate("Form", "Confirm Your Order:", None))
        self.ContactConfirm.setText(_translate("Form", "Additional Contact Info:", None))
        self.MailingConfirm.setText(_translate("Form", "Mailing Address:", None))
        self.BankConfirm.setText(_translate("Form", "Bank Wire/Direct Deposit:", None))
        self.WUConfirm.setText(_translate("Form", "Western Union:", None))
        self.MGConfirm.setText(_translate("Form", "MoneyGram:", None))
        self.DebitConfirm.setText(_translate("Form", "Prepaid Debit Cards:", None))
        self.OtherConfirm.setText(_translate("Form", "Other Funding Options:", None))
        self.ContactEdit.setText(_translate("Form", "Edit", None))
        self.AddressEdit.setText(_translate("Form", "Edit", None))
        self.BankEdit.setText(_translate("Form", "Edit", None))
        self.WUEdit.setText(_translate("Form", "Edit", None))
        self.DebitEdit.setText(_translate("Form", "Edit", None))
        self.MGEdit.setText(_translate("Form", "Edit", None))
        self.OtherEdit.setText(_translate("Form", "Edit", None))
        self.ConfirmTextEdit.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
                '<span style=" font-size:11px;">All sensitive information is encrypted and only shared with your counterparty once the contract is live. '
                "If the time limit expires, you both lose your deposits and escrow. This makes them unbreakable in theory. "
                "So please make sure you have enough time for your contract to complete.</span></p></body></html>",
                None,
            )
        )
        self.ContractSummary.setText(_translate("Form", "Contract:", None))
        self.MyDepositSummary.setText(_translate("Form", "My Deposit:", None))
        self.AmountSummary.setText(_translate("Form", "Amount:", None))
        self.TheirDepositSummary.setText(_translate("Form", "Their Deposit:", None))
        self.TimeLimitSummary.setText(_translate("Form", "Time Limit:", None))
        self.AutoAcceptValid.setText(_translate("Form", "Automatically Accept Valid Offers", None))
        self.AllowCounters.setText(_translate("Form", "Allow Counter-Offers", None))
        self.AllowChat.setText(_translate("Form", "Allow Chat In Escrow", None))
        self.AllowPriceTracking.setText(_translate("Form", "Allow Price Tracking", None))
        self.SendToText.setText(_translate("Form", "Send To:", None))
        self.SentToSelect.setItemText(0, _translate("Form", "Private Email/BitMessage/Coin Address...", None))
        self.TheirDepositText10.setText(_translate("Form", "Their Deposit:", None))
        self.SupplyAdditional10.setText(_translate("Form", "Supply Contact Information", None))
        self.MarketOrder.setText(_translate("Form", "Market Order:", None))
        self.TimeLimitDays10.setItemText(0, _translate("Form", "Days", None))
        self.TimeLimitDays10.setItemText(1, _translate("Form", "Hours", None))
        self.MyDepositText10.setText(_translate("Form", "My Deposit:", None))
        self.DepositSettings10.setItemText(0, _translate("Form", "Use Recommend Deposits and Settings", None))
        self.DepositSettings10.setItemText(1, _translate("Form", "Custom Deposits", None))
        self.Counter.setText(_translate("Form", "Counter-Offer", None))
        self.Accept.setText(_translate("Form", "Accept", None))
        self.Delete.setText(_translate("Form", "Delete", None))
        self.MarketExplanation.setToolTip(_translate("Form", "Help", None))
        self.MarketExplanation.setText(_translate("Form", "?", None))
        self.Text2.setText(_translate("Form", "Send Message:", None))
        self.MyDepositUSD10.setItemText(0, _translate("Form", "USD", None))
        self.MyDepositUSD10.setItemText(1, _translate("Form", "Coins", None))
        self.TimeLimitText10.setText(_translate("Form", "Time Limit:", None))
        self.Button1.setText(_translate("Form", "Full Size Image", None))
        self.TheirDepositUSD10.setItemText(0, _translate("Form", "USD", None))
        self.TheirDepositUSD10.setItemText(1, _translate("Form", "Coins", None))
        self.Button2.setText(_translate("Form", "Show User Profile", None))
        self.USD1.setItemText(0, _translate("Form", "USD", None))
        self.USD1.setItemText(1, _translate("Form", "Coins", None))
        self.Drop1.setItemText(0, _translate("Form", "Amount: 100", None))
        self.Drop1.setItemText(1, _translate("Form", "Coins", None))
        self.Drop3.setItemText(0, _translate("Form", "Payment: Western Union", None))
        self.Drop2.setItemText(0, _translate("Form", "Service Charge: 2%", None))
        self.USD3.setItemText(0, _translate("Form", "USD", None))
        self.USD3.setItemText(1, _translate("Form", "Coins", None))
        self.USD2.setItemText(0, _translate("Form", "USD", None))
        self.USD2.setItemText(1, _translate("Form", "Coins", None))
        self.Text1.setText(_translate("Form", "Link To Resume:", None))
        self.Link1.setText(_translate("Form", "You can upload for free at ", None))
        self.Link2.setText(_translate("Form", "www.sendspace.com", None))
        self.Attach.setToolTip(_translate("Form", "Attach an Image to your contract", None))
        self.Attach.setText(_translate("Form", "Attach Image", None))
        self.Drop4.setItemText(0, _translate("Form", "Per Milestone", None))
        self.CheckBox1.setText(_translate("Form", "Require Reports", None))
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

    def closeEvent(self, event):
        try:
            self.reply = {}
            self.Data = {}
            self.order = {}
        except Exception:
            pass


class MyApplication(QtWidgets.QApplication):
    def __init__(self, args):
        super(MyApplication, self).__init__(args)

    def notify(self, receiver, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.text() == "n":
                ui.changeindex += 1
                if ui.changeindex == 20:
                    ui.changeindex = 0
                ui.Pages.setCurrentIndex(ui.changeindex)
        return super(MyApplication, self).notify(receiver, event)


if __name__ == "__main__":
    import sys

    app = MyApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MyForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
