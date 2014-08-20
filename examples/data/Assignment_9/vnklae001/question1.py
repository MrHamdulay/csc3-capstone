# Assignment 9 - Question 1
# A program that reads a file and prints out the average correct to 2 decimal places, the standard deviation and a list of students that need to see the student advisor
# Written by: Laene van Niekerk
# VNKLAE001

import math

def average(s):     # To calculate the average
    count = len(s)
    total = 0       # A running total of the marks
    for i in range(count):
        number = eval(s[i])
        total = total + number
    average = total/count
    return average

def stdDev(nums, xbar):     # Where nums is the list of numbers entered and xbar is the mean of the numbers
    sumDevSq = 0.0      # To store a running sum of the squares of the deviations
    for num in range(len(nums)):    # Loop with accumulator to calculate the summation of the standard deviation
        x = eval(nums[num])
        dev = xbar - x
        sumDevSq = sumDevSq + dev * dev
    return math.sqrt(sumDevSq / (len(nums))) # Complete formula for calculating standard deviation

file_to_open = input("Enter the marks filename:\n")
f = open(file_to_open, "r")
student_marks = f.readlines()       # Creates a list with the student name and mark seperated by a comma
f.close()

marks = []
for i in range(len(student_marks)):   # Creates a list containing raw marks  
    item = student_marks[i]
    end = student_marks[i].find("\n")
    for j in range(len(item)):
        if item[j] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-":
            continue
        elif item[j] == ",":
            continue
        else:
            marks.append(item[j:])
            break

real_marks = []
for i in range(len(marks)):     # Creates a list containing actual marks
    if "\n" in marks[i]:
        pos = marks[i].find("\n")
        mark = marks[i][:pos]
        real_marks.append(mark)
    else:
        real_marks.append(marks[i])

names = []
for i in range(len(student_marks)):      # Creates a list containing names only
    item = student_marks[i]
    for j in range(len(item)):
        if item[j] == ",":
            names.append(item[0:j])
            
avg = average(real_marks)              
print("The average is:", "{0:.2f}".format(avg))
std = (stdDev(real_marks, avg))
print("The std deviation is:", "{0:.2f}".format(std))

requirement = avg - std

pos = []        # List containing the indexes of students that need to see the student advisor
for i in range(len(real_marks)):
    x = eval(real_marks[i])
    if x < requirement:
        pos.append(i)
    else: 
        continue
    
student_advisor_lst = []
for i in range(len(pos)):
    student = names[pos[i]]
    student_advisor_lst.append(student)

if student_advisor_lst != []:    
    print("List of students who need to see an advisor:")
    for i in range(len(student_advisor_lst)):
        print(student_advisor_lst[i])