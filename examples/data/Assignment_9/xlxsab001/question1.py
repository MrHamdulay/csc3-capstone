"""Evaluating marks
Sabelo
14-may-2014"""
import math
x=input("Enter the marks filename:\n")
f=open(x,"r")
b=0
sm=0
stdrd_sum=0
lines=f.readlines()
lst=[]
for i in range(len(lines)):
    a=lines[i]
    for j in range(len(a)):
        if a[j]==",":
            b=eval(a[j+1:])
            sm+=b
            lst.append(b)
mean="{0:.2f}".format(sm/len(lines))
print("The average is:",mean)
mean=eval(mean)
sm=0
i=0
while i<len(lst):
    b=lst[i]
    sm+=(b-mean)**2
    i+=1

standard_dev=math.sqrt(sm/len(lines))
print("The std deviation is:","{0:.2f}".format(standard_dev))
for i in range(len(lst)):
    if lst[i]<mean-standard_dev:
        print("List of students who need to see an advisor:")
        break
    
for i in range(len(lines)):
    a=lines[i]
    for j in range(len(a)):
        if a[j]==",":
            b=a[0:j]
    if lst[i]<(mean-standard_dev):
        print(b)