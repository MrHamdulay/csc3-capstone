"""11/05/2014 RFFADA002 Adam Ruff
Assignment 9 Question 1
Read from marks file to determine which students need to see a student advisor (those lower than 1 std dev below the mean)"""

import math

file = input("Enter the marks filename:\n")
names = []
marks = []
sum = 0
num = 0

#create list of lines from marks file
f = open(file, 'r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    
for i in range(len(lines)):
    names.append(lines[i][0])
    marks.append(lines[i][1])
    
marks[len(marks)-1] = marks[len(marks)-1]+"\n"
    
for i in range(len(marks)):
    marks[i] = int(marks[i][:-1])
    
for i in range(len(marks)):
    sum += marks[i]
mean = round(sum/len(marks),2)

for i in range(len(marks)):
    num += (marks[i] - mean)**2

stddev = round(math.sqrt(num/len(marks)),2)
    
print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % stddev)

risk = mean - stddev

for i in range(len(marks)):
    if marks[i] < risk:
        print("List of students who need to see an advisor:")
        break
    
for i in range(len(marks)):
    if marks[i] < risk:
        print(names[i])