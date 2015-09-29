from functionsfor6 import *

adminInput = raw_input("Administrator, give us a number that is 5 digits and has no duplicate integers: ").lower()


while validEntry(adminInput) == False:
	adminInput = raw_input("Administrator, give us a number that is 5 digits and has no duplicate integers: ").lower()


print "The number is: _ _ _ _ _" 

userGuess = raw_input("Player, guess the number. Must be 5 digits and have no duplicates. You have 10 tries. Press 'q' to quit:").lower()

tries = 0 

while userGuess != "q":
	if tries > 10: 
		print "You're out of tries."
		break

	while validEntry(userGuess) == False: 
		userGuess = raw_input("Player, guess the number. You have %s tries. Press 'q' to quit: " %(10-tries)).lower()
		
	if userGuess == adminInput: 
		print "CORRECT"
		print "You guess it in %s tries" %tries
		break

	elif userGuess != adminInput: 
		tries = tries + 1
		print "Correct digits in guess: %s" %(numInGuess(userGuess,adminInput))
		print "Digits in correct index: %s" %(compareGuessIndex(userGuess,adminInput))

		userGuess = raw_input("Player, guess the number. You have %s tries. Press 'q' to quit: " %(10-tries)).lower()


if userGuess == "q":
	print "You've quit the game."
	print "Tries: %s" %tries



"""
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

"""


































