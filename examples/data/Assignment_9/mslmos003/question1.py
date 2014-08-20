#Rorisang Moseli
#Question 1
#Assignment 9
#May 2014
import math
test = input("Enter the marks filename:\n")
infile = open(test, "r")
other = []

totalmarks = 0
lines=0
advisor = []
x = 0

for line in infile:
    
    student = line.split(",")
    totalmarks += eval(student[1])
    other.append(eval(student[1]))
    lines += 1

average = totalmarks/lines

infile.close()
infile = open(test ,"r") 

for y in other :
    
    x = x + ((y - average)**2)

deviation = math.sqrt(x/lines)

for y in infile:
    student = y.split(",")
    if eval(student[1]) < (average-deviation):
        advisor.append(student[0])

average = "%.2f"%round(average,2)
deviation = "%.2f"%round(deviation,2)
print ("The average is:", average)
print ("The std deviation is:", deviation )

if not advisor:
    print("")
else:
    print("List of students who need to see an advisor:")
    for i in advisor:
        print(i)
