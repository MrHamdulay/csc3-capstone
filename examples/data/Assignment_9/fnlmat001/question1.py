"""Program to analyse student marks from a file
Matthew Finlayson - FNLMAT001
11/05/2014"""

import math

file = input("Enter the marks filename:\n") 

f = open (file, "r")
totMarks = 0
numStudents = 0
line = f.readline()
while line != "": # while there is still more to be read
    arr =  line.split(",") # divides the line into the student num and mark
    totMarks += eval(arr[1]) # adds all the marks
    numStudents += 1 # counts how many lines (students) there are
    line = f.readline()
f.close()

mean = totMarks/numStudents

f = open(file,"r")
termsTot = 0 # used to calculate the std deviation
for i in range (numStudents):
    line = f.readline()
    arr = line.split(",")
    termsTot += math.pow((eval(arr[1]) - mean), 2) # (x-u)^2 
f.close()

stdDev = math.sqrt(termsTot/numStudents) 

print("The average is:", '{0:.2f}'.format(mean))
print("The std deviation is:", '{0:.2f}'.format(stdDev))


# code to determine which students have marks less than 1 std deviation below the mean
shouldPrint = False
f = open(file,"r")
for i in range (numStudents):
    line = f.readline()
    arr = line.split(",")
    if (eval(arr[1])< (mean - stdDev)): # if the student's mark is less than one std dev below the mean
        if (shouldPrint == False): # so that if there are no students to print then the heading isn't printed
            print("List of students who need to see an advisor:")
            shouldPrint = True
        print(arr[0])
f.close()