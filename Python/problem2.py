custmerCode = raw_input("Please enter customers code (r,c,i): ")

while (custmerCode == 'c') or (custmerCode =='r') or (custmerCode == 'i'):
	startMeter = input("Please enter the beginning meter reading: ")
	endMeter = input("Please enter the end meter reading: ")
	gallonUsed = startMeter - endMeter

	if custmerCode == "c":
		if gallonUsed < 4000001:
			bill = (gallonUsed * 0.00025) + 1000.00
			print bill

	if custmerCode == "i":
		if gallonUsed < 4000001:
			bill = (gallonUsed * 0.00025) + 1000.00
			print bill
		elif gallonUsed > 4000001 and gallonUsed < 10000001:
			bill = (gallonUsed * 0.00025) + 20000
		elif gallonUsed > 10000001:
			exUsage = gallonUsed - 10000000
			bill = (gallonUsed * 0.00025) + 20000 + (exUsage * 0.00025)

	if custmerCode == "r":
		bill = (gallonUsed * 0.0005) + 5.00
		print bill

	custmerCode = raw_input("Please enter custmer code: ")

print "We're done"
