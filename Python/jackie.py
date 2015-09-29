numstrNatDbtAmt = raw_input("Enter the current US national debt amount: ")
NatDbtAmt = float(numstrNatDbtAmt)
numstrBillDnm = raw_input("Enter a bill denomination: ")
BillDnm = float(numstrBillDnm)
ErthMnDst = 238857


MnyInch = NatDbtAmt/BillDnm * .0043
MlsDnm = MnyInch * .8333 * .0001893939
MltErthMnDst = MlsDnm/ErthMnDst


if BillDnm is 1 or 5 or 10 or 20 or 50 or 100 :
	print "The national debt amount of" , NatDbtAmt, "has a height in" , BillDnm, "'s as", MlsDnm, ". Wow! That is" , MltErthMnDst, " times the average distance from the earth to the moon!"