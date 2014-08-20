#Assignment 9
#Question 1 

import math
input_file = input("Enter the marks filename:\n")
infile = open(input_file, "r")
another = []

total_marks = 0
lines=0
advisor = []
y = 0

for line in infile:
    
    person = line.split(",")
    total_marks += eval(person[1])
    another.append(eval(person[1]))
    lines += 1
average = total_marks/lines

infile.close()
infile = open(input_file ,"r") 

for x in another :
    
    y = y + ((x - average)**2)

std_deviation = math.sqrt(y/lines)

for x in infile:
    person = x.split(",")
    if eval(person[1]) < (average-std_deviation):
        advisor.append(person[0])

average = "%.2f"%round(average,2)
std_deviation = "%.2f"%round(std_deviation,2)
print ("The average is:", average)
print ("The std deviation is:", std_deviation )

if not advisor:
    print("")
else:
    print("List of students who need to see an advisor:")
    for i in advisor:
        print(i)
