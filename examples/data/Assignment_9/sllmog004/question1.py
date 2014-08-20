"""Assignment 9 Question 1
Yaseen Sulliman 
11 May 2014"""

import math

mark=[]
advisor=[]
marks=[]
new_advisor=[]
file=input("Enter the marks filename:\n")
f=open(file,"r")

for line in f:
    mark.append(line)
f.close()
while "\n" in mark:
    mark.remove("\n") 
for student in range(len(mark)):                   
    if mark[student][-1:]=="\n":                   
        mark[student]=mark[student][:-1]
    
for individual in range(len(mark)):
    if mark[individual][-2:].isdigit():            
        newmark=eval(mark[individual][-2:])          
        marks.append(newmark)                              
    elif mark[individual][-1:].isdigit():         
        newmark=eval(mark[individual][-1:])
        marks.append(newmark)

add=0
dev=0
n=len(marks)
for a in marks:
    add+=int(a)
    average=round((add/n),2)
print("The average is:","{0:0.2f}".format(average))
for y in marks:
    dev+=(int(y)-average)**2
std=round((math.sqrt(dev/n)),2)
print("The std deviation is:","{0:0.2f}".format(std))
std_below_mean=average-std
        
if std>0:                             
    print("List of students who need to see an advisor:")
for newmark in range(len(marks)):                          
    if marks[newmark]<std_below_mean:                        
        if len(str(marks[newmark]))>1:                     
            print(mark[newmark][:-3])                 
        elif len(str(marks[newmark]))<=1:                  
            print(mark[newmark][:-2])
