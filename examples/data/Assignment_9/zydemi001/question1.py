""" A program that analyzes the marks of students read in from a file and determines which students need to see a student advisor
Author: Emiel Zyde
Date: 10 May 2014 """

import math 

file = input("Enter the marks filename:\n")
f = open(file, "r")
lines = f.readlines()

f.close() 

#remove the new-line figure inserted at the end of all lines, except for the last one
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]

#split the lines into the student's name and his/her mark   
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    
#determine the average mark
count = 0
sum = 0
for i in range(len(lines)):
    sum = sum + int(lines[i][1])
    count = count + 1 
average = sum / count 
average2 = "{0:.2f}".format(average)
print("The average is:", average2 )

#determine the standard deviation
summation = 0
counter = 0
for i in range(len(lines)):
    num = int(lines[i][1]) - average
    summation = summation + (num ** 2)
    counter = counter + 1
var = summation / counter
var = math.sqrt(var)
var2 = "{0:.2f}".format(var)
print("The std deviation is:", var2)

under_stddeviation = average - var

#print out the list of students who need to go see a student advisor
list_students = []
for i in range(len(lines)):
    if int(lines[i][1]) < under_stddeviation:
        list_students.append(lines[i][0])

if list_students != []:
    print("List of students who need to see an advisor:")
    for student in list_students:
        print(student)