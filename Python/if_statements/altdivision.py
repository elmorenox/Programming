# 	Get two floats from the user
dividend = float(input("Please enter a number to divide: "))
divisor = float(input("Please enter the second number to divide: "))

#	If possible, divide them and report the result
if divisor != 0: 
	quotient = dividend/divisor
	print(dividend, '/', divisor, '=', quotient)
print('Program Finished')

