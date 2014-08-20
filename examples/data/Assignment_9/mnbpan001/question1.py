"""Program to print out names of students who need to see an advisor
Pankaj Munbodh
10 May 2014"""

import math

file_name=input("Enter the marks filename:\n")
mean=0          #initialisation of variables
counter=0
f=open(file_name,"r")

#Calculate mean
for line in f:
    liste=line.split(',')
    mean+=eval(liste[1][:-1])
    counter+=1
f.close()
mean=mean/counter
print("The average is:","{0:0.2f}".format(mean))

#Calculate standard deviation    
sd=0
f=open(file_name,"r")
for line in f:
    liste=line.split(',')
    sd=sd+(eval(liste[1][:-1])-mean)**2
f.close()
sd=math.sqrt(sd/counter)
print("The std deviation is:","{0:0.2f}".format(sd))

#Calculate critical mark to see student advisor
critical_mark=mean-sd
students=[]

#Loop through file to check which students' marks are less than critical mark
f=open(file_name,'r')
for line in f:
    liste=line.split(',')
    if eval(liste[1][:-1]) < critical_mark:
        students.append(liste[0])

f.close()

#If there is at least one student who needs to see student advisor, print the following.
if len(students) !=0:
    print("List of students who need to see an advisor:")
    for i in students:
        print(i)
    
    

    