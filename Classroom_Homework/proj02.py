# Get number of years into the future
# Ouput population at input years
# 31556000 seconds in a year
# 1 birth per 7 seconds
# 1 death per 13 seconds
# 321,386,917 today 

input_year = float(raw_input("How many years?: "))

birth_pop = ((input_year*31536000)/7) 

death_pop = ((input_year*31536000)/13) 

change_pop = birth_pop - death_pop

output_pop = change_pop + 321386917

print "New poplation in %s years will by %s to be %s" %(input_year, change_pop, output_pop)