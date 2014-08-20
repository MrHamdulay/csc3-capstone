#Jason Smythe
#assignment 9
#question 1


import math

def openRead():
	#get the desired file and read its contents-
	fileName = input("Enter the marks filename:\n")
	marksFile = open (fileName, "r")
	lines = marksFile.readlines ()
	marksFile.close ()
	#process the list element by element to make it easier to understand
	for i in range (len (lines)):
		#this removes the "\n" from the end of each line
		lines[i] = lines[i][:-1]
		#splits the data into an two column table, name and grade
		fields = lines[i].split (',')
		lines[i] = fields
	return lines

def processData(data):
	total = 0
	totalDevience = 0
	number = len(data)
	deviences = []
	#sums a total of these numbers
	for student in data:
		total += int(student[1])
	average = total/number
	#calculates ((xi -µ)^2) for each element in data
	for student in data:
		deviences.append((int(student[1])-average)**2)
	#sums the total of the deviences
	for devience in deviences:
		totalDevience += devience
	stdDeviation = math.sqrt(totalDevience/number)
	return average, stdDeviation

#function goes through the list and prints out all the students who are 'not making the grade'
def advisorNeeded(data, ave, stdD):
	benchmark = ave - stdD
	helpList = ""
	for student in data:
		if int(student[1]) < benchmark:
			helpList += "\n" + student[0]
	if helpList != "":
		print("List of students who need to see an advisor:" + helpList)

def main():
	dataRaw = openRead()
	average, stdDev = processData(dataRaw)
	print("The average is: {0:.2f}".format(average))
	print("The std deviation is: {0:.2f}".format(stdDev))
	advisorNeeded(dataRaw, average, stdDev)
	
main()


"""
Sample File (test1.txt)

Alan,35
Siobhan,23
Mmberengeni,38

Sample I/O

Enter the marks filename:
test1.txt
The average is: 32.00
The std deviation is: 6.48
List of students who need to see an advisor:
Siobhan
"""
