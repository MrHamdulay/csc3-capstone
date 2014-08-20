"""Program to check a student needs to visit a student counselor
Runako Muzwidzwa
13/05/2014"""
import math
file=input("Enter the marks filename:\n")
f=open(file,"r")
lines=f.readlines()
marks_file=[]
names_file=[]
for line in (lines):
    names, marks = line.split(",")#split the file into marks and names
    marks_file.append(marks)
    names_file.append(names)
total_number=len(marks_file)
total=0
for mark in marks_file:
    total+=int(mark)
    
mean=round((total/total_number),2)
square_root_total=0   
for i in marks_file:
    x=int(i)
    square_root_total+=(x-mean)**2

standard_dv=math.sqrt(square_root_total/total_number)#standard deviation
standard_dev=round(standard_dv,2)
print("The average is:","{0:0.2f}".format(mean))#use format to make sure the numbers have 2 decimal places
print("The std deviation is:","{0:0.2f}".format(standard_dev))

counselor=(mean-standard_dev)#boundary value
student_names=[]#list that has th indicies of the students in need of a counselor 
for j in range(len(marks_file)):
    mrk=int(marks_file[j])
    if mrk<counselor:
        student_names.append(j)
if student_names!=[]:#to make sure the line is only printed if there is a student to help
    print("List of students who need to see an advisor:") 
for name in student_names:
    print(names_file[name])
    