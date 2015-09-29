dictionary = {
				"Apple" : "A red fruit that grows on trees" , 
				"Dog"	: "A four legged animal",
				"Program"	: "A list of instructions", 
}

print "Welcome to our interactive dictionary"
print "\nWhat would you like to do?"
print "Quit - Quit"
print "Find - Look up word in dictionary."
print "Add - Add a word to the dictionary."
print "Update - Update an existing word's definition."
print "Remove - Remove a word from the dictionary."

choice = raw_input("\n Please enter an option: ").lower()

while choice != "Quit":

	if choice == 'find': 
		word = raw_input("What word would you like to find: ").lower()
		if word in dictionary: 
			print "The word %s has been found and its defition is %s" %(word, dictionary[word])
		else: 
			print "%s not found. Try adding it to the dictionary."

	elif choice == 'add':
		if word in dictionary: 
			print "The %s is already present in dict., try updating it's defition." %word
		else: 
			definition = raw_input("What is the definition of the word?: ").lower()
			definition[word] = definition
			print "% has beend added t the dictionary with a definition of: %s" %(word, definition)

	elif choice == 'update': 
		term = raw_input("What word would you like to update?": ).lower()
		if word in dictionary: 
			definition = ("What is the definition of the word you are trying to update?: ").lower()
			dictionary[term] = definition
			print "The definition of %s has been updated in the dict. w the def. of: %s" %(word, definition)

		print "Update and existing word's def."

	elif choice == 'remove':
		print "Remove a word from the dictionary." 

	else: 
		print "Not a valid choice."

	print "\nWhat would you like to do?"
	print "Quit - Quit"
	print "Find - Look up word in dictionary."
	print "Add - Add a word to the dictionary."
	print "Update - Update an existing word's definition."
	print "Remove - Remove a word from the dictionary."

	choice = raw_input("\nPlease enter and option: ")

print "Done"