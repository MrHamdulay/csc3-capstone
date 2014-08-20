#Deepak Bhoojrajh
#BHJDEE001
#Question 1 

import math
txt=input("Enter the marks filename:\n")

f=open(txt,"r")
x=f.readlines()
names=[]
marks=[]
for i in range(len(x)):
    p=x[i].index(",")
    names.append(x[i][:p])
    marks.append(eval(x[i][p+1:]))
    
    

tot=0
for i in range(len(marks)):
    tot = tot+marks[i]
avg=tot/len(marks)

sum=0
for i in range(len(marks)):
    sum=sum+((avg-marks[i])**2)
sum=sum/len(marks)
sd=math.sqrt(sum)

advise=[]
for i in range(len(marks)):
    if marks[i]<(avg-sd):
        advise.append(names[i])
    
print("The average is: {:.2f}".format(avg))
print("The std deviation is: {:.2f}".format(sd))
if len(advise)>0:
    print("List of students who need to see an advisor:")
    for i in advise:
        print(i)