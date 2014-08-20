"""Assignment 9
Question 1
Barry Su
15 May 2014
Program to analyse student marks read in from a file"""

import math

#get name of file 
infile = input("Enter the marks filename:\n")

#open file in reading mode and get entire file into a list of strings, then close
f = open(infile, "r")
lines = f.readlines()
f.close()

#run through each line and remove newline chr
for i in range(len(lines)):
    lines[i] = lines[i][:-1]

#get marks from lines into a list
marks = []    
for i in range(len(lines)):
    entries = lines[i].split(",")
    marks.append(entries[1])

#using the mark list, calculate the mean mark
sum = 0.0
for num in marks:
    sum = sum + eval(num)
mean = sum/len(marks)

#calculate the standard deviation using the marks    
sumDevSq = 0.0
for num in marks:
    dev = eval(num) - mean
    sumDevSq = sumDevSq + dev**2
stdDev = math.sqrt(sumDevSq/(len(marks)))

#create a list of students whose marks are below one standard deviation of the mean
students = []
fail = mean - stdDev
for i in range(len(lines)):
    entries = lines[i].split(",")
    if eval(entries[1]) < fail:
        students.append(entries[0])

print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(stdDev))
if len(students) >0 :
    print("List of students who need to see an advisor:")
print("\n".join(students))