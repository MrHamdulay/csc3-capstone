"""Assignment 9 Question 1 analyse student marks read in from a file and determine which students need a student advisor
joshua wort
10 May 2014"""

import math
filename=input("Enter the marks filename:\n")

#open and load the data from the file
marks= open(filename,"r")
lines=marks.readlines()
marks.close()

#remove the newline tabs
for line in range(len(lines)-1):
    lines[line]=lines[line][:-1]
    
total=0
count=0
#split marks and names  
for line in lines:
    student=line.split(",")
    total+=eval(student[1])
    count+=1
average=total/count #calculate average mark

add=0
#calculate standard deviation of marks
for line in lines:
    student=line.split(",")
    add+=(average-eval(student[1]))**2
std_dev=math.sqrt(add/count)

passed=average-std_dev
failed_students=[]
for line in lines:
    student=line.split(",")
    student[1]=eval(student[1])
    if student[1]<passed:
        failed_students.append(student[0]) #create a list with names of students who have marks below 1 standard deviation of the mean

average="{0:.2f}".format(average)
std_dev="{0:.2f}".format(std_dev)
print("The average is:",average)
print("The std deviation is:",std_dev)
if len(failed_students)>0: #only print out list if there is indeed a list of names
    print("List of students who need to see an advisor:")
    for i in range(len(failed_students)):
        print(failed_students[i])
