userNum = raw_input("Please input a 4 digit number: ")

while userNum != "q":
	numberLen = int(len(str(userNum)))

	addNumberLen = numberLen

	while addNumberLen != 1: 

		if addNumberLen == 4: 
			num1 = int(userNum[:1])
			num2 = int(userNum[1:2])
			num3 = int(userNum[2:3])
			num4 = int(userNum[3:4])
			newAddNum = (num1 + num2 + num3 + num4)
			print "The sum of it's digits %s + %s + %s + %s = %s" %(num1, num2, num3, num4, newAddNum)
			addNumberLen = int(len(str(newAddNum)))
			userNum = str(newAddNum)

		if addNumberLen == 3: 
			num1 = int(userNum[:1])
			num2 = int(userNum[1:2])
			num3 = int(userNum[2:3])
			newAddNum = (num1 + num2 + num3)
			print "The sum of it's digits %s + %s + %s = %s" %(num1, num2, num3, newAddNum)
			addNumberLen = int(len(str(newAddNum)))
			userNum = str(newAddNum)

		if addNumberLen == 2: 
			num1 = int(userNum[:1])
			num2 = int(userNum[1:2])
			newAddNum = (num1 + num2)
			print "The sum of it's digits %s + %s = %s" %(num1, num2, newAddNum)
			addNumberLen = int(len(str(newAddNum)))
			userNum = str(newAddNum)

		finalAddNum = newAddNum

	print "The additive root is %s" %finalAddNum

	print "\nOkay, now let's try multiplicative persistence."
	userNum = raw_input("Please input a 4 digit number: ")
	numberLen = int(len(str(userNum)))
	multiNumberLen = numberLen

	while multiNumberLen != 1: 

		if multiNumberLen == 4: 
			num1 = int(userNum[:1])
			num2 = int(userNum[1:2])
			num3 = int(userNum[2:3])
			num4 = int(userNum[3:4])
			newMultiNum = (num1 * num2 * num3 * num4)
			print newMultiNum
			multiNumberLen = int(len(str(newMultiNum)))
			userNum = str(newMultiNum)

		if multiNumberLen == 3: 
			num1 = int(userNum[:1])
			num2 = int(userNum[1:2])
			num3 = int(userNum[2:3])
			newMultiNum = (num1 * num2 * num3)
			print newMultiNum
			multiNumberLen = int(len(str(newMultiNum)))
			userNum = str(newMultiNum)

		if multiNumberLen == 2: 
			num1 = int(userNum[:1])
			num2 = int(userNum[1:2])
			newMultiNum = (num1 * num2)
			print newMultiNum
			multiNumberLen = int(len(str(newMultiNum)))
			userNum = str(newMultiNum)

		finalMultiNum = newMultiNum

	print "The multiplicative root is %s" %finalMultiNum
	userNum = raw_input("Please input a 4 digit number: ")
