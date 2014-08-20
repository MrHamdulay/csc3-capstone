"""analyse student marks
Michelle Lu
10 May 2014"""

import math


def average(marks): #finds the average of the marks
    avg=0
    for i in range(len(marks)):
        avg+=int(marks[i])
    avg=avg/len(marks) 
    return avg

    
def stddev(marks): #finds the standard deviation
    N = len(marks)
    mean= average(marks)
    std=0
    for mark in marks:
        std = std + (int(mark) - mean) ** 2
    std = math.sqrt(std / N)     
    return std 
    
        

def getinfo(filename):
    f = open (filename, "r") 
    lines=f.readlines()
    f.close()
    
    for i in range (len (lines)): #cuts of the last character(\n)
        lines[i] = lines[i][:-1]
    
    marks=[]
    names=[]

    for line in lines:
        for j in range(len(line)):
            if line[j]==",":
                names.append(line[:j])     #adds all the names to one list
                marks.append(line[j+1:])   #adds all the marks to one list

    mean=average(marks)
    std=stddev(marks)
    print("The average is:","{:.2f}".format(mean))
    print("The std deviation is:", "{:.2f}".format(std))
    
    name=""
    
    for k in range(len(marks)):
        if int(marks[k])<mean-std: #if the marks are one stdev less than the mean
            name+=names[k]+ "\n"   #gives a string of names separated by a new line
    
    
    if name!="":
        print("List of students who need to see an advisor:\n", name, sep="")
        
    




filename=input("Enter the marks filename:\n")
getinfo(filename)

     
   