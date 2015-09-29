debt_str = raw_input("Enter U.S. national debt in dollars here: ")
debt_float = float(debt_str)
denom_str = raw_input("What denomination of U.S. currency here: ")
denom_float = float(denom_str)
print 'The debt',debt_str,'has a height in miles of', denom_str,"'s of",(((debt_float/denom_float)*0.0043)/63360)

print 'That is',((((debt_float/denom_float)*0.0043)/63360)/238857),'times the average distance from the earth to the moon'