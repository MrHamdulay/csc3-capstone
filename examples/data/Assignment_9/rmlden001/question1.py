#Denisha_Ramaloo

import math
def averagemark (marks):
    count=0
    for i in range(len(marks)):
        count= count + int(marks[i])
    
    
    average = count/len(marks)
    
    return average
    
def standard_deviation (marks):
    N = len(marks)
    mean = averagemark(marks)
    standardd=0
    
    for mark in marks:
        standardd= standardd + (int(mark) - mean)**2
    standardd= math.sqrt(standardd/N)
    
    return standardd

def open_function(x):
    
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
        
    mean = averagemark(marks)
    standarddeviation = standard_deviation(marks)
    print("The average is:", "{:.2f}".format(mean))
    print("The std deviation is:","{:.2f}".format(standarddeviation))
    
    names1 = []
    
    for i in range(len(marks)):
        if int(marks[i]) < mean-standarddeviation:
            names1.append(names[i])
            
    if len(names1) != 0:
        print("List of students who need to see an advisor:\n",("\n").join(names1), sep="")
            
            

x=input("Enter the marks filename:\n")
open_function(x)
