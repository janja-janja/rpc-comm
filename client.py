import xmlrpclib

gateway = xmlrpclib.ServerProxy("http://localhost:8000/")

while True:
	userInp = str(raw_input("Enter a number\n"))
	print "is %s even??:->> %s" % (userInp, str(gateway.isEven(userInp)))
	print "To quit press q\n"

	if userInp == 'q':
		break
	else:
		continue