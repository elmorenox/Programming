
for tries in range (1,4):
	usrInput = int(raw_input("Enter your password:" ))
	if usrInput == 123:
		print "OK"
		break
	print tries, "Tries"

if usrInput != 123:
	print "locked out"