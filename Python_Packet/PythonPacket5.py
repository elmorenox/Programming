einstenNum = 1089 #write 1089 on a paper and fold it 

userNum = raw_input("Input a three-digit number. \n First and last number must differ by 2:\n ")

while (abs( (int(userNum[0]) - int(userNum[2])) ) < 1 ) or ( len( userNum) != 3 ):

	print "Input must be a three-digit number and first and last number must differ by 2."
	userNum = raw_input()

userNumList = list(userNum)

userNumList.reverse()

userNumReversedStr = "".join(userNumList)

print "User number: %s" %userNum
print "User number reversed is: %s" %userNumReversedStr

userNumInt = int(userNum)

userNumReversedInt = int(userNumReversedStr)

if userNumInt > userNumReversedInt:
	diffInt = (userNumInt - userNumReversedInt)
elif userNumReversedInt > userNumInt: 
	diffInt = (userNumReversedInt - userNumInt)

print "Difference between entered num and num reversed is: %s" %(diffInt)

diffStr = str(diffInt)

diffList = list(diffStr)

diffList.reverse()

sumReversedStr = "".join(diffList)

sumReversedInt = int(sumReversedStr)

print "Reverse of difference is: %s" %sumReversedStr

print "Sum of the diff and the rev diff is: %s" %(diffInt + sumReversedInt)