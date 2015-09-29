name = "john"
print name.capitalize() # Capitalizes first letter on the first word in the string
print name.upper() # Capitalizes all letters in the string
print name.lower() # Makes all letters in the string lowercase



name = "john doe"
age = "28"
numbers = "12345678"
print name.title() # Capitalizes the first letter of each word in the string
print name.islower() # Verifies if the string is lowercase. Will return TRUE if is lower and False if not lower. 
print name.replace('john', 'michael') # Replaces element of a string with another. Takes two arguments.
print name.istitle() # Checks if string is title. Returns TRUE if string is title and FALSE if not. 
print name.isupper() # Checks if string is upper case. Returns TRUE if string is uppercase and FALSE if not. r
print name.isspace() # Checks if there are any spaces in the string.
print name.swapcase() # Swaps the case of a string. If string is upper will convert to lower and vice versa.
print name.isalpha() # Checks if string contains only letters. Returns TRUE if string only has characters, if not returns FALSE

print list(numbers) # Converts string into a list

## ////////// LIST METHODS \\\\\\\\\\ ##

numbersList = list(numbers)

numbersList.insert(0,"1") # Inserts an item into a list. Takes two arguments. The position and the item.

print numbersList

numbersList.reverse() # Reverses the order of the list. 


print numbersList
numbersList = ''.join(numbersList) # Joins multiple items in a list, but can be used to convert a list into a string

print numbersList

numbersList = list(numbersList)

numbersList.append("9") # Adds an item to a list at the end of the list

print numbersList

numbersList.pop(3) # Removes an item from a list using the items position. 

print numbersList

numbersList.remove("9") # Removes an item from a list using the items value. 

print numbersList

print numbersList.count("5") # Determines how many items of a given value exist in a list

numbersList2 = ["10", "11", "12", "13", "14"]

numbersList.extend(numbersList2) # Can be used to add list together

print numbersList

