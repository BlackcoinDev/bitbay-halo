withMessagingMenu = False
try:
    from gi.repository import MessagingMenu, Notify

    withMessagingMenu = True
except ImportError:
    MessagingMenu = None

import datetime
import hashlib
import os
import pickle
import platform
import subprocess
import sys
import textwrap
import time
from time import gmtime, localtime, strftime

from Bitmessage.addresses import *
from Bitmessage.namecoin import ensureNamecoinOptions, namecoinConnection
from pyelliptic.openssl import OpenSSL

from .. import debug, l10n, qidenticon, shared
from ..debug import logger
from ..helper_sql import *
from .about import *
from .addaddressdialog import *
from .bitmessageui import *
from .connect import *
from .help import *
from .iconglossary import *
from .newaddressdialog import *
from .newchandialog import *
from .newsubscriptiondialog import *
from .regenerateaddresses import *
from .settings import *
from .specialaddressbehavior import *

try:
    from PyQt6 import QtCore, QtGui, QtWidgets
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    from PyQt6.QtWidgets import *

except Exception as err:
    print(
        "PyBitmessage requires PyQt unless you want to run it as a daemon and interact with it using the API. You can download it from http://www.riverbankcomputing.com/software/pyqt/download or by searching Google for 'PyQt Download' (without quotes)."
    )
    print("Error message:", err)
    sys.exit()


def _translate(context, text):
    return QtWidgets.QApplication.translate(context, text)


