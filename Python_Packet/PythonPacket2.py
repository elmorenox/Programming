custCode = raw_input("What is the customer code?: ")

#how would i be able to to turn the customer code input into a number? 
# i tried if custCode = r then 1 = custCode ... 

while custCode == "r" or custCode == "c" or custCode == "i":

	startMeter = float(raw_input("What is the beginning meter reading?: "))
	endMeter = float(raw_input("What is the ending meter reading?: "))
	sumGallons = endMeter - startMeter

	if custCode == "r":
		resBill = 5.00 + (0.0005 * sumGallons)

	elif custCode == "c":
		if sumGallons < 4000000.00:
			resBill = 1000.00 
		else: 
			resBill = 1000.00 + (0.00025 + sumGallons)

	elif custCode == "i":
		if sumGallons < 4000000.00: 
			resBill = 1000.00
		elif sumGallons > 4000000.00 and sumGallons < 10000000.00:
			resBill = 2000.00
		elif sumGallons > 10000000.00:
			resBill = 2000.00 + (0.00025 + sumGallons)
	print custCode , startMeter , endMeter , sumGallons, resBill
	
	custCode = raw_input("What is the customer code?: ")

print "End"