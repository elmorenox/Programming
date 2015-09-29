"""Write a program that takes user input and finds if an alphabet is present in a string or not and if yes 
then print its position in a list and count how many times it present. 
"""

usrInput = raw_input("Give us a word, sentence: ")

usrCheck = raw_input("What letter are you looking for?: ")

usrList = list(usrInput)

print "This is the location of it's first occurence: %s" %(usrInput.index(usrCheck)) 
print "This is how many times it shows up: %s" %(usrInput.count(usrCheck))

# print position and times present



