#student mark checker
#Robin Hall
#16/05/2014

import math

file = input('Enter the marks filename:\n')
infile = open(file,'r') #opens file of choice, 'r' for reading functions

marks = [] #empty list for marks
names = [] #empty list for student names
#these two list are created in order to create the students list which will just contain the names of students who were lacking 
students = []

for line in infile: #evaluate each line in chosen file
    name,mark = line.split(',') #identifies comma to split the name and mark in a line
    names.append(name) 
    marks.append(int(mark))
    
infile.close() #closes chosen file

Sum = 0 #sum of marks initialised to 0
N = 0 #number of marks initialised to 0 
for i in marks: #iterate through marks list
    Sum += i
    N += 1
    
average = Sum/N 

stdSum = 0 #varibale for inner function of standard deviation function
for j in marks:
    stdSum += (j - average)**2

std_dev = math.sqrt(stdSum/N)

for i in range(len(names)):
    for j in range(len(marks)):
        if i == j and marks[j] < (average - std_dev): 
            students.append(names[i]) #for names corresponding to marks, if the mark is less than the average, name is added to students list
    
print('The average is: {:.2f}'.format(average))
print('The std deviation is: {:.2f}'.format(std_dev))
print('List of students who need to see an advisor:')

for student in students:
    print(student)
    
    