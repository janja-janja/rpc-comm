import socket # Import socket module
import time
import random

soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
host = "127.0.0.1"
port = 7002
soc.bind((host, port)) 

print "Server 3 started on port {0}...".format(port)


while 1:
	packet, addr = soc.recvfrom(1024)
	time.sleep(5)
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"	
	print 'Source	: {0} | time	: {1}\n'.format(addr[1], time.ctime(time.time()))
	print "Message 	: {0}".format(packet)
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	ports=[7005, 7006]
	
	counter = 0
	sentDest=list(range(4))
	while counter >-1:
		port_select=random.choice(ports)
		sendto = port_select
		state = False
		
		if counter == 0:
			state=True

		else:
			i=0
			if sendto in sentDest:
				state=False
			else:
				state=True

		if state is True:
			time.sleep(3)
			sentDest.append(sendto)
			soc.sendto(packet, (host, port_select))

		counter +=1

		if counter >2:
			counter =-1
	
soc.close() #Close the connection			