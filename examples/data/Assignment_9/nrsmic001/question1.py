"""Program to analyse students marks
Micaela Narasmulu
17 May 2014"""

import math
text=input("Enter the marks filename:\n")

f=open(text,"r") #read textfile

x=f.readlines() #convert each line in textfile to an item in an array
n=[] #empty list for names

m=[] #empty list for marks

for i in range(len(x)):
    p=x[i].index(",")
    n.append(x[i][:p])
    m.append(eval(x[i][p+1:]))
    

tot=0
for i in range(len(m)):
    tot = tot+m[i]
avg=tot/len(m)

sum=0
for i in range(len(m)):
    sum=sum+((avg-m[i])**2)
sum=sum/len(m)
sd=math.sqrt(sum)

advise=[]
for i in range(len(m)):
    if m[i]<(avg-sd):
        advise.append(n[i])
    
print("The average is: {:.2f}".format(avg))
print("The std deviation is: {:.2f}".format(sd))
if len(advise)>0:
    print("List of students who need to see an advisor:")
    for i in advise:
        print(i)