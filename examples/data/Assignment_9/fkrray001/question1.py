# Author : Rayaan Fakier FKRRAY001
# Date : 11 - 05 - 2014
# question1.py

import math

def mark_getter(file):
    '''Program that analyses student marks read in from a file'''
    ## Part 1 - file formatting
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    
    actlines = []
    # Creates array without '\n'
    for index in range(len(lines)-1):
        actlines.append(lines[index][:len(lines[index])-1])
    actlines.append(lines[len(lines)-1])
    
    # Creates array of marks and array of names
    marks = []
    names = []
    for line in actlines:
        for index2 in range(len(line)):
            if line[index2] == ",":
                marks.append(line[index2+1:])
                names.append(line[:index2])
    
    ## Part 2 - calculations and last printing
    total = 0
    for mark in marks:
        total += eval(mark)
        
    # Calculate average
    average = total / len(marks)
    rounded1 = '{0:.2f}'.format(average)
    print("The average is:", rounded1)
    
    stdrd_val = 0
    for mark2 in marks:
        stdrd_val += (eval(mark2) - average)**2
        
    # Calculate standard deviation
    stdrd_devi = math.sqrt(abs(stdrd_val/len(marks)))
    rounded2 = '{0:.2f}'.format(stdrd_devi)
    print("The std deviation is:", rounded2)
    
    # Checks who's in trouble
    print("List of students who need to see an advisor:")
    for index3 in range(len(marks)):
        if eval(marks[index3]) < (average - stdrd_devi):
            print(names[index3])
    
if __name__ == '__main__':
    file = input("Enter the marks filename:\n")
    mark_getter(file)