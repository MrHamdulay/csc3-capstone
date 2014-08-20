#A program to analyse student marks read in from a file and determine which students need to see a student advisor
#Author: Michelle Njoroge
#13 May 2014

import math


file=input("Enter the marks filename:\n")
f=open(file,"r")

#Append marks to list1 (array)
list1=[]
for line in f:
    for i in range(len(line)):
        if line[i]==",":
            list1.append(int(line[i+1:]))

f.close()
f=open(file,"r")

#Append names to names(array)
names=[]
for line in f:
    for i in range(len(line)):
        if line[i]==",":
            names.append(line[:i])
f.close()          

f=open(file,"r")
#Calculate the average
sum1=0
count=0
for line in f:
    for i in range(len(line)): 
        if line[i]==",":
            sum1+=int(line[i+1:])
        else: pass
    count+=1
mean=sum1/count
print("The average is:","{0:.2f}".format(mean))
f.close()

f=open(file,"r")

#Calculate the standard deviation
variance=0
for number in list1:
    variance+=(number-mean)**2
sd=math.sqrt(variance/len(list1))
print("The std deviation is:","{0:.2f}".format(sd))
f.close()

f=open(file,"r")
#Append marks and names to a dictionary
dictionary={}

for j in range(len(list1)):
    dictionary[list1[j]]=names[j]
f.close()

f=open(file,"r")

#check whether any student needs to see an advisor
advisor=False
for mark1 in dictionary:
    if mark1<(mean-sd):
        advisor=True
    else: pass
if advisor==True:
    print("List of students who need to see an advisor:")
else: pass

f.close
f=open(file,"r")
#Print out names of students who need to see an advisor
for mark1 in dictionary:
    if mark1<(mean-sd):
        print(dictionary[mark1])
f.close()


