"""Write an algorithm that reads user input for a student's grade point average and SAT exam score,
 and uses these values to decide whether the student is admitted to the university.
  A GPA below 1.8 will cause the student to be rejected; 
  and a SAT score below 900 will also cause a rejection. Otherwise the student is accepted. 
  If both the GPA and the SAT score are too low, print the message about the GPA being too low.
  Accept input 
"""

GPA = float(raw_input("What is your GPA?: "))
SAT = float(raw_input("What is your SAT?: "))

if SAT >= 900 or GPA >= 1.8:
	print "Congratulations! You've been accepted. Click here for loans."
elif SAT < 900 
	print "Sorry your SAT is too low."
elif GPA < 1.8:
	print "Sorry your GPA is too low."
elif SAT < 900 and GPA < 1.8:
	print "Sorry, your GPA is too low."