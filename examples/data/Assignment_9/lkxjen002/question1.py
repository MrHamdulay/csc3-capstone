#A program to determine which students need to see the student advisor
#Created by: Jenna Lake
#Date: 11 may 2014
import math

#open file and load entire file into list of strings
file_name=input("Enter the marks filename:\n")
f=open(file_name, "r")
lines=f.readlines()
f.close()

#separate the marks and student numbers into two lists
student_no=[]
marks=[]
for line in range(len(lines)):
    x,y=lines[line].split(",")
    student_no.append(x)
    marks.append(y)
    
sum=0
count=0
variance=0
for mark in range(len(marks)):
    t=marks[mark]
    sum+=int(t)
    count+=1

#caluclate and print average
average=round((sum/count),2)
if (average*100)%100==0:
    print("The average is: ", average, "0", sep="")
else:
    print("The average is: ", average, sep="")

#calculate and print the standard deviation
for mark in range(len(marks)):
    variance+=(int(marks[mark])-average)**2
std_dev=math.sqrt(variance/count)
std_deviation=round(std_dev,2)
if (std_deviation*100)%100==0:
    print("The std deviation is: ", std_deviation, "0", sep="") #if the decimal places are zeros(only prints one), print the missing zero
else:
    print("The std deviation is: ", std_deviation, sep="")

#Check which students are less than one std deviation below the mean
one_std_down=average-std_deviation
problem_list=[]
if std_deviation!=0:
    print("List of students who need to see an advisor:")
for mark in range(len(marks)):
    if int(marks[mark])<one_std_down: 
        print(student_no[mark])
        