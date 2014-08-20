"""program to analyse marks from a file
Nosipho Khumalo
10 May 2014"""

from math import sqrt

def marks():
    #creating variables
    filename = input("Enter the marks filename: \n")
    total = 0
    deviation_sum = 0
    marks = []   
    
    # open and load the data from the file
    f = open(filename, "r")
    lines = f.readlines ()
    f.close()
    
   
    # chop off the trailing carriage returns
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
         
 
    #separating the names and marks
    for i in range (len (lines)):
        student = lines[i].split (',')
        mark = student[1]
        marks.append(mark)
        total += int(mark)
    
    #calculating average
    avg = total/len(lines)
    print("The average is:", "{0:0.2f}".format(avg))
    
    #calculating standard deviation
    for i in range(len(marks)):
        deviation_sum += (int(marks[i]) - avg)**2
    std = sqrt(deviation_sum/len(lines))    
    print("The std deviation is:", "{0:0.2f}". format(std))
    
    advisor = []
    #printing out list of students to see advisor
    margin = round((avg - std), 2)
    for i in range(len(marks)):
        if int(marks[i]) < margin:
            #finding position of comma to separate string
            position = lines[i].index(",")
            advisor.append(lines[i][:position])
    if len(advisor) > 0:
        print("List of students who need to see an advisor:")
        for i in range(len(advisor)):
            print(advisor[i])

marks()
    
    