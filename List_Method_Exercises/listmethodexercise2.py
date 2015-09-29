# Write a program that capitalizes the first word of a the users input and outputs the result. Is this the first letter of the first word
# or the whole first word? 


usrSentence = raw_input("Give us a sentence: ")

usrList = []

usrList.extend(usrSentence.split())

firstWord = usrList[0]

restWord = usrList [1:]

print firstWord.upper() , " ".join(restWord)



