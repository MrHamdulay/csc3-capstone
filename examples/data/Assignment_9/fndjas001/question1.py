"""A program that determines whether or not a student needs an advisor
Jason Findlay
12/05/2014"""

import math
#Get data from file
file=input("Enter the marks filename:\n")
f=open(file,"r")
lines=f.readlines()
f.close()

#Split up the different entries
students=[]
for i in range(len(lines)):
    students.append("0")
    students[i]=(lines[i].split(","))

#Make the matks integers
for i in range(len(lines)):
    temp=students[i][1]
    temp=temp[0:2]
    students[i][1]=int(temp)

#Calculate and print average
total=0
count=0
for i in range(len(lines)):
    total+=students[i][1]
    count+=1
average=total/count
print("The average is: {0:.2f}".format(average))

#Calculate the standard deviation
temp=0
deviation=0
for i in range(len(lines)):
    temp+=(students[i][1]-average)**2
deviation=math.sqrt(temp/count)
print("The std deviation is: {0:.2f}".format(deviation))

#Determine which students need an advisor
if deviation!=0:
    print("List of students who need to see an advisor:")
for i in range(len(students)):
    if (students[i][1]+deviation)<average:
        print(students[i][0])
