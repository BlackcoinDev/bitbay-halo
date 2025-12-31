# This is an example of how to connect to and use the Bitmessage API.
# See https://bitmessage.org/wiki/API_Reference

import xmlrpclib
import json
import time

api = xmlrpclib.ServerProxy("http://bradley:password@localhost:8442/")

'Let\'s test the API first.''Let\'s test the API first.'
inputstr1 = "hello"
inputstr2 = "world"
api.helloWorld(inputstr1, inputstr2)api.helloWorld(inputstr1, inputstr2)
api.add(2,3)api.add(2,3)

'Let\'s set the status bar message.''Let\'s set the status bar message.'
api.statusBar("new status bar message")api.statusBar("new status bar message")

'Let\'s list our addresses:''Let\'s list our addresses:'
api.listAddresses()api.listAddresses()

'Let\'s list our address again, but this time let\'s parse the json data into a Python data structure:''Let\'s list our address again, but this time let\'s parse the json data into a Python data structure:'
jsonAddresses = json.loads(api.listAddresses())
jsonAddressesjsonAddresses
'Now that we have our address data in a nice Python data structure, let\'s look at the first address (index 0) and print its label:''Now that we have our address data in a nice Python data structure, let\'s look at the first address (index 0) and print its label:'
jsonAddresses['addresses'][0]['label']jsonAddresses['addresses'][0]['label']

'Uncomment the next two lines to create a new random address with a slightly higher difficulty setting than normal.''Uncomment the next two lines to create a new random address with a slightly higher difficulty setting than normal.'
#addressLabel = 'new address label'.encode('base64')
#print api.createRandomAddress(addressLabel,False,1.05,1.1111)

'Uncomment these next four lines to create new deterministic addresses.''Uncomment these next four lines to create new deterministic addresses.'
#passphrase = 'asdfasdfqwser'.encode('base64')
#jsonDeterministicAddresses = api.createDeterministicAddresses(passphrase, 2, 4, 1, False)
#print jsonDeterministicAddresses
#print json.loads(jsonDeterministicAddresses)

#print 'Uncomment this next line to print the first deterministic address that would be generated with the given passphrase. This will Not add it to the Bitmessage interface or the keys.dat file.'
#print api.getDeterministicAddress('asdfasdfqwser'.encode('base64'),4,1)

#print 'Uncomment this line to subscribe to an address. (You must use your own address, this one is invalid).'
#print api.addSubscription('2D94G5d8yp237GGqAheoecBYpdehdT3dha','test sub'.encode('base64'))

#print 'Uncomment this line to unsubscribe from an address.'
#print api.deleteSubscription('2D94G5d8yp237GGqAheoecBYpdehdT3dha')

'Let\'s now print all of our inbox messages:''Let\'s now print all of our inbox messages:'
api.getAllInboxMessages()api.getAllInboxMessages()
inboxMessages = json.loads(api.getAllInboxMessages())
inboxMessagesinboxMessages

'Uncomment this next line to decode the actual message data in the first message:''Uncomment this next line to decode the actual message data in the first message:'
#print inboxMessages['inboxMessages'][0]['message'].decode('base64')

'Uncomment this next line in the code to delete a message''Uncomment this next line in the code to delete a message'
#print api.trashMessage('584e5826947242a82cb883c8b39ac4a14959f14c228c0fbe6399f73e2cba5b59')

'Uncomment these lines to send a message. The example addresses are invalid; you will have to put your own in.''Uncomment these lines to send a message. The example addresses are invalid; you will have to put your own in.'
#subject = 'subject!'.encode('base64')
#message = 'Hello, this is the message'.encode('base64')
#ackData = api.sendMessage('BM-Gtsm7PUabZecs3qTeXbNPmqx3xtHCSXF', 'BM-2DCutnUZG16WiW3mdAm66jJUSCUv88xLgS', subject,message)
#print 'The ackData is:', ackData
#while True:
#    time.sleep(2)
#    print 'Current status:', api.getStatus(ackData)

'Uncomment these lines to send a broadcast. The example address is invalid; you will have to put your own in.''Uncomment these lines to send a broadcast. The example address is invalid; you will have to put your own in.'
#subject = 'subject within broadcast'.encode('base64')
#message = 'Hello, this is the message within a broadcast.'.encode('base64')
#print api.sendBroadcast('BM-onf6V1RELPgeNN6xw9yhpAiNiRexSRD4e', subject,message)
