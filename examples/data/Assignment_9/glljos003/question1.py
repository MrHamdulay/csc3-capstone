"""program to analyse student marks read in from a file and determine which students need to see a student advisor
joshua gullan
11 may 2014"""

from math import *

file_choice = input("Enter the marks filename:\n")
test_file = open(file_choice, "r")

file_list = test_file.read()
file_list = file_list.split("\n") #splits each line into a new item in the list

marks = []
for s in file_list:
    s=s.split(",")   #splits the items in the row at the comma
    for i in s:
        if i.isdigit() == True:  #finds number and appends it to marks
            marks.append(i)   
        else:
            continue

marks=list(map(int, marks))   #evaluates numbers so they can be worked with

average = sum(marks)/len(marks)

print('The average is:',"{0:0.2f}".format(average))

numerator = 0
N = len(marks)

for score in marks:   #finds the numerator value for standard deviation equation
    numerator += (score-average)**2

deviation = sqrt(numerator/N)  

print('The std deviation is:', "{0:0.2f}".format(deviation))

student_names = []
for student in file_list:
    if student.isdigit() == False:   #does opposite of the loop at the beginning, this one gets names not numbers
        student_names.append(student)
    else:
        continue



average = round(average, 2)
deviation = round(deviation, 2)

student_new_names = []

for pupil1 in student_names:
    pupil1 = pupil1.split(",")   
    student_new_names.append(pupil1[0])
    

student_fail = []
count = 0
for score1 in marks:   #finds students who need to see the advisor
    if score1 < (average-deviation):
        student_fail.append(student_new_names[count])
        count+=1
        
    else:
        count+=1
        continue

if len(student_fail) > 0:
    print("List of students who need to see an advisor:")
    for student in student_fail:
        print(student)

else:
    ()
       
       
test_file.close()