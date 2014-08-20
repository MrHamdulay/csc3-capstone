"""program to analyze students marks
tayla george
15 may 2014"""

import math                                     #importing the math library

filename = input('Enter the marks filename:\n')
inputfile = open(filename, 'r')                  #opening the input file for reading
lines = inputfile.readlines ()                   #creating a list where each line is an item
student_marks = []
inputfile.close ()

for line in lines:                  #spliting the list, where each student and their mark is an item                                            
    name, mark = line.split(',')
    result = mark
    student_marks.append(int(result))       #adding the results to the list marks

sum1=0
for i in student_marks:                     #calculating the total of all the marks and assigning it to sum1
    sum1+=i
    
mean=sum1/len(student_marks)                #calculating the average mark
d=0
for mark in range(len(student_marks)):
    d+=((student_marks[mark]-mean)**2)
    
sd =d/len(student_marks)
    
sdev = math.sqrt(sd)     #calculating the standard deviation
    
print('The average is: {0:.2f}'.format(mean))

print('The std deviation is: {0:.2f}'.format(sdev))

for i in range(len(student_marks)):
    
    if float(int(student_marks[i]))<(mean-sdev):
        print('List of students who need to see an advisor:')
        break


for i in range(len(student_marks)): #prints out the students who need to see a student advisor
        
    if float(int(student_marks[i]))<(mean-sdev):  #converting the marks to floats  
        student,score=lines[i].split(",")          #splitting it into student and their marks
        print(student)




