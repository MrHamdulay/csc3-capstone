"""program to decide if student needs to see student advisor
chris betteridge
15 may 2014"""

import math

marks = input("Enter the marks filename:\n")
marks_file = open(marks,"r")
marks_list = marks_file.readlines()
marks_file.close()

#total sum of all student marks
counter = 0
mark = 0
sum_mark = 0
list_marks = [] 
for student in marks_list:
    if len(student)-1 == counter:
        mark = eval(student[student.find(",")+1:])
    else:
        mark = eval(student[student.find(",")+1:])
    sum_mark += mark
    list_marks.append(mark)
    counter += 1
    
#standard deviation
mean = sum_mark/counter
total_sum = 0
for i in range(counter):
    x = list_marks[i-1]
    mean_sum = (x-mean)**2
    total_sum += mean_sum

standard_deviation = math.sqrt(total_sum/counter)

#students who need to see student advisor
students = []
student = ""
fail = mean - standard_deviation
for learner in range(counter):
    if list_marks[learner] < fail:
        student = marks_list[learner][:marks_list[learner].find(",")]
        students.append(student)       
        
print("The average is: {:0.2f}".format(mean))
print("The std deviation is: {:0.2f}".format(standard_deviation))

if students != []:
    print("List of students who need to see an advisor:")
    for s in students:
        print(s)
