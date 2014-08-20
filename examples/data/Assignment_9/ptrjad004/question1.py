"""A program to read marks of students in a file and check if they need to see a student advisor 
Jade Petersen
Assignment 9
Question 1
10 May 2014"""

import math

marks = []

filename = input('Enter the marks filename:\n')

f = open(filename, 'r')

lines = f.readlines ()

for line in lines:
    # get names and marks from line
    name, mark = line.split(',')
    m = mark
    marks.append(int(m))


sum1=0 
for i in marks: #calculate the mean
    sum1=sum1+i
mean=sum1/len(marks)
fd=0
for i in range(len(marks)): #calculate standard deviation
    fd=fd+((marks[i]-mean)**2)
sd = fd/len(marks)
    
std_dev = math.sqrt(sd)
    

f.close () #close file

print('The average is: {0:.2f}'.format(mean))

print('The std deviation is: {0:.2f}'.format(std_dev))


for k in range(len(marks)):
    
    if float(int(marks[k]))<(mean-std_dev):
        print('List of students who need to see an advisor:')
        break


for w in range(len(marks)):
        
    if float(int(marks[w]))<(mean-std_dev):    
        n,k=lines[w].split(",")
        print(n)

