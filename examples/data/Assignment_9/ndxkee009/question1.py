"""Keegan Naidoo
NDXKEE009
10 May 2014
Program to find standard deviation and find out who needs to see a student advisor"""

import math

marks=[]
names=[]

file_name=input("Enter the marks filename:\n")                      #inputs filename and opens to read
f = open(file_name,"r")

lines = []                                                         #Creates an empty array

for line in f:               
    
    lines.append(line)                                             #Adds liness from text file to array
    
values = []

arr = []

for i in range(len(lines)):                                      #Takes out '/n' /newline from text file 
    
    if i != len(lines)-1:
        
        lines[i] = lines[i][:-1]
    
for line in lines:                                               #Splits it into a values variable (according to ',') 
    
    values = line.split(",")
    
    arr.append(values)

f.close

for i in range(len(arr)):                                        #Adds names to array 
    
    names.append((arr[i][0]))
    
for i in range(len(arr)):                                        #Adds marks to array
    
    marks.append(int(arr[i][1]))    
    
total=0
count=0

for i in marks:                                         #Calculates total marks
    
    total+=int(i)
    
    count+=1
    
average=total/len(marks)                             #Calculates average marks

totalstd=0

for i in marks:                                      #Calculates standard deviation
    
    totalstd+=(i-average)**2
    
std=round(math.sqrt(totalstd/count),2) 

stddown= average - std                               #Calculates standard deviation from mean(1 standard deviation of the mean)

print("The average is: %.2f" %(average))

print("The std deviation is: %.2f"%(std))

Ad=[]

for mark in range(len(marks)):                             #Finds out if a student needs to see a student advisor
    
    if marks[mark]<stddown:
        
        Ad.append(names[mark])
        
if len(Ad)>0:
    
    print("List of students who need to see an advisor:\n",end ="")
    
    for i in Ad:
        
        print(i)