def identiconize(address):
    size = 48

    # If you include another identicon library, please generate an
    # example identicon with the following md5 hash:
    # 3fd4bf901b9d4ea1394f0fb358725b28

    try:
        identicon_lib = shared.config.get("bitmessagesettings", "identiconlib")
    except:
        # default to qidenticon_two_x
        identicon_lib = "qidenticon_two_x"

    # As an 'identiconsuffix' you could put "@bitmessge.ch" or "@bm.addr" to make it compatible with other identicon generators. (Note however, that E-Mail programs might convert the BM-address to lowercase first.)
    # It can be used as a pseudo-password to salt the generation of the identicons to decrease the risk
    # of attacks where someone creates an address to mimic someone else's identicon.
    identiconsuffix = shared.config.get("bitmessagesettings", "identiconsuffix")

    if not shared.config.getboolean("bitmessagesettings", "useidenticons"):
        idcon = QtGui.QIcon()
        return idcon

    if identicon_lib[: len("qidenticon")] == "qidenticon":
        # print identicon_lib
        # originally by:
        # :Author:Shin Adachi <shn@glucose.jp>
        # Licesensed under FreeBSD License.
        # stripped from PIL and uses QT instead (by sendiulo, same license)
        from .. import qidenticon

        hash = hashlib.md5((addBMIfNotPresent(address) + identiconsuffix).encode("utf-8")).hexdigest()
        use_two_colors = identicon_lib[: len("qidenticon_two")] == "qidenticon_two"
        opacity = (
            int(
                not (
                    (identicon_lib == "qidenticon_x")
                    | (identicon_lib == "qidenticon_two_x")
                    | (identicon_lib == "qidenticon_b")
                    | (identicon_lib == "qidenticon_two_b")
                )
            )
            * 255
        )
        penwidth = 0
        image = qidenticon.render_identicon(int(hash, 16), size, use_two_colors, opacity, penwidth)
        # filename = './images/identicons/'+hash+'.png'
        # image.save(filename)
        idcon = QtGui.QIcon()
        idcon.addPixmap(image, QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        return idcon
    elif identicon_lib == "pydenticon":
        # print identicon_lib
        # Here you could load pydenticon.py (just put it in the "src" folder of your Bitmessage source)
        from pydenticon import Pydenticon

        # It is not included in the source, because it is licensed under GPLv3
        # GPLv3 is a copyleft license that would influence our licensing
        # Find the source here: http://boottunes.googlecode.com/svn-history/r302/trunk/src/pydenticon.py
        # note that it requires PIL to be installed: http://www.pythonware.com/products/pil/
        idcon_render = Pydenticon(addBMIfNotPresent(address) + identiconsuffix, size * 3)
        rendering = idcon_render._render()
        data = rendering.convert("RGBA").tostring("raw", "RGBA")
        qim = QImage(data, size, size, QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        idcon = QtGui.QIcon()
        idcon.addPixmap(pix, QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        return idcon


def avatarize(address):
    """
    loads a supported image for the given address' hash form 'avatars' folder
    falls back to default avatar if 'default.*' file exists
    falls back to identiconize(address)
    """
    idcon = QtGui.QIcon()
    hash = hashlib.md5(addBMIfNotPresent(address).encode("utf-8")).hexdigest()
    str_broadcast_subscribers = "[Broadcast subscribers]"
    if address == str_broadcast_subscribers:
        # don't hash [Broadcast subscribers]
        hash = address
    # http://pyqt.sourceforge.net/Docs/PyQt4/qimagereader.html#supportedImageFormats
    # print QImageReader.supportedImageFormats ()
    # QImageReader.supportedImageFormats ()
    extensions = ["PNG", "GIF", "JPG", "JPEG", "SVG", "BMP", "MNG", "PBM", "PGM", "PPM", "TIFF", "XBM", "XPM", "TGA"]
    # try to find a specific avatar
    for ext in extensions:
        lower_hash = shared.appdata + "avatars/" + hash + "." + ext.lower()
        upper_hash = shared.appdata + "avatars/" + hash + "." + ext.upper()
        if os.path.isfile(lower_hash):
            # print 'found avatar of ', address
            idcon.addFile(lower_hash)
            return idcon
        elif os.path.isfile(upper_hash):
            # print 'found avatar of ', address
            idcon.addFile(upper_hash)
            return idcon
    # if we haven't found any, try to find a default avatar
    for ext in extensions:
        lower_default = shared.appdata + "avatars/" + "default." + ext.lower()
        upper_default = shared.appdata + "avatars/" + "default." + ext.upper()
        if os.path.isfile(lower_default):
            default = lower_default
            idcon.addFile(lower_default)
            return idcon
        elif os.path.isfile(upper_default):
            default = upper_default
            idcon.addFile(upper_default)
            return idcon
    # If no avatar is found
    return identiconize(address)


class MyForm(QtWidgets.QMainWindow):

    # sound type constants
    SOUND_NONE = 0
    SOUND_KNOWN = 1
    SOUND_UNKNOWN = 2
    SOUND_CONNECTED = 3
    SOUND_DISCONNECTED = 4
    SOUND_CONNECTION_GREEN = 5

    # the last time that a message arrival sound was played
    lastSoundTime = datetime.datetime.now() - datetime.timedelta(days=1)

    # the maximum frequency of message sounds in seconds
    maxSoundFrequencySec = 60

    str_broadcast_subscribers = "[Broadcast subscribers]"
    str_chan = "[chan]"

    def init_file_menu(self):
        self.ui.actionExit.triggered.connect(self.quit)
        self.ui.actionManageKeys.triggered.connect(self.click_actionManageKeys)
        self.ui.actionDeleteAllTrashedMessages.triggered.connect(self.click_actionDeleteAllTrashedMessages)
        self.ui.actionRegenerateDeterministicAddresses.triggered.connect(
            self.click_actionRegenerateDeterministicAddresses
        )
        self.ui.actionJoinChan.triggered.connect(self.click_actionJoinChan)  # also used for creating chans.
        self.ui.pushButtonNewAddress.clicked.connect(self.click_NewAddressDialog)
        self.ui.comboBoxSendFrom.activated.connect(self.redrawLabelFrom)
        self.ui.pushButtonAddAddressBook.clicked.connect(self.click_pushButtonAddAddressBook)
        self.ui.pushButtonAddSubscription.clicked.connect(self.click_pushButtonAddSubscription)
        self.ui.pushButtonAddBlacklist.clicked.connect(self.click_pushButtonAddBlacklist)
        self.ui.pushButtonSend.clicked.connect(self.click_pushButtonSend)
        self.ui.pushButtonLoadFromAddressBook.clicked.connect(self.click_pushButtonLoadFromAddressBook)
        self.ui.pushButtonFetchNamecoinID.clicked.connect(self.click_pushButtonFetchNamecoinID)
        self.ui.radioButtonBlacklist.clicked.connect(self.click_radioButtonBlacklist)
        self.ui.radioButtonWhitelist.clicked.connect(self.click_radioButtonWhitelist)
        self.ui.pushButtonStatusIcon.clicked.connect(self.click_pushButtonStatusIcon)
        self.ui.actionSettings.triggered.connect(self.click_actionSettings)
        self.ui.actionAbout.triggered.connect(self.click_actionAbout)
        self.ui.actionHelp.triggered.connect(self.click_actionHelp)

    def init_inbox_popup_menu(self):
        # Popup menu for the Inbox tab
        self.ui.inboxContextMenuToolbar = QtWidgets.QToolBar()
        # Actions
        self.actionReply = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "Reply"), self.on_action_InboxReply
        )
        self.actionAddSenderToAddressBook = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "Add sender to your Address Book"), self.on_action_InboxAddSenderToAddressBook
        )
        self.actionTrashInboxMessage = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "Move to Trash"), self.on_action_InboxTrash
        )
        self.actionForceHtml = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "View HTML code as formatted text"), self.on_action_InboxMessageForceHtml
        )
        self.actionSaveMessageAs = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "Save message as."), self.on_action_InboxSaveMessageAs
        )
        self.actionMarkUnread = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "Mark Unread"), self.on_action_InboxMarkUnread
        )
        self.ui.tableWidgetInbox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidgetInbox.customContextMenuRequested.connect(self.on_context_menuInbox)
        self.popMenuInbox = QtWidgets.QMenu(self)
        self.popMenuInbox.addAction(self.actionForceHtml)
        self.popMenuInbox.addAction(self.actionMarkUnread)
        self.popMenuInbox.addSeparator()
        self.popMenuInbox.addAction(self.actionReply)
        self.popMenuInbox.addAction(self.actionAddSenderToAddressBook)
        self.popMenuInbox.addSeparator()
        self.popMenuInbox.addAction(self.actionSaveMessageAs)
        self.popMenuInbox.addAction(self.actionTrashInboxMessage)

    def init_identities_popup_menu(self):
        # Popup menu for the Your Identities tab
        self.ui.addressContextMenuToolbar = QtWidgets.QToolBar()
        # Actions
        self.actionNew = self.ui.addressContextMenuToolbar.addAction(
            _translate("MainWindow", "New"), self.on_action_YourIdentitiesNew
        )
        self.actionEnable = self.ui.addressContextMenuToolbar.addAction(
            _translate("MainWindow", "Enable"), self.on_action_YourIdentitiesEnable
        )
        self.actionDisable = self.ui.addressContextMenuToolbar.addAction(
            _translate("MainWindow", "Disable"), self.on_action_YourIdentitiesDisable
        )
        self.actionSetAvatar = self.ui.addressContextMenuToolbar.addAction(
            _translate("MainWindow", "Set avatar."), self.on_action_YourIdentitiesSetAvatar
        )
        self.actionClipboard = self.ui.addressContextMenuToolbar.addAction(
            _translate("MainWindow", "Copy address to clipboard"), self.on_action_YourIdentitiesClipboard
        )
        self.actionSpecialAddressBehavior = self.ui.addressContextMenuToolbar.addAction(
            _translate("MainWindow", "Special address behavior."), self.on_action_SpecialAddressBehaviorDialog
        )
        self.ui.tableWidgetYourIdentities.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidgetYourIdentities.customContextMenuRequested.connect(self.on_context_menuYourIdentities)
        self.popMenu = QtWidgets.QMenu(self)
        self.popMenu.addAction(self.actionNew)
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.actionClipboard)
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.actionEnable)
        self.popMenu.addAction(self.actionDisable)
        self.popMenu.addAction(self.actionSetAvatar)
        self.popMenu.addAction(self.actionSpecialAddressBehavior)

    def init_addressbook_popup_menu(self):
        # Popup menu for the Address Book page
        self.ui.addressBookContextMenuToolbar = QtWidgets.QToolBar()
        # Actions
        self.actionAddressBookSend = self.ui.addressBookContextMenuToolbar.addAction(
            _translate("MainWindow", "Send message to this address"), self.on_action_AddressBookSend
        )
        self.actionAddressBookClipboard = self.ui.addressBookContextMenuToolbar.addAction(
            _translate("MainWindow", "Copy address to clipboard"), self.on_action_AddressBookClipboard
        )
        self.actionAddressBookSubscribe = self.ui.addressBookContextMenuToolbar.addAction(
            _translate("MainWindow", "Subscribe to this address"), self.on_action_AddressBookSubscribe
        )
        self.actionAddressBookSetAvatar = self.ui.addressBookContextMenuToolbar.addAction(
            _translate("MainWindow", "Set avatar."), self.on_action_AddressBookSetAvatar
        )
        self.actionAddressBookNew = self.ui.addressBookContextMenuToolbar.addAction(
            _translate("MainWindow", "Add New Address"), self.on_action_AddressBookNew
        )
        self.actionAddressBookDelete = self.ui.addressBookContextMenuToolbar.addAction(
            _translate("MainWindow", "Delete"), self.on_action_AddressBookDelete
        )
        self.ui.tableWidgetAddressBook.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidgetAddressBook.customContextMenuRequested.connect(self.on_context_menuAddressBook)
        self.popMenuAddressBook = QtWidgets.QMenu(self)
        self.popMenuAddressBook.addAction(self.actionAddressBookSend)
        self.popMenuAddressBook.addAction(self.actionAddressBookClipboard)
        self.popMenuAddressBook.addAction(self.actionAddressBookSubscribe)
        self.popMenuAddressBook.addAction(self.actionAddressBookSetAvatar)
        self.popMenuAddressBook.addSeparator()
        self.popMenuAddressBook.addAction(self.actionAddressBookNew)
        self.popMenuAddressBook.addAction(self.actionAddressBookDelete)

    def init_subscriptions_popup_menu(self):
        # Popup menu for the Subscriptions page
        self.ui.subscriptionsContextMenuToolbar = QtWidgets.QToolBar()
        # Actions
        self.actionsubscriptionsNew = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "New"), self.on_action_SubscriptionsNew
        )
        self.actionsubscriptionsDelete = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Delete"), self.on_action_SubscriptionsDelete
        )
        self.actionsubscriptionsClipboard = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Copy address to clipboard"), self.on_action_SubscriptionsClipboard
        )
        self.actionsubscriptionsEnable = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Enable"), self.on_action_SubscriptionsEnable
        )
        self.actionsubscriptionsDisable = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Disable"), self.on_action_SubscriptionsDisable
        )
        self.actionsubscriptionsSetAvatar = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Set avatar."), self.on_action_SubscriptionsSetAvatar
        )
        self.ui.tableWidgetSubscriptions.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidgetSubscriptions.customContextMenuRequested.connect(self.on_context_menuSubscriptions)
        self.popMenuSubscriptions = QtWidgets.QMenu(self)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsNew)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsDelete)
        self.popMenuSubscriptions.addSeparator()
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsEnable)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsDisable)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsSetAvatar)
        self.popMenuSubscriptions.addSeparator()
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsClipboard)

    def init_sent_popup_menu(self):
        # Popup menu for the Sent page
        self.ui.sentContextMenuToolbar = QtWidgets.QToolBar()
        # Actions
        self.actionTrashSentMessage = self.ui.sentContextMenuToolbar.addAction(
            _translate("MainWindow", "Move to Trash"), self.on_action_SentTrash
        )
        self.actionSentClipboard = self.ui.sentContextMenuToolbar.addAction(
            _translate("MainWindow", "Copy destination address to clipboard"), self.on_action_SentClipboard
        )
        self.actionForceSend = self.ui.sentContextMenuToolbar.addAction(
            _translate("MainWindow", "Force send"), self.on_action_ForceSend
        )
        self.ui.tableWidgetSent.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidgetSent.customContextMenuRequested.connect(self.on_context_menuSent)
        # self.popMenuSent = QtWidgets.QMenu( self )
        # self.popMenuSent.addAction( self.actionSentClipboard )
        # self.popMenuSent.addAction( self.actionTrashSentMessage )

    def init_blacklist_popup_menu(self):
        # Popup menu for the Blacklist page
        self.ui.blacklistContextMenuToolbar = QtWidgets.QToolBar()
        # Actions
        self.actionBlacklistNew = self.ui.blacklistContextMenuToolbar.addAction(
            _translate("MainWindow", "Add new entry"), self.on_action_BlacklistNew
        )
        self.actionBlacklistDelete = self.ui.blacklistContextMenuToolbar.addAction(
            _translate("MainWindow", "Delete"), self.on_action_BlacklistDelete
        )
        self.actionBlacklistClipboard = self.ui.blacklistContextMenuToolbar.addAction(
            _translate("MainWindow", "Copy address to clipboard"), self.on_action_BlacklistClipboard
        )
        self.actionBlacklistEnable = self.ui.blacklistContextMenuToolbar.addAction(
            _translate("MainWindow", "Enable"), self.on_action_BlacklistEnable
        )
        self.actionBlacklistDisable = self.ui.blacklistContextMenuToolbar.addAction(
            _translate("MainWindow", "Disable"), self.on_action_BlacklistDisable
        )
        self.actionBlacklistSetAvatar = self.ui.blacklistContextMenuToolbar.addAction(
            _translate("MainWindow", "Set avatar."), self.on_action_BlacklistSetAvatar
        )
        self.ui.tableWidgetBlacklist.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidgetBlacklist.customContextMenuRequested.connect(self.on_context_menuBlacklist)
        self.popMenuBlacklist = QtWidgets.QMenu(self)
        # self.popMenuBlacklist.addAction( self.actionBlacklistNew )
        self.popMenuBlacklist.addAction(self.actionBlacklistDelete)
        self.popMenuBlacklist.addSeparator()
        self.popMenuBlacklist.addAction(self.actionBlacklistClipboard)
        self.popMenuBlacklist.addSeparator()
        self.popMenuBlacklist.addAction(self.actionBlacklistEnable)
        self.popMenuBlacklist.addAction(self.actionBlacklistDisable)
        self.popMenuBlacklist.addAction(self.actionBlacklistSetAvatar)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ask the user if we may delete their old version 1 addresses if they
        # have any.
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != "bitmessagesettings":
                status, addressVersionNumber, streamNumber, hash = decodeAddress(addressInKeysFile)
                if addressVersionNumber == 1:
                    displayMsg = _translate(
                        "MainWindow",
                        "One of your addresses, %1, is an old version 1 address. Version 1 addresses are no longer supported. "
                        + "May we delete it now?",
                    ).replace("%1", addressInKeysFile)
                    reply = QtWidgets.QMessageBox.question(
                        self, "Message", displayMsg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No
                    )
                    if reply == QtWidgets.QMessageBox.Yes:
                        shared.config.remove_section(addressInKeysFile)
                        with open(shared.appdata + "keys.dat", "w") as configfile:
                            shared.config.write(configfile)

        # Configure Bitmessage to start on startup (or remove the
        # configuration) based on the setting in the keys.dat file
        if "win32" in sys.platform or "win64" in sys.platform:
            # Auto-startup for Windows
            RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            self.settings = QSettings(RUN_PATH, QSettings.NativeFormat)
            self.settings.remove(
                "PyBitmessage"
            )  # In case the user moves the program and the registry entry is no longer valid, this will delete the old registry entry.
            if shared.config.getboolean("bitmessagesettings", "startonlogon"):
                self.settings.setValue("PyBitmessage", sys.argv[0])
        elif "darwin" in sys.platform:
            # startup for mac
            pass
        elif "linux" in sys.platform:
            # startup for linux
            pass

        self.totalNumberOfBytesReceived = 0
        self.totalNumberOfBytesSent = 0

        self.ui.labelSendBroadcastWarning.setVisible(False)

        self.timer = QtCore.QTimer()
        self.timer.start(2000)  # milliseconds
        self.timer.timeout.connect(self.runEveryTwoSeconds)

        self.init_file_menu()
        self.init_inbox_popup_menu()
        self.init_identities_popup_menu()
        self.init_addressbook_popup_menu()
        self.init_subscriptions_popup_menu()
        self.init_sent_popup_menu()
        self.init_blacklist_popup_menu()

        # Initialize the user's list of addresses on the 'Your Identities' tab.
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != "bitmessagesettings":
                isEnabled = shared.config.getboolean(addressInKeysFile, "enabled")
                newItem = QtWidgets.QTableWidgetItem(str(shared.config.get(addressInKeysFile, "label"), "utf-8)"))
                if not isEnabled:
                    newItem.setTextColor(QtGui.QColor(128, 128, 128))
                self.ui.tableWidgetYourIdentities.insertRow(0)
                newItem.setIcon(avatarize(addressInKeysFile))
                self.ui.tableWidgetYourIdentities.setItem(0, 0, newItem)
                newItem = QtWidgets.QTableWidgetItem(addressInKeysFile)
                newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                if shared.safeConfigGetBoolean(addressInKeysFile, "chan"):
                    newItem.setTextColor(QtGui.QColor(216, 119, 0))  # orange
                if not isEnabled:
                    newItem.setTextColor(QtGui.QColor(128, 128, 128))
                if shared.safeConfigGetBoolean(addressInKeysFile, "mailinglist"):
                    newItem.setTextColor(QtWidgets.QColor(137, 4, 177))  # magenta
                self.ui.tableWidgetYourIdentities.setItem(0, 1, newItem)
                newItem = QtWidgets.QTableWidgetItem(str(decodeAddress(addressInKeysFile)[2]))
                newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                if not isEnabled:
                    newItem.setTextColor(QtGui.QColor(128, 128, 128))
                self.ui.tableWidgetYourIdentities.setItem(0, 2, newItem)
                if isEnabled:
                    status, addressVersionNumber, streamNumber, hash = decodeAddress(addressInKeysFile)

        # Load inbox from messages database file
        self.loadInbox()

        # Load Sent items from database
        self.loadSent()

        # Initialize the address book
        self.rerenderAddressBook()

        # Initialize the Subscriptions
        self.rerenderSubscriptions()

        # Initialize the inbox search
        self.ui.inboxSearchLineEdit.returnPressed.connect(self.inboxSearchLineEditPressed)

        # Initialize the sent search
        self.ui.sentSearchLineEdit.returnPressed.connect(self.sentSearchLineEditPressed)

        # Initialize the Blacklist or Whitelist
        if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
            self.loadBlackWhiteList()
        else:
            self.ui.tabWidget.setTabText(6, "Whitelist")
            self.ui.radioButtonWhitelist.click()
            self.loadBlackWhiteList()

        self.ui.tableWidgetYourIdentities.itemChanged.connect(self.tableWidgetYourIdentitiesItemChanged)
        self.ui.tableWidgetAddressBook.itemChanged.connect(self.tableWidgetAddressBookItemChanged)
        self.ui.tableWidgetSubscriptions.itemChanged.connect(self.tableWidgetSubscriptionsItemChanged)
        self.ui.tableWidgetInbox.itemSelectionChanged.connect(self.tableWidgetInboxItemClicked)
        self.ui.tableWidgetSent.itemSelectionChanged.connect(self.tableWidgetSentItemClicked)

        # Put the colored icon on the status bar
        # self.ui.pushButtonStatusIcon.setIcon(QIcon(":/newPrefix/images/yellowicon.png"))
        self.statusbar = self.statusBar()
        self.statusbar.insertPermanentWidget(0, self.ui.pushButtonStatusIcon)
        self.ui.labelStartupTime.setText(
            _translate("MainWindow", "Since startup on %1").replace("%1", l10n.formatTimestamp())
        )
        self.numberOfMessagesProcessed = 0
        self.numberOfBroadcastsProcessed = 0
        self.numberOfPubkeysProcessed = 0

        # Set the icon sizes for the identicons
        identicon_size = 3 * 7
        self.ui.tableWidgetInbox.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetSent.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetYourIdentities.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetSubscriptions.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetAddressBook.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetBlacklist.setIconSize(QtCore.QSize(identicon_size, identicon_size))

        self.UISignalThread = UISignaler()
        self.UISignalThread.writeNewAddressToTable.connect(self.writeNewAddressToTable)
        self.UISignalThread.updateStatusBar.connect(self.updateStatusBar)
        self.UISignalThread.updateSentItemStatusByHash.connect(self.updateSentItemStatusByHash)
        self.UISignalThread.updateSentItemStatusByAckdata.connect(self.updateSentItemStatusByAckdata)
        self.UISignalThread.displayNewInboxMessage.connect(self.displayNewInboxMessage)
        self.UISignalThread.displayNewSentMessage.connect(self.displayNewSentMessage)
        self.UISignalThread.updateNetworkStatusTab.connect(self.updateNetworkStatusTab)
        self.UISignalThread.updateNumberOfMessagesProcessed.connect(self.updateNumberOfMessagesProcessed)
        self.UISignalThread.updateNumberOfPubkeysProcessed.connect(self.updateNumberOfPubkeysProcessed)
        self.UISignalThread.updateNumberOfBroadcastsProcessed.connect(self.updateNumberOfBroadcastsProcessed)
        self.UISignalThread.setStatusIcon.connect(self.setStatusIcon)
        self.UISignalThread.changedInboxUnread.connect(self.changedInboxUnread)
        self.UISignalThread.rerenderInboxFromLabels.connect(self.rerenderInboxFromLabels)
        self.UISignalThread.rerenderSentToLabels.connect(self.rerenderSentToLabels)
        self.UISignalThread.rerenderAddressBook.connect(self.rerenderAddressBook)
        self.UISignalThread.rerenderSubscriptions.connect(self.rerenderSubscriptions)
        self.UISignalThread.removeInboxRowByMsgid.connect(self.removeInboxRowByMsgid)
        self.UISignalThread.displayAlert.connect(self.displayAlert)
        self.UISignalThread.start()

        # Below this point, it would be good if all of the necessary global data
        # structures were initialized.

        self.rerenderComboBoxSendFrom()

        # Check to see whether we can connect to namecoin. Hide the 'Fetch Namecoin ID' button if we can't.
        try:
            options = {}
            options["type"] = shared.config.get("bitmessagesettings", "namecoinrpctype")
            options["host"] = shared.config.get("bitmessagesettings", "namecoinrpchost")
            options["port"] = shared.config.get("bitmessagesettings", "namecoinrpcport")
            options["user"] = shared.config.get("bitmessagesettings", "namecoinrpcuser")
            options["password"] = shared.config.get("bitmessagesettings", "namecoinrpcpassword")
            nc = namecoinConnection(options)
            if nc.test()[0] == "failed":
                self.ui.pushButtonFetchNamecoinID.hide()
        except:
            print("There was a problem testing for a Namecoin daemon. Hiding the Fetch Namecoin ID button")
            self.ui.pushButtonFetchNamecoinID.hide()

    # Show or hide the application window after clicking an item within the
    # tray icon or, on Windows, the try icon itself.
    def appIndicatorShowOrHideWindow(self):
        if not self.actionShow.isChecked():
            self.hide()
        else:
            if sys.platform[0:3] == "win":
                self.setWindowFlags(Qt.Window)
            # else:
            # self.showMaximized()
            self.show()
            self.setWindowState(
                self.windowState() & ~QtCore.Qt.WindowState.WindowMinimized | QtCore.Qt.WindowState.WindowActive
            )
            self.activateWindow()

    # pointer to the application
    # app = None
    # The most recent message
    newMessageItem = None

    # The most recent broadcast
    newBroadcastItem = None

    # show the application window
    def appIndicatorShow(self):
        if self.actionShow is None:
            return
        if not self.actionShow.isChecked():
            self.actionShow.setChecked(True)
            self.appIndicatorShowOrHideWindow()

    # unchecks the show item on the application indicator
    def appIndicatorHide(self):
        if self.actionShow is None:
            return
        if self.actionShow.isChecked():
            self.actionShow.setChecked(False)
            self.appIndicatorShowOrHideWindow()

    # application indicator show or hide
    """# application indicator show or hide
    def appIndicatorShowBitmessage(self):
        #if self.actionShow == None:
        #    return
        print(self.actionShow.isChecked())
        if not self.actionShow.isChecked():
            self.hide()
            #self.setWindowState(self.windowState() & QtCore.Qt.WindowState.WindowMinimized)
        else:
            self.appIndicatorShowOrHideWindow()"""

    # Show the program window and select inbox tab
    def appIndicatorInbox(self, mm_app, source_id):
        self.appIndicatorShow()
        # select inbox
        self.ui.tabWidget.setCurrentIndex(0)
        selectedItem = None
        if source_id == "Subscriptions":
            # select unread broadcast
            if self.newBroadcastItem is not None:
                selectedItem = self.newBroadcastItem
                self.newBroadcastItem = None
        else:
            # select unread message
            if self.newMessageItem is not None:
                selectedItem = self.newMessageItem
                self.newMessageItem = None
        # make it the current item
        if selectedItem is not None:
            try:
                self.ui.tableWidgetInbox.setCurrentItem(selectedItem)
            except Exception:
                self.ui.tableWidgetInbox.setCurrentCell(0, 0)
            self.tableWidgetInboxItemClicked()
        else:
            # just select the first item
            self.ui.tableWidgetInbox.setCurrentCell(0, 0)
            self.tableWidgetInboxItemClicked()

    # Show the program window and select send tab
    def appIndicatorSend(self):
        self.appIndicatorShow()
        self.ui.tabWidget.setCurrentIndex(1)

    # Show the program window and select subscriptions tab
    def appIndicatorSubscribe(self):
        self.appIndicatorShow()
        self.ui.tabWidget.setCurrentIndex(4)

    # Show the program window and select the address book tab
    def appIndicatorAddressBook(self):
        self.appIndicatorShow()
        self.ui.tabWidget.setCurrentIndex(5)

    # Load Sent items from database
    def loadSent(self, where="", what=""):
        what = "%" + what + "%"
        if where == "To":
            where = "toaddress"
        elif where == "From":
            where = "fromaddress"
        elif where == "Subject":
            where = "subject"
        elif where == "Message":
            where = "message"
        else:
            where = "toaddress || fromaddress || subject || message"

        sqlStatement = """
            SELECT toaddress, fromaddress, subject, status, ackdata, lastactiontime 
            FROM sent WHERE folder="sent" AND %s LIKE ? 
            ORDER BY lastactiontime
            """ % (
            where,
        )

        while self.ui.tableWidgetSent.rowCount() > 0:
            self.ui.tableWidgetSent.removeRow(0)

        queryreturn = sqlQuery(sqlStatement, what)
        for row in queryreturn:
            toAddress, fromAddress, subject, status, ackdata, lastactiontime = row
            subject = shared.fixPotentiallyInvalidUTF8Data(subject)

            if shared.config.has_section(fromAddress):
                fromLabel = shared.config.get(fromAddress, "label")
            else:
                fromLabel = fromAddress

            toLabel = ""
            queryreturn = sqlQuery("""select label from addressbook where address=?""", toAddress)
            if queryreturn != []:
                for row in queryreturn:
                    (toLabel,) = row
            if toLabel == "":
                # It might be a broadcast message. We should check for that
                # label.
                queryreturn = sqlQuery("""select label from subscriptions where address=?""", toAddress)

                if queryreturn != []:
                    for row in queryreturn:
                        (toLabel,) = row

            if toLabel == "":
                if shared.config.has_section(toAddress):
                    toLabel = shared.config.get(toAddress, "label")
            if toLabel == "":
                toLabel = toAddress

            self.ui.tableWidgetSent.insertRow(0)
            toLabelStr = toLabel.decode("utf-8", "ignore") if isinstance(toLabel, bytes) else toLabel
            toAddressItem = QtWidgets.QTableWidgetItem(toLabelStr)
            toAddressItem.setToolTip(toLabelStr)
            toAddressItem.setIcon(avatarize(toAddress))
            toAddressItem.setData(Qt.UserRole, str(toAddress))
            toAddressItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 0, toAddressItem)

            if fromLabel == "":
                fromLabel = fromAddress
            fromAddressItem = QtWidgets.QTableWidgetItem(
                fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel
            )
            fromAddressItem.setToolTip(fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel)
            fromAddressItem.setIcon(avatarize(fromAddress))
            fromAddressItem.setData(Qt.UserRole, str(fromAddress))
            fromAddressItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 1, fromAddressItem)

            subjectItem = QtWidgets.QTableWidgetItem(subject.decode("utf-8") if isinstance(subject, bytes) else subject)
            subjectItem.setToolTip(subject.decode("utf-8") if isinstance(subject, bytes) else subject)
            subjectItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 2, subjectItem)

            if status == "awaitingpubkey":
                statusText = _translate("MainWindow", "Waiting for their encryption key. Will request it again soon.")
            elif status == "doingpowforpubkey":
                statusText = _translate("MainWindow", "Encryption key request queued.")
            elif status == "msgqueued":
                statusText = _translate("MainWindow", "Queued.")
            elif status == "msgsent":
                statusText = _translate("MainWindow", "Message sent. Waiting for acknowledgement. Sent at %1").replace(
                    "%1", l10n.formatTimestamp(lastactiontime)
                )
            elif status == "msgsentnoackexpected":
                statusText = _translate("MainWindow", "Message sent. Sent at %1").replace(
                    "%1", l10n.formatTimestamp(lastactiontime)
                )
            elif status == "doingmsgpow":
                statusText = _translate("MainWindow", "Need to do work to send message. Work is queued.")
            elif status == "ackreceived":
                statusText = _translate("MainWindow", "Acknowledgement of the message received %1").replace(
                    "%1", l10n.formatTimestamp(lastactiontime)
                )
            elif status == "broadcastqueued":
                statusText = _translate("MainWindow", "Broadcast queued.")
            elif status == "broadcastsent":
                statusText = _translate("MainWindow", "Broadcast on %1").replace(
                    "%1", l10n.formatTimestamp(lastactiontime)
                )
            elif status == "toodifficult":
                statusText = _translate(
                    "MainWindow",
                    "Problem: The work demanded by the recipient is more difficult than you are willing to do. %1",
                ).replace("%1", l10n.formatTimestamp(lastactiontime))
            elif status == "badkey":
                statusText = _translate(
                    "MainWindow", "Problem: The recipient's encryption key is no good. Could not encrypt message. %1"
                ).replace("%1", l10n.formatTimestamp(lastactiontime))
            elif status == "forcepow":
                statusText = _translate("MainWindow", "Forced difficulty override. Send should start soon.")
            else:
                statusText = (
                    _translate("MainWindow", "Unknown status: %1 %2")
                    .replace("%1", status)
                    .replace("%2", l10n.formatTimestamp(lastactiontime))
                )
            newItem = myTableWidgetItem(statusText)
            newItem.setToolTip(statusText)
            newItem.setData(Qt.UserRole, QByteArray(ackdata))
            newItem.setData(33, int(lastactiontime))
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 3, newItem)
        self.ui.tableWidgetSent.sortItems(3, QtCore.Qt.SortOrder.DescendingOrder)
        self.ui.tableWidgetSent.keyPressEvent = self.tableWidgetSentKeyPressEvent

    # Load inbox from messages database file
    def loadInbox(self, where="", what=""):
        what = "%" + what + "%"
        if where == "To":
            where = "toaddress"
        elif where == "From":
            where = "fromaddress"
        elif where == "Subject":
            where = "subject"
        elif where == "Message":
            where = "message"
        else:
            where = "toaddress || fromaddress || subject || message"

        sqlStatement = """
            SELECT msgid, toaddress, fromaddress, subject, received, read
            FROM inbox WHERE folder="inbox" AND %s LIKE ?
            ORDER BY received
            """ % (
            where,
        )

        while self.ui.tableWidgetInbox.rowCount() > 0:
            self.ui.tableWidgetInbox.removeRow(0)

        font = QFont()
        font.setBold(True)
        queryreturn = sqlQuery(sqlStatement, what)
        for row in queryreturn:
            msgid, toAddress, fromAddress, subject, received, read = row
            subject = shared.fixPotentiallyInvalidUTF8Data(subject)
            try:
                if toAddress == self.str_broadcast_subscribers:
                    toLabel = self.str_broadcast_subscribers
                else:
                    toLabel = shared.config.get(toAddress, "label")
            except:
                toLabel = ""
            if toLabel == "":
                toLabel = toAddress

            fromLabel = ""
            if shared.config.has_section(fromAddress):
                fromLabel = shared.config.get(fromAddress, "label")

            if fromLabel == "":  # If the fromAddress isn't one of our addresses and isn't a chan
                queryreturn = sqlQuery("""select label from addressbook where address=?""", fromAddress)
                if queryreturn != []:
                    for row in queryreturn:
                        (fromLabel,) = row

            if fromLabel == "":  # If this address wasn't in our address book.
                queryreturn = sqlQuery("""select label from subscriptions where address=?""", fromAddress)
                if queryreturn != []:
                    for row in queryreturn:
                        (fromLabel,) = row
            if fromLabel == "":
                fromLabel = fromAddress

            # message row
            self.ui.tableWidgetInbox.insertRow(0)
            # to
            to_item = QtWidgets.QTableWidgetItem(toLabel.decode("utf-8") if isinstance(toLabel, bytes) else toLabel)
            to_item.setToolTip(toLabel.decode("utf-8") if isinstance(toLabel, bytes) else toLabel)
            to_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            if not read:
                to_item.setFont(font)
            to_item.setData(Qt.UserRole, str(toAddress))
            if shared.safeConfigGetBoolean(toAddress, "mailinglist"):
                to_item.setTextColor(QtGui.QColor(137, 4, 177))  # magenta
            if shared.safeConfigGetBoolean(str(toAddress), "chan"):
                to_item.setTextColor(QtGui.QColor(216, 119, 0))  # orange
            to_item.setIcon(avatarize(toAddress))
            self.ui.tableWidgetInbox.setItem(0, 0, to_item)
            # from
            from_item = QtWidgets.QTableWidgetItem(
                fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel
            )
            from_item.setToolTip(fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel)
            from_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            if not read:
                from_item.setFont(font)
            from_item.setData(Qt.UserRole, str(fromAddress))
            if shared.safeConfigGetBoolean(str(fromAddress), "chan"):
                from_item.setTextColor(QtGui.QColor(216, 119, 0))  # orange
            from_item.setIcon(avatarize(fromAddress))
            self.ui.tableWidgetInbox.setItem(0, 1, from_item)
            # subject
            subject_item = QtWidgets.QTableWidgetItem(
                subject.decode("utf-8") if isinstance(subject, bytes) else subject
            )
            subject_item.setToolTip(subject.decode("utf-8") if isinstance(subject, bytes) else subject)
            subject_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            if not read:
                subject_item.setFont(font)
            self.ui.tableWidgetInbox.setItem(0, 2, subject_item)
            # time received
            time_item = myTableWidgetItem(l10n.formatTimestamp(received))
            time_item.setToolTip(l10n.formatTimestamp(received))
            time_item.setData(Qt.UserRole, QByteArray(msgid))
            time_item.setData(33, int(received))
            time_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            if not read:
                time_item.setFont(font)
            self.ui.tableWidgetInbox.setItem(0, 3, time_item)

        self.ui.tableWidgetInbox.sortItems(3, QtCore.Qt.SortOrder.DescendingOrder)
        self.ui.tableWidgetInbox.keyPressEvent = self.tableWidgetInboxKeyPressEvent

    # create application indicator
    def appIndicatorInit(self, app):
        self.initTrayIcon("can-icon-24px-red.png", app)
        if sys.platform[0:3] == "win":
            self.tray.activated.connect(self.__icon_activated)

        m = QMenu()

        self.actionStatus = QtGui.QAction(_translate("MainWindow", "Not Connected"), m, checkable=False)
        m.addAction(self.actionStatus)

        # separator
        actionSeparator = QtGui.QAction("", m, checkable=False)
        actionSeparator.setSeparator(True)
        m.addAction(actionSeparator)

        # show bitmessage
        self.actionShow = QtGui.QAction(_translate("MainWindow", "Show Bitmessage"), m, checkable=True)
        self.actionShow.setChecked(not shared.config.getboolean("bitmessagesettings", "startintray"))
        self.actionShow.triggered.connect(self.appIndicatorShowOrHideWindow)
        if not sys.platform[0:3] == "win":
            m.addAction(self.actionShow)

        # Send
        actionSend = QtGui.QAction(_translate("MainWindow", "Send"), m, checkable=False)
        actionSend.triggered.connect(self.appIndicatorSend)
        m.addAction(actionSend)

        # Subscribe
        actionSubscribe = QtGui.QAction(_translate("MainWindow", "Subscribe"), m, checkable=False)
        actionSubscribe.triggered.connect(self.appIndicatorSubscribe)
        m.addAction(actionSubscribe)

        # Address book
        actionAddressBook = QtGui.QAction(_translate("MainWindow", "Address Book"), m, checkable=False)
        actionAddressBook.triggered.connect(self.appIndicatorAddressBook)
        m.addAction(actionAddressBook)

        # Quit
        m.addAction(_translate("MainWindow", "Quit"), self.quit)

        self.tray.setContextMenu(m)
        self.tray.show()

    # Ubuntu Messaging menu object
    mmapp = None

    # is the operating system Ubuntu?
    def isUbuntu(self):
        for entry in platform.uname():
            if "Ubuntu" in entry:
                return True
        return False

    # When an unread inbox row is selected on then clear the messaging menu
    def ubuntuMessagingMenuClear(self, inventoryHash):
        global withMessagingMenu

        # if this isn't ubuntu then don't do anything
        if not self.isUbuntu():
            return

        # has messageing menu been installed
        if not withMessagingMenu:
            return

        # if there are no items on the messaging menu then
        # the subsequent query can be avoided
        if not (self.mmapp.has_source("Subscriptions") or self.mmapp.has_source("Messages")):
            return

        queryreturn = sqlQuery("""SELECT toaddress, read FROM inbox WHERE msgid=?""", inventoryHash)
        for row in queryreturn:
            toAddress, read = row
            if not read:
                if toAddress == self.str_broadcast_subscribers:
                    if self.mmapp.has_source("Subscriptions"):
                        self.mmapp.remove_source("Subscriptions")
                else:
                    if self.mmapp.has_source("Messages"):
                        self.mmapp.remove_source("Messages")

    # returns the number of unread messages and subscriptions
    def getUnread(self):
        unreadMessages = 0
        unreadSubscriptions = 0

        queryreturn = sqlQuery("""SELECT msgid, toaddress, read FROM inbox where folder='inbox' """)
        for row in queryreturn:
            msgid, toAddress, read = row

            try:
                if toAddress == self.str_broadcast_subscribers:
                    toLabel = self.str_broadcast_subscribers
                else:
                    toLabel = shared.config.get(toAddress, "label")
            except:
                toLabel = ""
            if toLabel == "":
                toLabel = toAddress

            if not read:
                if toLabel == self.str_broadcast_subscribers:
                    # increment the unread subscriptions
                    unreadSubscriptions = unreadSubscriptions + 1
                else:
                    # increment the unread messages
                    unreadMessages = unreadMessages + 1
        return unreadMessages, unreadSubscriptions

    # show the number of unread messages and subscriptions on the messaging
    # menu
    def ubuntuMessagingMenuUnread(self, drawAttention):
        unreadMessages, unreadSubscriptions = self.getUnread()
        # unread messages
        if unreadMessages > 0:
            self.mmapp.append_source("Messages", None, "Messages (" + str(unreadMessages) + ")")
            if drawAttention:
                self.mmapp.draw_attention("Messages")

        # unread subscriptions
        if unreadSubscriptions > 0:
            self.mmapp.append_source("Subscriptions", None, "Subscriptions (" + str(unreadSubscriptions) + ")")
            if drawAttention:
                self.mmapp.draw_attention("Subscriptions")

    # initialise the Ubuntu messaging menu
    def ubuntuMessagingMenuInit(self):
        global withMessagingMenu

        # if this isn't ubuntu then don't do anything
        if not self.isUbuntu():
            return

        # has messageing menu been installed
        if not withMessagingMenu:
            print("WARNING: MessagingMenu is not available.  Is libmessaging-menu-dev installed?")
            return

        # create the menu server
        if withMessagingMenu:
            try:
                self.mmapp = MessagingMenu.App(desktop_id="pybitmessage.desktop")
                self.mmapp.register()
                self.mmapp.connect("activate-source", self.appIndicatorInbox)
                self.ubuntuMessagingMenuUnread(True)
            except Exception:
                withMessagingMenu = False
                print("WARNING: messaging menu disabled")

    # update the Ubuntu messaging menu
    def ubuntuMessagingMenuUpdate(self, drawAttention, newItem, toLabel):
        global withMessagingMenu

        # if this isn't ubuntu then don't do anything
        if not self.isUbuntu():
            return

        # has messageing menu been installed
        if not withMessagingMenu:
            print("WARNING: messaging menu disabled or libmessaging-menu-dev not installed")
            return

        # remember this item to that the messaging menu can find it
        if toLabel == self.str_broadcast_subscribers:
            self.newBroadcastItem = newItem
        else:
            self.newMessageItem = newItem

        # Remove previous messages and subscriptions entries, then recreate them
        # There might be a better way to do it than this
        if self.mmapp.has_source("Messages"):
            self.mmapp.remove_source("Messages")

        if self.mmapp.has_source("Subscriptions"):
            self.mmapp.remove_source("Subscriptions")

        # update the menu entries
        self.ubuntuMessagingMenuUnread(drawAttention)

    # returns true if the given sound category is a connection sound
    # rather than a received message sound
    def isConnectionSound(self, category):
        if (
            category is self.SOUND_CONNECTED
            or category is self.SOUND_DISCONNECTED
            or category is self.SOUND_CONNECTION_GREEN
        ):
            return True
        return False

    # play a sound
    def playSound(self, category, label):
        # filename of the sound to be played
        soundFilename = None

        # whether to play a sound or not
        play = True

        # if the address had a known label in the address book
        if label is not None:
            # Does a sound file exist for this particular contact?
            if os.path.isfile(shared.appdata + "sounds/" + label + ".wav") or os.path.isfile(
                shared.appdata + "sounds/" + label + ".mp3"
            ):
                soundFilename = shared.appdata + "sounds/" + label

        # Avoid making sounds more frequently than the threshold.
        # This suppresses playing sounds repeatedly when there
        # are many new messages
        if soundFilename is None and not self.isConnectionSound(category):
            # elapsed time since the last sound was played
            dt = datetime.datetime.now() - self.lastSoundTime
            # suppress sounds which are more frequent than the threshold
            if dt.total_seconds() < self.maxSoundFrequencySec:
                play = False

        if soundFilename is None:
            # the sound is for an address which exists in the address book
            if category is self.SOUND_KNOWN:
                soundFilename = shared.appdata + "sounds/known"
            # the sound is for an unknown address
            elif category is self.SOUND_UNKNOWN:
                soundFilename = shared.appdata + "sounds/unknown"
            # initial connection sound
            elif category is self.SOUND_CONNECTED:
                soundFilename = shared.appdata + "sounds/connected"
            # disconnected sound
            elif category is self.SOUND_DISCONNECTED:
                soundFilename = shared.appdata + "sounds/disconnected"
            # sound when the connection status becomes green
            elif category is self.SOUND_CONNECTION_GREEN:
                soundFilename = shared.appdata + "sounds/green"

        if soundFilename is not None and play is True:
            if not self.isConnectionSound(category):
                # record the last time that a received message sound was played
                self.lastSoundTime = datetime.datetime.now()

            # if not wav then try mp3 format
            if not os.path.isfile(soundFilename + ".wav"):
                soundFilename = soundFilename + ".mp3"
            else:
                soundFilename = soundFilename + ".wav"

            if os.path.isfile(soundFilename):
                if "linux" in sys.platform:
                    # Note: QSound was a nice idea but it didn't work
                    if ".mp3" in soundFilename:
                        gst_available = False
                        try:
                            subprocess.call(["gst123", soundFilename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                            gst_available = True
                        except:
                            print("WARNING: gst123 must be installed in order to play mp3 sounds")
                        if not gst_available:
                            try:
                                subprocess.call(
                                    ["mpg123", soundFilename], stdin=subprocess.PIPE, stdout=subprocess.PIPE
                                )
                                gst_available = True
                            except:
                                print("WARNING: mpg123 must be installed in order to play mp3 sounds")
                    else:
                        try:
                            subprocess.call(["aplay", soundFilename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                        except:
                            print("WARNING: aplay must be installed in order to play WAV sounds")
                elif sys.platform[0:3] == "win":
                    # use winsound on Windows
                    import winsound

                    winsound.PlaySound(soundFilename, winsound.SND_FILENAME)

    # initialise the message notifier
    def notifierInit(self):
        global withMessagingMenu
        if withMessagingMenu:
            Notify.init("pybitmessage")

    # shows a notification
    def notifierShow(self, title, subtitle, fromCategory, label):
        global withMessagingMenu

        self.playSound(fromCategory, label)

        if withMessagingMenu:
            n = Notify.Notification.new(title, subtitle, "notification-message-email")
            try:
                n.show()
            except:
                # n.show() has been known to throw this exception:
                # gi._glib.GError: GDBus.Error:org.freedesktop.Notifications.
                # MaxNotificationsExceeded: Exceeded maximum number of
                # notifications
                pass
            return
        else:
            self.tray.showMessage(title, subtitle, 1, 2000)

    def tableWidgetInboxKeyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Delete:
            self.on_action_InboxTrash()
        return QtWidgets.QTableWidget.keyPressEvent(self.ui.tableWidgetInbox, event)

    def tableWidgetSentKeyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Delete:
            self.on_action_SentTrash()
        return QtWidgets.QTableWidget.keyPressEvent(self.ui.tableWidgetSent, event)

    def click_actionManageKeys(self):
        if "darwin" in sys.platform or "linux" in sys.platform:
            if shared.appdata == "":
                # reply = QtWidgets.QMessageBox.information(self, 'keys.dat?','You
                # may manage your keys by editing the keys.dat file stored in
                # the same directory as this program. It is important that you
                # back up this file.', QMessageBox.Ok)
                reply = QtWidgets.QMessageBox.information(
                    self,
                    "keys.dat?",
                    _translate(
                        "MainWindow",
                        "You may manage your keys by editing the keys.dat file stored in the same directory as this program. It is important that you back up this file.",
                    ),
                    QMessageBox.Ok,
                )

            else:
                QtWidgets.QMessageBox.information(
                    self,
                    "keys.dat?",
                    _translate(
                        "MainWindow",
                        "You may manage your keys by editing the keys.dat file stored in\n %1 \nIt is important that you back up this file.",
                    ).replace("%1", shared.appdata),
                    QMessageBox.Ok,
                )
        elif sys.platform == "win32" or sys.platform == "win64":
            if shared.appdata == "":
                reply = QtWidgets.QMessageBox.question(
                    self,
                    _translate("MainWindow", "Open keys.dat?"),
                    _translate(
                        "MainWindow",
                        "You may manage your keys by editing the keys.dat file stored in the same directory as this program. It is important that you back up this file. Would you like to open the file now? (Be sure to close Bitmessage before making any changes.)",
                    ),
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.No,
                )
            else:
                reply = QtWidgets.QMessageBox.question(
                    self,
                    _translate("MainWindow", "Open keys.dat?"),
                    _translate(
                        "MainWindow",
                        "You may manage your keys by editing the keys.dat file stored in\n %1 \nIt is important that you back up this file. Would you like to open the file now? (Be sure to close Bitmessage before making any changes.)",
                    ).replace("%1", shared.appdata),
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.No,
                )
            if reply == QtWidgets.QMessageBox.Yes:
                self.openKeysFile()

    def click_actionDeleteAllTrashedMessages(self):
        if (
            QtWidgets.QMessageBox.question(
                self,
                _translate("MainWindow", "Delete trash?"),
                _translate("MainWindow", "Are you sure you want to delete all trashed messages?"),
                QtWidgets.QMessageBox.Yes,
                QtWidgets.QMessageBox.No,
            )
            == QtWidgets.QMessageBox.No
        ):
            return
        sqlStoredProcedure("deleteandvacuume")

    def click_actionRegenerateDeterministicAddresses(self):
        self.regenerateAddressesDialogInstance = regenerateAddressesDialog(self)
        if self.regenerateAddressesDialogInstance.exec():
            if self.regenerateAddressesDialogInstance.ui.lineEditPassphrase.text() == "":
                QMessageBox.about(
                    self,
                    _translate("MainWindow", "bad passphrase"),
                    _translate(
                        "MainWindow",
                        "You must type your passphrase. If you don't have one then this is not the form for you.",
                    ),
                )
            else:
                streamNumberForAddress = int(self.regenerateAddressesDialogInstance.ui.lineEditStreamNumber.text())
                try:
                    addressVersionNumber = int(
                        self.regenerateAddressesDialogInstance.ui.lineEditAddressVersionNumber.text()
                    )
                except:
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Bad address version number"),
                        _translate("MainWindow", "Your address version number must be a number: either 3 or 4."),
                    )
                if addressVersionNumber < 3 or addressVersionNumber > 4:
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Bad address version number"),
                        _translate("MainWindow", "Your address version number must be either 3 or 4."),
                    )
                # self.addressGenerator = addressGenerator()
                # self.addressGenerator.setup(addressVersionNumber,streamNumberForAddress,"unused address",self.regenerateAddressesDialogInstance.ui.spinBoxNumberOfAddressesToMake.value(),self.regenerateAddressesDialogInstance.ui.lineEditPassphrase.text().toUtf8(),self.regenerateAddressesDialogInstance.ui.checkBoxEighteenByteRipe.isChecked())
                # QtCore.QObject.connect(self.addressGenerator, SIGNAL("writeNewAddressToTable(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.writeNewAddressToTable)
                # self.addressGenerator.updateStatusBar.addressVersionNumber.connect( streamNumberForAddress, "regenerated deterministic address", self.regenerateAddressesDialogInstance.ui.spinBoxNumberOfAddressesToMake.value(
                # ), self.regenerateAddressesDialogInstance.ui.lineEditPassphrase.text().toUtf8(), self.regenerateAddressesDialogInstance.ui.checkBoxEighteenByteRipe.isChecked())
                self.ui.tabWidget.setCurrentIndex(3)

    def click_actionJoinChan(self):
        self.newChanDialogInstance = newChanDialog(self)
        if self.newChanDialogInstance.exec():
            if self.newChanDialogInstance.ui.radioButtonCreateChan.isChecked():
                if self.newChanDialogInstance.ui.lineEditChanNameCreate.text() == "":
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Chan name needed"),
                        _translate("MainWindow", "You didn't enter a chan name."),
                    )
                    return
                shared.apiAddressGeneratorReturnQueue.queue.clear()
                shared.addressGeneratorQueue.put(
                    (
                        "createChan",
                        4,
                        1,
                        self.str_chan
                        + " "
                        + str(self.newChanDialogInstance.ui.lineEditChanNameCreate.text().encode("utf-8")),
                        self.newChanDialogInstance.ui.lineEditChanNameCreate.text().encode("utf-8"),
                    )
                )
                addressGeneratorReturnValue = shared.apiAddressGeneratorReturnQueue.get()
                print("addressGeneratorReturnValue", addressGeneratorReturnValue)
                if len(addressGeneratorReturnValue) == 0:
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Address already present"),
                        _translate(
                            "MainWindow", "Could not add chan because it appears to already be one of your identities."
                        ),
                    )
                    return
                createdAddress = addressGeneratorReturnValue[0]
                QMessageBox.about(
                    self,
                    _translate("MainWindow", "Success"),
                    _translate(
                        "MainWindow",
                        "Successfully created chan. To let others join your chan, give them the chan name and this Bitmessage address: %1. This address also appears in 'Your Identities'.",
                    ).replace("%1", createdAddress),
                )
                self.ui.tabWidget.setCurrentIndex(3)
            elif self.newChanDialogInstance.ui.radioButtonJoinChan.isChecked():
                if self.newChanDialogInstance.ui.lineEditChanNameJoin.text() == "":
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Chan name needed"),
                        _translate("MainWindow", "You didn't enter a chan name."),
                    )
                    return
                if (
                    decodeAddress(self.newChanDialogInstance.ui.lineEditChanBitmessageAddress.text())[0]
                    == "versiontoohigh"
                ):
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Address too new"),
                        _translate(
                            "MainWindow",
                            "Although that Bitmessage address might be valid, its version number is too new for us to handle. Perhaps you need to upgrade Bitmessage.",
                        ),
                    )
                    return
                if decodeAddress(self.newChanDialogInstance.ui.lineEditChanBitmessageAddress.text())[0] != "success":
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Address invalid"),
                        _translate("MainWindow", "That Bitmessage address is not valid."),
                    )
                    return
                shared.apiAddressGeneratorReturnQueue.queue.clear()
                shared.addressGeneratorQueue.put(
                    (
                        "joinChan",
                        addBMIfNotPresent(self.newChanDialogInstance.ui.lineEditChanBitmessageAddress.text()),
                        self.str_chan
                        + " "
                        + str(self.newChanDialogInstance.ui.lineEditChanNameJoin.text().encode("utf-8")),
                        self.newChanDialogInstance.ui.lineEditChanNameJoin.text().encode("utf-8"),
                    )
                )
                addressGeneratorReturnValue = shared.apiAddressGeneratorReturnQueue.get()
                print("addressGeneratorReturnValue", addressGeneratorReturnValue)
                if addressGeneratorReturnValue == "chan name does not match address":
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Address does not match chan name"),
                        _translate(
                            "MainWindow",
                            "Although the Bitmessage address you entered was valid, it doesn't match the chan name.",
                        ),
                    )
                    return
                if len(addressGeneratorReturnValue) == 0:
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Address already present"),
                        _translate(
                            "MainWindow", "Could not add chan because it appears to already be one of your identities."
                        ),
                    )
                    return
                createdAddress = addressGeneratorReturnValue[0]
                QMessageBox.about(
                    self, _translate("MainWindow", "Success"), _translate("MainWindow", "Successfully joined chan. ")
                )
                self.ui.tabWidget.setCurrentIndex(3)

    def showConnectDialog(self):
        self.connectDialogInstance = connectDialog(self)
        if self.connectDialogInstance.exec():
            if self.connectDialogInstance.ui.radioButtonConnectNow.isChecked():
                shared.config.remove_option("bitmessagesettings", "dontconnect")
                with open(shared.appdata + "keys.dat", "w") as configfile:
                    shared.config.write(configfile)
            else:
                self.click_actionSettings()

    def openKeysFile(self):
        if "linux" in sys.platform:
            subprocess.call(["xdg-open", shared.appdata + "keys.dat"])
        else:
            os.startfile(shared.appdata + "keys.dat")

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowState.WindowMinimized:
                self.actionShow.setChecked(False)
        if shared.config.getboolean("bitmessagesettings", "minimizetotray") and not "darwin" in sys.platform:
            if event.type() == QtCore.QEvent.Type.WindowStateChange:
                if self.windowState() & QtCore.Qt.WindowState.WindowMinimized:
                    self.appIndicatorHide()
                    if "win32" in sys.platform or "win64" in sys.platform:
                        self.hide()
                elif event.oldState() & QtCore.Qt.WindowState.WindowMinimized:
                    # The window state has just been changed to
                    # Normal/Maximised/FullScreen
                    pass
            # QtWidgets.QWidget.changeEvent(self, event)

    def __icon_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.actionShow.setChecked(not self.actionShow.isChecked())
            self.appIndicatorShowOrHideWindow()

    def updateNumberOfMessagesProcessed(self):
        self.ui.labelMessageCount.setText(
            _translate("MainWindow", "Processed %1 person-to-person messages.").replace(
                "%1", str(shared.numberOfMessagesProcessed)
            )
        )

    def updateNumberOfBroadcastsProcessed(self):
        self.ui.labelBroadcastCount.setText(
            _translate("MainWindow", "Processed %1 broadcast messages.").replace(
                "%1", str(shared.numberOfBroadcastsProcessed)
            )
        )

    def updateNumberOfPubkeysProcessed(self):
        self.ui.labelPubkeyCount.setText(
            _translate("MainWindow", "Processed %1 public keys.").replace("%1", str(shared.numberOfPubkeysProcessed))
        )

    def formatBytes(self, num):
        for x in ["bytes", "KB", "MB", "GB"]:
            if num < 1000.0:
                return "%3.0f %s" % (num, x)
            num /= 1000.0
        return "%3.0f %s" % (num, "TB")

    def formatByteRate(self, num):
        num /= 1000
        return "%4.0f KB" % num

    def updateNumberOfBytes(self):
        """
        This function is run every two seconds, so we divide the rate of bytes
        sent and received by 2.
        """
        self.ui.labelBytesRecvCount.setText(
            _translate("MainWindow", "Down: %1/s  Total: %2")
            .replace("%1", self.formatByteRate(shared.numberOfBytesReceived / 2))
            .replace("%2", self.formatBytes(self.totalNumberOfBytesReceived))
        )
        self.ui.labelBytesSentCount.setText(
            _translate("MainWindow", "Up: %1/s  Total: %2")
            .replace("%1", self.formatByteRate(shared.numberOfBytesSent / 2))
            .replace("%2", self.formatBytes(self.totalNumberOfBytesSent))
        )
        self.totalNumberOfBytesReceived += shared.numberOfBytesReceived
        self.totalNumberOfBytesSent += shared.numberOfBytesSent
        shared.numberOfBytesReceived = 0
        shared.numberOfBytesSent = 0

    def updateNetworkStatusTab(self):
        # print 'updating network status tab'
        totalNumberOfConnectionsFromAllStreams = 0  # One would think we could use len(sendDataQueues) for this but the number doesn't always match: just because we have a sendDataThread running doesn't mean that the connection has been fully established (with the exchange of version messages).
        streamNumberTotals = {}
        for host, streamNumber in shared.connectedHostsList.items():
            if not streamNumber in streamNumberTotals:
                streamNumberTotals[streamNumber] = 1
            else:
                streamNumberTotals[streamNumber] += 1

        while self.ui.tableWidgetConnectionCount.rowCount() > 0:
            self.ui.tableWidgetConnectionCount.removeRow(0)
        for streamNumber, connectionCount in streamNumberTotals.items():
            self.ui.tableWidgetConnectionCount.insertRow(0)
            if streamNumber == 0:
                newItem = QtWidgets.QTableWidgetItem("?")
            else:
                newItem = QtWidgets.QTableWidgetItem(str(streamNumber))
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetConnectionCount.setItem(0, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(str(connectionCount))
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetConnectionCount.setItem(0, 1, newItem)
        """for currentRow in range(self.ui.tableWidgetConnectionCount.rowCount()):
            rowStreamNumber = int(self.ui.tableWidgetConnectionCount.item(currentRow,0).text())
            if streamNumber == rowStreamNumber:
                foundTheRowThatNeedsUpdating = True
                self.ui.tableWidgetConnectionCount.item(currentRow,1).setText(str(connectionCount))
                #totalNumberOfConnectionsFromAllStreams += connectionCount
        if foundTheRowThatNeedsUpdating == False:
            #Add a line to the table for this stream number and update its count with the current connection count.
            self.ui.tableWidgetConnectionCount.insertRow(0)
            newItem =  QtWidgets.QTableWidgetItem(str(streamNumber))
            newItem.setFlags( QtCore.Qt.ItemFlag.ItemIsSelectable |  QtCore.Qt.ItemFlag.ItemIsEnabled )
            self.ui.tableWidgetConnectionCount.setItem(0,0,newItem)
            newItem =  QtWidgets.QTableWidgetItem(str(connectionCount))
            newItem.setFlags( QtCore.Qt.ItemFlag.ItemIsSelectable |  QtCore.Qt.ItemFlag.ItemIsEnabled )
            self.ui.tableWidgetConnectionCount.setItem(0,1,newItem)
            totalNumberOfConnectionsFromAllStreams += connectionCount"""
        self.ui.labelTotalConnections.setText(
            _translate("MainWindow", "Total Connections: %1").replace("%1", str(len(shared.connectedHostsList)))
        )
        if (
            len(shared.connectedHostsList) > 0 and shared.statusIconColor == "red"
        ):  # FYI: The 'singlelistener' thread sets the icon color to green when it receives an incoming connection, meaning that the user's firewall is configured correctly.
            self.setStatusIcon("yellow")
        elif len(shared.connectedHostsList) == 0:
            self.setStatusIcon("red")

    # timer driven
    def runEveryTwoSeconds(self):
        self.ui.labelLookupsPerSecond.setText(
            _translate("MainWindow", "Inventory lookups per second: %1").replace(
                "%1", str(shared.numberOfInventoryLookupsPerformed / 2)
            )
        )
        shared.numberOfInventoryLookupsPerformed = 0
        self.updateNumberOfBytes()

    # Indicates whether or not there is a connection to the Bitmessage network
    connected = False

    def setStatusIcon(self, color):
        global withMessagingMenu
        # print 'setting status icon color'
        if color == "red":
            self.ui.pushButtonStatusIcon.setIcon(QIcon(":/newPrefix/images/redicon.png"))
            shared.statusIconColor = "red"
            # if the connection is lost then show a notification
            if self.connected:
                self.notifierShow(
                    "Bitmessage",
                    str(_translate("MainWindow", "Connection lost").encode("utf-8")),
                    self.SOUND_DISCONNECTED,
                    None,
                )
            self.connected = False

            if self.actionStatus is not None:
                self.actionStatus.setText(_translate("MainWindow", "Not Connected"))
                self.setTrayIconFile("can-icon-24px-red.png")
        if color == "yellow":
            if (
                self.statusBar().currentMessage()
                == "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won't send until you connect."
            ):
                self.statusBar().showMessage("")
            self.ui.pushButtonStatusIcon.setIcon(QIcon(":/newPrefix/images/yellowicon.png"))
            shared.statusIconColor = "yellow"
            # if a new connection has been established then show a notification
            if not self.connected:
                self.notifierShow(
                    "Bitmessage", str(_translate("MainWindow", "Connected").encode("utf-8")), self.SOUND_CONNECTED, None
                )
            self.connected = True

            if self.actionStatus is not None:
                self.actionStatus.setText(_translate("MainWindow", "Connected"))
                self.setTrayIconFile("can-icon-24px-yellow.png")
        if color == "green":
            if (
                self.statusBar().currentMessage()
                == "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won't send until you connect."
            ):
                self.statusBar().showMessage("")
            self.ui.pushButtonStatusIcon.setIcon(QIcon(":/newPrefix/images/greenicon.png"))
            shared.statusIconColor = "green"
            if not self.connected:
                self.notifierShow(
                    "Bitmessage",
                    str(_translate("MainWindow", "Connected").encode("utf-8")),
                    self.SOUND_CONNECTION_GREEN,
                    None,
                )
            self.connected = True

            if self.actionStatus is not None:
                self.actionStatus.setText(_translate("MainWindow", "Connected"))
                self.setTrayIconFile("can-icon-24px-green.png")

    def initTrayIcon(self, iconFileName, app):
        self.currentTrayIconFileName = iconFileName
        self.tray = QSystemTrayIcon(self.calcTrayIcon(iconFileName, self.findInboxUnreadCount()), app)

    def setTrayIconFile(self, iconFileName):
        self.currentTrayIconFileName = iconFileName
        self.drawTrayIcon(iconFileName, self.findInboxUnreadCount())

    def calcTrayIcon(self, iconFileName, inboxUnreadCount):
        pixmap = QtGui.QPixmap(":/newPrefix/images/" + iconFileName)
        if inboxUnreadCount > 0:
            # choose font and calculate font parameters
            fontName = "Lucida"
            fontSize = 10
            font = QtGui.QFont(fontName, fontSize, QtGui.QFont.Bold)
            fontMetrics = QtGui.QFontMetrics(font)
            # text
            txt = str(inboxUnreadCount)
            rect = fontMetrics.boundingRect(txt)
            # margins that we add in the top-right corner
            marginX = 2
            marginY = 0  # it looks like -2 is also ok due to the error of metric
            # if it renders too wide we need to change it to a plus symbol
            if rect.width() > 20:
                txt = "+"
                fontSize = 15
                font = QtGui.QFont(fontName, fontSize, QtGui.QFont.Bold)
                fontMetrics = QtGui.QFontMetrics(font)
                rect = fontMetrics.boundingRect(txt)
            # draw text
            painter = QPainter()
            painter.begin(pixmap)
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), Qt.SolidPattern))
            painter.setFont(font)
            painter.drawText(24 - rect.right() - marginX, -rect.top() + marginY, txt)
            painter.end()
        return QtGui.QIcon(pixmap)

    def drawTrayIcon(self, iconFileName, inboxUnreadCount):
        self.tray.setIcon(self.calcTrayIcon(iconFileName, inboxUnreadCount))

    def changedInboxUnread(self):
        self.drawTrayIcon(self.currentTrayIconFileName, self.findInboxUnreadCount())

    def findInboxUnreadCount(self):
        queryreturn = sqlQuery("""SELECT count(*) from inbox WHERE folder='inbox' and read=0""")
        cnt = 0
        for row in queryreturn:
            (cnt,) = row
        return int(cnt)

    def updateSentItemStatusByHash(self, toRipe, textToDisplay):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            toAddress = str(self.ui.tableWidgetSent.item(i, 0).data(Qt.UserRole))
            status, addressVersionNumber, streamNumber, ripe = decodeAddress(toAddress)
            if ripe == toRipe:
                self.ui.tableWidgetSent.item(i, 3).setToolTip(textToDisplay)
                try:
                    newlinePosition = textToDisplay.indexOf("\n")
                except:  # If someone misses adding a "_translate" to a string before passing it to this function, this function won't receive a qstring which will cause an exception.
                    newlinePosition = 0
                if newlinePosition > 1:
                    self.ui.tableWidgetSent.item(i, 3).setText(textToDisplay[:newlinePosition])
                else:
                    self.ui.tableWidgetSent.item(i, 3).setText(textToDisplay)

    def updateSentItemStatusByAckdata(self, ackdata, textToDisplay):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            toAddress = str(self.ui.tableWidgetSent.item(i, 0).data(Qt.UserRole))
            tableAckdata = self.ui.tableWidgetSent.item(i, 3).data(Qt.UserRole)
            status, addressVersionNumber, streamNumber, ripe = decodeAddress(toAddress)
            if ackdata == tableAckdata:
                self.ui.tableWidgetSent.item(i, 3).setToolTip(textToDisplay)
                try:
                    newlinePosition = textToDisplay.indexOf("\n")
                except:  # If someone misses adding a "_translate" to a string before passing it to this function, this function won't receive a qstring which will cause an exception.
                    newlinePosition = 0
                if newlinePosition > 1:
                    self.ui.tableWidgetSent.item(i, 3).setText(textToDisplay[:newlinePosition])
                else:
                    self.ui.tableWidgetSent.item(i, 3).setText(textToDisplay)

    def removeInboxRowByMsgid(self, msgid):  # msgid and inventoryHash are the same thing
        for i in range(self.ui.tableWidgetInbox.rowCount()):
            if msgid == str(self.ui.tableWidgetInbox.item(i, 3).data(Qt.UserRole)):
                self.statusBar().showMessage(_translate("MainWindow", "Message trashed"))
                self.ui.tableWidgetInbox.removeRow(i)
                break
        self.changedInboxUnread()

    def displayAlert(self, title, text, exitAfterUserClicksOk):
        self.statusBar().showMessage(text)
        QtWidgets.QMessageBox.critical(self, title, text, QMessageBox.Ok)
        if exitAfterUserClicksOk:
            os._exit(0)

    def rerenderInboxFromLabels(self):
        for i in range(self.ui.tableWidgetInbox.rowCount()):
            addressToLookup = str(self.ui.tableWidgetInbox.item(i, 1).data(Qt.UserRole))
            fromLabel = ""
            queryreturn = sqlQuery("""select label from addressbook where address=?""", addressToLookup)

            if queryreturn != []:
                for row in queryreturn:
                    (fromLabel,) = row

            if fromLabel == "":
                # It might be a broadcast message. We should check for that
                # label.
                queryreturn = sqlQuery("""select label from subscriptions where address=?""", addressToLookup)

                if queryreturn != []:
                    for row in queryreturn:
                        (fromLabel,) = row
            if fromLabel == "":
                # Message might be from an address we own like a chan address. Let's look for that label.
                if shared.config.has_section(addressToLookup):
                    fromLabel = shared.config.get(addressToLookup, "label")
            if fromLabel == "":
                fromLabel = addressToLookup
            self.ui.tableWidgetInbox.item(i, 1).setText(
                fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel
            )
            self.ui.tableWidgetInbox.item(i, 1).setIcon(avatarize(addressToLookup))
            # Set the color according to whether it is the address of a mailing
            # list or not.
            if shared.safeConfigGetBoolean(addressToLookup, "chan"):
                self.ui.tableWidgetInbox.item(i, 1).setTextColor(QtGui.QColor(216, 119, 0))  # orange
            else:
                self.ui.tableWidgetInbox.item(i, 1).setTextColor(QApplication.palette().text().color())

    def rerenderInboxToLabels(self):
        for i in range(self.ui.tableWidgetInbox.rowCount()):
            toAddress = str(self.ui.tableWidgetInbox.item(i, 0).data(Qt.UserRole))
            # Message might be to an address we own like a chan address. Let's look for that label.
            if shared.config.has_section(toAddress):
                toLabel = shared.config.get(toAddress, "label")
            else:
                toLabel = toAddress
            self.ui.tableWidgetInbox.item(i, 0).setText(
                toLabel.decode("utf-8") if isinstance(toLabel, bytes) else toLabel
            )
            self.ui.tableWidgetInbox.item(i, 0).setIcon(avatarize(toAddress))
            # Set the color according to whether it is the address of a mailing
            # list, a chan or neither.
            if shared.safeConfigGetBoolean(toAddress, "chan"):
                self.ui.tableWidgetInbox.item(i, 0).setTextColor(QtGui.QColor(216, 119, 0))  # orange
            elif shared.safeConfigGetBoolean(toAddress, "mailinglist"):
                self.ui.tableWidgetInbox.item(i, 0).setTextColor(QtGui.QColor(137, 4, 177))  # magenta
            else:
                self.ui.tableWidgetInbox.item(i, 0).setTextColor(QApplication.palette().text().color())

    def rerenderSentFromLabels(self):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            fromAddress = str(self.ui.tableWidgetSent.item(i, 1).data(Qt.UserRole))
            # Message might be from an address we own like a chan address. Let's look for that label.
            if shared.config.has_section(fromAddress):
                fromLabel = shared.config.get(fromAddress, "label")
            else:
                fromLabel = fromAddress
            self.ui.tableWidgetSent.item(i, 1).setText(
                fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel
            )
            self.ui.tableWidgetSent.item(i, 1).setIcon(avatarize(fromAddress))

    def rerenderSentToLabels(self):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            addressToLookup = str(self.ui.tableWidgetSent.item(i, 0).data(Qt.UserRole))
            toLabel = ""
            queryreturn = sqlQuery("""select label from addressbook where address=?""", addressToLookup)
            if queryreturn != []:
                for row in queryreturn:
                    (toLabel,) = row

            if toLabel == "":
                # Message might be to an address we own like a chan address. Let's look for that label.
                if shared.config.has_section(addressToLookup):
                    toLabel = shared.config.get(addressToLookup, "label")
            if toLabel == "":
                toLabel = addressToLookup
            self.ui.tableWidgetSent.item(i, 0).setText(
                toLabel.decode("utf-8") if isinstance(toLabel, bytes) else toLabel
            )

    def rerenderAddressBook(self):
        self.ui.tableWidgetAddressBook.setRowCount(0)
        queryreturn = sqlQuery("SELECT * FROM addressbook")
        for row in queryreturn:
            label, address = row
            self.ui.tableWidgetAddressBook.insertRow(0)
            newItem = QtWidgets.QTableWidgetItem(label.decode("utf-8") if isinstance(label, bytes) else label)
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetAddressBook.setItem(0, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(address)
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetAddressBook.setItem(0, 1, newItem)

    def rerenderSubscriptions(self):
        self.ui.tableWidgetSubscriptions.setRowCount(0)
        queryreturn = sqlQuery("SELECT label, address, enabled FROM subscriptions")
        for row in queryreturn:
            label, address, enabled = row
            self.ui.tableWidgetSubscriptions.insertRow(0)
            newItem = QtWidgets.QTableWidgetItem(label.decode("utf-8") if isinstance(label, bytes) else label)
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetSubscriptions.setItem(0, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(address)
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            self.ui.tableWidgetSubscriptions.setItem(0, 1, newItem)

    def click_pushButtonSend(self):
        self.statusBar().showMessage("")
        toAddresses = str(self.ui.lineEditTo.text())
        fromAddress = str(self.ui.labelFrom.text())
        subject = self.ui.lineEditSubject.text()
        message = str(self.ui.textEditMessage.document().toPlainText().encode("utf-8"))
        if self.ui.radioButtonSpecific.isChecked():  # To send a message to specific people (rather than broadcast)
            toAddressesList = [s.strip() for s in toAddresses.replace(",", ";").split(";")]
            toAddressesList = list(
                set(toAddressesList)
            )  # remove duplicate addresses. If the user has one address with a BM- and the same address without the BM-, this will not catch it. They'll send the message to the person twice.
            for toAddress in toAddressesList:
                if toAddress != "":
                    status, addressVersionNumber, streamNumber, ripe = decodeAddress(toAddress)
                    if status != "success":
                        with shared.printLock:
                            print("Error: Could not decode", toAddress, ":", status)

                        if status == "missingbm":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1"
                                ).replace("%1", toAddress)
                            )
                        elif status == "checksumfailed":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow",
                                    "Error: The address %1 is not typed or copied correctly. Please check it.",
                                ).replace("%1", toAddress)
                            )
                        elif status == "invalidcharacters":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow", "Error: The address %1 contains invalid characters. Please check it."
                                ).replace("%1", toAddress)
                            )
                        elif status == "versiontoohigh":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow",
                                    "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.",
                                ).replace("%1", toAddress)
                            )
                        elif status == "ripetooshort":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow",
                                    "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.",
                                ).replace("%1", toAddress)
                            )
                        elif status == "ripetoolong":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow",
                                    "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.",
                                ).replace("%1", toAddress)
                            )
                        else:
                            self.statusBar().showMessage(
                                _translate("MainWindow", "Error: Something is wrong with the address %1.").replace(
                                    "%1", toAddress
                                )
                            )
                    elif fromAddress == "":
                        self.statusBar().showMessage(
                            _translate(
                                "MainWindow",
                                "Error: You must specify a From address. If you don't have one, go to the 'Your Identities' tab.",
                            )
                        )
                    else:
                        toAddress = addBMIfNotPresent(toAddress)
                        if addressVersionNumber > 4 or addressVersionNumber <= 1:
                            QMessageBox.about(
                                self,
                                _translate("MainWindow", "Address version number"),
                                _translate(
                                    "MainWindow",
                                    "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.",
                                )
                                .replace("%1", toAddress)
                                .replace("%2", str(addressVersionNumber)),
                            )
                            continue
                        if streamNumber > 1 or streamNumber == 0:
                            QMessageBox.about(
                                self,
                                _translate("MainWindow", "Stream number"),
                                _translate(
                                    "MainWindow",
                                    "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.",
                                )
                                .replace("%1", toAddress)
                                .replace("%2", str(streamNumber)),
                            )
                            continue
                        self.statusBar().showMessage("")
                        if shared.statusIconColor == "red":
                            self.statusBar().showMessage(
                                _translate(
                                    "MainWindow",
                                    "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won't send until you connect.",
                                )
                            )
                        ackdata = OpenSSL.rand(32)
                        t = ()
                        sqlExecute(
                            """INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            "",
                            toAddress,
                            ripe,
                            fromAddress,
                            subject,
                            message,
                            ackdata,
                            int(time.time()),
                            "msgqueued",
                            1,
                            1,
                            "sent",
                            2,
                        )

                        toLabel = ""
                        queryreturn = sqlQuery("""select label from addressbook where address=?""", toAddress)
                        if queryreturn != []:
                            for row in queryreturn:
                                (toLabel,) = row

                        self.displayNewSentMessage(toAddress, toLabel, fromAddress, subject, message, ackdata)
                        shared.workerQueue.put(("sendmessage", toAddress))

                        self.ui.comboBoxSendFrom.setCurrentIndex(0)
                        self.ui.labelFrom.setText("")
                        self.ui.lineEditTo.setText("")
                        self.ui.lineEditSubject.setText("")
                        self.ui.textEditMessage.setText("")
                        self.ui.tabWidget.setCurrentIndex(2)
                        self.ui.tableWidgetSent.setCurrentCell(0, 0)
                else:
                    self.statusBar().showMessage(_translate("MainWindow", "Your 'To' field is empty."))
        else:  # User selected 'Broadcast'
            if fromAddress == "":
                self.statusBar().showMessage(
                    _translate(
                        "MainWindow",
                        "Error: You must specify a From address. If you don't have one, go to the 'Your Identities' tab.",
                    )
                )
            else:
                self.statusBar().showMessage("")
                # We don't actually need the ackdata for acknowledgement since
                # this is a broadcast message, but we can use it to update the
                # user interface when the POW is done generating.
                ackdata = OpenSSL.rand(32)
                toAddress = self.str_broadcast_subscribers
                ripe = ""
                t = (
                    "",
                    toAddress,
                    ripe,
                    fromAddress,
                    subject,
                    message,
                    ackdata,
                    int(time.time()),
                    "broadcastqueued",
                    1,
                    1,
                    "sent",
                    2,
                )
                sqlExecute("""INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", *t)

                toLabel = self.str_broadcast_subscribers

                self.displayNewSentMessage(toAddress, toLabel, fromAddress, subject, message, ackdata)

                shared.workerQueue.put(("sendbroadcast", ""))

                self.ui.comboBoxSendFrom.setCurrentIndex(0)
                self.ui.labelFrom.setText("")
                self.ui.lineEditTo.setText("")
                self.ui.lineEditSubject.setText("")
                self.ui.textEditMessage.setText("")
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.tableWidgetSent.setCurrentCell(0, 0)

    def click_pushButtonLoadFromAddressBook(self):
        self.ui.tabWidget.setCurrentIndex(5)
        for i in range(4):
            time.sleep(0.1)
            self.statusBar().showMessage("")
            time.sleep(0.1)
            self.statusBar().showMessage(
                _translate(
                    "MainWindow",
                    "Right click one or more entries in your address book and select 'Send message to this address'.",
                )
            )

    def click_pushButtonFetchNamecoinID(self):
        nc = namecoinConnection()
        err, addr = nc.query(str(self.ui.lineEditTo.text()))
        if err is not None:
            self.statusBar().showMessage(_translate("MainWindow", "Error: " + err))
        else:
            self.ui.lineEditTo.setText(addr)
            self.statusBar().showMessage(_translate("MainWindow", "Fetched address from namecoin identity."))

    def redrawLabelFrom(self, index):
        self.ui.labelFrom.setText(self.ui.comboBoxSendFrom.itemData(index))
        self.setBroadcastEnablementDependingOnWhetherThisIsAChanAddress(self.ui.comboBoxSendFrom.itemData(index))

    def setBroadcastEnablementDependingOnWhetherThisIsAChanAddress(self, address):
        # If this is a chan then don't let people broadcast because no one
        # should subscribe to chan addresses.
        if shared.safeConfigGetBoolean(str(address), "chan"):
            self.ui.radioButtonSpecific.click()
            self.ui.radioButtonBroadcast.setEnabled(False)
        else:
            self.ui.radioButtonBroadcast.setEnabled(True)

    def rerenderComboBoxSendFrom(self):
        self.ui.comboBoxSendFrom.clear()
        self.ui.labelFrom.setText("")
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != "bitmessagesettings":
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, "enabled"
                )  # I realize that this is poor programming practice but I don't care. It's easier for others to read.
                if isEnabled:
                    self.ui.comboBoxSendFrom.insertItem(
                        0,
                        avatarize(addressInKeysFile),
                        shared.config.get(addressInKeysFile, "label").decode("utf-8"),
                        addressInKeysFile,
                    )
        self.ui.comboBoxSendFrom.insertItem(0, "", "")
        if self.ui.comboBoxSendFrom.count() == 2:
            self.ui.comboBoxSendFrom.setCurrentIndex(1)
            self.redrawLabelFrom(self.ui.comboBoxSendFrom.currentIndex())
        else:
            self.ui.comboBoxSendFrom.setCurrentIndex(0)

    # This function is called by the processmsg function when that function
    # receives a message to an address that is acting as a
    # pseudo-mailing-list. The message will be broadcast out. This function
    # puts the message on the 'Sent' tab.
    def displayNewSentMessage(self, toAddress, toLabel, fromAddress, subject, message, ackdata):
        subject = shared.fixPotentiallyInvalidUTF8Data(subject)
        message = shared.fixPotentiallyInvalidUTF8Data(message)
        try:
            fromLabel = shared.config.get(fromAddress, "label")
        except:
            fromLabel = ""
        if fromLabel == "":
            fromLabel = fromAddress

        self.ui.tableWidgetSent.setSortingEnabled(False)
        self.ui.tableWidgetSent.insertRow(0)
        if toLabel == "":
            newItem = QtWidgets.QTableWidgetItem(
                toAddress.decode("utf-8") if isinstance(toAddress, bytes) else toAddress
            )
            newItem.setToolTip(toAddress.decode("utf-8") if isinstance(toAddress, bytes) else toAddress)
        else:
            newItem = QtWidgets.QTableWidgetItem(toLabel.decode("utf-8") if isinstance(toLabel, bytes) else toLabel)
            newItem.setToolTip(toLabel.decode("utf-8") if isinstance(toLabel, bytes) else toLabel)
        newItem.setData(Qt.UserRole, str(toAddress))
        newItem.setIcon(avatarize(toAddress))
        self.ui.tableWidgetSent.setItem(0, 0, newItem)
        if fromLabel == "":
            newItem = QtWidgets.QTableWidgetItem(
                fromAddress.decode("utf-8") if isinstance(fromAddress, bytes) else fromAddress
            )
            newItem.setToolTip(fromAddress.decode("utf-8") if isinstance(fromAddress, bytes) else fromAddress)
        else:
            newItem = QtWidgets.QTableWidgetItem(
                fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel
            )
            newItem.setToolTip(fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel)
        newItem.setData(Qt.UserRole, str(fromAddress))
        newItem.setIcon(avatarize(fromAddress))
        self.ui.tableWidgetSent.setItem(0, 1, newItem)
        newItem = QtWidgets.QTableWidgetItem(subject.decode("utf-8") if isinstance(subject, bytes) else subject)
        newItem.setToolTip(subject.decode("utf-8") if isinstance(subject, bytes) else subject)
        # newItem.setData(Qt.UserRole, str(message, 'utf-8)')) # No longer hold the message in the table; we'll use a SQL query to display it as needed.
        self.ui.tableWidgetSent.setItem(0, 2, newItem)
        # newItem =  QtWidgets.QTableWidgetItem('Doing work necessary to send
        # broadcast.'+
        # l10n.formatTimestamp())
        newItem = myTableWidgetItem(
            _translate("MainWindow", "Work is queued. %1").replace("%1", l10n.formatTimestamp())
        )
        newItem.setToolTip(_translate("MainWindow", "Work is queued. %1").replace("%1", l10n.formatTimestamp()))
        newItem.setData(Qt.UserRole, QByteArray(ackdata))
        newItem.setData(33, int(time.time()))
        self.ui.tableWidgetSent.setItem(0, 3, newItem)
        self.ui.textEditSentMessage.setPlainText(str(message, "utf-8)"))
        self.ui.tableWidgetSent.setSortingEnabled(True)

    def displayNewInboxMessage(self, inventoryHash, toAddress, fromAddress, subject, message):
        subject = shared.fixPotentiallyInvalidUTF8Data(subject)
        fromLabel = ""
        queryreturn = sqlQuery("""select label from addressbook where address=?""", fromAddress)
        if queryreturn != []:
            for row in queryreturn:
                (fromLabel,) = row
        else:
            # There might be a label in the subscriptions table
            queryreturn = sqlQuery("""select label from subscriptions where address=?""", fromAddress)
            if queryreturn != []:
                for row in queryreturn:
                    (fromLabel,) = row

        try:
            if toAddress == self.str_broadcast_subscribers:
                toLabel = self.str_broadcast_subscribers
            else:
                toLabel = shared.config.get(toAddress, "label")
        except:
            toLabel = ""
        if toLabel == "":
            toLabel = toAddress

        font = QFont()
        font.setBold(True)
        self.ui.tableWidgetInbox.setSortingEnabled(False)
        toLabelStr = toLabel.decode("utf-8", "ignore") if isinstance(toLabel, bytes) else toLabel
        newItem = QtWidgets.QTableWidgetItem(toLabelStr)
        newItem.setToolTip(toLabelStr)
        newItem.setFont(font)
        newItem.setData(Qt.UserRole, str(toAddress))
        if shared.safeConfigGetBoolean(str(toAddress), "mailinglist"):
            newItem.setTextColor(QtGui.QColor(137, 4, 177))  # magenta
        if shared.safeConfigGetBoolean(str(toAddress), "chan"):
            newItem.setTextColor(QtGui.QColor(216, 119, 0))  # orange
        self.ui.tableWidgetInbox.insertRow(0)
        newItem.setIcon(avatarize(toAddress))
        self.ui.tableWidgetInbox.setItem(0, 0, newItem)

        if fromLabel == "":
            fromAddressStr = fromAddress.decode("utf-8", "ignore") if isinstance(fromAddress, bytes) else fromAddress
            newItem = QtWidgets.QTableWidgetItem(fromAddressStr)
            newItem.setToolTip(fromAddressStr)
            if shared.config.getboolean("bitmessagesettings", "showtraynotifications"):
                self.notifierShow(
                    _translate("MainWindow", "New Message"),
                    _translate("MainWindow", "From ")
                    + (fromAddress.decode("utf-8") if isinstance(fromAddress, bytes) else fromAddress),
                    self.SOUND_UNKNOWN,
                    None,
                )
        else:
            newItem = QtWidgets.QTableWidgetItem(
                fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel
            )
            newItem.setToolTip(fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel)
            if shared.config.getboolean("bitmessagesettings", "showtraynotifications"):
                self.notifierShow(
                    _translate("MainWindow", "New Message"),
                    _translate("MainWindow", "From ")
                    + (fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel),
                    self.SOUND_KNOWN,
                    (fromLabel.decode("utf-8") if isinstance(fromLabel, bytes) else fromLabel),
                )
        newItem.setData(Qt.UserRole, str(fromAddress))
        newItem.setFont(font)
        newItem.setIcon(avatarize(fromAddress))
        self.ui.tableWidgetInbox.setItem(0, 1, newItem)
        newItem = QtWidgets.QTableWidgetItem(str(subject, "utf-8)"))
        newItem.setToolTip(str(subject, "utf-8)"))
        # newItem.setData(Qt.UserRole, str(message, 'utf-8)')) # No longer hold the message in the table; we'll use a SQL query to display it as needed.
        newItem.setFont(font)
        self.ui.tableWidgetInbox.setItem(0, 2, newItem)
        newItem = myTableWidgetItem(l10n.formatTimestamp())
        newItem.setToolTip(l10n.formatTimestamp())
        newItem.setData(Qt.UserRole, QByteArray(inventoryHash))
        newItem.setData(33, int(time.time()))
        newItem.setFont(font)
        self.ui.tableWidgetInbox.setItem(0, 3, newItem)
        self.ui.tableWidgetInbox.setSortingEnabled(True)
        self.ubuntuMessagingMenuUpdate(True, newItem, toLabel)

    def click_pushButtonAddAddressBook(self):
        self.AddAddressDialogInstance = AddAddressDialog(self)
        if self.AddAddressDialogInstance.exec():
            if self.AddAddressDialogInstance.ui.labelAddressCheck.text() == _translate(
                "MainWindow", "Address is valid."
            ):
                # First we must check to see if the address is already in the
                # address book. The user cannot add it again or else it will
                # cause problems when updating and deleting the entry.
                address = addBMIfNotPresent(str(self.AddAddressDialogInstance.ui.lineEditAddress.text()))
                label = self.AddAddressDialogInstance.ui.newAddressLabel.text().toUtf8()
                self.addEntryToAddressBook(address, label)
            else:
                self.statusBar().showMessage(
                    _translate("MainWindow", "The address you entered was invalid. Ignoring it.")
                )

    def addEntryToAddressBook(self, address, label):
        queryreturn = sqlQuery("""select * from addressbook where address=?""", address)
        if queryreturn == []:
            self.ui.tableWidgetAddressBook.setSortingEnabled(False)
            self.ui.tableWidgetAddressBook.insertRow(0)
            newItem = QtWidgets.QTableWidgetItem(label.decode("utf-8", "ignore") if isinstance(label, bytes) else label)
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetAddressBook.setItem(0, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(address)
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetAddressBook.setItem(0, 1, newItem)
            self.ui.tableWidgetAddressBook.setSortingEnabled(True)
            sqlExecute("""INSERT INTO addressbook VALUES (?,?)""", str(label), address)
            self.rerenderInboxFromLabels()
            self.rerenderSentToLabels()
        else:
            self.statusBar().showMessage(
                _translate(
                    "MainWindow",
                    "Error: You cannot add the same address to your address book twice. Try renaming the existing one if you want.",
                )
            )

    def addSubscription(self, address, label):
        address = addBMIfNotPresent(address)
        # This should be handled outside of this function, for error displaying and such, but it must also be checked here.
        if shared.isAddressInMySubscriptionsList(address):
            return
        # Add to UI list
        self.ui.tableWidgetSubscriptions.setSortingEnabled(False)
        self.ui.tableWidgetSubscriptions.insertRow(0)
        newItem = QtWidgets.QTableWidgetItem(label.decode("utf-8", "ignore") if isinstance(label, bytes) else label)
        newItem.setIcon(avatarize(address))
        self.ui.tableWidgetSubscriptions.setItem(0, 0, newItem)
        newItem = QtWidgets.QTableWidgetItem(address)
        newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidgetSubscriptions.setItem(0, 1, newItem)
        self.ui.tableWidgetSubscriptions.setSortingEnabled(True)
        # Add to database (perhaps this should be separated from the MyForm class)
        sqlExecute("""INSERT INTO subscriptions VALUES (?,?,?)""", str(label), address, True)
        self.rerenderInboxFromLabels()
        shared.reloadBroadcastSendersForWhichImWatching()

    def click_pushButtonAddSubscription(self):
        self.NewSubscriptionDialogInstance = NewSubscriptionDialog(self)
        if self.NewSubscriptionDialogInstance.exec():
            if self.NewSubscriptionDialogInstance.ui.labelAddressCheck.text() != _translate(
                "MainWindow", "Address is valid."
            ):
                self.statusBar().showMessage(
                    _translate("MainWindow", "The address you entered was invalid. Ignoring it.")
                )
                return
            address = addBMIfNotPresent(str(self.NewSubscriptionDialogInstance.ui.lineEditSubscriptionAddress.text()))
            # We must check to see if the address is already in the subscriptions list. The user cannot add it again or else it will cause problems when updating and deleting the entry.
            if shared.isAddressInMySubscriptionsList(address):
                self.statusBar().showMessage(
                    _translate(
                        "MainWindow",
                        "Error: You cannot add the same address to your subsciptions twice. Perhaps rename the existing one if you want.",
                    )
                )
                return
            label = self.NewSubscriptionDialogInstance.ui.newsubscriptionlabel.text()
            self.addSubscription(address, label)
            # Now, if the user wants to display old broadcasts, let's get them out of the inventory and put them
            # in the objectProcessorQueue to be processed
            if self.NewSubscriptionDialogInstance.ui.checkBoxDisplayMessagesAlreadyInInventory.isChecked():
                status, addressVersion, streamNumber, ripe = decodeAddress(address)
                shared.flushInventory()
                doubleHashOfAddressData = hashlib.sha512(
                    hashlib.sha512(encodeVarint(addressVersion) + encodeVarint(streamNumber) + ripe).digest()
                ).digest()
                tag = doubleHashOfAddressData[32:]
                queryreturn = sqlQuery("""select payload from inventory where objecttype='broadcast' and tag=?""", tag)
                for row in queryreturn:
                    (payload,) = row
                    objectType = "broadcast"
                    with shared.objectProcessorQueueSizeLock:
                        shared.objectProcessorQueueSize += len(payload)
                        shared.objectProcessorQueue.put((objectType, payload))

    def loadBlackWhiteList(self):
        # Initialize the Blacklist or Whitelist table
        listType = shared.config.get("bitmessagesettings", "blackwhitelist")
        if listType == "black":
            queryreturn = sqlQuery("""SELECT label, address, enabled FROM blacklist""")
        else:
            queryreturn = sqlQuery("""SELECT label, address, enabled FROM whitelist""")
        for row in queryreturn:
            label, address, enabled = row
            self.ui.tableWidgetBlacklist.insertRow(0)
            newItem = QtWidgets.QTableWidgetItem(label.decode("utf-8", "ignore") if isinstance(label, bytes) else label)
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetBlacklist.setItem(0, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(address)
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            self.ui.tableWidgetBlacklist.setItem(0, 1, newItem)

    def click_pushButtonStatusIcon(self):
        print("click_pushButtonStatusIcon")
        self.iconGlossaryInstance = iconGlossaryDialog(self)
        if self.iconGlossaryInstance.exec():
            pass

    def click_actionHelp(self):
        self.helpDialogInstance = helpDialog(self)
        self.helpDialogInstance.exec()

    def click_actionAbout(self):
        self.aboutDialogInstance = aboutDialog(self)
        self.aboutDialogInstance.exec()

    def click_actionSettings(self):
        self.settingsDialogInstance = settingsDialog(self)
        if self.settingsDialogInstance.exec():
            shared.config.set(
                "bitmessagesettings",
                "startonlogon",
                str(self.settingsDialogInstance.ui.checkBoxStartOnLogon.isChecked()),
            )
            shared.config.set(
                "bitmessagesettings",
                "minimizetotray",
                str(self.settingsDialogInstance.ui.checkBoxMinimizeToTray.isChecked()),
            )
            shared.config.set(
                "bitmessagesettings",
                "showtraynotifications",
                str(self.settingsDialogInstance.ui.checkBoxShowTrayNotifications.isChecked()),
            )
            shared.config.set(
                "bitmessagesettings", "startintray", str(self.settingsDialogInstance.ui.checkBoxStartInTray.isChecked())
            )
            shared.config.set(
                "bitmessagesettings",
                "willinglysendtomobile",
                str(self.settingsDialogInstance.ui.checkBoxWillinglySendToMobile.isChecked()),
            )
            shared.config.set(
                "bitmessagesettings",
                "useidenticons",
                str(self.settingsDialogInstance.ui.checkBoxUseIdenticons.isChecked()),
            )
            shared.config.set(
                "bitmessagesettings", "replybelow", str(self.settingsDialogInstance.ui.checkBoxReplyBelow.isChecked())
            )

            lang_ind = int(self.settingsDialogInstance.ui.languageComboBox.currentIndex())
            if not languages[lang_ind] == "other":
                shared.config.set("bitmessagesettings", "userlocale", languages[lang_ind])

            if int(shared.config.get("bitmessagesettings", "port")) != int(
                self.settingsDialogInstance.ui.lineEditTCPPort.text()
            ):
                if not shared.safeConfigGetBoolean("bitmessagesettings", "dontconnect"):
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Restart"),
                        _translate(
                            "MainWindow", "You must restart Bitmessage for the port number change to take effect."
                        ),
                    )
                shared.config.set(
                    "bitmessagesettings", "port", str(self.settingsDialogInstance.ui.lineEditTCPPort.text())
                )
            # print 'self.settingsDialogInstance.ui.comboBoxProxyType.currentText()', self.settingsDialogInstance.ui.comboBoxProxyType.currentText()
            # print 'self.settingsDialogInstance.ui.comboBoxProxyType.currentText())[0:5]', self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5]
            if (
                shared.config.get("bitmessagesettings", "socksproxytype") == "none"
                and self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5] == "SOCKS"
            ):
                if shared.statusIconColor != "red":
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Restart"),
                        _translate(
                            "MainWindow",
                            "Bitmessage will use your proxy from now on but you may want to manually restart Bitmessage now to close existing connections (if any).",
                        ),
                    )
            if (
                shared.config.get("bitmessagesettings", "socksproxytype")[0:5] == "SOCKS"
                and self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5] != "SOCKS"
            ):
                self.statusBar().showMessage("")
            if self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5] == "SOCKS":
                shared.config.set(
                    "bitmessagesettings",
                    "socksproxytype",
                    str(self.settingsDialogInstance.ui.comboBoxProxyType.currentText()),
                )
            else:
                shared.config.set("bitmessagesettings", "socksproxytype", "none")
            shared.config.set(
                "bitmessagesettings",
                "socksauthentication",
                str(self.settingsDialogInstance.ui.checkBoxAuthentication.isChecked()),
            )
            shared.config.set(
                "bitmessagesettings", "sockshostname", str(self.settingsDialogInstance.ui.lineEditSocksHostname.text())
            )
            shared.config.set(
                "bitmessagesettings", "socksport", str(self.settingsDialogInstance.ui.lineEditSocksPort.text())
            )
            shared.config.set(
                "bitmessagesettings", "socksusername", str(self.settingsDialogInstance.ui.lineEditSocksUsername.text())
            )
            shared.config.set(
                "bitmessagesettings", "sockspassword", str(self.settingsDialogInstance.ui.lineEditSocksPassword.text())
            )
            shared.config.set(
                "bitmessagesettings", "sockslisten", str(self.settingsDialogInstance.ui.checkBoxSocksListen.isChecked())
            )

            shared.config.set("bitmessagesettings", "namecoinrpctype", self.settingsDialogInstance.getNamecoinType())
            shared.config.set(
                "bitmessagesettings", "namecoinrpchost", str(self.settingsDialogInstance.ui.lineEditNamecoinHost.text())
            )
            shared.config.set(
                "bitmessagesettings", "namecoinrpcport", str(self.settingsDialogInstance.ui.lineEditNamecoinPort.text())
            )
            shared.config.set(
                "bitmessagesettings", "namecoinrpcuser", str(self.settingsDialogInstance.ui.lineEditNamecoinUser.text())
            )
            shared.config.set(
                "bitmessagesettings",
                "namecoinrpcpassword",
                str(self.settingsDialogInstance.ui.lineEditNamecoinPassword.text()),
            )

            if float(self.settingsDialogInstance.ui.lineEditTotalDifficulty.text()) >= 1:
                shared.config.set(
                    "bitmessagesettings",
                    "defaultnoncetrialsperbyte",
                    str(
                        int(
                            float(self.settingsDialogInstance.ui.lineEditTotalDifficulty.text())
                            * shared.networkDefaultProofOfWorkNonceTrialsPerByte
                        )
                    ),
                )
            if float(self.settingsDialogInstance.ui.lineEditSmallMessageDifficulty.text()) >= 1:
                shared.config.set(
                    "bitmessagesettings",
                    "defaultpayloadlengthextrabytes",
                    str(
                        int(
                            float(self.settingsDialogInstance.ui.lineEditSmallMessageDifficulty.text())
                            * shared.networkDefaultPayloadLengthExtraBytes
                        )
                    ),
                )
            if (
                float(self.settingsDialogInstance.ui.lineEditMaxAcceptableTotalDifficulty.text()) >= 1
                or float(self.settingsDialogInstance.ui.lineEditMaxAcceptableTotalDifficulty.text()) == 0
            ):
                shared.config.set(
                    "bitmessagesettings",
                    "maxacceptablenoncetrialsperbyte",
                    str(
                        int(
                            float(self.settingsDialogInstance.ui.lineEditMaxAcceptableTotalDifficulty.text())
                            * shared.networkDefaultProofOfWorkNonceTrialsPerByte
                        )
                    ),
                )
            if (
                float(self.settingsDialogInstance.ui.lineEditMaxAcceptableSmallMessageDifficulty.text()) >= 1
                or float(self.settingsDialogInstance.ui.lineEditMaxAcceptableSmallMessageDifficulty.text()) == 0
            ):
                shared.config.set(
                    "bitmessagesettings",
                    "maxacceptablepayloadlengthextrabytes",
                    str(
                        int(
                            float(self.settingsDialogInstance.ui.lineEditMaxAcceptableSmallMessageDifficulty.text())
                            * shared.networkDefaultPayloadLengthExtraBytes
                        )
                    ),
                )
            # start:UI setting to stop trying to send messages after X days/months
            # I'm open to changing this UI to something else if someone has a better idea.
            if (self.settingsDialogInstance.ui.lineEditDays.text() == "") and (
                self.settingsDialogInstance.ui.lineEditMonths.text() == ""
            ):  # We need to handle this special case. Bitmessage has its default behavior. The input is blank/blank
                shared.config.set("bitmessagesettings", "stopresendingafterxdays", "")
                shared.config.set("bitmessagesettings", "stopresendingafterxmonths", "")
                shared.maximumLengthOfTimeToBotherResendingMessages = float("inf")
            try:
                float(self.settingsDialogInstance.ui.lineEditDays.text())
                lineEditDaysIsValidFloat = True
            except:
                lineEditDaysIsValidFloat = False
            try:
                float(self.settingsDialogInstance.ui.lineEditMonths.text())
                lineEditMonthsIsValidFloat = True
            except:
                lineEditMonthsIsValidFloat = False
            if lineEditDaysIsValidFloat and not lineEditMonthsIsValidFloat:
                self.settingsDialogInstance.ui.lineEditMonths.setText("0")
            if lineEditMonthsIsValidFloat and not lineEditDaysIsValidFloat:
                self.settingsDialogInstance.ui.lineEditDays.setText("0")
            if lineEditDaysIsValidFloat or lineEditMonthsIsValidFloat:
                if (
                    float(self.settingsDialogInstance.ui.lineEditDays.text()) >= 0
                    and float(self.settingsDialogInstance.ui.lineEditMonths.text()) >= 0
                ):
                    shared.maximumLengthOfTimeToBotherResendingMessages = (
                        float(str(self.settingsDialogInstance.ui.lineEditDays.text())) * 24 * 60 * 60
                    ) + (float(str(self.settingsDialogInstance.ui.lineEditMonths.text())) * (60 * 60 * 24 * 365) / 12)
                    if (
                        shared.maximumLengthOfTimeToBotherResendingMessages < 432000
                    ):  # If the time period is less than 5 hours, we give zero values to all fields. No message will be sent again.
                        QMessageBox.about(
                            self,
                            _translate("MainWindow", "Will not resend ever"),
                            _translate(
                                "MainWindow",
                                "Note that the time limit you entered is less than the amount of time Bitmessage waits for the first resend attempt therefore your messages will never be resent.",
                            ),
                        )
                        shared.config.set("bitmessagesettings", "stopresendingafterxdays", "0")
                        shared.config.set("bitmessagesettings", "stopresendingafterxmonths", "0")
                        shared.maximumLengthOfTimeToBotherResendingMessages = 0
                    else:
                        shared.config.set(
                            "bitmessagesettings",
                            "stopresendingafterxdays",
                            str(float(self.settingsDialogInstance.ui.lineEditDays.text())),
                        )
                        shared.config.set(
                            "bitmessagesettings",
                            "stopresendingafterxmonths",
                            str(float(self.settingsDialogInstance.ui.lineEditMonths.text())),
                        )
            # end

            # if str(self.settingsDialogInstance.ui.comboBoxMaxCores.currentText()) == 'All':
            #    shared.config.set('bitmessagesettings', 'maxcores', '99999')
            # else:
            # shared.config.set('bitmessagesettings', 'maxcores',
            # str(self.settingsDialogInstance.ui.comboBoxMaxCores.currentText()))

            with open(shared.appdata + "keys.dat", "w") as configfile:
                shared.config.write(configfile)

            if "win32" in sys.platform or "win64" in sys.platform:
                # Auto-startup for Windows
                RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                self.settings = QSettings(RUN_PATH, QSettings.NativeFormat)
                if shared.config.getboolean("bitmessagesettings", "startonlogon"):
                    self.settings.setValue("PyBitmessage", sys.argv[0])
                else:
                    self.settings.remove("PyBitmessage")
            elif "darwin" in sys.platform:
                # startup for mac
                pass
            elif "linux" in sys.platform:
                # startup for linux
                pass

            if (
                shared.appdata != "" and self.settingsDialogInstance.ui.checkBoxPortableMode.isChecked()
            ):  # If we are NOT using portable mode now but the user selected that we should.
                # Write the keys.dat file to disk in the new location
                sqlStoredProcedure("movemessagstoprog")
                with open("keys.dat", "w") as configfile:
                    shared.config.write(configfile)
                # Write the knownnodes.dat file to disk in the new location
                shared.knownNodesLock.acquire()
                output = open("knownnodes.dat", "wb")
                pickle.dump(shared.knownNodes, output)
                output.close()
                shared.knownNodesLock.release()
                os.remove(shared.appdata + "keys.dat")
                os.remove(shared.appdata + "knownnodes.dat")
                previousAppdataLocation = shared.appdata
                shared.appdata = ""
                debug.restartLoggingInUpdatedAppdataLocation()
                try:
                    os.remove(previousAppdataLocation + "debug.log")
                    os.remove(previousAppdataLocation + "debug.log.1")
                except:
                    pass

            if (
                shared.appdata == "" and not self.settingsDialogInstance.ui.checkBoxPortableMode.isChecked()
            ):  # If we ARE using portable mode now but the user selected that we shouldn't.
                shared.appdata = shared.lookupAppdataFolder()
                if not os.path.exists(shared.appdata):
                    os.makedirs(shared.appdata)
                sqlStoredProcedure("movemessagstoappdata")
                # Write the keys.dat file to disk in the new location
                with open(shared.appdata + "keys.dat", "w") as configfile:
                    shared.config.write(configfile)
                # Write the knownnodes.dat file to disk in the new location
                shared.knownNodesLock.acquire()
                output = open(shared.appdata + "knownnodes.dat", "wb")
                pickle.dump(shared.knownNodes, output)
                output.close()
                shared.knownNodesLock.release()
                os.remove("keys.dat")
                os.remove("knownnodes.dat")
                debug.restartLoggingInUpdatedAppdataLocation()
                try:
                    os.remove("debug.log")
                    os.remove("debug.log.1")
                except:
                    pass

    def click_radioButtonBlacklist(self):
        if shared.config.get("bitmessagesettings", "blackwhitelist") == "white":
            shared.config.set("bitmessagesettings", "blackwhitelist", "black")
            with open(shared.appdata + "keys.dat", "w") as configfile:
                shared.config.write(configfile)
            # self.ui.tableWidgetBlacklist.clearContents()
            self.ui.tableWidgetBlacklist.setRowCount(0)
            self.loadBlackWhiteList()
            self.ui.tabWidget.setTabText(6, "Blacklist")

    def click_radioButtonWhitelist(self):
        if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
            shared.config.set("bitmessagesettings", "blackwhitelist", "white")
            with open(shared.appdata + "keys.dat", "w") as configfile:
                shared.config.write(configfile)
            # self.ui.tableWidgetBlacklist.clearContents()
            self.ui.tableWidgetBlacklist.setRowCount(0)
            self.loadBlackWhiteList()
            self.ui.tabWidget.setTabText(6, "Whitelist")

    def click_pushButtonAddBlacklist(self):
        self.NewBlacklistDialogInstance = AddAddressDialog(self)
        if self.NewBlacklistDialogInstance.exec():
            if self.NewBlacklistDialogInstance.ui.labelAddressCheck.text() == _translate(
                "MainWindow", "Address is valid."
            ):
                address = addBMIfNotPresent(str(self.NewBlacklistDialogInstance.ui.lineEditAddress.text()))
                # First we must check to see if the address is already in the
                # address book. The user cannot add it again or else it will
                # cause problems when updating and deleting the entry.
                t = (address,)
                if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
                    sql = """select * from blacklist where address=?"""
                else:
                    sql = """select * from whitelist where address=?"""
                queryreturn = sqlQuery(sql, *t)
                if queryreturn == []:
                    self.ui.tableWidgetBlacklist.setSortingEnabled(False)
                    self.ui.tableWidgetBlacklist.insertRow(0)
                    newItem = QtWidgets.QTableWidgetItem(
                        str(self.NewBlacklistDialogInstance.ui.newAddressLabel.text().toUtf8(), "utf-8")
                    )
                    newItem.setIcon(avatarize(address))
                    self.ui.tableWidgetBlacklist.setItem(0, 0, newItem)
                    newItem = QtWidgets.QTableWidgetItem(address)
                    newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                    self.ui.tableWidgetBlacklist.setItem(0, 1, newItem)
                    self.ui.tableWidgetBlacklist.setSortingEnabled(True)
                    t = (str(self.NewBlacklistDialogInstance.ui.newAddressLabel.text().toUtf8()), address, True)
                    if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
                        sql = """INSERT INTO blacklist VALUES (?,?,?)"""
                    else:
                        sql = """INSERT INTO whitelist VALUES (?,?,?)"""
                    sqlExecute(sql, *t)
                else:
                    self.statusBar().showMessage(
                        _translate(
                            "MainWindow",
                            "Error: You cannot add the same address to your list twice. Perhaps rename the existing one if you want.",
                        )
                    )
            else:
                self.statusBar().showMessage(
                    _translate("MainWindow", "The address you entered was invalid. Ignoring it.")
                )

    def on_action_SpecialAddressBehaviorDialog(self):
        self.dialog = SpecialAddressBehaviorDialog(self)
        # For Modal dialogs
        if self.dialog.exec():
            currentRow = self.ui.tableWidgetYourIdentities.currentRow()
            addressAtCurrentRow = str(self.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
            if shared.safeConfigGetBoolean(addressAtCurrentRow, "chan"):
                return
            if self.dialog.ui.radioButtonBehaveNormalAddress.isChecked():
                shared.config.set(str(addressAtCurrentRow), "mailinglist", "false")
                # Set the color to either black or grey
                if shared.config.getboolean(addressAtCurrentRow, "enabled"):
                    self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(
                        QApplication.palette().text().color()
                    )
                else:
                    self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
            else:
                shared.config.set(str(addressAtCurrentRow), "mailinglist", "true")
                shared.config.set(
                    str(addressAtCurrentRow),
                    "mailinglistname",
                    str(self.dialog.ui.lineEditMailingListName.text().toUtf8()),
                )
                self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(137, 4, 177))  # magenta
            with open(shared.appdata + "keys.dat", "w") as configfile:
                shared.config.write(configfile)
            self.rerenderInboxToLabels()

    def click_NewAddressDialog(self):
        self.dialog = NewAddressDialog(self)
        # For Modal dialogs
        if self.dialog.exec():
            # self.dialog.ui.buttonBox.enabled = False
            if self.dialog.ui.radioButtonRandomAddress.isChecked():
                if self.dialog.ui.radioButtonMostAvailable.isChecked():
                    streamNumberForAddress = 1
                else:
                    # User selected 'Use the same stream as an existing
                    # address.'
                    streamNumberForAddress = decodeAddress(self.dialog.ui.comboBoxExisting.currentText())[2]
                shared.addressGeneratorQueue.put(
                    (
                        "createRandomAddress",
                        4,
                        streamNumberForAddress,
                        str(self.dialog.ui.newaddresslabel.text().toUtf8()),
                        1,
                        "",
                        self.dialog.ui.checkBoxEighteenByteRipe.isChecked(),
                    )
                )
            else:
                if self.dialog.ui.lineEditPassphrase.text() != self.dialog.ui.lineEditPassphraseAgain.text():
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Passphrase mismatch"),
                        _translate("MainWindow", "The passphrase you entered twice doesn't match. Try again."),
                    )
                elif self.dialog.ui.lineEditPassphrase.text() == "":
                    QMessageBox.about(
                        self,
                        _translate("MainWindow", "Choose a passphrase"),
                        _translate("MainWindow", "You really do need a passphrase."),
                    )
                else:
                    streamNumberForAddress = 1  # this will eventually have to be replaced by logic to determine the most available stream number.
                    shared.addressGeneratorQueue.put(
                        (
                            "createDeterministicAddresses",
                            4,
                            streamNumberForAddress,
                            "unused deterministic address",
                            self.dialog.ui.spinBoxNumberOfAddressesToMake.value(),
                            self.dialog.ui.lineEditPassphrase.text().toUtf8(),
                            self.dialog.ui.checkBoxEighteenByteRipe.isChecked(),
                        )
                    )
        else:
            print("new address dialog box rejected")

    # Quit selected from menu or application indicator
    def quit(self):
        """quit_msg = "Are you sure you want to exit Bitmessage?"
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                         quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply is QtWidgets.QMessageBox.No:
            return
        """
        shared.doCleanShutdown()
        self.tray.hide()
        # unregister the messaging system
        if self.mmapp is not None:
            self.mmapp.unregister()
        self.statusBar().showMessage(_translate("MainWindow", "All done. Closing user interface."))
        os._exit(0)

    # window close event
    def closeEvent(self, event):
        self.appIndicatorHide()
        minimizeonclose = False

        try:
            minimizeonclose = shared.config.getboolean("bitmessagesettings", "minimizeonclose")
        except Exception:
            pass

        if minimizeonclose:
            # minimize the application
            event.ignore()
        else:
            # quit the application
            event.accept()
            self.quit()

    def on_action_InboxMessageForceHtml(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()

        msgid = str(self.ui.tableWidgetInbox.item(currentInboxRow, 3).data(Qt.UserRole))
        queryreturn = sqlQuery("""select message from inbox where msgid=?""", msgid)
        if queryreturn != []:
            for row in queryreturn:
                (messageText,) = row

        lines = messageText.split("\n") if isinstance(messageText, str) else messageText.split(b"\n")
        totalLines = len(lines)
        for i in range(totalLines):
            line = lines[i] if isinstance(lines[i], str) else lines[i].decode("utf-8", "ignore")
            if "Message ostensibly from " in line:
                lines[i] = '<p style="font-size: 12px; color: grey;">%s</span></p>' % (line)
            elif line == "------------------------------------------------------":
                lines[i] = "<hr>"
            elif line == "" and (i + 1) < totalLines:
                next_line = lines[i + 1] if isinstance(lines[i + 1], str) else lines[i + 1].decode("utf-8", "ignore")
                if next_line != "------------------------------------------------------":
                    lines[i] = "<br><br>"
            elif not isinstance(lines[i], str):
                lines[i] = line
        content = " ".join(lines)  # To keep the whitespace between lines
        if isinstance(content, bytes):
            content = content.decode("utf-8", "ignore")
        self.ui.textEditInboxMessage.setHtml(content)

    def on_action_InboxMarkUnread(self):
        font = QFont()
        font.setBold(True)
        for row in self.ui.tableWidgetInbox.selectedIndexes():
            currentRow = row.row()
            inventoryHashToMarkUnread = str(self.ui.tableWidgetInbox.item(currentRow, 3).data(Qt.UserRole))
            sqlExecute("""UPDATE inbox SET read=0 WHERE msgid=?""", inventoryHashToMarkUnread)
            self.ui.tableWidgetInbox.item(currentRow, 0).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 1).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 2).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 3).setFont(font)
        self.changedInboxUnread()
        # self.ui.tableWidgetInbox.selectRow(currentRow + 1)
        # This doesn't de-select the last message if you try to mark it unread, but that doesn't interfere. Might not be necessary.
        # We could also select upwards, but then our problem would be with the topmost message.
        # self.ui.tableWidgetInbox.clearSelection() manages to mark the message as read again.

    # Format predefined text on message reply.
    def quoted_text(self, message):
        if not shared.safeConfigGetBoolean("bitmessagesettings", "replybelow"):
            return "\n\n------------------------------------------------------\n" + message

        quoteWrapper = textwrap.TextWrapper(
            replace_whitespace=False,
            initial_indent="> ",
            subsequent_indent="> ",
            break_long_words=False,
            break_on_hyphens=False,
        )

        def quote_line(line):
            # Do quote empty lines.
            if line == "" or line.isspace():
                return "> "
            # Quote already quoted lines, but do not wrap them.
            elif line[0:2] == "> ":
                return "> " + line
            # Wrap and quote lines/paragraphs new to this message.
            else:
                return quoteWrapper.fill(line)

        return "\n".join([quote_line(l) for l in message.splitlines()]) + "\n\n"

    def on_action_InboxReply(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()
        toAddressAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(currentInboxRow, 0).data(Qt.UserRole))
        fromAddressAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(currentInboxRow, 1).data(Qt.UserRole))
        msgid = str(self.ui.tableWidgetInbox.item(currentInboxRow, 3).data(Qt.UserRole))
        queryreturn = sqlQuery("""select message from inbox where msgid=?""", msgid)
        if queryreturn != []:
            for row in queryreturn:
                (messageAtCurrentInboxRow,) = row
        if toAddressAtCurrentInboxRow == self.str_broadcast_subscribers:
            self.ui.labelFrom.setText("")
        elif not shared.config.has_section(toAddressAtCurrentInboxRow):
            QtWidgets.QMessageBox.information(
                self,
                _translate("MainWindow", "Address not found"),
                _translate("MainWindow", "Bitmessage cannot find your address %1. Perhaps you removed it?").replace(
                    "%1", toAddressAtCurrentInboxRow
                ),
                QMessageBox.Ok,
            )
            self.ui.labelFrom.setText("")
        elif not shared.config.getboolean(toAddressAtCurrentInboxRow, "enabled"):
            QtWidgets.QMessageBox.information(
                self,
                _translate("MainWindow", "Address disabled"),
                _translate(
                    "MainWindow",
                    "Error: The address from which you are trying to send is disabled. You'll have to enable it on the 'Your Identities' tab before using it.",
                ),
                QMessageBox.Ok,
            )
            self.ui.labelFrom.setText("")
        else:
            self.ui.labelFrom.setText(toAddressAtCurrentInboxRow)
            self.setBroadcastEnablementDependingOnWhetherThisIsAChanAddress(toAddressAtCurrentInboxRow)

        self.ui.lineEditTo.setText(str(fromAddressAtCurrentInboxRow))

        # If the previous message was to a chan then we should send our reply to the chan rather than to the particular person who sent the message.
        if shared.config.has_section(toAddressAtCurrentInboxRow):
            if shared.safeConfigGetBoolean(toAddressAtCurrentInboxRow, "chan"):
                print("original sent to a chan. Setting the to address in the reply to the chan address.")
                self.ui.lineEditTo.setText(str(toAddressAtCurrentInboxRow))

        listOfAddressesInComboBoxSendFrom = [
            str(self.ui.comboBoxSendFrom.itemData(i)) for i in range(self.ui.comboBoxSendFrom.count())
        ]
        if toAddressAtCurrentInboxRow in listOfAddressesInComboBoxSendFrom:
            currentIndex = listOfAddressesInComboBoxSendFrom.index(toAddressAtCurrentInboxRow)
            self.ui.comboBoxSendFrom.setCurrentIndex(currentIndex)
        else:
            self.ui.comboBoxSendFrom.setCurrentIndex(0)

        msgStr = (
            messageAtCurrentInboxRow.decode("utf-8", "ignore")
            if isinstance(messageAtCurrentInboxRow, bytes)
            else messageAtCurrentInboxRow
        )
        quotedText = self.quoted_text(msgStr)
        self.ui.textEditMessage.setText(quotedText)
        if self.ui.tableWidgetInbox.item(currentInboxRow, 2).text()[0:3] in ["Re:", "RE:"]:
            self.ui.lineEditSubject.setText(self.ui.tableWidgetInbox.item(currentInboxRow, 2).text())
        else:
            self.ui.lineEditSubject.setText("Re: " + self.ui.tableWidgetInbox.item(currentInboxRow, 2).text())
        self.ui.radioButtonSpecific.setChecked(True)
        self.ui.tabWidget.setCurrentIndex(1)

    def on_action_InboxAddSenderToAddressBook(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()
        # self.ui.tableWidgetInbox.item(currentRow,1).data(Qt.UserRole)
        addressAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(currentInboxRow, 1).data(Qt.UserRole))
        # Let's make sure that it isn't already in the address book
        queryreturn = sqlQuery("""select * from addressbook where address=?""", addressAtCurrentInboxRow)
        if queryreturn == []:
            self.ui.tableWidgetAddressBook.insertRow(0)
            newItem = QtWidgets.QTableWidgetItem("--New entry. Change label in Address Book.--")
            self.ui.tableWidgetAddressBook.setItem(0, 0, newItem)
            newItem.setIcon(avatarize(addressAtCurrentInboxRow))
            newItem = QtWidgets.QTableWidgetItem(addressAtCurrentInboxRow)
            newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidgetAddressBook.setItem(0, 1, newItem)
            sqlExecute(
                """INSERT INTO addressbook VALUES (?,?)""",
                "--New entry. Change label in Address Book.--",
                addressAtCurrentInboxRow,
            )
            self.ui.tabWidget.setCurrentIndex(5)
            self.ui.tableWidgetAddressBook.setCurrentCell(0, 0)
            self.statusBar().showMessage(
                _translate("MainWindow", "Entry added to the Address Book. Edit the label to your liking.")
            )
        else:
            self.statusBar().showMessage(
                _translate(
                    "MainWindow",
                    "Error: You cannot add the same address to your address book twice. Try renaming the existing one if you want.",
                )
            )

    # Send item on the Inbox tab to trash
    def on_action_InboxTrash(self):
        while self.ui.tableWidgetInbox.selectedIndexes() != []:
            currentRow = self.ui.tableWidgetInbox.selectedIndexes()[0].row()
            inventoryHashToTrash = str(self.ui.tableWidgetInbox.item(currentRow, 3).data(Qt.UserRole))
            sqlExecute("""UPDATE inbox SET folder='trash' WHERE msgid=?""", inventoryHashToTrash)
            self.ui.textEditInboxMessage.setText("")
            self.ui.tableWidgetInbox.removeRow(currentRow)
            self.statusBar().showMessage(
                _translate(
                    "MainWindow",
                    "Moved items to trash. There is no user interface to view your trash, but it is still on disk if you are desperate to get it back.",
                )
            )
        if currentRow == 0:
            self.ui.tableWidgetInbox.selectRow(currentRow)
        else:
            self.ui.tableWidgetInbox.selectRow(currentRow - 1)

    def on_action_InboxSaveMessageAs(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()
        try:
            subjectAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(currentInboxRow, 2).text())
        except:
            subjectAtCurrentInboxRow = ""

        # Retrieve the message data out of the SQL database
        msgid = str(self.ui.tableWidgetInbox.item(currentInboxRow, 3).data(Qt.UserRole))
        queryreturn = sqlQuery("""select message from inbox where msgid=?""", msgid)
        if queryreturn != []:
            for row in queryreturn:
                (message,) = row

        defaultFilename = "".join(x for x in subjectAtCurrentInboxRow if x.isalnum()) + ".txt"
        filename = QFileDialog.getSaveFileName(
            self, _translate("MainWindow", "Save As."), defaultFilename, "Text files (*.txt);;All files (*.*)"
        )
        if filename == "":
            return
        try:
            f = open(filename, "w")
            f.write(message)
            f.close()
        except Exception as e:
            sys.stderr.write("Write error: " + e)
            self.statusBar().showMessage(_translate("MainWindow", "Write error."))

    # Send item on the Sent tab to trash
    def on_action_SentTrash(self):
        while self.ui.tableWidgetSent.selectedIndexes() != []:
            currentRow = self.ui.tableWidgetSent.selectedIndexes()[0].row()
            ackdataToTrash = str(self.ui.tableWidgetSent.item(currentRow, 3).data(Qt.UserRole))
            sqlExecute("""UPDATE sent SET folder='trash' WHERE ackdata=?""", ackdataToTrash)
            self.ui.textEditSentMessage.setPlainText("")
            self.ui.tableWidgetSent.removeRow(currentRow)
            self.statusBar().showMessage(
                _translate(
                    "MainWindow",
                    "Moved items to trash. There is no user interface to view your trash, but it is still on disk if you are desperate to get it back.",
                )
            )
        if currentRow == 0:
            self.ui.tableWidgetSent.selectRow(currentRow)
        else:
            self.ui.tableWidgetSent.selectRow(currentRow - 1)

    def on_action_ForceSend(self):
        currentRow = self.ui.tableWidgetSent.currentRow()
        addressAtCurrentRow = str(self.ui.tableWidgetSent.item(currentRow, 0).data(Qt.UserRole))
        toRipe = decodeAddress(addressAtCurrentRow)[3]
        sqlExecute(
            """UPDATE sent SET status='forcepow' WHERE toripe=? AND status='toodifficult' and folder='sent' """, toRipe
        )
        queryreturn = sqlQuery("""select ackdata FROM sent WHERE status='forcepow' """)
        for row in queryreturn:
            (ackdata,) = row
            shared.UISignalQueue.put(
                ("updateSentItemStatusByAckdata", (ackdata, "Overriding maximum-difficulty setting. Work queued."))
            )
        shared.workerQueue.put(("sendmessage", ""))

    def on_action_SentClipboard(self):
        currentRow = self.ui.tableWidgetSent.currentRow()
        addressAtCurrentRow = str(self.ui.tableWidgetSent.item(currentRow, 0).data(Qt.UserRole))
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    # Group of functions for the Address Book dialog box
    def on_action_AddressBookNew(self):
        self.click_pushButtonAddAddressBook()

    def on_action_AddressBookDelete(self):
        while self.ui.tableWidgetAddressBook.selectedIndexes() != []:
            currentRow = self.ui.tableWidgetAddressBook.selectedIndexes()[0].row()
            labelAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow, 0).text().toUtf8()
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow, 1).text()
            sqlExecute(
                """DELETE FROM addressbook WHERE label=? AND address=?""",
                str(labelAtCurrentRow),
                str(addressAtCurrentRow),
            )
            self.ui.tableWidgetAddressBook.removeRow(currentRow)
            self.rerenderInboxFromLabels()
            self.rerenderSentToLabels()

    def on_action_AddressBookClipboard(self):
        fullStringOfAddresses = ""
        listOfSelectedRows = {}
        for i in range(len(self.ui.tableWidgetAddressBook.selectedIndexes())):
            listOfSelectedRows[self.ui.tableWidgetAddressBook.selectedIndexes()[i].row()] = 0
        for currentRow in listOfSelectedRows:
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow, 1).text()
            if fullStringOfAddresses == "":
                fullStringOfAddresses = addressAtCurrentRow
            else:
                fullStringOfAddresses += ", " + str(addressAtCurrentRow)
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(fullStringOfAddresses)

    def on_action_AddressBookSend(self):
        listOfSelectedRows = {}
        for i in range(len(self.ui.tableWidgetAddressBook.selectedIndexes())):
            listOfSelectedRows[self.ui.tableWidgetAddressBook.selectedIndexes()[i].row()] = 0
        for currentRow in listOfSelectedRows:
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow, 1).text()
            if self.ui.lineEditTo.text() == "":
                self.ui.lineEditTo.setText(str(addressAtCurrentRow))
            else:
                self.ui.lineEditTo.setText(str(self.ui.lineEditTo.text()) + "; " + str(addressAtCurrentRow))
        if listOfSelectedRows == {}:
            self.statusBar().showMessage(_translate("MainWindow", "No addresses selected."))
        else:
            self.statusBar().showMessage("")
            self.ui.tabWidget.setCurrentIndex(1)

    def on_action_AddressBookSubscribe(self):
        listOfSelectedRows = {}
        for i in range(len(self.ui.tableWidgetAddressBook.selectedIndexes())):
            listOfSelectedRows[self.ui.tableWidgetAddressBook.selectedIndexes()[i].row()] = 0
        for currentRow in listOfSelectedRows:
            addressAtCurrentRow = str(self.ui.tableWidgetAddressBook.item(currentRow, 1).text())
            # Then subscribe to it. provided it's not already in the address book
            if shared.isAddressInMySubscriptionsList(addressAtCurrentRow):
                self.statusBar().showMessage(
                    QtWidgets.QApplication.translate(
                        "MainWindow",
                        "Error: You cannot add the same address to your subsciptions twice. Perhaps rename the existing one if you want.",
                    )
                )
                continue
            labelAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow, 0).text().toUtf8()
            self.addSubscription(addressAtCurrentRow, labelAtCurrentRow)
            self.ui.tabWidget.setCurrentIndex(4)

    def on_context_menuAddressBook(self, point):
        self.popMenuAddressBook.exec_(self.ui.tableWidgetAddressBook.mapToGlobal(point))

    # Group of functions for the Subscriptions dialog box
    def on_action_SubscriptionsNew(self):
        self.click_pushButtonAddSubscription()

    def on_action_SubscriptionsDelete(self):
        print("clicked Delete")
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 1).text()
        sqlExecute(
            """DELETE FROM subscriptions WHERE label=? AND address=?""",
            str(labelAtCurrentRow),
            str(addressAtCurrentRow),
        )
        self.ui.tableWidgetSubscriptions.removeRow(currentRow)
        self.rerenderInboxFromLabels()
        shared.reloadBroadcastSendersForWhichImWatching()

    def on_action_SubscriptionsClipboard(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 1).text()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    def on_action_SubscriptionsEnable(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 1).text()
        sqlExecute(
            """update subscriptions set enabled=1 WHERE label=? AND address=?""",
            str(labelAtCurrentRow),
            str(addressAtCurrentRow),
        )
        self.ui.tableWidgetSubscriptions.item(currentRow, 0).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetSubscriptions.item(currentRow, 1).setTextColor(QApplication.palette().text().color())
        shared.reloadBroadcastSendersForWhichImWatching()

    def on_action_SubscriptionsDisable(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 1).text()
        sqlExecute(
            """update subscriptions set enabled=0 WHERE label=? AND address=?""",
            str(labelAtCurrentRow),
            str(addressAtCurrentRow),
        )
        self.ui.tableWidgetSubscriptions.item(currentRow, 0).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetSubscriptions.item(currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
        shared.reloadBroadcastSendersForWhichImWatching()

    def on_context_menuSubscriptions(self, point):
        self.popMenuSubscriptions.exec_(self.ui.tableWidgetSubscriptions.mapToGlobal(point))

    # Group of functions for the Blacklist dialog box
    def on_action_BlacklistNew(self):
        self.click_pushButtonAddBlacklist()

    def on_action_BlacklistDelete(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetBlacklist.item(currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(currentRow, 1).text()
        if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
            sqlExecute(
                """DELETE FROM blacklist WHERE label=? AND address=?""",
                str(labelAtCurrentRow),
                str(addressAtCurrentRow),
            )
        else:
            sqlExecute(
                """DELETE FROM whitelist WHERE label=? AND address=?""",
                str(labelAtCurrentRow),
                str(addressAtCurrentRow),
            )
        self.ui.tableWidgetBlacklist.removeRow(currentRow)

    def on_action_BlacklistClipboard(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(currentRow, 1).text()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    def on_context_menuBlacklist(self, point):
        self.popMenuBlacklist.exec_(self.ui.tableWidgetBlacklist.mapToGlobal(point))

    def on_action_BlacklistEnable(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(currentRow, 1).text()
        self.ui.tableWidgetBlacklist.item(currentRow, 0).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetBlacklist.item(currentRow, 1).setTextColor(QApplication.palette().text().color())
        if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
            sqlExecute("""UPDATE blacklist SET enabled=1 WHERE address=?""", str(addressAtCurrentRow))
        else:
            sqlExecute("""UPDATE whitelist SET enabled=1 WHERE address=?""", str(addressAtCurrentRow))

    def on_action_BlacklistDisable(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(currentRow, 1).text()
        self.ui.tableWidgetBlacklist.item(currentRow, 0).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetBlacklist.item(currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
        if shared.config.get("bitmessagesettings", "blackwhitelist") == "black":
            sqlExecute("""UPDATE blacklist SET enabled=0 WHERE address=?""", str(addressAtCurrentRow))
        else:
            sqlExecute("""UPDATE whitelist SET enabled=0 WHERE address=?""", str(addressAtCurrentRow))

    # Group of functions for the Your Identities dialog box
    def on_action_YourIdentitiesNew(self):
        self.click_NewAddressDialog()

    def on_action_YourIdentitiesEnable(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = str(self.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
        shared.config.set(addressAtCurrentRow, "enabled", "true")
        with open(shared.appdata + "keys.dat", "w") as configfile:
            shared.config.write(configfile)
        self.ui.tableWidgetYourIdentities.item(currentRow, 0).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetYourIdentities.item(currentRow, 2).setTextColor(QApplication.palette().text().color())
        if shared.safeConfigGetBoolean(addressAtCurrentRow, "mailinglist"):
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(137, 4, 177))  # magenta
        if shared.safeConfigGetBoolean(addressAtCurrentRow, "chan"):
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(216, 119, 0))  # orange
        shared.reloadMyAddressHashes()

    def on_action_YourIdentitiesDisable(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = str(self.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
        shared.config.set(str(addressAtCurrentRow), "enabled", "false")
        self.ui.tableWidgetYourIdentities.item(currentRow, 0).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetYourIdentities.item(currentRow, 2).setTextColor(QtGui.QColor(128, 128, 128))
        if shared.safeConfigGetBoolean(addressAtCurrentRow, "mailinglist"):
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(137, 4, 177))  # magenta
        with open(shared.appdata + "keys.dat", "w") as configfile:
            shared.config.write(configfile)
        shared.reloadMyAddressHashes()

    def on_action_YourIdentitiesClipboard(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetYourIdentities.item(currentRow, 1).text()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    def on_action_YourIdentitiesSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetYourIdentities)

    def on_action_AddressBookSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetAddressBook)

    def on_action_SubscriptionsSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetSubscriptions)

    def on_action_BlacklistSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetBlacklist)

    def on_action_SetAvatar(self, thisTableWidget):
        # thisTableWidget =  self.ui.tableWidgetYourIdentities
        if not os.path.exists(shared.appdata + "avatars/"):
            os.makedirs(shared.appdata + "avatars/")
        currentRow = thisTableWidget.currentRow()
        addressAtCurrentRow = thisTableWidget.item(currentRow, 1).text()
        hash = hashlib.md5(addBMIfNotPresent(addressAtCurrentRow).encode("utf-8")).hexdigest()
        extensions = [
            "PNG",
            "GIF",
            "JPG",
            "JPEG",
            "SVG",
            "BMP",
            "MNG",
            "PBM",
            "PGM",
            "PPM",
            "TIFF",
            "XBM",
            "XPM",
            "TGA",
        ]
        # http://pyqt.sourceforge.net/Docs/PyQt4/qimagereader.html#supportedImageFormats
        names = {
            "BMP": "Windows Bitmap",
            "GIF": "Graphic Interchange Format",
            "JPG": "Joint Photographic Experts Group",
            "JPEG": "Joint Photographic Experts Group",
            "MNG": "Multiple-image Network Graphics",
            "PNG": "Portable Network Graphics",
            "PBM": "Portable Bitmap",
            "PGM": "Portable Graymap",
            "PPM": "Portable Pixmap",
            "TIFF": "Tagged Image File Format",
            "XBM": "X11 Bitmap",
            "XPM": "X11 Pixmap",
            "SVG": "Scalable Vector Graphics",
            "TGA": "Targa Image Format",
        }
        filters = []
        all_images_filter = []
        current_files = []
        for ext in extensions:
            filters += [names[ext] + " (*." + ext.lower() + ")"]
            all_images_filter += ["*." + ext.lower()]
            upper = shared.appdata + "avatars/" + hash + "." + ext.upper()
            lower = shared.appdata + "avatars/" + hash + "." + ext.lower()
            if os.path.isfile(lower):
                current_files += [lower]
            elif os.path.isfile(upper):
                current_files += [upper]
        filters[0:0] = ["Image files (" + " ".join(all_images_filter) + ")"]
        filters[1:1] = ["All files (*.*)"]
        sourcefile = QFileDialog.getOpenFileName(
            self, _translate("MainWindow", "Set avatar."), filter=";;".join(filters)
        )
        # determine the correct filename (note that avatars don't use the suffix)
        destination = shared.appdata + "avatars/" + hash + "." + sourcefile.split(".")[-1]
        exists = QtCore.QFile.exists(destination)
        if sourcefile == "":
            # ask for removal of avatar
            if exists | (len(current_files) > 0):
                displayMsg = _translate("MainWindow", "Do you really want to remove this avatar?")
                overwrite = QtWidgets.QMessageBox.question(
                    self, "Message", displayMsg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No
                )
            else:
                overwrite = QtWidgets.QMessageBox.No
        else:
            # ask whether to overwrite old avatar
            if exists | (len(current_files) > 0):
                displayMsg = _translate(
                    "MainWindow", "You have already set an avatar for this address. Do you really want to overwrite it?"
                )
                overwrite = QtWidgets.QMessageBox.question(
                    self, "Message", displayMsg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No
                )
            else:
                overwrite = QtWidgets.QMessageBox.No

        # copy the image file to the appdata folder
        if (not exists) | (overwrite == QtWidgets.QMessageBox.Yes):
            if overwrite == QtWidgets.QMessageBox.Yes:
                for file in current_files:
                    QtCore.QFile.remove(file)
                QtCore.QFile.remove(destination)
            # copy it
            if sourcefile != "":
                copied = QtCore.QFile.copy(sourcefile, destination)
                if not copied:
                    print("couldn't copy :(")
                    return False
            # set the icon
            thisTableWidget.item(currentRow, 0).setIcon(avatarize(addressAtCurrentRow))
            self.rerenderSubscriptions()
            self.rerenderComboBoxSendFrom()
            self.rerenderInboxFromLabels()
            self.rerenderInboxToLabels()
            self.rerenderSentFromLabels()
            self.rerenderSentToLabels()

    def on_context_menuYourIdentities(self, point):
        self.popMenu.exec_(self.ui.tableWidgetYourIdentities.mapToGlobal(point))

    def on_context_menuInbox(self, point):
        self.popMenuInbox.exec_(self.ui.tableWidgetInbox.mapToGlobal(point))

    def on_context_menuSent(self, point):
        self.popMenuSent = QtWidgets.QMenu(self)
        self.popMenuSent.addAction(self.actionSentClipboard)
        self.popMenuSent.addAction(self.actionTrashSentMessage)

        # Check to see if this item is toodifficult and display an additional
        # menu option (Force Send) if it is.
        currentRow = self.ui.tableWidgetSent.currentRow()
        ackData = str(self.ui.tableWidgetSent.item(currentRow, 3).data(Qt.UserRole))
        queryreturn = sqlQuery("""SELECT status FROM sent where ackdata=?""", ackData)
        for row in queryreturn:
            (status,) = row
        if status == "toodifficult":
            self.popMenuSent.addAction(self.actionForceSend)
        self.popMenuSent.exec_(self.ui.tableWidgetSent.mapToGlobal(point))

    def inboxSearchLineEditPressed(self):
        searchKeyword = self.ui.inboxSearchLineEdit.text().toUtf8().data()
        searchOption = self.ui.inboxSearchOptionCB.currentText().toUtf8().data()
        self.ui.inboxSearchLineEdit.setText(QString(""))
        self.ui.textEditInboxMessage.setPlainText(QString(""))
        self.loadInbox(searchOption, searchKeyword)

    def sentSearchLineEditPressed(self):
        searchKeyword = self.ui.sentSearchLineEdit.text().toUtf8().data()
        searchOption = self.ui.sentSearchOptionCB.currentText().toUtf8().data()
        self.ui.sentSearchLineEdit.setText(QString(""))
        self.ui.textEditInboxMessage.setPlainText(QString(""))
        self.loadSent(searchOption, searchKeyword)

    def tableWidgetInboxItemClicked(self):
        currentRow = self.ui.tableWidgetInbox.currentRow()
        if currentRow >= 0:
            font = QFont()
            font.setBold(False)
            self.ui.textEditInboxMessage.setCurrentFont(font)

            fromAddress = str(self.ui.tableWidgetInbox.item(currentRow, 1).data(Qt.UserRole))
            msgid = str(self.ui.tableWidgetInbox.item(currentRow, 3).data(Qt.UserRole))
            queryreturn = sqlQuery("""select message from inbox where msgid=?""", msgid)
            if queryreturn != []:
                for row in queryreturn:
                    (messageText,) = row
            messageText = shared.fixPotentiallyInvalidUTF8Data(messageText)
            messageText = str(messageText, "utf-8)")
            if len(messageText) > 30000:
                messageText = (
                    messageText[:30000]
                    + "\n"
                    + "--- Display of the remainder of the message "
                    + "truncated because it is too long.\n"
                    + "--- To see the full message, right-click in the "
                    + 'Inbox view and select "View HTML code as formatted '
                    + 'text",\n'
                    + '--- or select "Save message as." to save it to a '
                    + 'file, or select "Reply" and '
                    + "view the full message in the quote."
                )
            # If we have received this message from either a broadcast address
            # or from someone in our address book, display as HTML
            if decodeAddress(fromAddress)[
                3
            ] in shared.broadcastSendersForWhichImWatching or shared.isAddressInMyAddressBook(fromAddress):
                self.ui.textEditInboxMessage.setText(messageText)
            else:
                self.ui.textEditInboxMessage.setPlainText(messageText)

            self.ui.tableWidgetInbox.item(currentRow, 0).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 1).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 2).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 3).setFont(font)

            inventoryHash = str(self.ui.tableWidgetInbox.item(currentRow, 3).data(Qt.UserRole))
            self.ubuntuMessagingMenuClear(inventoryHash)
            sqlExecute("""update inbox set read=1 WHERE msgid=?""", inventoryHash)
            self.changedInboxUnread()

    def tableWidgetSentItemClicked(self):
        currentRow = self.ui.tableWidgetSent.currentRow()
        if currentRow >= 0:
            ackdata = str(self.ui.tableWidgetSent.item(currentRow, 3).data(Qt.UserRole))
            queryreturn = sqlQuery("""select message from sent where ackdata=?""", ackdata)
            if queryreturn != []:
                for row in queryreturn:
                    (message,) = row
            else:
                message = "Error occurred: could not load message from disk."
            message = str(message, "utf-8)")
            self.ui.textEditSentMessage.setPlainText(message)

    def tableWidgetYourIdentitiesItemChanged(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        if currentRow >= 0:
            addressAtCurrentRow = self.ui.tableWidgetYourIdentities.item(currentRow, 1).text()
            shared.config.set(
                str(addressAtCurrentRow),
                "label",
                str(self.ui.tableWidgetYourIdentities.item(currentRow, 0).text().toUtf8()),
            )
            with open(shared.appdata + "keys.dat", "w") as configfile:
                shared.config.write(configfile)
            self.rerenderComboBoxSendFrom()
            # self.rerenderInboxFromLabels()
            self.rerenderInboxToLabels()
            self.rerenderSentFromLabels()
            # self.rerenderSentToLabels()

    def tableWidgetAddressBookItemChanged(self):
        currentRow = self.ui.tableWidgetAddressBook.currentRow()
        if currentRow >= 0:
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow, 1).text()
            sqlExecute(
                """UPDATE addressbook set label=? WHERE address=?""",
                str(self.ui.tableWidgetAddressBook.item(currentRow, 0).text().toUtf8()),
                str(addressAtCurrentRow),
            )
        self.rerenderInboxFromLabels()
        self.rerenderSentToLabels()

    def tableWidgetSubscriptionsItemChanged(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        if currentRow >= 0:
            addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(currentRow, 1).text()
            sqlExecute(
                """UPDATE subscriptions set label=? WHERE address=?""",
                str(self.ui.tableWidgetSubscriptions.item(currentRow, 0).text().toUtf8()),
                str(addressAtCurrentRow),
            )
        self.rerenderInboxFromLabels()
        self.rerenderSentToLabels()

    def writeNewAddressToTable(self, label, address, streamNumber):
        self.ui.tableWidgetYourIdentities.setSortingEnabled(False)
        self.ui.tableWidgetYourIdentities.insertRow(0)
        newItem = QtWidgets.QTableWidgetItem(label.decode("utf-8", "ignore") if isinstance(label, bytes) else label)
        newItem.setIcon(avatarize(address))
        self.ui.tableWidgetYourIdentities.setItem(0, 0, newItem)
        newItem = QtWidgets.QTableWidgetItem(address)
        newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        if shared.safeConfigGetBoolean(address, "chan"):
            newItem.setTextColor(QtGui.QColor(216, 119, 0))  # orange
        self.ui.tableWidgetYourIdentities.setItem(0, 1, newItem)
        newItem = QtWidgets.QTableWidgetItem(streamNumber)
        newItem.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidgetYourIdentities.setItem(0, 2, newItem)
        # self.ui.tableWidgetYourIdentities.setSortingEnabled(True)
        self.rerenderComboBoxSendFrom()

    def updateStatusBar(self, data):
        if data != "":
            with shared.printLock:
                print("Status bar:", data)

        self.statusBar().showMessage(data)


class helpDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_helpDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.labelHelpURI.setOpenExternalLinks(True)
        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


class connectDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_connectDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


class aboutDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.labelVersion.setText("version " + shared.softwareVersion)


class regenerateAddressesDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_regenerateAddressesDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


class settingsDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_settingsDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.checkBoxStartOnLogon.setChecked(shared.config.getboolean("bitmessagesettings", "startonlogon"))
        self.ui.checkBoxMinimizeToTray.setChecked(shared.config.getboolean("bitmessagesettings", "minimizetotray"))
        self.ui.checkBoxShowTrayNotifications.setChecked(
            shared.config.getboolean("bitmessagesettings", "showtraynotifications")
        )
        self.ui.checkBoxStartInTray.setChecked(shared.config.getboolean("bitmessagesettings", "startintray"))
        self.ui.checkBoxWillinglySendToMobile.setChecked(
            shared.safeConfigGetBoolean("bitmessagesettings", "willinglysendtomobile")
        )
        self.ui.checkBoxUseIdenticons.setChecked(shared.safeConfigGetBoolean("bitmessagesettings", "useidenticons"))
        self.ui.checkBoxReplyBelow.setChecked(shared.safeConfigGetBoolean("bitmessagesettings", "replybelow"))

        global languages
        languages = [
            "system",
            "en",
            "eo",
            "fr",
            "de",
            "es",
            "ru",
            "no",
            "ar",
            "zh_cn",
            "ja",
            "nl",
            "en_pirate",
            "other",
        ]
        user_countrycode = str(shared.config.get("bitmessagesettings", "userlocale"))
        if user_countrycode in languages:
            curr_index = languages.index(user_countrycode)
        else:
            curr_index = languages.index("other")
        self.ui.languageComboBox.setCurrentIndex(curr_index)

        if shared.appdata == "":
            self.ui.checkBoxPortableMode.setChecked(True)
        if "darwin" in sys.platform:
            self.ui.checkBoxStartOnLogon.setDisabled(True)
            self.ui.checkBoxStartOnLogon.setText(
                _translate("MainWindow", "Start-on-login not yet supported on your OS.")
            )
            self.ui.checkBoxMinimizeToTray.setDisabled(True)
            self.ui.checkBoxMinimizeToTray.setText(
                _translate("MainWindow", "Minimize-to-tray not yet supported on your OS.")
            )
            self.ui.checkBoxShowTrayNotifications.setDisabled(True)
            self.ui.checkBoxShowTrayNotifications.setText(
                _translate("MainWindow", "Tray notifications not yet supported on your OS.")
            )
        elif "linux" in sys.platform:
            self.ui.checkBoxStartOnLogon.setDisabled(True)
            self.ui.checkBoxStartOnLogon.setText(
                _translate("MainWindow", "Start-on-login not yet supported on your OS.")
            )
            self.ui.checkBoxMinimizeToTray.setDisabled(True)
            self.ui.checkBoxMinimizeToTray.setText(
                _translate("MainWindow", "Minimize-to-tray not yet supported on your OS.")
            )
        # On the Network settings tab:
        self.ui.lineEditTCPPort.setText(str(shared.config.get("bitmessagesettings", "port")))
        self.ui.checkBoxAuthentication.setChecked(shared.config.getboolean("bitmessagesettings", "socksauthentication"))
        self.ui.checkBoxSocksListen.setChecked(shared.config.getboolean("bitmessagesettings", "sockslisten"))
        if str(shared.config.get("bitmessagesettings", "socksproxytype")) == "none":
            self.ui.comboBoxProxyType.setCurrentIndex(0)
            self.ui.lineEditSocksHostname.setEnabled(False)
            self.ui.lineEditSocksPort.setEnabled(False)
            self.ui.lineEditSocksUsername.setEnabled(False)
            self.ui.lineEditSocksPassword.setEnabled(False)
            self.ui.checkBoxAuthentication.setEnabled(False)
            self.ui.checkBoxSocksListen.setEnabled(False)
        elif str(shared.config.get("bitmessagesettings", "socksproxytype")) == "SOCKS4a":
            self.ui.comboBoxProxyType.setCurrentIndex(1)
            self.ui.lineEditTCPPort.setEnabled(False)
        elif str(shared.config.get("bitmessagesettings", "socksproxytype")) == "SOCKS5":
            self.ui.comboBoxProxyType.setCurrentIndex(2)
            self.ui.lineEditTCPPort.setEnabled(False)

        self.ui.lineEditSocksHostname.setText(str(shared.config.get("bitmessagesettings", "sockshostname")))
        self.ui.lineEditSocksPort.setText(str(shared.config.get("bitmessagesettings", "socksport")))
        self.ui.lineEditSocksUsername.setText(str(shared.config.get("bitmessagesettings", "socksusername")))
        self.ui.lineEditSocksPassword.setText(str(shared.config.get("bitmessagesettings", "sockspassword")))
        self.ui.comboBoxProxyType.currentIndexChanged.connect(self.comboBoxProxyTypeChanged)

        self.ui.lineEditTotalDifficulty.setText(
            str(
                (
                    float(shared.config.getint("bitmessagesettings", "defaultnoncetrialsperbyte"))
                    / shared.networkDefaultProofOfWorkNonceTrialsPerByte
                )
            )
        )
        self.ui.lineEditSmallMessageDifficulty.setText(
            str(
                (
                    float(shared.config.getint("bitmessagesettings", "defaultpayloadlengthextrabytes"))
                    / shared.networkDefaultPayloadLengthExtraBytes
                )
            )
        )

        # Max acceptable difficulty tab
        self.ui.lineEditMaxAcceptableTotalDifficulty.setText(
            str(
                (
                    float(shared.config.getint("bitmessagesettings", "maxacceptablenoncetrialsperbyte"))
                    / shared.networkDefaultProofOfWorkNonceTrialsPerByte
                )
            )
        )
        self.ui.lineEditMaxAcceptableSmallMessageDifficulty.setText(
            str(
                (
                    float(shared.config.getint("bitmessagesettings", "maxacceptablepayloadlengthextrabytes"))
                    / shared.networkDefaultPayloadLengthExtraBytes
                )
            )
        )

        # Namecoin integration tab
        nmctype = shared.config.get("bitmessagesettings", "namecoinrpctype")
        self.ui.lineEditNamecoinHost.setText(str(shared.config.get("bitmessagesettings", "namecoinrpchost")))
        self.ui.lineEditNamecoinPort.setText(str(shared.config.get("bitmessagesettings", "namecoinrpcport")))
        self.ui.lineEditNamecoinUser.setText(str(shared.config.get("bitmessagesettings", "namecoinrpcuser")))
        self.ui.lineEditNamecoinPassword.setText(str(shared.config.get("bitmessagesettings", "namecoinrpcpassword")))

        if nmctype == "namecoind":
            self.ui.radioButtonNamecoinNamecoind.setChecked(True)
        elif nmctype == "nmcontrol":
            self.ui.radioButtonNamecoinNmcontrol.setChecked(True)
            self.ui.lineEditNamecoinUser.setEnabled(False)
            self.ui.labelNamecoinUser.setEnabled(False)
            self.ui.lineEditNamecoinPassword.setEnabled(False)
            self.ui.labelNamecoinPassword.setEnabled(False)
        else:
            assert False

        self.ui.radioButtonNamecoinNamecoind.toggled.connect(self.namecoinTypeChanged)
        self.ui.radioButtonNamecoinNmcontrol.toggled.connect(self.namecoinTypeChanged)
        self.ui.pushButtonNamecoinTest.clicked.connect(self.click_pushButtonNamecoinTest)

        # Message Resend tab
        self.ui.lineEditDays.setText(str(shared.config.get("bitmessagesettings", "stopresendingafterxdays")))
        self.ui.lineEditMonths.setText(str(shared.config.get("bitmessagesettings", "stopresendingafterxmonths")))

        #'System' tab removed for now.
        """try:
            maxCores = shared.config.getint('bitmessagesettings', 'maxcores')
        except:
            maxCores = 99999
        if maxCores <= 1:
            self.ui.comboBoxMaxCores.setCurrentIndex(0)
        elif maxCores == 2:
            self.ui.comboBoxMaxCores.setCurrentIndex(1)
        elif maxCores <= 4:
            self.ui.comboBoxMaxCores.setCurrentIndex(2)
        elif maxCores <= 8:
            self.ui.comboBoxMaxCores.setCurrentIndex(3)
        elif maxCores <= 16:
            self.ui.comboBoxMaxCores.setCurrentIndex(4)
        else:
            self.ui.comboBoxMaxCores.setCurrentIndex(5)"""

        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))

    def comboBoxProxyTypeChanged(self, comboBoxIndex):
        if comboBoxIndex == 0:
            self.ui.lineEditSocksHostname.setEnabled(False)
            self.ui.lineEditSocksPort.setEnabled(False)
            self.ui.lineEditSocksUsername.setEnabled(False)
            self.ui.lineEditSocksPassword.setEnabled(False)
            self.ui.checkBoxAuthentication.setEnabled(False)
            self.ui.checkBoxSocksListen.setEnabled(False)
            self.ui.lineEditTCPPort.setEnabled(True)
        elif comboBoxIndex == 1 or comboBoxIndex == 2:
            self.ui.lineEditSocksHostname.setEnabled(True)
            self.ui.lineEditSocksPort.setEnabled(True)
            self.ui.checkBoxAuthentication.setEnabled(True)
            self.ui.checkBoxSocksListen.setEnabled(True)
            if self.ui.checkBoxAuthentication.isChecked():
                self.ui.lineEditSocksUsername.setEnabled(True)
                self.ui.lineEditSocksPassword.setEnabled(True)
            self.ui.lineEditTCPPort.setEnabled(False)

    # Check status of namecoin integration radio buttons and translate
    # it to a string as in the options.
    def getNamecoinType(self):
        if self.ui.radioButtonNamecoinNamecoind.isChecked():
            return "namecoind"
        if self.ui.radioButtonNamecoinNmcontrol.isChecked():
            return "nmcontrol"
        assert False

    # Namecoin connection type was changed.
    def namecoinTypeChanged(self, checked):
        nmctype = self.getNamecoinType()
        assert nmctype == "namecoind" or nmctype == "nmcontrol"

        isNamecoind = nmctype == "namecoind"
        self.ui.lineEditNamecoinUser.setEnabled(isNamecoind)
        self.ui.labelNamecoinUser.setEnabled(isNamecoind)
        self.ui.lineEditNamecoinPassword.setEnabled(isNamecoind)
        self.ui.labelNamecoinPassword.setEnabled(isNamecoind)

        if isNamecoind:
            self.ui.lineEditNamecoinPort.setText(shared.namecoinDefaultRpcPort)
        else:
            self.ui.lineEditNamecoinPort.setText("9000")

    # Test the namecoin settings specified in the settings dialog.
    def click_pushButtonNamecoinTest(self):
        self.ui.labelNamecoinTestResult.setText(_translate("MainWindow", "Testing."))
        options = {}
        options["type"] = self.getNamecoinType()
        options["host"] = self.ui.lineEditNamecoinHost.text()
        options["port"] = self.ui.lineEditNamecoinPort.text()
        options["user"] = self.ui.lineEditNamecoinUser.text()
        options["password"] = self.ui.lineEditNamecoinPassword.text()
        nc = namecoinConnection(options)
        response = nc.test()
        responseStatus = response[0]
        responseText = response[1]
        self.ui.labelNamecoinTestResult.setText(responseText)
        if responseStatus == "success":
            self.parent.ui.pushButtonFetchNamecoinID.show()


class SpecialAddressBehaviorDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SpecialAddressBehaviorDialog()
        self.ui.setupUi(self)
        self.parent = parent
        currentRow = parent.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = str(parent.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
        if not shared.safeConfigGetBoolean(addressAtCurrentRow, "chan"):
            if shared.safeConfigGetBoolean(addressAtCurrentRow, "mailinglist"):
                self.ui.radioButtonBehaviorMailingList.click()
            else:
                self.ui.radioButtonBehaveNormalAddress.click()
            try:
                mailingListName = shared.config.get(addressAtCurrentRow, "mailinglistname")
            except:
                mailingListName = ""
            self.ui.lineEditMailingListName.setText(
                mailingListName.decode("utf-8", "ignore") if isinstance(mailingListName, bytes) else mailingListName
            )
        else:  # if addressAtCurrentRow is a chan address
            self.ui.radioButtonBehaviorMailingList.setDisabled(True)
            self.ui.lineEditMailingListName.setText(
                _translate("MainWindow", "This is a chan address. You cannot use it as a pseudo-mailing list.")
            )

        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


class AddAddressDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_AddAddressDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.lineEditAddress.textChanged.connect(self.addressChanged)

    def addressChanged(self, QString):
        status, a, b, c = decodeAddress(str(QString))
        if status == "missingbm":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "The address should start with ''BM-''"))
        elif status == "checksumfailed":
            self.ui.labelAddressCheck.setText(
                _translate("MainWindow", "The address is not typed or copied correctly (the checksum failed).")
            )
        elif status == "versiontoohigh":
            self.ui.labelAddressCheck.setText(
                _translate(
                    "MainWindow",
                    "The version number of this address is higher than this software can support. Please upgrade Bitmessage.",
                )
            )
        elif status == "invalidcharacters":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "The address contains invalid characters."))
        elif status == "ripetooshort":
            self.ui.labelAddressCheck.setText(
                _translate("MainWindow", "Some data encoded in the address is too short.")
            )
        elif status == "ripetoolong":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "Some data encoded in the address is too long."))
        elif status == "success":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "Address is valid."))


class NewSubscriptionDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_NewSubscriptionDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.lineEditSubscriptionAddress.textChanged.connect(self.addressChanged)
        self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(_translate("MainWindow", "Enter an address above."))

    def addressChanged(self, QString):
        self.ui.checkBoxDisplayMessagesAlreadyInInventory.setEnabled(False)
        self.ui.checkBoxDisplayMessagesAlreadyInInventory.setChecked(False)
        status, addressVersion, streamNumber, ripe = decodeAddress(str(QString))
        if status == "missingbm":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "The address should start with ''BM-''"))
        elif status == "checksumfailed":
            self.ui.labelAddressCheck.setText(
                _translate("MainWindow", "The address is not typed or copied correctly (the checksum failed).")
            )
        elif status == "versiontoohigh":
            self.ui.labelAddressCheck.setText(
                _translate(
                    "MainWindow",
                    "The version number of this address is higher than this software can support. Please upgrade Bitmessage.",
                )
            )
        elif status == "invalidcharacters":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "The address contains invalid characters."))
        elif status == "ripetooshort":
            self.ui.labelAddressCheck.setText(
                _translate("MainWindow", "Some data encoded in the address is too short.")
            )
        elif status == "ripetoolong":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "Some data encoded in the address is too long."))
        elif status == "success":
            self.ui.labelAddressCheck.setText(_translate("MainWindow", "Address is valid."))
            if addressVersion <= 3:
                self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
                    _translate("MainWindow", "Address is an old type. We cannot display its past broadcasts.")
                )
            else:
                shared.flushInventory()
                doubleHashOfAddressData = hashlib.sha512(
                    hashlib.sha512(encodeVarint(addressVersion) + encodeVarint(streamNumber) + ripe).digest()
                ).digest()
                tag = doubleHashOfAddressData[32:]
                queryreturn = sqlQuery("""select hash from inventory where objecttype='broadcast' and tag=?""", tag)
                if len(queryreturn) == 0:
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
                        _translate("MainWindow", "There are no recent broadcasts from this address to display.")
                    )
                elif len(queryreturn) == 1:
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setEnabled(True)
                    self.ui.tableWidgetSubscriptions.item(currentRow, 1).setToolTip(
                        _translate("MainWindow", "Display the %1 recent broadcast from this address.").replace(
                            "%1", str(len(queryreturn))
                        )
                    )
                else:
                    self.ui.tableWidgetSubscriptions.item(currentRow, 1).setToolTip(
                        _translate("MainWindow", "Display the %1 recent broadcasts from this address.").replace(
                            "%1", str(len(queryreturn))
                        )
                    )


class NewAddressDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_NewAddressDialog()
        self.ui.setupUi(self)
        self.parent = parent
        row = 1
        # Let's fill out the 'existing address' combo box with addresses from
        # the 'Your Identities' tab.
        while self.parent.ui.tableWidgetYourIdentities.item(row - 1, 1):
            self.ui.radioButtonExisting.click()
            # print
            # self.parent.ui.tableWidgetYourIdentities.item(row-1,1).text()
            self.ui.comboBoxExisting.addItem(self.parent.ui.tableWidgetYourIdentities.item(row - 1, 1).text())
            row += 1
        self.ui.groupBoxDeterministic.setHidden(True)
        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


class newChanDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_newChanDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.groupBoxCreateChan.setHidden(True)
        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


class iconGlossaryDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_iconGlossaryDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.labelTCPPort.setText(
            _translate("MainWindow", "You are using TCP port %1. (This can be changed in the settings).").replace(
                "%1", str(shared.config.getint("bitmessagesettings", "port"))
            )
        )
        QtWidgets.QWidget.resize(self, QtWidgets.QWidget.sizeHint(self))


# In order for the time columns on the Inbox and Sent tabs to be sorted
# correctly (rather than alphabetically), we need to overload the <
# operator and use this class instead of QTableWidgetItem.
class myTableWidgetItem(QtWidgets.QTableWidgetItem):

    def __lt__(self, other):
        return int(self.data(33)) < int(other.data(33))


