import xmlrpclib

gateway = xmlrpclib.ServerProxy("http://localhost:8000/")

while True:
	userInp = str(raw_input("Enter a number\n"))
	print "\tis %s even??:->> %s" % (userInp, str(gateway.isEven(userInp)))
	print "\tTo quit press q\n"

	if userInp == 'q' or userInp == 'Q':
		break
	else:
		continue