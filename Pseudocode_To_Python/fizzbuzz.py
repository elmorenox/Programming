input_Num = float(raw_input("Input a number: "))

if input_Num%3 == 0 and input_Num%5 == 0:
	print "FizzBuzz" , input_Num
elif input_Num%3 == 0:
	print "Fizz" , input_Num
elif input_Num%5 == 0: 
	print "Buzz" , input_Num
else:
	print input_Num