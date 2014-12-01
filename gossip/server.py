'''
	Role : listening to the message sent from the client and sending it to 2 other randomly picked servers
	File : Server	
'''

import socket
import random
import time

soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
host = "127.0.0.1"
port = 7001
soc.bind((host, port)) 
print "Server 1 started on port {0}...".format(port)
'''
	Server waits for the servers connection
	which is established through the socket in line : 21
'''

while True:
	packet, addr = soc.recvfrom(1024)
	time.sleep(3)
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"	
	print 'Source	: {0} | time	: {1}\n'.format(addr[1], time.ctime(time.time()))
	print "Message 	: {0}".format(packet)
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	ports=[7003, 7004]
	
	counter = 0
	sentDest=list(range(3))
	while counter >-1:
		port_select=random.choice(ports)
		sendto = port_select
		state = False
	
		if counter==0:
			state=True

		else:
			if sendto in sentDest:
				state=False
			else:
				state=True
		if state is True:
			time.sleep(2)
			sentDest.append(sendto)
			soc.sendto(packet, (host, port_select)) #address to send the message to contains [host : port]

		counter+=1

		if counter>3:
			counter=-1

soc.close() #close the server connection