#	Request input from the user
num = int(input("Please enter a number in the range 0...9999: "))

#	Attenute the number if necesary
if num < 0: 		#	Make sure number is not too small
	num = 0
if num > 9999:		#	Make sure number is not too large
	num = 9999: 
print (end)