"""
Assignment 9 - Question 1
Program to analyse student marks
Jayan Smart
04 May 2014
"""

#import required functions
from math import sqrt


#read the mark sheet
def readmarks(file):
    f = open(file, 'r')
    students = []
    for line in f:
        students.append(line.split(','))
    f.close()
    for i in range(len(students)-1):
        students[i][1] = (students[i][1])[:-1]
    for i in range(len(students)):
        students[i][1] = eval(students[i][1])
        
    return students


#calculate the standard deviation
def stddev(nums, xbar):
    if len(nums) == 1:
        return 0.00
    sumdevsq = 0.0
    for num in nums:
        sumdevsq += (num - xbar)**2
    stddev = sqrt(sumdevsq/(len(nums)))
    return stddev
    


    
def main():
    file = input("Enter the marks filename:\n")
    #create list of students and marks (2d array)
    students = readmarks(file)
    #extract list of marks from students
    marks = []
    for i in range(len(students)):
        marks.append(students[i][1])
    
    #find average mark
    total = 0.0
    for j in marks:
        total += j
    mean =  total/len(marks)

    
    #find standard deviation5
    stdDev = stddev(marks, mean)


    print ("The average is:", "{:.2f}".format(mean))
    print ("The std deviation is:", "{:.2f}".format(stdDev))
    #Check which students, if any need to see the advisor
    for k in range(len(students)):
        if students[k][1] < mean - stdDev:
            print("List of students who need to see an advisor:")
            break
    for l in range(len(students)):
        if students[l][1] < mean - stdDev:
            print(students[l][0])
main()
