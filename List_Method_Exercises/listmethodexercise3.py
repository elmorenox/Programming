# Write a program that takes a word from the user and determines if the word is a palindrome

usrWord = raw_input("Give us a word and we'll determine if it's a palindrome: ")

usrList = list(usrWord)

usrList.reverse() #reverses usrList

usrList = "".join(usrList) #joins the reversed usrInpu

if usrWord == usrList:
	print "palindrome"
else: 
	print "not palindrome"


