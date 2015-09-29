print "Welcome to The Old number 115. "

birthMonth = int(raw_input("What is your birth month(no. 1-12)?: "))
inputAge = int(raw_input("What is your age?"))

specialNum = (((((birthMonth * 2) + 5) * 50) + inputAge) - 365)

secretNum = specialNum + 115

secretNum = str(secretNum)

strSize = int(len(secretNum))

#below is using the strSize not the birthMonth input altough it'd be easier to just output the inputs of both birth mo number and age

if strSize == 3: 
	birthNum = secretNum[:1]
	outputAge = secretNum[1:3]

if strSize == 4:
	birthNum = secretNum[:2]
	outputAge = secretNum[2:4]

monthList = ["Jan" , "Feb", "March" , "April" , "May" , "Jun" , "July" , "August" , "Sep" , "Oct" , "Nov" , "Dec"]

print "Your birth month is %s and your age is %s" %(monthList[(int(birthNum) - 1)] , outputAge)