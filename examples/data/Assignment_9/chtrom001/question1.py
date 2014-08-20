# question2.py
# program to analyse student marks read in from a file and determine which students need to see a student advisor. The students who (hypothetically!) need to see a student advisor are those with marks less than one standard deviation below the mean.
# romelon chetty(chtrom001)
# 12May 2014

from math import *

def main():
    # Function to control the entire program
    markfile = input("Enter the marks filename:\n")
  
    marks = open(markfile, "r")
    
    sdic = {}
    listmarks = []
    studentslist = []
    
    for line in marks:
        student, mark = line.split(",")
        sdic[student] = mark[:len(mark)]
        listmarks.append(eval(mark[:len(mark)]))
        studentslist.append(student)
        
        

    # This part calculates the average as well as the standard deviation of the marks
    totm = 0
    for x in sdic:
        totm = totm + eval(sdic.get(x))
        
    average = totm/len(sdic)    
    
    div = 0
    for i in sdic:
        number = eval(sdic.get(i))
        div = div + (number - average)**2
        
    stdDev = sqrt(div/(len(sdic)))
    stdDev1 = average - stdDev
    
    # This part now checks which students need to consult
    consults = []
    
    for mark in range(len(listmarks)):
        if listmarks[mark] < stdDev1:
            consult = studentslist[mark]
            consults.append(consult)
    
    print("The average is: {0:0.2f}".format(average))
    print("The std deviation is: {0:0.2f}".format(stdDev))
    
    
    for i in listmarks:
        if i < stdDev1:
            print("List of students who need to see an advisor:")
            break

    for s in consults:
        print(s)
    
            
    marks.close()
main()
