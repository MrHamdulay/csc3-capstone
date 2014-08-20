# Aaron Krishna
# 15 May 2014
# A program to analyse student marks read in from a file and determine which students need to see a student advisor

import math

filename = input("Enter the marks filename:\n")
f = open(filename, "r")
marks = f.readlines() #string array
f.close()

total = 0
standard = 0
average = 0
student_advisor = ""

for i in range(len(marks)):
    marks[i] = marks[i][:-1] #removes nextline character
    marks[i] = marks[i].split(",")
    total += int(marks[i][1]) 

average = total/len(marks)
print("The average is: {0:.2f}".format(average)) #two demical places

for k in range(len(marks)):
    standard += (int(marks[k][1]) - average) ** 2 #sum of the squares
    
standard = math.sqrt(standard/len(marks)) #deviation being standard
print("The std deviation is: {0:.2f}".format(standard))

for j in range(len(marks)):
    if int(marks[j][1]) < average - standard:
        student_advisor += marks[j][0] + " "

if student_advisor != "":
    print("List of students who need to see an advisor:")
    student_advisor = student_advisor[:-1].split(" ")
    for k in range(len(student_advisor)):
        print(student_advisor[k])