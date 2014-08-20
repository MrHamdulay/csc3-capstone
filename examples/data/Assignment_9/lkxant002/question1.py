#Assignment 9
#Question 1

import math

filename=input("Enter the marks filename:\n")
f=open(filename,"r")

#f1=f.read()
lines=[]
marks=[]

for i in range(100):
    x=f.readline()
    if x!="":
        if x[-1:]=="\n":
            
            if x[-4]==",":    
                lines.append(x[0:-4])                
                marks.append(int(x[-3:-1]))
            else:
                lines.append(x[0:-3])
                marks.append(int(x[-2:-1]))
        else:
            lines.append(x[0:-3])
            if x[-3]==",":    
                lines.append(x[0:-3])
                marks.append(int(x[-2:]))
            else:
                lines.append(x[0:-2])
                marks.append(int(x[-1:]))            
            
       
mu=round(sum(marks)/len(marks),2)

Sx=0
for i in marks:
    Sx=Sx+(i-mu)*(i-mu)
sd=round(math.sqrt(Sx/len(marks)),2)

if str(mu)[-2:]==".0":
    mus=str(mu)+"0"
else:
    mus=mu
    
if str(sd)[-2:]==".0":
    sds=str(sd)+"0"
else:
    sds=sd

print("The average is:",mus)
print("The std deviation is:",sds)

x=0
for i in range(len(marks)):
    if marks[i]<(mu-sd):
        x=1
if x==1:
    print("List of students who need to see an advisor:")            
        
for i in range(len(marks)):
    if marks[i]<(mu-sd):
        print(lines[i])

