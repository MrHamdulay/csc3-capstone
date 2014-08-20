#Phumelele Ndimande 
#Assignment 9

import math


def calculation():
    
    filename = input("Enter the marks filename:\n")
    f= open(filename, "r")   
    
    #calculate the average
    marks=[]
    
    
    for lines in f:
        y=lines.split(",")
        mark=int(y[1])
        marks.append(int(mark))
   
    count=len(marks)
    summ=sum(marks)
   
    
    
    #average
    r='{0:0.2f}'
    average=round(summ//count,2)
    print("The average is:",r.format(average))
    
    #standard deviation
    total=0
    for j in marks:
            total+=((j-average)**2)
    r='{0:0.2f}'
    SD=round(math.sqrt(total/count),2)
    print("The std deviation is:", r.format(SD))   
    

    
    markbook={}
    names=[]
    f= open(filename, "r")
    
    for lines in f:
        x=lines.split(",")
        x[1]=int(x[1])
        markbook[x[0]]=x[1]
        
        
    for i in markbook:
        if markbook[i] < (average-SD):
            names.append(i)
    if names != []:
        
        print("List of students who need to see an advisor:")
        for i in names:
            print(i)
        
        
    
calculation()