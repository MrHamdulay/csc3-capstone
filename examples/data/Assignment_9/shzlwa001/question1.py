# Program for determining the students who need to see the student adviser
# Lwazi Shezi
# 16 May 2014

import math
filename = input('Enter the marks filename:\n')

# Stor each line on the file with the students on a list
file = open(filename,'r')
file = file.readlines()

# Remove unwanted charecters, like the '\n'
lines = []
for i in file:
    if i != file[-1] :
        for j in range(len(i)):
            lines.append(i[:j-1])
            break
lines.append(file[-1])

marks = []
counter = 0
# Define digits
digits = ['1','2','3','4','5','6','7','8','9','0']

# Reverse all the strings in the lines list, so as to easily chop out the '\n'          
for i in lines:
    lines[counter] = i[::-1]
    counter += 1
    
# Keep all the students' marks in a list
for i in lines :
    mark = ''
    for char in i:
        if char in digits :
            mark = mark + char
            
    marks.append(mark[::-1])
    
total = 0
# Get the total of the students' marks
for i in marks :
    i = eval(i)
    total += i

# calculate the average    
mean = total/len(marks)

print('The average is:','%.2f'%(mean))

# get the standard deviation, by getting the variance first (standard deviation squared)
variance = 0
for i in marks :
    variance += ((eval(i) - mean)**2)/len(marks)
    
std_dev = math.sqrt(variance)
print('The std deviation is:','%.2f'%(std_dev))

# Get all the students' names in a list
names = []
for i in lines :
    name = ''
    for char in i:
        if not char in digits and char != ',' :
            name += char
            
    names.append(name)
    
names_working = names

# Make a dictionary for the students' marks, each student must be indexed by their mark

marks_dict = {}   
for mark in marks :
    for name in names :
        marks_dict[mark] = name
        names = names [1:]
        break
    marks = marks[1:]
 
# Make a list of all students that need to see the student adviser as per the given condition
adviser = []           
for mark in marks_dict :
    if eval(mark) < (mean - std_dev) :
        adviser.append(marks_dict[mark][::-1])
        
# print out the names of all those students that must see the adviser, if there are any
if adviser != [] :
    print('List of students who need to see an advisor:')
    for name in names_working :
        if name[::-1] in adviser:
            print(name[::-1])
