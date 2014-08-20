#This Python Python program analyses student marks read in from a file and 
#determine which students need to see a student advisor. 
#The students who (hypothetically!) need to see a student advisor are those 
#with marks less than one standard deviation below the mean.

#The marks file is composed of lines of text, where each line contains 
#a student number and mark separated by a comma.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 11 May 2014

import math

name = input("Enter the marks filename:\n")

f = open(name,"r") # Open the file
content = f.readlines() # Store the contents of the file in a list
f.close() # Close the file

grade = [] #store marks
stdname = []#store student names
total = 0
sqrtotal = 0

# Isolate the marks and names from the file
for i in range(len(content)):    
    grade.append(int(content[i][content[i].find(",")+1:-1]))
    stdname.append(content[i][:content[i].find(",")])
    total += grade[i] # calculate total marks

# calculate the average
avg = total/len(grade)
print("The average is: {average:0.2f}".format(average=avg))

# Calculate the standard deviation
for mark in grade:
    sqrtotal += (mark - avg)**2
stddev = math.sqrt(sqrtotal/len(grade))
print("The std deviation is: {dev:0.2f}".format(dev=stddev))

# Print names of students with marks less than one standard deviation of the mean
if len(grade) > 1:
    print("List of students who need to see an advisor:")
    pos = 0
    for j in grade:    
        if j < (avg - stddev):
            print(stdname[pos])
        pos += 1

#Sample File (test1.txt)

#Alan,35
#Siobhan,23
#Mmberengeni,38

#Sample I/O

#Enter the marks filename:
#test1.txt
#The average is: 32.00
#The std deviation is: 6.48
#List of students who need to see an advisor:
#Siobhan