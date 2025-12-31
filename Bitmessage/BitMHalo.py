import sys
from . import class_api
from . import parallelTestModule
import time
import os
import rpyc #For communication between the server and BitHalo for now not being used
import ast

if __name__ ==  '__main__':
	extractor = parallelTestModule.ParallelExtractor()
	extractor.runInParallel(numProcesses=1, numThreads=1)#EDIT:Was two processes is now one
	api = class_api.getAPI(silent=True)
	ch=""
	path=os.path.join("Bitmessage","BitTMP.dat")
	data=[]
	data.append("0")
	data.append("0")
	data.append("0")
	data.append("0")
	data.append("0")
	data.append("0")
	data.append("0")
	while ch != "exit":
		time.sleep(1.23456)
		try:
			with open(path,'r') as f:
				data[0]=f.readline().strip()
				data[1]=f.readline().strip()
				try:
					data[2]=f.readline().strip()
				except:
					print("")
				f.close()
		except Exception as e:
			sys.stderr.write(str(e))
		if data[0] == "0":			
			ch=data[1]
			if ch == "Send":
				#Sends a message
				Order=ast.literal_eval(data[2])
				ret = api.sendMessage(Order['MyBMAddress'],Order['TheirBMAddress'],"BitHalo",str(Order))
				sys.stderr.write(str(ret))
				try:
					with open(path,'w') as f:
						f.write("1"+"\n")
						f.write("Send1"+"\n")
						f.write(str(ret)+"\n")
						f.close()
				except:
					print("error")
			if ch == "GetMessages":
				#Gets messages
				#Command=ast.literal_eval(data[2])#This gets the specific addresss as well
				a = api.getAllInboxMessages()
				try:
					with open(path,'w') as f:
						f.write("1"+"\n")
						f.write("GetMessages1"+"\n")
						f.write(str(a)+"\n")
						f.close()
				except:
					sys.stderr.write("BitMHalo-error")
			if ch == "new":
				#Make a new address and return it
				try:
					with open(path,'w') as f:
						addr=api.createRandomAddress("BitHalo")
						f.write("1"+"\n")
						f.write("new1"+"\n")
						f.write(addr+"\n")
						f.close()
				except:
					sys.stderr.write("BitMHalo-error")