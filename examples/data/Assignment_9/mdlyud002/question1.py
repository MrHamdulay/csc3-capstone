# Yudhi Moodley
# Assignment 9- question 1
# 16/05/2014

import math

# mean calculator
def average(marks): 
    avg=0
    
    for i in range(len(marks)):
        avg+=int(marks[i])
    avg=avg/len(marks) 
    
    return avg

# standard deviation calculator
def stddev(marks): 
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
                #adds all the names to one list
                names.append(line[:j])
                #adds all the marks to one list
                marks.append(line[j+1:])   
    
    mean=average(marks)
    std=stddev(marks)
    print("The average is:","{:.2f}".format(mean))
    print("The std deviation is:", "{:.2f}".format(std))
    
    name=""
    
    for k in range(len(marks)):
        
        #if the marks are one stdev less than the mean
        if int(marks[k])<mean-std:
            
            #gives a string of names separated by a new line
            name+=names[k]+ "\n"   
    
    
    if name!="":
        print("List of students who need to see an advisor:\n", name, sep="")
        
    




filename=input("Enter the marks filename:\n")
getinfo(filename)

     
   