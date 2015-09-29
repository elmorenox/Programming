# Write a program that takes in a string given by the user and replaces the character with another one on user's prompt


usrInput = raw_input("Give us a word, sentence or a number: ")

usrCheck = raw_input("What letter or number do you want to replace?: ")

usrReplace = raw_input("What letter or number do you want to place?: ")

usrInput = usrInput.replace(usrCheck,usrReplace)

print usrInput