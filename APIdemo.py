try:
    import xmlrpc.client as xmlrpclib
except ImportError:
    import xmlrpclib
from pyblackcointools import *
#This is only a demo! The RPC calls were done during testing and this is only
#to give you some ideas on how to interact with the exchange. You should become
#familiar with the source code so you can strategize how handle the API.
accounts={'john':{'reserve':0,'liquid':0},'alice':{'reserve':0,'liquid':0},'karen':{'reserve':0,'liquid':0},'dave':{'reserve':0,'liquid':0},'james':{'reserve':0,'liquid':0}}
HaloRPC = xmlrpclib.ServerProxy('http://localhost:55779')

def GenerateAddress():
    key,res=HaloRPC.GenerateDepositAddress('pw')
    address=privkey_to_address(key,25)
    return key,address
def LoadExchange():
    res=HaloRPC.SetPassword('pw','')
    res=HaloRPC.StartExchange('pw')
    exchangeaddress="BQWPRHbTKbo6VJwCjtvLaUg4fykPmiWZdN"
    feeaccount="B65aJgkuAinZ35Rt1EnqVB3yX8gESe9ogV"
    time.sleep(.2)
    res=HaloRPC.ExchangeSettings([exchangeaddress],feeaccount,{'min':10000000,'max':1000000000,'percent':.001},'','pw')
#It's recommended to iterate and ask for specific addresses instead of all at once
#When you see a user has some new deposits, you can add them to their account
global alicetxids
def ScanForDeposits(): 
    global alicetxids
    alicetxids={}
    aliceaddress='BSiotcQ4DqQ8g7ijffu3n9pTB4QSNVEUTH'
    Spendable=HaloRPC.GetSpendable(aliceaddress,'pw')
    d=[]
    for s in Spendable:
        if s not in alicetxids and 'change' not in Spendable[s]:
            d.append(s)
    if d==[]:
        return
    res=HaloRPC.Deposit('alice',d,'pw')
    print(str(res))
    if res==True:
        for s in d:
            alicetxids[s]=1

#This can actually take a lot of time to scan liquidity of all the inputs. In Python it takes a few minutes.
#LoadExchange()

#ScanForDeposits()
#Check to see if deposits are registered
#res=HaloRPC.GetDeposits('','pw')
#Get exchange balance
#res=HaloRPC.GetBalance('exchange','pw')
#Get user balance
#res=HaloRPC.GetBalance('alice','pw')
#res=HaloRPC.GetBalance('karen','pw')
#Make a trade
#res=HaloRPC.Trade('karen', 100000000, 'dave', 'liquid', 'pw')
#if res != True:
#    pass #If the server is busy, let the user know or let the orderbook stack
#res=HaloRPC.GetBalance('dave','pw')

#The other style of trading. Deposit to the pool and the withdraw from it
#res=HaloRPC.Trade('karen', -20000000, '', 'liquid', 'pw')
#res=HaloRPC.Trade('john', 20000000, '', 'liquid', 'pw')

#res=HaloRPC.Trade('john', 20000000, 'james', 'liquid', 'pw')
#res=HaloRPC.Trade('james', 200000, 'john', 'reserve', 'pw')

#res, ID=HaloRPC.Withdraw('dave', 100000000, 'bNgmCcxPKgQQqUe6rhNtbGWowMJFCuxjZ3', 'liquid', 'pw')
#The Uniquie ID was: 3df074f7a97c2ea876d985289ccffbc6
#ID="a7df9561e0af93d3b0067eee8f048b74"
#Now we track the withdraw
#res=HaloRPC.CheckWithdraw(ID, '', 'pw')

#res=HaloRPC.GetBalance('alice','pw')
#res, ID=HaloRPC.Withdraw('alice', 100000000, 'bNgmCcxPKgQQqUe6rhNtbGWowMJFCuxjZ3', 'liquid', 'pw')
#The Uniquie ID was: 3df074f7a97c2ea876d985289ccffbc6
#ID="867cc85b59a4052417f6b29d08fb1ef6"
#Now we track the withdraw
#res=HaloRPC.CheckWithdraw(ID, '', 'pw')

#res=HaloRPC.GetBalance('alice','pw')
#res, ID=HaloRPC.Withdraw('alice', 100000000, 'bNgmCcxPKgQQqUe6rhNtbGWowMJFCuxjZ3', 'reserve', 'pw')
#The Uniquie ID was: 3df074f7a97c2ea876d985289ccffbc6
#ID="e6d3b3e0e92ef4a120c930cf537b91b9"
#Now we track the withdraw
#res=HaloRPC.CheckWithdraw(ID, '', 'pw')

#When you are running your exchange, you will want to have a loop that checks for deposits, changes
#in intervals, trades, balances and so forth. You will need to check every 1/2 second or so if there
#has been a change to the supply rate. If so then you should compare users balance against their
#open orders or against their previous balances and then adjust their orders accordingly. It is also
#possible to check balances once a trade commences before executing it. However this method is not
#recommended because then buy/sell walls will not properly represent how much they have to trade.
#It may be recommended to check both balance and cycle to be sure. The cycle changes every 200 blocks.

#This is only an example. The production code should be efficient and work with your exchange orderbook system.
"""
AliceOrders={'ORDER:323509092304521':{'SellBitBay':100000000,'BitcoinRate':5000},'ORDER:981240909230452':{'SellBitBay':50000000,'BitcoinRate':7000}}
CurrentCycle=15
res=HaloRPC.GetCycle('pw')
if res>CurrentCycle:
    print("cycle change")
    CurrentCycle=res
    atotal=0
    for Ordernumber in AliceOrders:
        atotal+=AliceOrders[Ordernumber]['SellBitBay']
    res=HaloRPC.GetBalance('alice','pw')
    #We check to see if liquid funds became reserve and if she has enough to cover her orders.
    #It's possible that the exchange may want to pause trading for a couple seconds while it checks balances.
    print(str(res))
    print(str(res['liquid']))
    print(str(atotal))
    res['liquid']=40000000
    try:
        if res['liquid']<atotal:
            perc=float(res['liquid'])/float(atotal)
            print(str(perc))
            for Ordernumber in AliceOrders:
                AliceOrders[Ordernumber]['SellBitBay']=int(float(AliceOrders[Ordernumber]['SellBitBay'])*perc)
    except:
        pass
print(str(AliceOrders))
"""
#res=HaloRPC.GetBalance('alice','pw')
#print(str(res))
#Although you should keep the exchange running as much as possible. You can shut down using this command.
#res=HaloRPC.ShutDown('pw')