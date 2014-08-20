#Nikhil Jiten Naik
#NKXNIK003
#Assignement 9-Question 1


import math

filename=input("Enter the marks filename:\n")
f = open(filename,"r")
lines=f.readlines()
marks=[]
names=[]
mean=0

for i in range(len(lines)):
    marks.append(lines[i].split(',')[1].split("\n")[0])
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    mean+=marks[i]
mean=mean/len(marks)
sd=0
for i in range(len(marks)):
    sd+=(marks[i]-mean)**2
sd=math.sqrt(sd/len(marks))
print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(sd))
flag=False

for i in range(len(marks)):
    if(marks[i]<(mean-sd)):
        flag=True
if(flag):
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if(marks[i]<(mean-sd)):
            print(names[i])
