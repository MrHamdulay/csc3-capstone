"""Ananlyse student marks
Shane Robinson
10 May 2014"""

import math

print("Enter the marks filename:")
filename = input()
f = open(filename, "r")
lines = f.readlines()
f.close()

#calculate average
sum_marks = 0
count = 0
for line in lines:
    c = line.find(',')
    sum_marks+=eval(line[c+1:])
    count+=1

average = sum_marks/count

#calculate standard deviation
sum_dev = 0
for line in lines:
    c = line.find(',')
    sum_dev+=(eval(line[c+1:])-average)**2

std_dev = math.sqrt(sum_dev/count)

print("The average is:", "{:0.2f}".format(average))
print("The std deviation is:", "{:0.2f}".format(std_dev))

#check if student needs advisor
def func():
    for line in lines:
        c = line.find(',')
        student = line[:c]
        mark = eval(line[c+1:])
        if mark<(average-std_dev):
            return True

if func():
    print("List of students who need to see an advisor:")
    for line in lines:
        c = line.find(',')
        student = line[:c]
        mark = eval(line[c+1:])
        if mark<(average-std_dev):
            print(student)