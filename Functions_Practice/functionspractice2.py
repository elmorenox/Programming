def multiple2of1(num1,num2): 
	if abs(num2) / abs(num1) == 0:
		print "True"
	else: 
		print "False"

num1 = input("Give us a number: ")
num2 = input("Give us a second: ")

multiple2of1(num1,num2)