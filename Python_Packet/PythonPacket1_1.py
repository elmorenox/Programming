"""
1. ask the user for an interger 
2. if the given interger is a single digit, report it's additive persistence and multiplicative persistence as 0 and 
both its additive and multiplicative root as itself
3. if the integer is less than 0, that is a signal to quit the program
Otherwise, find the additive and multiplicative persistence as well as the additive and multiplicative root of
the given interger and report the result to the user. 
4. Continue by prompting the user until they quit""" 

from functionsfor1 import *

inputStr = raw_input("Give me an interger. A number less than zero will quit the program: ").lower()

while inputStr != "q": 

	strSize = len(inputStr)
	inputInt = int(inputStr)

	if inputInt < 0:
		print "You've entered a number less than zero."
		break

	while strSize >= 1:

		if strSize == 1: 

			addPer = 0 
			multPer = 0 
			addRoot = inputStr
			mulRoot = inputStr

			print "Additive persistence is %s." %addPer
			print "Multiplicative persistence is %s." %multPer
			print "Additive roots is %s" %addRoot
			print "Multiplicative root is %s" %mulRoot
			break

		if strSize > 1: 
			addFunction(inputStr)
			prodFunction(inputStr)
			break

	inputStr = raw_input("Give me an interger. A number less than zero will quit the program: ").lower()

print "You've quit the game."