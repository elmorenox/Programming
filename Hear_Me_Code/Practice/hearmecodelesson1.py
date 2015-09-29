print """Lesson \t Topic \n 1 \t String \n 2 \t Lists and loops \n 3 \t Dictionaries and files"""

twitter = "@hearmecode"

print len(twitter)

print twitter[1:5]

phone = "(202) 456-7890"

print phone[1:4]

name = "Shannon"
age = 29 
print "My name is: {0} and my age is: {1}" .format(name, age)

phone = "202-555-6789"
print "Call {0} for great pizza".format(phone[4:])

tweet = """In just over one year, @hearmecode has reached over 800 members who arelearning how to code together."""

print """That tweet is {0} characters.
You have {1} characters left.""".format(len(tweet), 140-len(tweet))

phone = "202-555-9876"
print "Area code: {0}".format(phone[0:3])
print "Local area: {0}".format(phone[4:])

position = phone.find("0(1")
print position
#print "Different format: ".format(phone)

email = "shannon@hearmecode.com"
print email.find("@")

print email.find("Z")

twitter = "@hearmecode"
twitter.replace("@" ,"#")

print twitter

twitter = twitter.replace("@" , "#")

print twitter

length = len(tweet)
#tweet: the string to measure
#len(): function that finds the length
#length:a new variable, the length is stored here

position = phone.find("(")
#.find("("): look for a left parenthesis in the variable phone
# phone:  a string containig a phone number
#position: a new variable, the position is stored here

address = "                    1600 Pennsylvania Avenue    "
print address.strip()

gender = "F"

print gender 

print gender.lower()

article = """ At Hear Me Code, students are teachers in training. 
The key to classes' appeal, said Criqui, who is now an assistant 
teacher at hear me code? "It's by women, for women," she said..."""

print article.count(" he said")
print article.count(" she said")
