
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

while priceInput != "q": 

	#This is my check to see if it's divisible by .05 and positive. 
	if float(priceInput)*100 % 5 != 0 or float(priceInput) < 0: 
		print "Illegal price: Must be a non-negative multiple of 5 cents."
	else: 
		print ("Accepted form of payment:")
		print ("'N' for Nickels")
		print ("'D' for Dimes")
		print ("'Q' for Quarters")
		print ("'O' for $1 bill")
		print ("'F' for $5 bill")
		print ("'c' to cancel purchase")

	priceFloat = float(priceInput)
	amountDue = priceFloat
	paymentCompiled = 0

	while amountDue >= 0:

		print "Amount due %s" %(amountDue)
		paymentProvided = raw_input("Choose coinage and bills: ").upper()

		if paymentProvided == "N":
			amountDue = amountDue - 0.05 
			NinMachine = NinMachine + 1
			paymentCompiled = paymentCompiled + 0.05
		elif paymentProvided == "D": 
			amountDue = amountDue - 0.10
			DinMachine = DinMachine + 1
			paymentCompiled = paymentCompiled + 0.10
		elif paymentProvided == "Q":
			amountDue = amountDue - 0.25
			QinMachine = QinMachine + 1
			paymentCompiled = paymentCompiled + 0.25
		elif paymentProvided == "O":
			amountDue = amountDue - 1.00
			OinMachine = OinMachine + 1
			paymentCompiled = paymentCompiled + 1.00
		elif paymentProvided == "F":
			amountDue = amountDue - 5.00
			FinMachine = FinMachine + 1
			paymentCompiled = paymentCompiled + 5.00
		elif paymentProvided != "N" and paymentProvided != "D" and paymentProvided != "Q" and paymentProvided != "O" and paymentProvided != "F" and paymentProvided != "C":
			print "Must be accepted form of payment"
		elif paymentProvided == "C":
			paymentCompiled = paymentCompiled
			print "Transaction canceled"
			break

	if paymentProvided == "C":
		changeDue = paymentCompiled
	else:
		changeDue = paymentCompiled - priceFloat

	if changeDue == 0:
		print "No change"
	else:  
		print "This is change due %s" %changeDue 

	totalCoinage = ((N * NinMachine) + (D * DinMachine) + (Q * QinMachine ))

	#not the greedy algorithm	
	#remaingingChange = changeDue

	changeInQ = 0 
	changeInD = 0
	changeInN = 0 

	#remaingingChange = changeDue

	while changeDue > 0:

		if changeDue >= 0.25 and QinMachine > 0:
			changeDue = changeDue - 0.25
			changeInQ = changeInQ + 1  
			QinMachine = QinMachine - 1
			#remaingingChange = changeDue
		elif changeDue >= 0.10 and DinMachine > 0:  
			changeDue = changeDue - 0.10
			changeInQ = changeInQ + 1  
			QinMachine = QinMachine - 1
			#remaingingChange = changeDue
		elif changeDue >= 0.05 and NinMachine > 0: 
			changeDue = changeDue - 0.05
			changeInQ = changeInQ + 1  
			QinMachine = QinMachine - 1
			#remaingingChange = changeDue
		else: 
			break
		
	print "Please take your change below: "
	if changeInQ > 0: 
		print "%s Quarters" %(changeInQ)
	elif changeInD > 0:
		print "%s Dimes" %(changeInD)
	elif changeInN > 0: 
		print "%s Nickles" %(changeInN)
	if changeDue < 0: 
		print ("See clerk for remaining change: %s") %changeDue

	print "STOCK"
	print "%s Nickles in Machine" %(NinMachine)
	print "%s Dimes in Machine" %(DinMachine)
	print "%s Quarters in Machine" %(QinMachine)
	print "%s Dollars in Machine" %(OinMachine)
	print "%s Fives in Machine" %(FinMachine)

	totalMoney = ((N * NinMachine) + (D * DinMachine) + (Q * QinMachine ) + (O * OinMachine ) + (F * FinMachine))

	print "%s in total cash" %(totalMoney)

	priceInput = raw_input("Please enter the price of your purchase in the form of xx.xx.\n Press q to quit:")	

print "Transaction quit"
