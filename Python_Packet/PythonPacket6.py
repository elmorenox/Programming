adminInput = raw_input("Administrator, give us a number that is 5 digits and has no duplicate integers: ")

adminList = list(adminInput)

dupCheckList = []

for element in adminList:
	if element not in dupCheckList:
		dupCheckList.append(element)

while (len(adminInput) != 5) or (adminInput.isdigit() == False) or (adminList != dupCheckList):

	if len(adminInput) != 5:
		print "Number must be 5 digits."
	
	if adminInput.isdigit() == False: 
		print "Input must be a number."

	if adminList != dupCheckList: 
		print "There can not be any duplicate digits."

	adminInput = raw_input("Administrtor, give us a number that is 5 digits and has no duplicate integers: ")

	adminList = list(adminInput)

	dupCheckList = []

	for element in adminList:
		if element not in dupCheckList:
			dupCheckList.append(element)


print "The number is: _ _ _ _ _" 

#userGuess = ''

#while userGuess != 'Q' or userGuess != adminInput:

userGuess = raw_input("Player, guess the number. Must be 5 digits and have no duplicates. You have 10 tries. Press 'q' to quit:").upper()

userList = list(userGuess)

#checking for dup in userGuess

dupCheckList2 = []

for element2 in userList:
	if element2 not in dupCheckList2:
		dupCheckList2.append(element2)

tries = 0 

while tries < 10: 

	if userGuess == "Q": 
		print "You've quit"
		print "%s tries" %tries
		break
		
	elif len(userGuess) != 5:
		print "Number must be 5 digits."
		
	elif userGuess.isdigit() == False: 
		print "Input must be a number."

	elif userList != dupCheckList2: 
		print "There can not be any duplicate digits."

	if tries == 0:
		tries == 0
	else: 
		tries = tries

	# actually start guessing game. After user has given a valid input. 

	# check if user guess is correct

	if userGuess == adminInput: 
		tries = tries + 1
		print "%s tries" %tries 
		print "Youre right"
		break

	#check how mnay numbers are in admin input

	count = 0
	count2 = 0 

	if userGuess != adminInput:
		tries = tries + 1
		for element3 in userList: 
			if element3 in adminList: 
				count = count + 1

		print "Correct digits in guess: %s" %count

	#check how many numbers in same index place

	count2 = 0

	if userGuess[0] == adminInput[0]:
		count2 = count2 + 1
	if userGuess[1] == adminInput[1]:
		count2 = count2 + 1
	if userGuess[2] == adminInput[2]: 
		count2 = count2 + 1
	if userGuess[3] == adminInput[3]:
		count2 = count2 + 1
	if userGuess[4] == adminInput[4]:
		count2 = count2 + 1

	print "Correct digits in place: %s" %count2

	userGuess = raw_input("Player, guess the number. Must be 5 digits and have no duplicates. You have %s tries. Press 'q' to quit: " %(10-tries)).upper()

	userList = list(userGuess)

	dupCheckList2 = []

	for element2 in userList:
		if element2 not in dupCheckList2:
			dupCheckList2.append(element2)


































