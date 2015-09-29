NinMachine = 25 
DinMachine = 25 
QinMachine = 25
OinMachine = 0
FinMachine = 0 

N = 0.05
D = 0.10 
Q = 0.25
O = 1.0
F = 5.0 

print "There are:\n%s Nickels\n%s Dimes\n%s Quarters\n%s Ones\n%s Fives" %(NinMachine, DinMachine, QinMachine, OinMachine, FinMachine)

priceInput = raw_input("Please enter the price of your purchase in the form of xx.xx.\n Press q to quit: ")

priceFloat = float(priceInput)

if (priceFloat*100) % 5 != 0 or priceFloat < 0: 
	print raw_input("Please enter the price of your purchase in the form of xx.xx.\n Press q to quit: ")
	if priceInput == "q":
		print "End transaction"

while (priceFloat*100) % 5 == 0 and priceFloat > 0:

    #elif priceStr == "q"
    	#break

	print ("Accepted form of payment:")
	print ("'N' for Nickels")
	print ("'D' for Dimes")
	print ("'Q' for Quarters")
	print ("'O' for $1 bill")
	print ("'F' for $5 bill")
	print ("'c' to cancel purchase")

	while priceFloat > 0: 
		print "Amount due: %s dollars and %s cents" %(int(priceFloat), round((float(priceFloat) - int(priceFloat)) * 100))
		paymentProvided = raw_input("Choose coinage and bills:")
		'''
		if paymentProvided != "N" or paymentProvided != "D" or paymentProvided != "Q" or paymentProvided != "O" or paymentProvided != "F":
			print "Please choose accepted for of payment: "
		'''
		if paymentProvided == "N":
			priceFloat = priceFloat - N
			NinMachine = NinMachine + 1
		elif paymentProvided == "D":
			priceFloat = priceFloat - D
			DinMachine = DinMachine + 1
		elif paymentProvided == "Q":
			priceFloat = priceFloat - Q
			QinMachine = QinMachine + 1
		elif paymentProvided == "O":
			priceFloat = priceFloat - O
			OinMachine = OinMachine + 1
		elif paymentProvided == "F":
			priceFloat = priceFloat - F
			FinMachine = FinMachine + 1
		elif paymentProvided == "c":
			print "Purchase canceled. Plase take change."
		else: 
			print "Please choose accepted for of payment: "

	
	#priceInput = raw_input("Enter the purchase price (xx.xx) or 'q' to quit:")
	#priceFloat = float(priceInput)
	print "endwhile"

print "endwhile"

	

	