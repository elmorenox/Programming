

#function to determine size of user input
def strSize(userInput): 
	strSize = len(userInput)
	return strSize

#additive persistence and additive root function	

def addFunction(userInput): 

	count = 0 #to count how many times needed to loop before reaching single digit 

#loop till I get to additive root
	while len(userInput) > 1: 

		strList = list(userInput)

		intList = []

		for element in strList: 
			intList.append(int(element))

		count += 1
		sumNum = sum(intList) #additive root

		userInput = str(sumNum)

	
	print "Additive root is %s" %sumNum
	print "Additive persistence is %s" %count

def prodFunction(userInput): 

	multNum = 1
	count = 0 

	while len(userInput) > 1: 

		strList = list(userInput)

		intList = []

		for element in strList: 
			intList.append(int(element))

		for element in intList: 
			multNum = multNum * element
			userInput = str(multNum)

		multNum = 1
		count = count + 1

	print "Multiplicative root is: %s" %userInput
	print "Multiplicative persistence is: %s" %count



