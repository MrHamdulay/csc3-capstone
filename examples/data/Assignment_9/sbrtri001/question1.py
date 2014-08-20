''' Assignment 9, question 1
Analyse student marks read in from a text file
Tristan Subroyen
10 May 2014 '''

import math
# open the file:
filename = input("Enter the marks filename:\n")
file = open(filename, "r")
lines = [line.strip() for line in open(filename)]

marks = [] # list to hold marks
# read each mark into the list marks
for i in range (len(lines)):
    index = lines[i].index(",")
    end = len(lines[i])
    marks.append(lines[i][index+1:end])

names = []
# read in each student name into the list names
for i in range (len(lines)):
    index = lines[i].index(",")
    names.append(lines[i][0:index])
    
# find the mean:
total = 0
for i in range (len(marks)):
    total += int(marks[i])
mean = round((total/(len(marks))),2)

# find the standard deviation:
total_sum = 0
for i in range (len(marks)):
    total_sum += (int(marks[i]) - mean)**2
under_root = (total_sum*1.0) / len(marks)
stdDev = round(math.sqrt(under_root),2)


# determine which students need to see a student advisor:
students = []
for i in range (len(marks)):
    oneStd = mean - stdDev
    if int(marks[i]) < oneStd:
        students.append(names[i])

# Display output:
print("The average is:","%.2f" % mean)
print("The std deviation is:","%.2f" % stdDev)
if len(students) > 0:
    print("List of students who need to see an advisor:")
    for i in range (len(students)):
        print(students[i])
        

