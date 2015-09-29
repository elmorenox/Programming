usrSentence = raw_input("Give us a sentence: ")

usrList = list(usrSentence)

usrList.reverse() # I don't get why I don't have to set a variable for this

usrList = "".join(usrList) #Why do i have to set it here but not for reverse? List vs string? 

print usrList

#sentence = "this is a sentence"

#senList = [] #creates an empty list

#print sentence.split() # splits the sentence at spaces
#print sentence # prints

#senList.extend(sentence.split())

#senList.reverse()

#print senList