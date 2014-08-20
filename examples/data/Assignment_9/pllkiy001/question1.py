#program to analyse a student's marks based on standard deviation
#kiyarah pillay
#16 may 2014

import math

#get filename from user
f_name=input("Enter the marks filename:\n")
#open the file to read
f=open(f_name, "r")

#read the lines one by one
r_lines=f.readlines()

#make marks and names into lists
student_marks=[]
names=[]
mean = 0

#calculate the mean 
for i in range (len(r_lines)):
    student_marks.append(r_lines[i].split(',')[1].split("\n")[0])
    names.append(r_lines[i].split(',')[0])
    student_marks[i]=int(student_marks[i])
    mean=mean+student_marks[i]
mean=mean/len(student_marks)
standard_d=0

#calculate the standard deviation
for i in range (len(student_marks)):
    standard_d=standard_d + (student_marks[i]-mean)**2
standard_d=math.sqrt(standard_d/len(student_marks))
print ("The average is:","{:.2f}".format(mean))
print ("The std deviation is:","{:.2f}".format(standard_d))
say=False

#see if the marks meet the criteria or if student must see advisor
for i in range (len(student_marks)):
    if (student_marks[i]<(mean-standard_d)):
        say=True
if (say):
    print ("List of students who need to see an advisor:")
    for i in range (len(student_marks)):
        if (student_marks[i]<(mean-standard_d)):
            print(names[i])
                            
