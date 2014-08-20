"""
Analyse marks from a file
Keyoolin Padayachee
13 May 2014
"""

import math
# Reads the data from a file
file = input("Enter the marks filename:\n")
marks = open (file, "r")
lines = marks.readlines()
marks.close()
average = 0
length = len(lines)
#Modifies the data to a format which is more practical to work with
for i in range(length):
    lines[i] = lines[i].split(",")
    if i < length-1:
        lines[i][1] = lines[i][1][:-1]
        
    lines[i][1] = eval(lines[i][1])
    average = average + lines[i][1]
#calculates the average    
average = average/length
stddeviation = 0
# calculates the standard deviation
for i in range(length):
    stddeviation = stddeviation + (lines[i][1] - average)**2
stddeviation = math.sqrt(stddeviation/length)
#prints the data that was calculated
print("The average is:", "{0:5.2f}".format(average))
print("The std deviation is: "+ "{0:4.2f}".format(stddeviation))
#prints of the students who need to see an advisor
printed = 0
for i in range(length):
    if (average-lines[i][1]) > stddeviation:
        if printed == 0:
            print("List of students who need to see an advisor:")
            printed = 1
        print(lines[i][0])