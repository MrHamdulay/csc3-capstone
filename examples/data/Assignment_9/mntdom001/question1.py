""" a Python program to analyse student marks read in from a file and determine
which students need to see a student advisor.
Dominic Manthoko
11 May 2014"""

from math import *

# prompt the user to enter a file name
filename = input('Enter the marks filename: \n')
infile = open(filename, 'r')

# create an empty list to store the names of students 
name_list = []
# create an empty list to store the marks of students
mark_list = []

# go through each line in the file and store the names and marks in the dictionary
for line in infile:
    name, mark = line.split(',')
    name_list.append(name)
    mark_list.append(eval(mark))
    
infile.close()

# creat a variable to store the total of the marks
total = 0

for val in mark_list:
    total+= val
    
# calculate the average
avg = total/len(mark_list)

# create a variable to store the sum squared difference of the marks and average
num = 0

for val in mark_list:
    square_dif = (val - avg) ** 2
    num += square_dif

# calculate the standard deviation    
Stan_Dev = sqrt(num/len(mark_list))

print("The average is: {0:0.2f}\nThe std deviation is: {1:0.2f}".format(avg, Stan_Dev))

if Stan_Dev >0:
    print('List of students who need to see an advisor:')
    
    for item in range(len(mark_list)):
        if int(mark_list[item]) < (avg - Stan_Dev):           # will print  the name of the student only if their mark is less than one standard deviation from the mean/average
            print(name_list[item])
            