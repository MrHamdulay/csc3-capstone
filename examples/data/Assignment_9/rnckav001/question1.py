#Assignment 9 Q1 - Student sorter
#Kavir Ranchod RNCKAV001
#11/05/2014

from math import *

filename = input("Enter the marks filename:\n")
def studentsort(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    
    for i in range(len(lines)-1):
        lines[i] = lines[i][:-1]    
    
    listlines=[]
    markslist=[]
    for line in lines:
        listlines.append(line.split(","))

    for i in range(len(listlines)):
        markslist.append(listlines[i][1])
    
    count=0
    for mark in markslist:
        count+=eval(mark)
    average=count/len(markslist)
    
    variance = 0
    for mark in markslist:
        variance += (eval(mark)-average)**2
                
    stddev = round(sqrt(variance/len(markslist)), 2)

    faillist = []
    for line in listlines:
        if eval(line[1]) < (average-stddev):
            faillist.append(line[0])
            
    if stddev == 0.0:
        stddev="0.00"
    
    stringaverage = str(average)
    listaverage = stringaverage.split(".")
    if len(listaverage[-1]) < 2:
        average = stringaverage + "0"
    else:
        average = round(average, 2)
        
    print("The average is:", average)
    print("The std deviation is:", round(stddev, 2))
    print("List of students who need to see an advisor:")
    
    for i in range(len(faillist)):
        print(faillist[i])

studentsort(filename)