"""Object oriented program. Think about the data. 

Different than sequentially. 

Makes it diffucult for collaborative projects. 

Working on objects themselves makes it easier for collab projects by working different sets of data. 

Classes are a collection of functions. 

"""
#creating a function that determines if odd or even

def odd_even(number): #in the parantheses are the paramaters. You don't have to have parameters. 

	if number % 2 == 0:
		return True
	else: 
		return False

print is_even(3)
print is even(10)

var1 = 13
var2 = 26
var3 = 1234442447

print is_even(var3)

####/////////\\\\\\\\\\####

def is_even(var1): #you are only naming the variable but not assigning the variable
	if var1 % 2 == 0: 
		return True 
	else: 
		return False

print is_even(3) #you have to print because the function only "returns"

####/////////\\\\\\\\\\####

def month(x): 
	months = ("Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec")
	return months[(x-1)]

userInput = input("Please enter a number: ")
print months(userInput)

####/////////\\\\\\\\\\####

def month(x): 
	months = {	1:"Jan", 
				2:"Feb", 
				3:"Mar", 
				4:"Apr", 
				5:"May", 
				6:"Jun", 
				7:"Jul", 
				8:"Aug", 
				9:"Sep", 
				10:"Oct", 
				11:"Nov", 
				12:"Dec"
			}
	return months{x}

userInput = input("Please enter a number: ")
print months(userInput)

####/////////\\\\\\\\\\#### 

#To import a module (file containing python)
# an asterik after the name of the file means import all data
# the name of a piece of code after the name of the file means to import that funcion, class, var 

from functions import *
