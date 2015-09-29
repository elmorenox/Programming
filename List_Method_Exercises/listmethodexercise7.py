"""Write a program that accepts a list of elements from the user 
and then print the list after removing all duplicate values, preserving the original order
"""

usrList = []

while True: 

	usrInput = (raw_input("Give us number or print 'q' to quit: "))

	if usrInput != "q": 
		usrList.append(usrInput)
	else: 
		break
		print "You've quit"

newList = []

for element in usrList:
	if element not in  newList: 
		newList.append(element)

print newList



