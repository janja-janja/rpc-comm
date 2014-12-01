#RPC program
from SimpleXMLRPCServer import SimpleXMLRPCServer
HOST = (("localhost", 8000))

def isEven(n):
    return int(n)%2 == 0

server = SimpleXMLRPCServer(HOST)

print "Server is now running at ->> " + str(HOST)
server.register_function(isEven, "isEven")
server.serve_forever()