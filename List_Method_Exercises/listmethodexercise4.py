# Write a program that find and displays the most popular item in the list

testList = ["A" , "E" , "A" , "E" , "B" , "D" , "C" , "D" , "D" , "C" , "D" , "E" , "E" , "E"]


maxNum = 0 

for element in testList: 

	if testList.count(element) > maxNum:
		maxNum = testList.count(element)
		maxitem = element

print maxitem

""" I cheated off of this code i found on flowchart 
    max = 0
    maxitem = None
    for x in set(l):
        count =  l.count(x)
        if count > max:
            max = count
            maxitem = x
    return maxitem
"""