from PyQt6.QtCore import QThread, pyqtSignal


class UISignaler(QThread):
    writeNewAddressToTable = pyqtSignal(object, object, object)
    updateStatusBar = pyqtSignal(object)
    updateSentItemStatusByHash = pyqtSignal(object, object)
    updateSentItemStatusByAckdata = pyqtSignal(object, object)
    displayNewInboxMessage = pyqtSignal(object, object, object, object, object)
    displayNewSentMessage = pyqtSignal(object, object, object, object, object, object)
    updateNetworkStatusTab = pyqtSignal()
    updateNumberOfMessagesProcessed = pyqtSignal()
    updateNumberOfPubkeysProcessed = pyqtSignal()
    updateNumberOfBroadcastsProcessed = pyqtSignal()
    setStatusIcon = pyqtSignal(object)
    changedInboxUnread = pyqtSignal(object)
    rerenderInboxFromLabels = pyqtSignal()
    rerenderSentToLabels = pyqtSignal()
    rerenderAddressBook = pyqtSignal()
    rerenderSubscriptions = pyqtSignal()
    removeInboxRowByMsgid = pyqtSignal(object)
    displayAlert = pyqtSignal(object, object, object)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        while True:
            command, data = shared.UISignalQueue.get()
            if command == "writeNewAddressToTable":
                label, address, streamNumber = data
                self.writeNewAddressToTable.emit(label, address, str(streamNumber))
            elif command == "updateStatusBar":
                self.updateStatusBar.emit(data)
            elif command == "updateSentItemStatusByHash":
                hash, message = data
                self.updateSentItemStatusByHash.emit(hash, message)
            elif command == "updateSentItemStatusByAckdata":
                ackData, message = data
                self.updateSentItemStatusByAckdata.emit(ackData, message)
            elif command == "displayNewInboxMessage":
                inventoryHash, toAddress, fromAddress, subject, body = data
                self.displayNewInboxMessage.emit(inventoryHash, toAddress, fromAddress, subject, body)
            elif command == "displayNewSentMessage":
                toAddress, fromLabel, fromAddress, subject, message, ackdata = data
                self.displayNewSentMessage.emit(toAddress, fromLabel, fromAddress, subject, message, ackdata)
            elif command == "updateNetworkStatusTab":
                self.updateNetworkStatusTab.emit()
            elif command == "updateNumberOfMessagesProcessed":
                self.updateNumberOfMessagesProcessed.emit()
            elif command == "updateNumberOfPubkeysProcessed":
                self.updateNumberOfPubkeysProcessed.emit()
            elif command == "updateNumberOfBroadcastsProcessed":
                self.updateNumberOfBroadcastsProcessed.emit()
            elif command == "setStatusIcon":
                self.setStatusIcon.emit(data)
            elif command == "changedInboxUnread":
                self.changedInboxUnread.emit(data)
            elif command == "rerenderInboxFromLabels":
                self.rerenderInboxFromLabels.emit()
            elif command == "rerenderSentToLabels":
                self.rerenderSentToLabels.emit()
            elif command == "rerenderAddressBook":
                self.rerenderAddressBook.emit()
            elif command == "rerenderSubscriptions":
                self.rerenderSubscriptions.emit()
            elif command == "removeInboxRowByMsgid":
                self.removeInboxRowByMsgid.emit(data)
            elif command == "alert":
                title, text, exitAfterUserClicksOk = data
                self.displayAlert.emit(title, text, exitAfterUserClicksOk)
            else:
                sys.stderr.write("Command sent to UISignaler not recognized: %s\n" % command)


def run():
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()

    translationpath = os.path.join(
        getattr(sys, "_MEIPASS", ""), "translations", "bitmessage_" + l10n.getTranslationLanguage()
    )
    translator.load(translationpath)

    QtWidgets.QApplication.installTranslator(translator)
    app.setStyleSheet("QStatusBar::item { border: 0px solid black }")
    myapp = MyForm()

    if not shared.config.getboolean("bitmessagesettings", "startintray"):
        myapp.show()

    myapp.appIndicatorInit(app)
    myapp.ubuntuMessagingMenuInit()
    myapp.notifierInit()
    if shared.safeConfigGetBoolean("bitmessagesettings", "dontconnect"):
        myapp.showConnectDialog()  # ask the user if we may connect
    sys.exit(app.exec())
