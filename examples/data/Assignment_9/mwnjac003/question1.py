# program to check student marks and determine which students need advise
# by Jacob Mwanza
# 13/05/2014

import math


def help():
    # enter name of file
    file = input('Enter the marks filename:\n')
    
    # open file for reading
    f = open(file, 'r')
    
    # get marks of students and put them in a list
    marks = []
    for line in f:
        if line[len(line)-1:] == '\n':
            line = line[:-1]
        marks.append(line[line.find(',')+1:])
        
        
    # find the average mark
    sum_marks = 0
    for mark in marks:
        sum_marks += int(mark)
    mean = (sum_marks/len(marks))
    print("The average is: {0:0.2f}".format(mean))
    
    # find the sum of (mark - average)^2
    deviation = 0
    for mark in marks:
        deviation += ((int(mark)-mean)*(int(mark)-mean))
        
    # find the standard deviation
    std = math.sqrt(deviation/len(marks))
    print("The std deviation is: {0:0.2f}".format(std))
    
    # open file and find pupils who failed
    pupils = 'True'
    count1 = 0
    f = open(file, 'r')
    for j in f:
        if int(marks[count1]) < (mean - std):
            pupils = 'False'
        count1 += 1    
    if pupils == 'False':
        print('List of students who need to see an advisor:')
    count2 = -1
    
    
    f = open(file, 'r')
    for line_2 in f:
        count2 += 1
        if line[len(line)-1:] == '\n':
            line = line[:-1]
        if int(marks[count2]) < (mean - std):
            print(line_2[:line_2.find(',')])
        
    f.close ()    
    
help()
    
                    
    
    