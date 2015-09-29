numCount = input("How many numbers will you be entering? ") 
sumNum = 0
for x in range(0,numCount):
	inputNum = input("Please enter a number: ")
	sumNum = sumNum + inputNum

numAvg = sumNum/numCount
print "The average is", numAvg



	