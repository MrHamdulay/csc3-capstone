"""Aiden Walton
Assignment 9 - Question 1"""
import math
filename=input("Enter the marks filename:\n")
f=open(filename,"r")
marklist=f.readlines()
f.close()
mean_sum=0
mean_div=0
dev_sum=0
dev_div=0
for line in marklist:
    i=line.split(",")
    mean_sum+=int(i[1])
    mean_div+=1
mean=mean_sum/mean_div
print("The average is:","{0:.2f}".format(mean))
for line in marklist:
    i=line.split(",")
    dev_sum+=(int(i[1])-mean)**2
    dev_div+=1
dev=math.sqrt(dev_sum/dev_div)
print("The std deviation is:","{0:.2f}".format(dev))
names=[]
for line in marklist:
    i=line.split(",")
    if int(i[1])<(mean-dev):
        names.append(i[0])
if names!=[]:
    print("List of students who need to see an advisor:")
    for name in names:
        print(name)
    
