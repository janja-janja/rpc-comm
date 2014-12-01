import socket # Import socket module
import time

soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
host = "127.0.0.1"
port = 7003
soc.bind((host, port)) 
print "Server 6 started on port {0}...".format(port)

counter = 0
incoming_data=list(range(20))
while counter >-1:
	packet, addr = soc.recvfrom(1024)	
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"	
	print 'Source	: {0} | time	: {1}\n'.format(addr[1], time.ctime(time.time()))
	print "Message 	: {0}".format(packet)
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

	counter+=1
	
soc.close() # Close the connection