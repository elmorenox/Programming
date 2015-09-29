myList = ['1' , '2' , '3']

print myList [1]

#Dictionaries
#Key is the name of the item. Key is the word.
#Value — what it is. Value is the definition. 

#myDictionary = {"Key":"Value" , "Key2":"Value2"}

#print myDictionary["key"]
#calling something from a dictionary can be in brackets 


myDictionary = {"apple":"A red fruit" , "key":True , "orange":1 , "list" : ['1','2', '3']

print myDictionary ["apple"]
print myDictionary ["apple"][0:1]
print myDictionary ["key"]
print myDictionary ["orange"]
print myDictionary ["list"][2]

myDictionary["new"] = "This is a new value"
print myDictionary["new"]

myDictionary["new"] = "New replaced string"
print ['new']

myDictionary['new'] = myList
print  myDictionary['new']


print myDictionary
