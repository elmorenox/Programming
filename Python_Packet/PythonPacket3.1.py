N = 0.05
D = 1.0 
Q = 0.25
O = 1.0
F = 5.0 

NinMachine = 25
DinMachine = 25
QinMachine = 25
OinMachine = 0 
FinMachine = 0

totalMoney = ((N * NinMachine) + (D * DinMachine) + (Q * QinMachine ) + (O * OinMachine ) + (F * FinMachine))

#while totalMone > 0 

print "Machine has %s Dimes, %s Nickels, %s Quarters, for a total %s of dollars." %(NinMachine, DinMachine, QinMachine)

if payment == "dimes"
	payment = D
	DinMachine = DinMachine + 1
	print DinMachine

if payment == "nickel"
	payment = N 
	NinMachine = NinMachine + 1
	print N_InMachine

if payment == "quarters"
	payment = Q
	QinMachine = QinMachine + 1
	print Q_InMachine

itemCost = int(input("Please enter cost of item: "))

paymentProvided = int(input("Pease enter payment provided: "))

changeDispensed = paymentProvided - itemCost


