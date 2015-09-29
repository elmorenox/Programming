print ("Help! My computer doesn't work!")
while True:
	print ("Does the computer make any sounds (fans, etc.)")
	choice = input(" or show any lights? (Y/N): ")
	# The troubleshooting control logic
	if choice == 'n': # The computer does not have power
		choice = raw_input("Is it plugged in? (Y/N):")
		if choice == 'n': # It is not plugged in, plug it in
			print ("Plug it in")
		else: 
			choice = raw_input('Is the switch in the "ON" position?: ')
			if choice == 'n': # The switch is off, turn it on!
				print ("Turn it on")
			else: # The switch is on
				choice = input("Does the computer have a fuse? (Y/N): ")
				if choice == 'n': # No fuse
					choice = input('Is the outlet OK? (Y/N): ')
					if choice == 'n': # Fix outlet
						print "Check the outlet's circuit "
						print "breaker or fuse. Move to a"
						print "new outlet, if necessary. "
					else: # Beats me!
						print "Please consult a service technician."
						break # Nothing else I can do, exit the loop 
				else: 
					print "Check the fuse. Replace if "
					print 

