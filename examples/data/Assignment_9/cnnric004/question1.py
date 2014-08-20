"""Ricky Conn
CNNRIC004
Reading marks from file and deteriming who needs to go to the student councellor, if the student's
mark falls more than a standard deviation below the average mark"""

import math
filename = input("Enter the marks filename:\n")
file = open(filename,"r")
#lines is an array of all of the lines in the file supplied
lines = file.readlines()

def findAverage(lines):
    totalMarks = 0
    #Loops through each line in lines of the file
    for line in lines:
        totalMarks += eval(line.split(",")[1])
    return round(totalMarks/len(lines),2)

def stdDeviation(lines):
    totalMarksSq = 0.0
    ave = findAverage(lines)
    for line in lines:
        totalMarksSq += (eval(line.split(",")[1])-ave)*(eval(line.split(",")[1])-ave)
    return round(math.sqrt(totalMarksSq/len(lines)),2)      

#Determines which students need to go see the student advisor and prints their name
def printStudents(lines):
    count = 0
    ave = findAverage(lines)
    std = stdDeviation(lines)
    #seeAd = must they see the sudent advisor
    seeAd = False
    for line in lines:
        #if marks is less than a standard deviation below the average
        if(eval(line.split(",")[1])<(ave-std)):
            #forces the program to only print heaading once and to not print it if there are no students below a standard deviation deviation below the average
            count+=1
            if(count == 1):
                print("List of students who need to see an advisor:")
            seeAd = True
            #Prints the name of the current student if hey are below a standard deviation below the average
            print(line.split(",")[0])
    return seeAd
    
print("The average is:","%0.2f" % findAverage(lines))
print("The std deviation is:","%0.2f" % stdDeviation(lines))
printStudents(lines)
file.close()
