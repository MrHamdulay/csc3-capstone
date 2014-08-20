"""A program that analyses a file with marks and determines which student need to see an adviser
Tafadzwa Moyo
11 May 2014"""

import math

#Gets input
fname=input("Enter the marks filename:\n")
f=open(fname, "r")
lines=f.readlines()
f.close()
marks=0 

#process lines
for i in range(len(lines)):
    lines[i]=lines[i].split(",")#splits lines in names and marks
    if lines[i][1].find("\n")>-1:
        lines[i][1]=eval(lines[i][1][:lines[i][1].find("\n")]) #converts marks from string to numbers
    else:
        lines[i][1]=eval(lines[i][1])
    marks+=lines[i][1]

mean=round(marks/(i+1), 2)

x=0 
#gets the sum of the squeared differences between te mean and individual values
for i in range(len(lines)):
    x+=(lines[i][1]-mean)**2

dev=round(math.sqrt(x/(i+1)), 2)

#makes sure the output is 2 demical places
d0=str(mean).rfind(".")
if str(mean)[d0]!=str(mean)[-3]:
    mean=str(mean)+"0"
d1=str(dev).rfind(".")
if str(dev)[d1]!=str(dev)[-3]:
    dev=str(dev)+"0"
    
#Prints standard deviation and mean
print("The average is:", mean)
print("The std deviation is:", dev)

#checks students that need to see adviser
list_stu=[]
x=0
for i in range(len(lines)):
    if lines[i][1]<eval(str(mean))-eval(str(dev)):
        list_stu.append(lines[i][0])
        x=1
if x:
    print("List of students who need to see an advisor:")
    for i in list_stu:
        print(i)