# Exercise: PinLoop.py
'''
Write a program that gives the user only three tries 
to guess the correct pin of the account.

'''
pin = 1234

for tries in range(3):
	print "Please enter your PIN: "
	userPin = input()

	if userPin == pin:
		break

if userPin == pin:
	print "PIN ACCEPTED"
else: 
	print "YOU HAVE RUN OUT OF TRIES. YOUR ACCOUNT HAS BEEN LOCKED"