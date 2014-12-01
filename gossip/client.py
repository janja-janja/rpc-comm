'''
	Role : Implementation of Gossip algorithm using binary trees
	File : Client :- initiates the message to be sent across all the other computers
'''

import socket
import time
import random
soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM) #create and initialize a new socket
host = "127.0.0.1" #local machine host
port = 7000

soc.bind((host, port)) #local machine to listen on port:7000

print "Server 0 started on port {0}...".format(port)

while True: #server maintains an active state as long as the program is running
	
	#select ports to send to
	ports =[7001, 7002]
	counter = 0
	sentDest=list(range(3))
	packet=raw_input("Enter Data to send:\n")
	while counter>-1:
		port_select=random.choice(ports)	

		if counter == 0:
			state=True

		else:
			if port_select in sentDest:
				state=False
			else:
				state=True

		if state is True:
			sentDest.append(port_select)
			soc.sendto(packet, (host, port_select)) #address to send the message to contains [host : port]
			print "Message: {0} sent to {1}\n".format(packet, port_select)
			time.sleep(1)

		counter+=1

		if counter > 3: #loops 3 times to gaurantee random node selection
			counter=-1
	else:
		print "\n"
soc.close