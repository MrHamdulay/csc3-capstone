"""Cherise Dube
14 May 2014
Program to analyse student marks read in from a file and determine which students need to see a student advisor."""

import math
filename=input("Enter the marks filename:\n")
f=open (filename,"r")

strings=f.readlines()
f.close()

marks={}
students=[] #Will later help to maintain the order of students inputted (i.e. if a name was put in first it will be printed out first)

#Creates a dictionary of students' names and marks 
for i in strings:
        marks[i[0:i.find(",")]]=i[i.find(",")+1:-1]
        students.append(i[0:i.find(",")])
        
        
        
    
#Finding the average
add=0
for i in marks.values():
        add+=eval(i)
    
average=add/len(marks.values())
average="%.2f"%average

#Finding the standard deviation
add=0
for i in (list(marks.values())):
        add+=((eval(i)-eval(average))**2)
    
std_dev=math.sqrt(add/len(marks.values()))    
std_dev="%.2f"%std_dev

#Finding out who needs to see a student advisor
cut_off=eval(average)-eval(std_dev)
low_marks=[] #students who need to see an advisor
for i in marks:
        if eval(marks[i])<cut_off:
                low_marks.append(i)
        else:
                pass
   
print("The average is:",average)
print("The std deviation is:",std_dev)
if len(low_marks)>0:
        print("List of students who need to see an advisor:")
        for i in students:
                if i in low_marks:
                        print(i)
        