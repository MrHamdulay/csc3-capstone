#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014 - 05 -15
#Function       : Looks for students at risk
#Title          : Question

from math import *

filename = input("Enter the marks filename:\n")

marks_file = open(filename, "r")
marks = marks_file.readlines()
marks_file.close()


#removes end_line character
for i in range(len(marks)):
    if marks[-1] == "\n":
        #puts the mark and the student in a list 2d list
        #student names are at index position 0 and marks at 1 of the second list
        marks[i] = marks[i][:-1].split(",")
    else:
        marks[i] = marks[i].split(",")

average = 0
standard_d = 0
#calculates the average by dividing the sum by the number of students
for i in range(len(marks)):
    average += int(marks[i][1])
average /= len(marks)
#finds the standard deviation
for i in range(len(marks)):
    standard_d += (int(marks[i][1]) - average)**2
    
standard_d = sqrt(standard_d / len(marks))

below_sd = []
print("The average is:", "{0:.2f}".format(average))
print("The std deviation is:", "{0:.2f}".format(standard_d))

#finds the students who are one standard deviation or more below the mean
for i in range(len(marks)):
    if int(marks[i][1]) < (average - standard_d):
        below_sd.append(marks[i][0])

if not len(below_sd) < 1:
    print("List of students who need to see an advisor:")
for students in below_sd:
    print(students)
