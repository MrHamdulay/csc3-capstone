'''program to find sa=tandard deviation
matshepo mashabela
15 may 2014'''

markfile=input("Enter the marks filename:\n")
f=open(markfile, "r")
lines = f.readlines ()
f.close ()

import math
marks=[]
for line in lines:
    line=line[:len(line)-1]
    for i in range(len(line)):
        if line[i]==",":
            s_mark=(line[i+1:])
            marks.append(s_mark)
for i in range(len(marks)):
    marks[i]=eval(marks[i])  

def mean(marks):
    if len(marks)==1:
        return marks[0]
    elif len(marks)>1:
        return marks[0] + mean(marks[1:]) 

##calc mean
realmean=mean(marks)/len(marks)
realmean=round(realmean,2)
realmean="%.2f" % realmean
print("The average is:",realmean)
realmean=eval(realmean)

def standard(marks,realmean):
    if len(marks)==1:
        return (marks[0]-realmean)**2    
    elif len(marks)>1:
        return (marks[0]-realmean)**2 + standard(marks[1:],realmean)

std=standard(marks,realmean)/len(marks)
standiv=math.sqrt(std)
standiv="%.2f" % standiv #round(standiv,2)
    
print("The std deviation is:",standiv)
standiv=eval(standiv)
if standiv>0:
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if realmean-standiv >marks[i]:
            com=lines[i].find(",")
            print(lines[i][:com])
            
            
##reference
#'''rounding off method from stackoverflow.com'''