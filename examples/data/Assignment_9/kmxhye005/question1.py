# A program to analyse student marks read in from a file and determine which students need to see a student advisor. 
# The students who (hypothetically!) need to see a student advisor are those with marks less than one standard deviation below the mean.


import math

def averagemark (marks):
    count = 0
    for i in range(len(marks)):
        count = count + int(marks[i])
    
    
    average = count / len(marks)
    
    return average
    
    
def std_deviation (marks):
    n = len(marks)
    mean = averagemark(marks)
    std_d = 0
    
    for mark in marks:
        std_d = std_d + (int(mark) - mean)**2
    std_d = math.sqrt(std_d / n)
    
    return std_d


def function (z):
    
    m = open(z,"a")
    lines = m.readlines() 
    m.close()

    for i in range (len(lines)):
        lines[i] = lines[i][:-1]
        
    marks = []
    for i in range(len(lines)):
        if lines != " ":
            a = lines[i].split(",")
            marks.append(a[1])
       
    names = []
    
    for i  in range(len(lines)):
        if lines != " ":
            a = lines[i].split(",")
            names.append(a[0])
        
    mean = averagemark(marks)
    std_deviation = standard_deviation(marks)
    
    print("The average is:", "{:.2m}".format(mean))
    print("The std deviation is:","{:.2m}".format(std_deviation))
    
    names_1 = []
    
    for i in range(len(marks)):
        if int(marks[i]) < mean - std_deviation:
            names_1.append(names[i])
            
    if len(names_1) != 0:
        print("List of students who need to see an advisor:\n",("\n").join(names_1), sep="")
            
           
z = input("Enter the marks filename:\n")

function(z)
