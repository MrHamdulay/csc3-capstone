# A program to read marks of students in a file and check if they need to see a student advisor 
# Wongwa Giqwa
# 10 May 2014

import math

marks = []

file = input('Enter the marks filename:\n')

f = open(file, 'r')

lines = f.readlines ()

for line in lines:
    # get names and marks from line
    name, mark = line.split(',')
    m = mark
    marks.append(int(m))


sum1=0
for i in marks:
    sum1=sum1+i
mean=sum1/len(marks)
fd=0
for i in range(len(marks)):
    fd=fd+((marks[i]-mean)**2)
sd = fd/len(marks)
    
std_dev = math.sqrt(sd)
    

f.close ()

print('The average is: {0:.2f}'.format(mean))

print('The std deviation is: {0:.2f}'.format(std_dev))


for i in range(len(marks)):
    
    if float(int(marks[i]))<(mean-std_dev):
        print('List of students who need to see an advisor:')
        break


for i in range(len(marks)):
        
    if float(int(marks[i]))<(mean-std_dev):    
        p,k=lines[i].split(",")
        print(p)

