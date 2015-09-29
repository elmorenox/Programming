firstName = raw_input("Enter your first name: ").lower()
lastName = raw_input("Enter your last name: ").lower()

if firstName == "john" and lastName == "doe":
	print "Hello, %s %s" %(firstName, lastName)
else:
	print "Have we met?"	