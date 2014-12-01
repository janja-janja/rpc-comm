import socket
import time
import random

soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM) #create and initialize a new socket
host = "127.0.0.1" #local machine host
port = 7000

soc.bind((host, port)) #local machine to listen on port:7000

print "Initiator started on port {0}...".format(port)

while True: #server maintains an active state as long as the program is running
	
	#select ports to send to
	ports =[7001, 7002]

	port_selected=random.choice(ports)
	print "Port %s chosen" % str(port_selected)

	while True:
		packet=raw_input("Enter Data to send:\n")
		soc.sendto(packet, (host, port_selected)) #address to send the message to contains [host : port]
		print "Message: {0} sent to {1}\n".format(packet, port_selected)
		time.sleep(1)

	else:
		print "\n"
soc.close