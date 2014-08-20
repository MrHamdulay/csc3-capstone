"""KLSADA002
Assignment 9 Q1
2014-05-13"""
import math
try:
    filename = input('Enter the marks filename:\n')
    f = open(filename,"r")
    lines = f.readlines()
    f.close
    marks = []
    names = []
    for i in lines:
        z = i.split(',')
        if "\n" in z[1]:
            temp = z[1]
            temp = temp[:len(temp)-1]
            temp=eval(temp)
            marks.append(temp)
        else:
            marks.append(eval(z[1]))
        names.append(z[0])
    mean = 0
    for i in marks:
        mean += i
    mean = mean/len(marks)
    print('The average is: {0:.2f}'.format(mean))
    stddev=0
    sigma = 0
    for i in marks:
        sigma += (i-mean)**2
    stddev = (sigma/len(marks))**0.5
    print("The std deviation is: {0:.2f}".format(stddev))
    students=[]
    for i in range(len(marks)):
        if marks[i] < (mean-stddev):
            students.append(names[i])
    if len(students) > 0:
        print('List of students who need to see an advisor:')
        for i in students:
            print(i)
except IOError as errno:
    print ("Could not read file")
    print ("Error number:",errno)
except ZeroDivisionError as errno:
    print("Marks list is empty")
    print(errno)
