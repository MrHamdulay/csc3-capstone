"""2014-05-13
Assignment 9: question 1 
Program to find list of students with marks lower than one standard deviation below the mean
MCKAIL001 Ailsa Mackay"""

import math

filename = input("Enter the marks filename:\n")
f = open (filename, "r")
lines = f.readlines ()
f.close ()

marks = []  #create list of marks only. ie separate names from marks
for i in lines:
    if i.isdigit():
        marks.append(eval(i))
    else:
        continue
    
names = [] #create list of names only. ie separate marks from names
for i in lines:
    if i.isalpha():
        names.append(i)

if len(names) > 0:
    mean = "%.2f"%round(sum(marks)/len(names),2)

#now calculate standard deviation
totalA = 0 #initialise counter
for i in marks:
    Num = int(i)
    A = (Num-float(mean))*(Num-float(mean))
    totalA = totalA+A

underRoot= totalA/len(names)
standard_dev = "%.2f"%round(math.sqrt(underRoot),2)

print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % standard_dev)
print("List of students who need to see an advisor:")

for i in range(len(marks)): #calculate the indices of the marks which are lower than one standard deviation below the mean
    if marks[i] < mean - standard_dev:
        print(names[i]) #print the names with the corresponding index
