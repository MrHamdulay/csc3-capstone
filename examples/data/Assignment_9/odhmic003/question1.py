"""Michael Odhiambo
ODHMIC003
Assignment 9_Question 1"""

import math
filename= input("Enter the marks filename:\n")#Prompt user for input
fob= open(filename,"r")#Open file to read contents
read= fob.readlines()
marks=[]
names=[]
average=[]
advisor=[]
d={}
"""Seperate marks and names from input and append them to seperate arrays"""
for i in read:
    j= i.rstrip("\n")
    
    if j[-2].isdigit()==True:
        mark= j[-2:]
        name= j[:-3]
    else:  
        mark= j[-1:]
        name= j[:-2]
    marks.append(mark)
    names.append(name)
"""Add marks and names to a dictionary"""
for i in range(len(marks)):
    d[names[i]] = marks[i]
sum= 0
"""Sum marks to be used in calculation of average and standard deviation"""
for i in marks:
    if len(marks)>1:
        sum= sum + eval(i)
    elif len(marks)==1:
        sum= eval(i)
average= round(sum/(len(marks)),2)
x= '{0:.2f}'.format(average)
sd_num=0
"""Calculation of standard deviation"""
for i in marks:
    sd_num= sd_num + (eval(i)-average)**2
sd= math.sqrt(sd_num/len(marks))
y= '{0:.2f}'.format(sd)
print("The average is:",x)
print("The std deviation is:",y)
"""Search for students in need of visiting the student advisor"""
for i in marks:
    if eval(i)<(average-sd):
        advisor.append(i)
if len(advisor)>0:
    print("List of students who need to see an advisor:")
#for i in d:
#    if eval(d[i])<(average-sd):
#        print(i)
for i in marks:
    if eval(i)<(average-sd):
        x= marks.index(i)
        print(names[x])
    
        
    
    
    
    