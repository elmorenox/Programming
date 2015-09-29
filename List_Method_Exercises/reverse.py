sentence = "This is a sentence"

senlist = []

senList.extend(sentence.split()) #puts it into a list through .extend and splits it at empty spaces through .split

senList.reverse()

print senList

userinput = raw_input("Please enter a number")

userInput = list(userInput) # turns it into  a list

userInput.reverse() #reverses the list

userInput = ''.join(userinput) #joins the reversed list into a string

userinput = int(userinput) #string to int

print userInput + userInput