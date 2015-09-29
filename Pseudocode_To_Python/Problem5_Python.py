# write a program that reads three numbers then displays the largest
highNum=0
num1 = input( "Input the first of three numbers: ")
num2 = input( "Input the second of three numbers: ")
num3 = input( "Input the last of three numbers: ")

if num1 > num2:
	highNum = num1
else: 
	highNum = num2

if highNum > num3:
	print highNum
else: 
	print num3
