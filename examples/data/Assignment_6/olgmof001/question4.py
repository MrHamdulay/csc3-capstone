"""Tofunmi Olagoke
OLGMOF001
23rd April 2014
Classifying of marks"""

A=input("Enter a space-separated list of marks:\n")
listA=A.split(" ")

#empty spaces
first=[]
us=[]
ls=[]
t=[]
f=[]

#loop adding the marks to different classes
for x in listA:
    x=eval(x)
    if x<50:
        f=f+[x]
    if 50<=x<60:
        t=t+[x]
    if 60<=x<70:
        ls=ls+[x]
    if 70<=x<75:
        us=us+[x]
    if x>=75:
        first=first+[x]

#printing output        
print("1 |"+len(first)*"X")   
print("2+|"+len(us)*"X")
print("2-|"+len(ls)*"X")
print("3 |"+len(t)*"X")
print("F |"+len(f)*"X")
