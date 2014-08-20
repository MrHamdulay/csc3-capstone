'''Question 1
Assignment 9
Tauriq Dolley

Reads a file and calculates a standard deviation based on marks and prints names of students one deviation below average'''

import math

file = input("Enter the marks filename:\n")
f = open(file, "r")
marks = []
names = []
total = 0
average = 0
numerator = 0
#print(f.read())

for line in f:
    line = line.split(",")
    line[1] = line[1][:(len(line))]
    marks.append(eval(line[1]))
    names.append(line[0])
    
f.close()
    
for i in range(len(marks)):
    total = marks[i] + total
    
average = total / len(marks)

print("The average is: ","{0:2.2f}".format(average),sep="")

for i in range(len(marks)):
    numerator = numerator + ((marks[i] - average)**2)
    
deviation = math.sqrt(numerator/(len(marks)))
print("The std deviation is: ","{0:2.2f}".format(deviation),sep="")

test = False
for i in range(len(names)):
    if average - deviation > marks[i]:
        test = True
        
if test == True:
    print("List of students who need to see an advisor:")
    for i in range(len(names)):
        if average - deviation > marks[i]:
            print(names[i])
        
    

    
    
    
