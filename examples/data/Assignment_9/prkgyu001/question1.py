"""Assignment 9 Question 1
Gyu Park
16/05/2014"""

import math
def ave (marks):
    count=0
    for i in range(len(marks)):
        count= count + int(marks[i])
    
    
    average = count/len(marks)
    
    return average
    
def stan_dev (marks):
    N = len(marks)
    mean = ave(marks)
    standar=0
    
    for mark in marks:
        standar= standar + (int(mark) - mean)**2
    standar= math.sqrt(standar/N)
    
    return standar

def opnfunc (x):
    
    f = open(x,"r")
    lines = f.readlines() 
    f.close()

    for i in range (len(lines)):
        lines[i] = lines[i][:-1]
        
    marks = []
    for i in range(len(lines)):
        if lines!= " ":
            a=lines[i].split(",")
            marks.append(a[1])
       
    names = []
    
    for i  in range(len(lines)):
        if lines!= " ":
            a=lines[i].split(",")
            names.append(a[0])
        
    mean = ave(marks)
    standard_dev = stan_dev(marks)
    print("The average is:", "{:.2f}".format(mean))
    print("The std deviation is:","{:.2f}".format(standard_dev))
    
    names1 = []
    
    for i in range(len(marks)):
        if int(marks[i]) < mean-standard_dev:
            names1.append(names[i])
            
    if len(names1) != 0:
        print("List of students who need to see an advisor:\n",("\n").join(names1), sep="")
            
            

x=input("Enter the marks filename:\n")
opnfunc(x)
