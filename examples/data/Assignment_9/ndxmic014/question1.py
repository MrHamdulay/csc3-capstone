#NDXMIC014
#ASSIGNMENT 9
#QUESTION 1
#This program analyzes students marks from a list and determines who needs to see the student advisor
import math

filename=input("Enter the marks filename:\n")   #asks user for file name
f = open(filename,"r")   # opens a readable copy of the file
lines=f.readlines() #reads the lines of file and converts it to a long list
student_marks=[]
student_names=[]
mean=0
for i in range(len(lines)):
    student_marks.append(lines[i].split(',')[1].split("\n")[0])
    student_names.append(lines[i].split(',')[0])
    student_marks[i]=int(student_marks[i])
    mean+=student_marks[i]
mean=mean/len(student_marks)
sd=0
for i in range(len(student_marks)):
    sd+=(student_marks[i]-mean)**2
sd=math.sqrt(sd/len(student_marks))
print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(sd))
flag=False

for i in range(len(student_marks)):
    if(student_marks[i]<(mean-sd)):
        flag=True
if(flag):
    print("List of students who need to see an advisor:")
    for i in range(len(student_marks)):
        if(student_marks[i]<(mean-sd)):
            print(student_names[i])
