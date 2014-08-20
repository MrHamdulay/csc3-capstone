#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     determines who needs to see a student advisor based on test
#              results stored in a file of the format <name>,<mark>\n
# Author:      Matthias
#
# Created:     11-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

file_name = input("Enter the marks filename: \n")
file_content = open(file_name, "r")
data = file_content.readlines()
file_content.close()

# append the marks in the line (without \n) in a new list
marks = []
for line in data:
    marks.append(line.split(",")[1][:2])

# calculate the average
avg = 0
for i in marks:
    avg += eval(i)
avg /= len(marks)

# calculate the standard deviation
stddev = 0
for i in marks:
    stddev += (eval(i)-avg) ** 2
stddev = math.sqrt(stddev/len(marks))

print("The average is: {0:0.2f}".format(avg))
print("The std deviation is: {0:0.2f}".format(stddev))

# determine who needs to see an advisor
# mark is lower than one standard deviation below the mean
fails = []
for line in data:
    line = line.split(",")
    if eval(line[1][:2]) < avg-stddev:
        fails.append(line[0])

if fails:
    print("List of students who need to see an advisor:")
    for i in fails:
        print(i)