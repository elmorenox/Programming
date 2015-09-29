usrNum = int(raw_input("Enter a number: "))

usrMul = int(raw_input("Enter a multiple: "))
usrMul = usrMul + 1

for mul in range (1 , usrMul):
	print "%s * %s = %s" %(usrNum, mul, usrNum * mul) 
