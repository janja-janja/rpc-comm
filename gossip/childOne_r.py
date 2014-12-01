import socket
import random
import time

soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
host = "127.0.0.1"
port = 7001
HOST = ((host, port))

soc.bind(HOST) 
print "Child one started on port {0}...".format(port)

#children to This node
ports = [7003, 7004]

while True:
	packet, addr = soc.recvfrom(1024)
	time.sleep(3)
	port_selected = random.choice(ports)
	print "\nPort %s chosen" % str(port_selected)	

	print 'Sender::{0}  at ->> {1}\n'.format(addr[1], time.ctime(time.time()))
	print "Message ->> {0}".format(packet)
	
	soc.sendto(packet, (host, port_selected)) 

soc.close() #close the server connection