# Exercise: MultiLoop.py

'''
Write a program that ask user for a number then a multiple
display the product of the numbers up to the multiple

'''

userNum = input("Please enter a number: ")
multiNum = input("Please enter number of multiples: ")

multiNum = multiNum + 1

for multi in range(1, multiNum):
	print "%s * %s = %s" %(userNum, multi, (userNum * multi))