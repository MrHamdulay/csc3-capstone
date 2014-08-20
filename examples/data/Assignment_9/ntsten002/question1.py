#Tendani Netshitenzhe
#question1
#16May2014

#Import from math module
from math import *

#Ask the user for the name of the textfile
filename = input("Enter the marks filename:\n")

#Read from the textfile
marks_file = open(filename, "r")
lines = marks_file.readlines()

#Close File
marks_file.close()

#Create empty lists for the names and corresponding marks
marks = []
names = []

length = len(lines)

#Read the names and marks into their respective lists
for k in range(length):
    position = lines[k].find(",")
    marks.append(int(lines[k][position+1:]))
    names.append(lines[k][:position])
    
addition = 0

#Add all the marks together
for k in range(length):
    addition += marks[k]

#Get the average of the marks
average = addition/length

SD=0

#Get the standard deviation of the marks entered
for k in range(length):
    SD += (marks[k] - average)**2
    
SD = sqrt(SD/length)

#Display the average and std deviation
print("The average is:", "%.2f" % average)
print("The std deviation is:", "%.2f" % SD)

SA =[]
#Display whoever is below the first standard deviation below the mean
for k in range(length):
    if marks[k] < average-SD:
        SA.append(names[k])
        
if len(SA) != 0:
    print("List of students who need to see an advisor:")
    for k in range(len(SA)):
        print(SA[k])