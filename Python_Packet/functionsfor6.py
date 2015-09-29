#valid entry check 

def validEntry(entry): 
	if len(entry) != 5: 
		print "MUST BE 5 DIGIT NUMBER."
		return False

	if entry.isdigit() == False: 
		print "ALL CHARACTERS MUST BE NUMBERS."
		return False


	entryList = list(str(entry))
	for element in entryList:
		if entryList.count(element) > 1:
			print "ENTRY CAN NOT CONTAIN DUPLICATES."
			return False
			break

	return True


def numInGuess(var1,var2):
	varList1 = list(var1)
	varList2 = list(var2)
	count = 0

	for element in varList1:
		if element in varList2:
			count = count + 1
	return count
	

def compareGuessIndex(usrVar,adminVar):
	usrVarList = list(str(usrVar))
	adminVarList = list(str(adminVar))
	count = 0

	for element in range(len(usrVar)):
		if usrVar[element] == adminVar[element]:
			count = count + 1
	return count

