#a Python program to analyse student marks read in from a file and determine which students need to see a student advisor
#sankara mallane
#11 may 2014

import math

infileName = input("Enter the marks filename:\n")
infile = open(infileName,"r")
file = infile.readlines()

names = []
marks = []
for line in file:
    y = line.split(",")
    names.append(y[0])
    marks.append(eval(y[1]))

sum = 0
for mark in marks:
    sum += mark
average = (sum)/(len(marks))

dev = 0
for mark in marks:
    dev += (average - mark)**2    
stdDev = math.sqrt((dev)/(len(marks)))

print("The average is: {0:0.2f}".format(average))     
print("The std deviation is: {0:0.2f}".format(stdDev))

notPrinted = True

for i in range(len(marks)):
    if marks[i] <  average - stdDev:
        if notPrinted:
            print("List of students who need to see an advisor:")
            notPrinted=  False
            
        print(names[i])