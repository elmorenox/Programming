birthMonth = input("Please enter your birth month in number format: ")
while birthMonth < 1 or birthMonth > 12:
	birthMonth = input("Please enter a valid birth month: ")

age = input("Please input your age: ")
while age < 1 or age > 99:
 if age > 99: 
 	print "Sorry this trick only works up to 100."
 	break
 if age < 1:
 	print "Sorry, but this trick isn't for babies"
 age = input("If you would like to play, Please pick a new age: ")


specialNumber = (((birthMonth*2)+5)*50) + age - 365
specialTrick = specialNumber + 115

specialTrick = str(specialTrick)
stSize = int(len(specialTrick))

if stSize == 3: 
	birthMonthNumber = specialTrick[:1]
	ageNumber = specialTrick[1:3]

	print birthMonthNumber
	print ageNumber

if stSize == 4: 
	birthMonthNumber = specialTrick[:2]
	ageNumber = specialTrick[2:4] 

	print birthMonthNumber
	print ageNumber

monthList = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print "Your birth month is %s" %monthList[(int(birthMonthNumber) - 1)]











