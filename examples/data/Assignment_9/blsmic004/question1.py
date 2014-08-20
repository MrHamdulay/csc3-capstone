# program to analyse student marks read in from a file and determine which students need to see a student advisor
# Michele Balestra  BLSMIC004
# 13 May 2014

import math

def openfile(name):
    '''function to open file with given name and assign contents to a list'''
    f = open(name,'r')
    wholeFile = f.read()
    f.close()
    
    lines = wholeFile.split('\n')
    
    # assigns contents to a list, splits by a ','
    line = []
    for item in lines:
        if len(item) > 2:
            line.append(item.split(','))
        
    return line


def average(marks):
    '''function to calculate average marks from file of names and marks'''
    ave = 0
    for i in marks:
        ave += eval(i[1])
        
    return round(ave/len(marks),2)
 
    
def standard_dev(marks,ave):
    '''function to calculate standard deviation of marks from file of names and marks'''
    stdev = 0
    for j in marks:
        stdev += (int(j[1])-ave)**2
        
    return round(math.sqrt((stdev)/len(marks)),2)


def advisor(marks,stdev,ave):
    '''function to determine students who need to see advisor if mark is mroe than one standard deviation below the average'''
    students = []
    for k in marks:
        if int(k[1]) < (ave-stdev):
            students.append(k[0])
    return students
    
    
if __name__=="__main__":
    # gets filename from user and calculates necessary details
    filename = input("Enter the marks filename:\n")
    lines = openfile(filename)
    ave = average(lines)
    print("The average is:", "{0:.2f}".format(ave))
    stdev = standard_dev(lines,ave)
    print("The std deviation is:", "{0:.2f}".format(stdev))
    studentList = advisor(lines,stdev,ave)
    if studentList:
        print("List of students who need to see an advisor:\n", end='')
        for i in studentList:
            print(i)