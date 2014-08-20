# Assigment 9- question1.py
# BXTNAA002
# May 2014

import math #import math to do calculations
filename = input("Enter the marks filename:\n")
infile = open(filename, "r")

thesum = 0
marks= [] #create a list of marks
names = [] # create a list of names 
for line in infile:
    line = line.rstrip("\n")
    name, mark = line.split(",") # go through each line and spilt the name and respective mark
    thesum += eval(mark)
    marks.append(mark) # append name and corresponding mark to their respective lists at the same time so they have the same index
    names.append(name)

average = thesum/(len(marks)) #calculate the mean mark

sd = 0
for i in marks:
    sd += (eval(i)-average)**2

stand_dev = math.sqrt(sd/len(marks)) #calculate the standard deviation

print("The average is:","{0:.2f}".format(average)) #print the mean to two decimal places
print("The std deviation is:", "{0:.2f}".format(stand_dev)) #print the standard deviation to two decimal places

if stand_dev > 0:
    print("List of students who need to see an advisor:")

j= 0
for i in marks: #go through each mark in the list of marks and check if mark is 1 std dev below mean
    if eval(i) < (average-stand_dev):
        j = marks.index(i)
        print(names[j]) #if mark is 1 std dev below mean print name of corresponding mark
        
infile.close()