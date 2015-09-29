#Get debt value 
#Get currency denomination 
#Print height of debt in chosen currency denomination 
#Print distance in miles translated to a multiple of the average distance to the Earth's moon. 

debt_num = float(raw_input("What is the current debt?: "))
currency_num = float(raw_input("What is the currency?:  "))

#avg distance to moon = 238857
# 1in = 0.0000157828mi 
# thickness of denominiation = 0.0043in
# 1mi = 63360in

height_inch = 0.0043 * (debt_num / currency_num)

# Conversion of inch to miles 

height_num = height_inch / 63360

if debt_num != 0 and currency_num == 1 or currency_num == 5 or currency_num == 10 or currency_num == 20 or currency_num == 50 or currency_num == 100:
	print "The debt of" , debt_num , "has a height in miles of" , currency_num , "dollar bills," , height_num , "That's" , height_num/238857 , "times the average distance from the earth to the moon."
else: 
	print "Must be a 1,5,10,20,50, or 100 currency."