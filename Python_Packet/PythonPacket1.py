"""
1. ask the user for an interger 
2. if the given interger is a single digit, report it's additive persistence and multiplicative persistence as 0 and 
both its additive and multiplicative root as itself
3. if the integer is less than 0, that is a signal to quit the program
Otherwise, find the additive and multiplicative persistence as well as the additive and multiplicative root of
the given interger and report the result to the user. 
4. Continue by prompting the user until they quit""" 

inputStr = raw_input("Give me an interger. A number less than zero will quit the program: ")

inputInt = int(inputStr)

while inputInt > 0: 

	strSize = len(inputStr)
	addStr = strSize
	prodStr = strSize
	count = 0
	sumNum = inputStr
	prodNum = inputStr

	while addStr >= 1:

		if addStr == 1: 

			addPer = 0 
			multPer = 0 
			addRoot = inputStr
			mulRoot = inputStr

			print "Additive persistence is %s." %addPer
			print "Multiplicative persistence is %s." %multPer
			print "Additive roots is %s" %addRoot
			print "Multiplicative root is %s" %mulRoot
			break

		if addStr == 4: 
			sumNum = (int(inputStr[:1]) + int(inputStr[1:2]) + int(inputStr[3:4])) 
			print "Additive root is %s" %sumNum
			addStr = len(str(sumNum))
			print "Additive persistence is 3"


		if addStr == 3: 

			sumNum = (int(inputStr[:1]) + int(inputStr[1:2]) + int(inputStr[2:3])) 
			print "Additive root is %s" %sumNum
			addStr = len(str(sumNum))
			print "Additive persistence is 2"
			

		if addStr == 2:

			sumNum = (int(inputStr[:1]) + int(inputStr[1:2]))
			print "Additive root is %s" %sumNum
			addStr = len(str(sumNum))
			print "Additive persistence is 1" 
			break



	inputStr = raw_input("Give me an interger or press 'q' to quit: ")

print "You've quit." 
