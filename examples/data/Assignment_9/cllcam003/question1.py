# Cameron Collum 
# Student advisor program
# 15/05/2014

from math import *

file_input = input("Enter the marks filename:\n")
test_data = open(file_input, "r")

lis = test_data.read()
lis = lis.split("\n") #splits lines into list

marks = []
for s in lis:
    s=s.split(",")   #splits items by comma
    for i in s:
        if i.isdigit() == True:  # appends only numbers to marks
            marks.append(i)   
        else:
            continue

marks=list(map(int, marks))   

average = sum(marks)/len(marks)

print('The average is:',"{0:0.2f}".format(average))

numerator = 0
N = len(marks)

for score in marks:   
    numerator += (score-average)**2

deviation = sqrt(numerator/N)  

print('The std deviation is:', "{0:0.2f}".format(deviation))

names = []
for student in lis:
    if student.isdigit() == False:   # Gets the name of the students
        names.append(student)
    else:
        continue



average = round(average, 2)
deviation = round(deviation, 2)

student_new_names = []

for pupil1 in names:
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
       
       
test_data.close()