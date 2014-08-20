"""CSC1015F Assignment 9 Question 1
Xola Matlanyane MTLXOL002
20 May 2014"""

import math

x=input("Enter the marks filename:\n") #request file name
txtf=open(x,"r")    #open and read the file

z=0
som=0
stdrd_sum=0

lns=txtf.readlines()    #"lns" variable created - representing lines of the file
lst=[]      #a list is created
for i in range(len(lns)):
    y=lns[i]
    for j in range(len(y)):
        if y[j]==",":       #accounting for the comma
            z=eval(y[j+1:])
            som+=z
            lst.append(z)
mean="{0:.2f}".format(som/len(lns))   #getting the mean value
print("The average is:",mean)
mean=eval(mean)
som=0
i=0
while i<len(lst):
    z=lst[i]
    som+=(z-mean)**2
    i+=1

stndrd_dev=math.sqrt(som/len(lns))      #getting the standard deviation
print("The std deviation is:","{0:.2f}".format(stndrd_dev))
for i in range(len(lst)):
    if lst[i]<mean-stndrd_dev:
        print("List of students who need to see an advisor:")
        break
    
for i in range(len(lns)):
    y=lns[i]
    for j in range(len(y)):
        if y[j]==",":
            z=y[0:j]
    if lst[i]<(mean-stndrd_dev):
        print(z)