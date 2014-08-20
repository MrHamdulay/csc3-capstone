### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 9 - Q1
### 11 / 05 /2014

## Uses
import math

## Live Code
sFile = input("Enter the marks filename:\n")
try: # Just some exception handeling for practise
	# input
	Database = []
	iStudents = 0 # Student Counter
	iAverage = 0 
	fFile = open(sFile,"r") # opens textfile
	for Line in fFile: # iterates through textfile line by line
		sName,sMark = (Line.strip()).split(",") #.strip() removes formatting characters
		aStudent = [sName,int(sMark)]
		iStudents += 1
		iAverage += int(sMark)
		Database.append(aStudent) # building database of data in memory
	fFile.close() # close textfile	
	iAverage = iAverage / iStudents
	print("The average is: {0:.2f}".format(iAverage))

	# Standard Deviation Calculation
	stdDev = 0
	for Student in range(iStudents):
		stdDev += (Database[Student][1] - iAverage)**2
	stdDev = math.sqrt(stdDev / iStudents)	
	print("The std deviation is: {0:.2f}".format(stdDev))

	# Student checking
	aOutput = [] # To store students who need help
	iSafePoint = iAverage - stdDev
	for Student in range(iStudents):
		if Database[Student][1] < iSafePoint:
			aOutput.append(Database[Student][0]) 
	if aOutput != []:
		print("List of students who need to see an advisor:")
		for Student in aOutput:
			print(Student)  

except IOError: # handles file not found error
	print("File count not be found")



