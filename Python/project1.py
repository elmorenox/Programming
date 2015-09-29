curr = input('Please enter a denomination of US Bill (i.e. $1, $5, $10, $20, $50, or $100 [only put the number, not the $]): ')
emDist = 238857
# This is the distance between the Earth & Moon in Miles
billIn = 0.0043
# This is the height of bills in inches
billMi = 0.0043 * 0.00001578
# This multiplies the height of bills in inches by the converion for inches to miles, to figure out the height of bills in miles
debtUS = 18159910413978.79
# This is the figure of the US Debt
numBill = debtUS/curr
# The number of bills necessary is the total debt, divided by the currency used
billHeight = numBill * billMi
# The number of bills times the thickness of a bill in miles is the total height of all the debt
moonTrip = billHeight/emDist
# The total height of the bills divided by the distance between the earth  & moon will tell us how many trips between the earth and moon are possible
print "The total debt of the United States in $%s bills is %s miles high! This means you could go to the moon and back %s times!" %(curr, billMi, moonTrip)