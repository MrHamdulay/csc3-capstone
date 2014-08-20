"""
Oliver Funk
Assignment 9 - Files
"""

#Imports
from math import sqrt


#Get user input
which_file = input("Enter the marks filename:\n")


#Read file
file = open(which_file)

try:
    file_lines = file.readlines()
except IOError:
    print("File read error!")
finally:
    file.close()


#Fill a dic with name mark pairs
students = []
marks = []

for line in file_lines:
    line_split = line.split(',')
    if "\n" in line_split[-1]:
        students.append(line_split[0])
        marks.append(int(line_split[-1][:-1]))
    else:
        students.append(line_split[0])
        marks.append(int(line_split[-1]))


#Go through dict doing calculations

#Find average
avg = 0

for no in marks:
    avg += no
else:
    avg /= len(marks)

print("The average is: %.2f" % avg)

#Find std
sum_vals = 0

for no in marks:
    sum_vals += (no - avg) ** 2

std = sqrt(sum_vals / len(marks))
print("The std deviation is: %.2f" % std)

#Find marks that are less than 1 std away from mean
students_c_advisor = ""

for i in range(len(marks)):
    if marks[i] < (avg - std):
        students_c_advisor += students[i]+"\n"

#Print the list of students
if len(students_c_advisor) > 1:
    print("List of students who need to see an advisor:\n" + students_c_advisor)