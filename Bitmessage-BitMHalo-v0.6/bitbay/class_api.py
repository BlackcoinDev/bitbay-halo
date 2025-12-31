import os
import sys
import time
import threading
import logging
import socket

app_dir = os.path.dirname(os.path.abspath(__file__))+'/./src'
sys.path.insert(0, app_dir)

from pyelliptic import openssl

import addresses
import helper_sent
import helper_inbox
import defaults
import queues
import network.stats
from bmconfigparser import BMConfigParser
from helper_ackPayload import genAckPayload

###############
import parallelTestModule

if __name__ == '__main__':
    extractor = parallelTestModule.ParallelExtractor()
    extractor.runInParallel(numProcesses=1, numThreads=4)
###############

SUPPORTED_VERSIONS = ['0.4.1', '0.6.3.2']

logger = logging.getLogger('console')

# A hack to let pybitmessage source directory exist as Subdir for testing
if os.path.exists(os.path.abspath('PyBitmessage')):
    sys.path.append(os.path.abspath('PyBitmessage/src'))


class APIError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "API Error: %s" % self.error_message


def getAPI(workingdir=None, silent=False):

    if workingdir:
        os.environ["BITMESSAGE_HOME"] = workingdir

    # Workaround while logging is not completed
    if silent:
        import StringIO
        fobj = StringIO.StringIO()
        sys.stdout = fobj

    import bitmessagemain
    from version import softwareVersion

    version = softwareVersion
    if not version in SUPPORTED_VERSIONS:
        sys.stderr.write(
            'Bitmessage Vesion %s is not Supported officially.\n' % version)

    global ADDRESSVERSION
    ADDRESSVERSION = 4

    class MainAPI(bitmessagemain.Main):
        def _close_and_wait(self):
            """For Testing purposes only"""

            self.stop()
            while 1:
                import time
                time.sleep(2)
                print self._count_threads()
                bitmessagemain.shared.shutdown = 1

        def _count_threads(self):
            """This function counts running Threads"""

            thcount = 0
            threads = threading.enumerate()
            for th in threads:
                if th.is_alive():
                    print th
                    thcount += 1
            return thcount

        def clientStatus(self):
            '''Returns the Status of the Bitmessage Daemon
            Usage: status = api.clinetStatus()
            print status['externalIPAddress']
            print status['networkConnections']
            print status['numberOfMessagesProcessed']
            print status['numberOfBroadcastsProcessed']
            print status['numberOfPubkeysProcessed']
            print status['networkStatus']
            '''

            if len(network.stats.connectedHostsList()) == 0:
                networkStatus = 'notConnected'
            elif len(network.stats.connectedHostsList()) > 0 and not bitmessagemain.shared.clientHasReceivedIncomingConnections:
                networkStatus = 'connectedButHaveNotReceivedIncomingConnections'
            else:
                networkStatus = 'connectedAndReceivingIncomingConnections'
            info = {}
            try:
                info['externalIPAddress'] = socket.inet_ntoa(data[40:44])
            except:
                info['externalIPAddress'] = 'Not implemented jet'
            info['networkConnections'] = len(
                network.stats.connectedHostsList())
            info['numberOfMessagesProcessed'] = bitmessagemain.shared.numberOfMessagesProcessed
            info['numberOfBroadcastsProcessed'] = bitmessagemain.shared.numberOfBroadcastsProcessed
            info['numberOfPubkeysProcessed'] = bitmessagemain.shared.numberOfPubkeysProcessed
            info['networkStatus'] = networkStatus
            logger.debug('Status: %s' % info)
            return info

        def createDeterministicAddresses(self, passphrase, label='', numberOfAddresses=1, eighteenByteRipe=False, totalDifficulty=1, smallMessageDifficulty=1, streamNumberForAddress=1):
            '''Creates a Deterministic Bitmessage Address (an Address based on a password)
            Usage: api.createDeterministicAddresses(passphrase,label,numberOfAddresses,eighteenByteRipe,totalDifficulty,smallMessageDifficulty)'''

            logger.debug('Passphrase: %s Label: %s' % (passphrase, label))
            if len(passphrase) == 0:
                raise APIError('The specified passphrase is blank.')

            if not isinstance(eighteenByteRipe, bool):
                raise APIError(
                    'Bool expected in eighteenByteRipe, got %s instead' % type(eighteenByteRipe))

            if streamNumberForAddress != 1:
                raise APIError(
                    'Only Stream Number 1 is Supported jet. Got: %s' % streamNumberForAddress)

            if numberOfAddresses == 0:
                raise APIError('Why do you want to create 0 Addresses.')

            if numberOfAddresses > 999:
                raise APIError('You have (accidentally?) specified too many addresses to make. Maximum 999. \
                This check only exists to prevent mischief; if you really want to create more addresses than this, \
                contact the Bitmessage developers and we can modify the check or you can do it yourself by \
                searching the source code for this message.')

            if not label:
                label = passphrase

            label = unicode(label, 'utf-8')
            nonceTrialsPerByte = int(
                defaults.networkDefaultProofOfWorkNonceTrialsPerByte * totalDifficulty)
            payloadLengthExtraBytes = int(
                defaults.networkDefaultPayloadLengthExtraBytes * smallMessageDifficulty)
            queues.apiAddressGeneratorReturnQueue.queue.clear()
            queues.addressGeneratorQueue.put(
                ('createDeterministicAddresses', ADDRESSVERSION, streamNumberForAddress,
                 label, numberOfAddresses, passphrase, eighteenByteRipe, nonceTrialsPerByte, payloadLengthExtraBytes))
            queueReturn = queues.apiAddressGeneratorReturnQueue.get()
            return queueReturn

        def createRandomAddress(self, label, eighteenByteRipe=False, totalDifficulty=1, smallMessageDifficulty=1, streamNumberForAddress=1):
            '''Create a reandom Bitmessage Address
            Usage: api.createRandomAddress(label,eighteenByteRipe,totalDifficulty,smallMessageDifficulty)'''

            if not isinstance(eighteenByteRipe, bool):
                raise APIError(
                    'Bool expected in eighteenByteRipe, got %s instead' % type(eighteenByteRipe))

            if streamNumberForAddress != 1:
                raise APIError(
                    'Only Stream Number 1 is Supported jet. Got: %s' % streamNumberForAddress)

            unicode(label, 'utf-8')
            nonceTrialsPerByte = int(
                defaults.networkDefaultProofOfWorkNonceTrialsPerByte * totalDifficulty)
            payloadLengthExtraBytes = int(
                defaults.networkDefaultPayloadLengthExtraBytes * smallMessageDifficulty)
            queues.apiAddressGeneratorReturnQueue.queue.clear()
            queues.addressGeneratorQueue.put((
                'createRandomAddress', ADDRESSVERSION, streamNumberForAddress, label, 1, "", eighteenByteRipe, nonceTrialsPerByte, payloadLengthExtraBytes))
            return queues.apiAddressGeneratorReturnQueue.get()

        def deleteAddress(self, address):

            status, addressVersionNumber, streamNumber, toRipe = self._verifyAddress(
                address)
            address = addresses.addBMIfNotPresent(address)
            if not bitmessagemain.shared.config.has_section(address):
                raise APIError(
                    'Could not find this address in your keys.dat file.')

            bitmessagemain.shared.config.remove_section(address)
            with open(bitmessagemain.shared.appdata + 'keys.dat', 'wb') as configfile:
                bitmessagemain.shared.config.write(configfile)
                configfile.close()

            bitmessagemain.shared.reloadMyAddressHashes()
            return True

        def deleteChannel(self, address):
            self.deleteAddress(address)
            self.deleteFromAddressBook(address)
            return True

        def deleteFromAddressBook(self, address):
            '''Delete a Contact from Address Book
            Usage: api.deleteContact(bmaddress)'''

            queryreturn = bitmessagemain.shared.sqlExecute(
                '''delete from addressbook where address=?''', address)
            return True

        def getAllInboxMessageIDs(self):
            '''Get a List of IDs of all Inbox Messages
            Usage: api.getAllInboxMessageIDs()'''

            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid FROM inbox where folder='inbox' ORDER BY received''')
            data = []
            for msgid in queryreturn:
                data.append(msgid[0].encode('hex'))
            return data

        def getAllInboxMessages(self):
            '''Return a List of all Inbox Messages
            Usage: api.getAllInboxMessages()'''

            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid, toaddress, fromaddress, subject, received, message, encodingtype, read FROM inbox where folder='inbox' ORDER BY received''')
            messages = []
            for row in queryreturn:
                msgid, toAddress, fromAddress, subject, received, message, encodingtype, read = row
                subject = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    subject)
                message = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    message)
                messages.append({'msgid': msgid.encode('hex'), 'toAddress': toAddress, 'fromAddress': fromAddress,
                                 'subject': subject, 'message': message, 'encodingType': encodingtype, 'receivedTime': received, 'read': read})
            return messages

        def getAllSentMessageIDs(self):
            '''Get a List of IDs of all Outbox Messages
            Usage: getAllSentMessageIDs()'''

            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid FROM sent where folder='sent' ORDER BY lastactiontime''')
            data = []
            for row in queryreturn:
                msgid = row[0]
                data.append(msgid.encode('hex'))
            return data

        def getAllSentMessages(self):
            '''Get a List of all Outbox Messages
            Usage: api.getAllSentMessages()'''

            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid, toaddress, fromaddress, subject, lastactiontime, message, encodingtype, status, ackdata FROM sent where folder='sent' ORDER BY lastactiontime''')
            data = []
            for row in queryreturn:
                msgid, toAddress, fromAddress, subject, lastactiontime, message, encodingtype, status, ackdata = row
                subject = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    subject)
                message = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    message)
                data.append({'msgid': msgid.encode('hex'), 'toAddress': toAddress, 'fromAddress': fromAddress, 'subject': subject, 'message': message,
                             'encodingType': encodingtype, 'lastActionTime': lastactiontime, 'status': status, 'ackData': ackdata.encode('hex')})
            return data

        def getDeterministicAddress(self, passphrase):
            '''Returns a Deterministic Address for a give Passphrase
            Usage: api.getDeterministicAddress()'''

            # hardcoded in correct version and stream number, because they shouldn't be changed until now
            streamNumberForAddress = 1
            streamNumber = 1
            numberOfAddresses = 1
            eighteenByteRipe = False
            queues.addressGeneratorQueue.put(
                ('getDeterministicAddress', ADDRESSVERSION,
                 streamNumber, 'unused API address', numberOfAddresses, passphrase, eighteenByteRipe))
            return queues.apiAddressGeneratorReturnQueue.get()

        def getInboxMessageByID(self, msgid):
            '''Return an Inbox Message by a given ID
            Usage: print api.getInboxMessageByID(MessageID)'''

            msgid = msgid.decode('hex')
            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid, toaddress, fromaddress, subject, received, message, encodingtype, read FROM inbox WHERE msgid=?''', msgid)
            data = []
            for row in queryreturn:
                msgid, toAddress, fromAddress, subject, received, message, encodingtype, read = row
                subject = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    subject)
                message = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    message)
                data.append({'msgid': msgid.encode('hex'), 'toAddress': toAddress, 'fromAddress': fromAddress,
                             'subject': subject, 'message': message, 'encodingType': encodingtype, 'receivedTime': received, 'read': read})
            return data

        def getSentMessageByID(self, msgid):
            '''Return an Outbox Message by a given ID
            Usage: print api.getSentMessageByID(MessageID)'''

            msgid = msgid.decode('hex')
            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid, toaddress, fromaddress, subject, lastactiontime, message, encodingtype, status, ackdata FROM sent WHERE msgid=?''', msgid)
            data = []
            for row in queryreturn:
                msgid, toAddress, fromAddress, subject, lastactiontime, message, encodingtype, status, ackdata = row
                subject = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    subject)
                message = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    message)
                data.append({'msgid': msgid.encode('hex'), 'toAddress': toAddress, 'fromAddress': fromAddress, 'subject': subject.encode('base64'), 'message': message.encode(
                    'base64'), 'encodingType': encodingtype, 'lastActionTime': lastactiontime, 'status': status, 'ackData': ackdata.encode('hex')})
            return data

        def getSentMessagesBySender(self, fromAddress):
            '''Return a List of Message by a given Send Address
            Usage: print api.getSentMessagesBySender(SendAddress)'''

            queryreturn = bitmessagemain.shared.sqlQuery(
                '''SELECT msgid, toaddress, fromaddress, subject, lastactiontime, message, encodingtype, status, ackdata FROM sent WHERE folder='sent' AND fromAddress=? ORDER BY lastactiontime''', fromAddress)
            data = []
            for row in queryreturn:
                msgid, toAddress, fromAddress, subject, lastactiontime, message, encodingtype, status, ackdata = row
                subject = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    subject)
                message = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    message)
                data.append({'msgid': msgid.encode('hex'), 'toAddress': toAddress, 'fromAddress': fromAddress, 'subject': subject, 'message': message,
                             'encodingType': encodingtype, 'lastActionTime': lastactiontime, 'status': status, 'ackData': ackdata.encode('hex')})
            return data

        def joinChannel(self, label, testaddress=None):
            '''Join a Channel by a Given Name or Password
            api.joinChannel(label,testaddress[Only for Testing if the Name is correct])'''

            str_chan = '[chan]'

            # Precheck Address Book
            queryreturn = bitmessagemain.shared.sqlQuery(
                '''select * from addressbook where label=?''', str_chan + ' ' + label)
            if queryreturn != []:
                raise APIError('Channel already in Addressbook: %s' % label)

            # Add Channel to Own Addresses
            queues.apiAddressGeneratorReturnQueue.queue.clear()
            queues.addressGeneratorQueue.put(
                ('createChan', 4, 1, str_chan + ' ' + label, label, True))
            addressGeneratorReturnValue = queues.apiAddressGeneratorReturnQueue.get()

            if len(addressGeneratorReturnValue) == 0:
                raise APIError('The Channel is already in use: %s' % label)

            address = addressGeneratorReturnValue[0]
            if testaddress:
                if str(address) != str(testaddress):
                    raise APIError(
                        'The entered address does not match the address generated by the label')

            # Precheck Address Book
            queryreturn = bitmessagemain.shared.sqlQuery(
                '''select * from addressbook where label=?''', address)
            if queryreturn != []:
                raise APIError('Channel already in Addressbook: %s' % label)

            # Add Address to Address Book
            bitmessagemain.shared.sqlExecute(
                '''INSERT INTO addressbook VALUES (?,?)''', str_chan + ' ' + label, address)
            return address

        def listAddressBook(self):
            '''List the Address Book
            Usage: print api.listContacts()'''

            queryreturn = bitmessagemain.shared.sqlQuery(
                '''select * from addressbook''')
            data = []
            for row in queryreturn:
                label, address = row
                label = bitmessagemain.shared.fixPotentiallyInvalidUTF8Data(
                    label)
                data.append({'label': label, 'address': address})
            return data

        def sendMessage(self, fromAddress, toAddress, subject, message):
            '''Send a Message to a given Address or Channel
            Usage: api.sendBroadcast(OwnAddress, TargetAddress, Subject, Message)'''

            # Hardcoded Encoding Type, no othe supported jet
            encodingType = 2

            status, addressVersionNumber, streamNumber, toRipe = addresses.decodeAddress(
                toAddress)
            if status != 'success':
                with bitmessagemain.shared.printLock:
                    print 'ToAddress Error: %s , %s' % (toAddress, status)
                return (toAddress, status)
            status, addressVersionNumber, streamNumber, fromRipe = addresses.decodeAddress(
                fromAddress)
            if status != 'success':
                with bitmessagemain.shared.printLock:
                    print 'fromAddress Error: %s , %s' % (fromAddress, status)
                return (fromAddress, status)
            toAddress = addresses.addBMIfNotPresent(toAddress)
            fromAddress = addresses.addBMIfNotPresent(fromAddress)
            try:
                fromAddressEnabled = BMConfigParser().getboolean(
                    fromAddress, 'enabled')
            except:
                return (fromAddress, 'fromAddressNotPresentError')
            if not fromAddressEnabled:
                return (fromAddress, 'fromAddressDisabledError')

            stealthLevel = BMConfigParser().safeGetInt('bitmessagesettings', 'ackstealthlevel')
            ackdata = genAckPayload(streamNumber, stealthLevel)

            TTL = 4 * 24 * 60 * 60
            t = ('',
                 toAddress,
                 toRipe,
                 fromAddress,
                 subject,
                 message,
                 ackdata,
                 int(time.time()),  # sentTime (this won't change)
                 int(time.time()),  # lastActionTime
                 0,
                 'msgqueued',
                 0,
                 'sent',
                 2,
                 TTL)
            helper_sent.insert(t)
            queues.workerQueue.put(('sendmessage', toAddress))
            return ackdata.encode('hex')

        def trashInboxMessage(self, msgid):
            '''Trash a Message from Inbox by a given ID
            Usage: api.trashInboxMessage(MessageID)'''

            msgid = msgid.decode('hex')
            helper_inbox.trash(msgid)
            return True

        def trashSentMessage(self, msgid):
            '''Trash a Message from Outbox by a given ID
            Usage: api.trashSentMessage(MessageID)'''

            msgid = msgid.decode('hex')
            bitmessagemain.shared.sqlExecute(
                '''UPDATE sent SET folder='trash' WHERE msgid=?''', msgid)
            return True

        def _verifyAddress(self, address):
            status, addressVersionNumber, streamNumber, ripe = addresses.decodeAddress(
                address)
            if status != 'success':
                logger.warn(
                    'API Error 0007: Could not decode address %s. Status: %s.', address, status)

                if status == 'checksumfailed':
                    raise APIError('Checksum failed for address: ' + address)
                if status == 'invalidcharacters':
                    raise APIError('Invalid characters in address: ' + address)
                if status == 'versiontoohigh':
                    raise APIError(
                        'Address version number too high (or zero) in address: ' + address)
                raise APIError('Could not decode address: ' +
                               address + ' : ' + status)
            if addressVersionNumber < 2 or addressVersionNumber > 4:
                raise APIError(
                    'The address version number currently must be 2, 3 or 4. Others aren\'t supported. Check the address.')
            if streamNumber != 1:
                raise APIError(
                    'The stream number must be 1. Others aren\'t supported. Check the address.')

            return (status, addressVersionNumber, streamNumber, ripe)

    api = MainAPI()
    api.start(daemon=True)
    time.sleep(3)
    return api
