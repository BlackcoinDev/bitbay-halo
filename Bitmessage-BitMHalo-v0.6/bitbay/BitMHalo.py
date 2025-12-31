
import sys
sys.frozen = False
import os
import re
from logging import Logger

app_dir = os.path.dirname(os.path.abspath(__file__))+'/src'
sys.path.insert(0, app_dir)

import depends
depends.check_dependencies()

from api import MySimpleXMLRPCRequestHandler, StoppableXMLRPCServer
from helper_startup import isOurOperatingSystemLimitedToHavingVeryFewHalfOpenConnections

import class_api as class_api
#import parallelTestModule as parallelTestModule
import time
import ast
import platform
import appdirs
import errno
import traceback
import xmlrpclib
import password
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import logging

import BitMHalo_email as email_support
from BitMHalo_shared import shared

email_password = ''

readmessages = []
prevaccount = ""
typ = ""
msg_data = ""
connection = ""

#print txhash(open("blackhalo2.py", 'rb').read())
#########################################

from PyQt6.QtCore import QThread
from PyQt6.QtCore import QCoreApplication
import threading

logger = logging.getLogger('both')  # type: Logger

os.environ['no_proxy'] = '127.0.0.1,localhost'


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class RPCThread(QThread):  # threading.Thread
    def __init__(self, url):
        QThread.__init__(self)  # super(RPCThread, self).__init__()
        self.url = url

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'div').
    class MyFuncs:
        def ExitBitmessage(self, passw):
            logger.warning(str("bitmhalo: Closing Bitmessage."))
            #Bitmessage doesn't do clean exit, so do a safe BitMHalo exit instead.
            shared.systemexit = 1
            return True

        def StorePassword(self, password1, passw):
            # To prevent sending mail loss, we only use this for retreiving mail
            shared.mypassword = password1
            return True

        def FileLock(self, islocked):
            if islocked == "0":  # Checking
                if shared.lockTHIS == 1:
                    return False
                else:
                    return True
            if islocked == "1":
                shared.lockTHIS = 2
                return True
            else:
                shared.lockTHIS = 0
                return True

    def run(self):
        # Create server
        server = SimpleXMLRPCServer(
            ("localhost", 8878), requestHandler=RequestHandler, logRequests=False)
        server.register_introspection_functions()
        # Register functions
        server.register_instance(self.MyFuncs())
        # Run the server's main loop
        return server.serve_forever()


bitmrpc = RPCThread("RPC")
bitmrpc.start()

def waitlock():
    count = 0
    while count < 300 and shared.lockTHIS == 2:
        time.sleep(.1)
        count += 1
    shared.lockTHIS = 0


def getPythonFileLocation():
    """  returns the location of where the python file is located """
    if os.path.dirname(__file__) != "":
        return os.path.dirname(__file__)
    elif os.path.dirname(os.path.abspath(__file__)) != "":
        return os.path.dirname(os.path.abspath(__file__))
    elif os.path.dirname(os.getcwd()) != "":
        return os.path.dirname(os.getcwd())
    else:
        from inspect import getsourcefile
        return os.path.dirname(os.path.abspath(getsourcefile(lambda _: None)))


application_path = getPythonFileLocation()


