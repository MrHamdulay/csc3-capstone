""" program to analyse student marks read in from a file and determine which students need to see a student advisor
Brandon Pickup
11 May 2014
Assignment 9 Question 1"""
import math
file_name = input("Enter the marks filename:\n")
in_file = open(file_name,"r")
lines = in_file.readlines() #reads every line of the code into one single variable
in_file.close()
marks =[] #empty list for marks
names = [] #empty list for names
total=0#total marks variable
std_dev = 0 #standard deviation variable
num_marks = 0
for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1] #removes the \n from the end of each line read in from the file
    student = lines[i].split(",") #splits each line by ',' leaving a name and a mark
    names.append(student[0])
    marks.append(student[1]) 
    total += eval(student[1]) #accumulates the total marks for an average calculation\num_students+=1
    num_marks+=1
    
ave = total/num_marks 
for mark in range(num_marks):
    std_dev += (eval(marks[mark])-ave)**2 #calculation for standard deviation, squaring the difference between the mean and mark for every mark
std_dev = math.sqrt(std_dev / num_marks)

print("The average is: {0:0.2f}".format(ave,2))
print("The std deviation is: {0:.2f}".format(std_dev))

student_advisor_names = []
for i in range(num_marks):
    if eval(marks[i]) < (ave-std_dev):#checks which student have marks less than one standard deviation from the mean, and then prints their names as a reccomendation to see the student advisor
        student_advisor_names.append(names[i])

if student_advisor_names:#only print the names if there are names in the list
    print("List of students who need to see an advisor:")
    for name in student_advisor_names:
        print(name)