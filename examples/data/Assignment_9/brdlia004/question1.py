"""Program to determine students need to see a student advisor"""
#Liam Brodie
#BRDLIA004
#11 May 2014

import collections
import math

data = collections.OrderedDict()

def process():
    """Function to run through input & produce output"""
    print("Enter the marks filename:")
    filename = input("")
    f = open(filename,"r")
    for line in f:
        x = line.split(",")
        Student = x[0]
        Grade = x[1]
        if "\n" in Grade:
            n = len(Grade)-1
            Grade = Grade[:n]
        data[Student] = Grade
        
    grades = []
    for Student, Grade in data.items():
        grades.append(data[Student])
        
    students = []
    for key in data:
        students.append(key)    
        
    count = 0
    total = 0        
    for j in grades:
        j = eval(j)
        total += j
        count += 1
        avg = total/count
        avg = round(avg,2)
    print("The average is:", '{:<5.2f}'.format(avg))
    
    
    newterm = 0
    terms = 0
    for i in grades:
        i = eval(i)
        newterm = (i - avg)**2
        terms += newterm
    std = math.sqrt(terms/count)
    std = round(std,2)
    print("The std deviation is:", '{:<5.2f}'.format(std))
    
    for Student, Grade in data.items():
        if eval(Grade) < (avg-std):    
            print("List of students who need to see an advisor:")
            break
    for Student, Grade in data.items():
        if eval(Grade) < (avg-std):
            print(Student)
    
    f.close()
    
    
        
process()
