"""Rishen Singh
Assignment 9 question 1
SNGRIS012"""
import math

filename=input("Enter the marks filename:\n")
f = open(filename,"r") #opens file
lines=f.readlines() #stores each line of the file into a list
marks=[]
names=[]
mean=0
for i in range(len(lines)):
    marks.append(lines[i].split(',')[1].split("\n")[0]) #splits the original list into two seprate lists, separates the names and the marks into two separate corresponding lists
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    mean+=marks[i]
mean=mean/len(marks) #calculates the mean value of the marks
std_dev=0
i=0
while (i<len(marks)):
    std_dev+=(marks[i]-mean)**2 #calculates standard deviation
    i+=1
std_dev=math.sqrt(std_dev/len(marks))
print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(std_dev))
flag=False
k=0
while (k<len(marks)):
    if(marks[k]<(mean-std_dev)):
        flag=True
    k+=1
if(flag):
    print("List of students who need to see an advisor:") #prints out the names of all the students who are more than one standard deviation below the mean,
    for i in range(len(marks)):
        if(marks[i]<(mean-std_dev)):
            print(names[i])
