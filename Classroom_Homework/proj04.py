miles_per_hour = float(raw_input("How many miles per hour?: "))

meters_per_mile = 1609.34

barleycorns_per_mile = 117.647

hours_per_days = 0.04163923632

barley_per_day = ((miles_per_hour * meters_per_mile) * barleycorns_per_mile) / hours_per_days

#1 mi = 1760 yds , furlong = 220 yds , mi = 8 furlong fortnight = 2 weeks

hours_per_fortnight = 1.0/336.00 

furlong = miles_per_hour * 8.0

furlong_per_fortnight = furlong / hours_per_fortnight

#Mach = 1130/second 3600sec = 1 hr

feet = miles_per_hour * 5280

seconds_per_hour = 3600

mach = 1130/1.0

mach_number = (feet / seconds_per_hour) / mach

sl = 299792458 

psl = ((miles_per_hour * meters_per_mile) / seconds_per_hour) / sl 

print "Original speed in mph is %s" %(miles_per_hour)
print "Converted to barleycorn/day is: %s"  %(barley_per_day) 
print "Converted to frulongs/fornights: %s" %(furlong_per_fortnight)
print "Converted to Mach number is: %s" %(mach_number)
print "Converted to the percentage of the speed of light is: %s" %(psl)