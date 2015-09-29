# Exercise: ForSum.py 
''' 
Write a program that gets an integer from the user. 
Add up all the numbers from 1 to that number, and display the total.

'''
userNum = input("Please enter a number: ")
numSum = 0

for number in range(1, userNum+1):
	numSum = numSum + number
print numSum