def cmd_remove_channel(str_data):
    # Make a new channel address and return it
    data = ast.literal_eval(str_data)
    try:
        waitlock()
        shared.lockTHIS = 1
        with open(shared.bittmp_path, 'w') as f:
            try:
                addr = shared.bm_api.deleteChannel(data['Address'])
                if addr:
                    addr = "Success"
                else:
                    addr = "Failed"
            except:
                traceback.print_exc()
                addr = "Exception"
            f.write("1" + "\n")
            f.write("remchan" + "\n")
            f.write(addr + "\n")
            f.write(data['Address'] + "\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()
        shared.lockTHIS = 0
    except:
        shared.lockTHIS = 0
        logger.error("bitmhalo: remove channel: %s" % traceback.format_exc())


def cmd_add_channel(str_data):
    # Make a new channel address and return it
    data = ast.literal_eval(str_data)
    try:
        waitlock()
        shared.lockTHIS = 1
        with open(shared.bittmp_path, 'w') as f:
            try:
                addr = shared.bm_api.joinChannel(data['Address'])
            except:
                try:
                    addrdata = shared.bm_api.listAddressBook()
                    for add in addrdata:
                        if add['label'] == "[chan] " + data['Address']:
                            addr = add['address']
                            break
                except:
                    addr = "Exception"
            f.write("1" + "\n")
            f.write("chan1" + "\n")
            f.write(addr + "\n")
            f.write(data['Address'] + "\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()
        shared.lockTHIS = 0
    except:
        shared.lockTHIS = 0
        logger.error("bitmhalo: add channel: %s" % traceback.format_exc())


def cmd_new_address(str_data):
    # Make a new address and return it
    data = ast.literal_eval(str_data)
    try:
        waitlock()
        shared.lockTHIS = 1
        with open(shared.bittmp_path, 'w') as f:
            if data["Pubs"] == []:
                addr = shared.bm_api.createRandomAddress("BitHalo")
            else:
                key = str(data['Pubs'][0])
                key2 = str(data['Pubs'][1])
                addr = shared.bm_api.createDeterministicAddresses(
                    str(key[:14] + key2[-14:]), "BitHalo")
                try:
                    addr = addr[0]
                except:
                    try:
                        addr = shared.bm_api.getDeterministicAddress(
                            str(key[:14] + key2[-14:]))
                    except:
                        addr = " "
                addr2 = shared.bm_api.createDeterministicAddresses(
                    str(key2[:14] + key[-14:]), "BitHalo")
                logger.warning("addr: " + str(addr))
            f.write("1" + "\n")
            f.write("new1" + "\n")
            f.write(addr + "\n")
            f.write(data["multisig"] + "\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()
        shared.lockTHIS = 0
    except:
        shared.lockTHIS = 0
        logger.error("bitmhalo: new address: %s" % traceback.format_exc())


def cmd_send(str_data, data3):
    original = str_data
    is_email, from_address = email_support.is_email(str_data)
    verified, imap_name, smtp_name, port, is_ssl = email_support.is_email_provider_supported(
        from_address)
    ret = True
    if is_email and verified:
        from_address, to_address, content, email_password = email_support.exctract_email_data(
            str_data)
        ret = email_support.send_email(
            email_password, content, from_address, to_address, smtp_name, port)
        # It failed lets write it to an outbox.
        # We could also try repeating until solved.
        # Reporting an email fail via api.
        if ret == False:
            outbox = []
            try:
                with open(shared.outbox_path, 'r') as f:
                    outbox = f.readline().strip()
                    outbox = ast.literal_eval(outbox)
                    f.close()
            except Exception, e:
                pass
            try:
                if str(original) not in outbox:
                    outbox.append(str(original))
                with open(shared.outbox_path, 'w') as f:
                    f.write(str(outbox))
                    f.flush()
                    os.fsync(f.fileno())
                    f.close()
            except:
                logger.error("bitmhalo: file: %s, %s" %
                             (shared.outbox_path, traceback.format_exc()))
            ret = "False" + str(str_data)
    else:
        if "ENCRYPTED:" in str_data:
            try:
                match_obj = re.match(r'(MY:)(.*?)(THEIR:)(.*?)(ENCRYPTED:)(.*?)(###)', str_data, re.M | re.I)
                content = match_obj.group(5) + match_obj.group(6)
                from_address = match_obj.group(2)
                to_address = match_obj.group(4)
            except:
                logger.error("bitmhalo: encryption: %s" % traceback.format_exc())
        else:
            try:
                content = ast.literal_eval(str_data)
                from_address = content['MyBMAddress']
                to_address = content['TheirBMAddress']
            except:
                logger.error("bitmhalo: parse: %s" % traceback.format_exc())
                to_address = ""
                content = "####"

        logger.info("bitmhalo: about to send: %s" % str(content))
        try:
            ret = shared.bm_api.sendMessage(from_address, to_address,
                                  "BitHalo", str(content))
            logger.info("bitmhalo: send return info: %s" % str(ret))
        except Exception, e:
            logger.error("bitmhalo: bm send: %s, %s" %
                         (str(e), traceback.format_exc()))
            ret = "False" + str(content)
    try:
        waitlock()
        shared.lockTHIS = 1
        with open(shared.bittmp_path, 'w') as f:
            f.write("1" + "\n")
            f.write("Send1" + "\n")
            f.write(str(ret) + "\n")
            f.write(str(data3) + "\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()
        shared.lockTHIS = 0
    except:
        shared.lockTHIS = 0
        logger.error("bitmhalo: file: %s, %s" % (shared.bittmp_path, traceback.format_exc()))


def cmd_clean_inbox(cmd, str_data):
    data = ast.literal_eval(str_data)

    try:
        inbox_messages = shared.bm_api.getAllInboxMessages()
    except Exception, e:
        logger.error("bitmhalo: getAllInboxMessages: %s %s" %
                     (str(e), traceback.format_exc()))
        inbox_messages = []

    try:
        msgids = shared.bm_api.getAllInboxMessageIDs()
        data['Address'] = data['Bitmessage Address']
        sent_messages = shared.bm_api.getSentMessagesBySender(data['Address'])

        # Clear Sent symbolizes we have no open contracts to worry about message loss
        if 'Clear Sent' in data:
            for msg_id in shared.bm_api.getAllSentMessageIDs():
                message = shared.bm_api.getSentMessageByID(msg_id)
                if message[0]['fromAddress'] == data['Bitmessage Address']:
                    if 'msgsent' in message[0]['status'] or 'ackreceived' in message[0]['status']:
                        shared.bm_api.trashSentMessage(msg_id)

        for msg_id in msgids:
            message = shared.bm_api.getInboxMessageByID(msg_id)
            if message[0]['toAddress'] == data['Bitmessage Address'] and 'Clear Sent' in data:
                shared.bm_api.trashInboxMessage(msg_id)
            if message[0]['toAddress'] in data['MyMarkets']:
                # Market orders are more expendable
                shared.bm_api.trashInboxMessage(msg_id)
    except:
        sent_messages = "False"
        logger.error("bitmhalo: inbox: %s" % traceback.format_exc())

    try:
        status = shared.bm_api.clientStatus()
    except:
        logger.error("bitmhalo: status: %s" % traceback.format_exc())
        status = ""

    try:
        waitlock()
        shared.lockTHIS = 1
        with open(shared.bittmp_path, 'w') as f:
            f.write("1" + "\n")
            f.write(cmd + "1:" + str(status) + "\n")
            f.write(str(inbox_messages) + "\n")
            f.write(str(sent_messages) + "\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()
        shared.lockTHIS = 0
    except Exception, e:
        shared.lockTHIS = 0
        logger.error("bitmhalo: open: %s, %s" % (shared.bittmp_path, traceback.format_exc()))


def get_datadir_path():
    path1 = sys.argv[0]
    application_path = path1
    application_path = application_path.replace("python ", "")
    application_path = application_path.replace("python2.7 ", "")
    application_path = application_path.replace("BitMHalo.py", "")
    application_path = application_path.replace("BitMHalo.exe", "")
    application_path = application_path.replace("BitMHalo", "")
    if os.name != "nt":
        if application_path == "":
            application_path += "./"
        application_path = application_path.replace("//", "/")
    logger.warning("BITMHALO PATH: "+application_path)
    datadir_path = application_path
    if platform.system() == "Darwin":
        datadir_path = appdirs.user_data_dir("BitBayClient", "BitBay")
        try:
            os.makedirs(datadir_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(datadir_path):
                pass
            else:
                raise
    for arg in sys.argv:
        if "path=" in arg:
            datadir_path = arg
            if os.name == 'nt':
                datadir_path = datadir_path + "\\"
            else:
                datadir_path = datadir_path + "/"
            datadir_path = datadir_path.replace("path=", "")
            break

    return datadir_path

def init():
    datadir_path = get_datadir_path()
    os.environ['no_proxy'] = '127.0.0.1,localhost'
    os.environ["BITMESSAGE_HOME"] = datadir_path
    logger.warning("BITMESSAGE_HOME: "+datadir_path)
    shared.bittmp_path = os.path.join(datadir_path, "BitTMP.dat")
    shared.outbox_path = os.path.join(datadir_path, "Outbox.dat")
    shared.mailcache_path = os.path.join(datadir_path, "MailCache.dat")

    with open(shared.outbox_path, 'a+') as f:
        f.close()

    if os.stat(shared.outbox_path)[6] == 0:
        with open(shared.outbox_path, 'w') as f:
            f.write("[]")
            f.flush()
            os.fsync(f.fileno())
            f.close()

    with open(shared.mailcache_path, 'a+') as f:
        f.close()

    if os.stat(shared.mailcache_path)[6] == 0:
        with open(shared.mailcache_path, 'w') as f:
            f.write("{}")
            f.flush()
            os.fsync(f.fileno())
            f.close()

    shared.bm_api = class_api.getAPI(workingdir=datadir_path, silent=False)
    shared.myrpc = xmlrpclib.ServerProxy('http://127.0.0.1:8877')

class BMHaloApp(QCoreApplication):

    def __init__(self, *argv):
        super(BMHaloApp, self).__init__(*argv)
        self.str_data_st = "0"
        self.str_data_cmd = "0"
        self.str_data_arg1 = "0"
        self.str_data_arg2 = "0"
        self.readInputTimerId = self.startTimer(234)
        self.doCommandsTimerId = self.startTimer(468)
        self.doMessagesTimerId = self.startTimer(5148)
        self.resendEmailsTimerId = self.startTimer(234000)
        self.refreshMessagesTimerId = self.startTimer(234000)

    def timerEvent(self, te):
        try:
            if shared.lockTHIS >0:
                return
            if te.timerId()==self.resendEmailsTimerId:
                email_support.resend_pending_in_outbox(shared.outbox_path)
            elif te.timerId() == self.refreshMessagesTimerId:
                global readmessages
                readmessages = []
            elif te.timerId() == self.readInputTimerId:
                self.read_input()
            elif te.timerId() == self.doCommandsTimerId:
                self.do_cmds()
            elif te.timerId() == self.doMessagesTimerId:
                self.do_get_messages()
        except Exception, e:
            logger.error("bitmhalo: timerEvent: %s %s" %
                         (str(e), traceback.format_exc()))

    def read_input(self):
        try:
            with open(shared.bittmp_path, 'r') as f:
                self.str_data_st = f.readline().strip()
                self.str_data_cmd = f.readline().strip()
                try:
                    self.str_data_arg1 = f.readline().strip()
                except:
                    logger.error("bitmhalo: file: %s %s" %
                                 (shared.bittmp_path, traceback.format_exc()))
                try:
                    self.str_data_arg2 = f.readline().strip()
                except:
                    pass
                f.close()
        except Exception, e:
            logger.error("bitmhalo: read_input: %s %s %s" %
                         (str(e), shared.bittmp_path, traceback.format_exc()))
            #logger.error("bitmhalo: SLEEP!!!")
            #time.sleep(360000)

    def do_cmds(self):
        if self.str_data_st != "0":
            # not ready for input commands
            return
        if shared.systemexit == 1:
            shared.systemexit = 2
            logger.warning("bitmhalo: closing bitmessage.")
            self.quit()
            return
        if shared.systemexit == 2:
            return
        try:
            cmd = self.str_data_cmd
            logger.debug("do1: %s, %s, %s" % (str(cmd), str(self.str_data_arg1), str(self.str_data_arg2)))
            if cmd == "Send":
                cmd_send(self.str_data_arg1, self.str_data_arg2)
            if cmd == "Clean Inbox":
                cmd_clean_inbox(cmd, self.str_data_arg1)
            if cmd == "new":
                cmd_new_address(self.str_data_arg1)
            if cmd == "Add Channel":
                cmd_add_channel(self.str_data_arg1)
            if cmd == "Remove Channel":
                cmd_remove_channel(self.str_data_arg1)
            if cmd == "exit":
                shared.systemexit = 2
                logger.warning("bitmhalo: closing bitmessage.")
                self.quit()
        except Exception, e:
            logger.error("bitmhalo: checking/thread: %s %s" %
                         (str(e), traceback.format_exc()))

    def do_get_messages(self):
        if self.str_data_st != "0":
            # not ready for input commands
            return
        if shared.systemexit == 1:
            shared.systemexit = 2
            logger.warning(str("bitmhalo: closing bitmessage."))
            self.quit()
            return
        if shared.systemexit == 2:
            return
        try:
            cmd = self.str_data_cmd
            logger.debug("do2: %s, %s, %s" % (str(cmd), str(self.str_data_arg1), str(self.str_data_arg2)))
            if cmd == "GetMessages" or cmd == "Remove Order":
                logger.info("bitmhalo: checking Inbox.")
                inbox = []
                ret = ""
                try:
                    dat = ast.literal_eval(self.str_data_arg1)
                    if 'Password' in dat:
                        if dat['Password'] == "#!#":
                            dat['Password'] = shared.mypassword
                        try:
                            dat['Password'] = password.DecryptWithAES(
                                "Halo Master", dat['Password'])
                        except:
                            logger.error(
                                "bitmhalo: password aes decrypt: %s" % traceback.format_exc())
                        verified, imap_name, smtp_name, port, is_ssl = email_support.is_email_provider_supported(
                            dat['Email Address'])
                        if verified:
                            global prevaccount, readmessages
                            if dat['Email Address'] != prevaccount or cmd == "Remove Order":
                                # reset on new accounts or maintenance
                                # For now we maintain the record of read messages on the client side
                                readmessages = []

                            ret, readmessages, mailbox = email_support.read_inbox_messages(
                                dat, readmessages, shared.mailcache_path, imap_name, shared.myrpc)
                            prevaccount = dat['Email Address']

                            try:
                                waitlock()
                                shared.lockTHIS = 1
                                with open(shared.mailcache_path, 'w') as f:
                                    f.write(str(mailbox))
                                    f.flush()
                                    os.fsync(f.fileno())
                                    f.close()
                                shared.lockTHIS = 0
                            except:
                                shared.lockTHIS = 0
                                logger.error("bitmhalo: cache: %s, %s" % (
                                    shared.mailcache_path, traceback.format_exc()))

                except Exception, e:
                    logger.error("bitmhalo: inbox: %s" %
                                 traceback.format_exc())

                inbox_messages = shared.bm_api.getAllInboxMessages()

                try:
                    sentmessages = shared.bm_api.getSentMessagesBySender(
                        dat['Address'])
                except:
                    sentmessages = "False"

                for inmessage in inbox:
                    inbox_messages.append(inmessage)

                try:
                    status = shared.bm_api.clientStatus()
                except:
                    logger.error("bitmhalo: status: %s" %
                                 traceback.format_exc())
                    status = ""

                logger.info(str("bitmhalo: inbox checked"))
                try:
                    waitlock()
                    shared.lockTHIS = 1
                    with open(shared.bittmp_path, 'w') as f:
                        f.write("1" + "\n")
                        if cmd == "GetMessages":
                            if ret == False:
                                f.write(cmd + "1:False:" + str(status) + "\n")
                            else:
                                f.write(cmd + "1:" + str(status) + "\n")
                            f.write(str(inbox_messages) + "\n")
                            f.write(str(sentmessages) + "\n")
                        if cmd == "Remove Order":
                            f.write("RemoveOrder1\n")
                            f.write("True\n")
                            f.write("True\n")
                        f.flush()
                        os.fsync(f.fileno())
                        f.close()
                    shared.lockTHIS = 0
                except Exception, e:
                    shared.lockTHIS = 0
                    logger.error("bitmhalo: open: %s, %s" %
                                 (shared.bittmp_path, traceback.format_exc()))
                    pass
            if cmd == "exit":
                shared.systemexit = 2
                self.quit()
        except Exception, e:
            logger.error("bitmhalo: checking/thread: %s %s" %
                         (str(e), traceback.format_exc()))

def main():
    init()
    app = BMHaloApp(sys.argv)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
