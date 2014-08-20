'''CSC1015F Assign 9 - Q1
Adam Rosendorff - RSNADA001
11 May 2014'''
from math import sqrt
file_name = input('Enter the marks filename:\n')
f = open(file_name, 'r')
lines = f.readlines()
f.close()

marks = []
below_deviation = [] #students below 1 std deviation
student_no = len(lines) #number of students read
mean = 0
deviation = 0

for i in range(student_no):
    marks.append(int(lines[i].split(',')[1])) #extracts marks to list
if len(marks) != 0: #to make sure the file isnt empty
    mean = sum(marks)/len(marks) #calculates mean
    for i in range(student_no): #calculates standard deviation
        deviation += (marks[i] - mean)**2
    deviation = deviation/student_no
    deviation = sqrt(deviation)
    for i in range(student_no):
        if marks[i] < mean-deviation: #students below 1 standard deviation
            below_deviation.append(lines[i].split(',')[0])
        
print('The average is: {:.2f}'.format(mean)) #.2f = 2 decimal places
print('The std deviation is: {:.2f}'.format(deviation))
if len(below_deviation) > 0:
    print('List of students who need to see an advisor:')
    print('\n'.join(below_deviation))
