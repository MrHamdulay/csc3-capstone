""" a program to scan through a file of student marks and print the names of student with a mark below
one standard deviation from the mean
Lehlogonolo Masetla
13 May 2014"""

import math

mark=[]
marks=[]
file=input("Enter the marks filename:\n") #prompt the user for a file with marks

f=open(file,"r")

for line in f:
    mark.append(line) 
f.close()

while "\n" in mark:
    mark.remove("\n") 
for student in range(len(mark)):
    
    if mark[student][-1:]=="\n": # checks the last character           
        mark[student]=mark[student][:-1]
    
for individual in range(len(mark)):
    if mark[individual][-2:].isdigit():            
        newmark=eval(mark[individual][-2:])          
        marks.append(newmark)                              
    elif mark[individual][-1:].isdigit():         
        newmark=eval(mark[individual][-1:])
        marks.append(newmark)

addition=0
deviation=0
n=len(marks)
for a in marks:
    addition+=int(a)
    average=round((addition/n),2)
print("The average is:","{0:0.2f}".format(average))
for y in marks:
    deviation+=(int(y)-average)**2
std=round((math.sqrt(deviation/n)),2)
print("The std deviation is:","{0:0.2f}".format(std))
dev_from_mean=average-std
        
if std>0:                             
    print("List of students who need to see an advisor:")
    
for mark2 in range(len(marks)):   
    
    if marks[mark2]<dev_from_mean:                        
        if len(str(marks[mark2]))>1:                     
            print(mark[mark2][:-3])                 
        elif len(str(marks[mark2]))<=1:                  
            print(mark[mark2][:-2])