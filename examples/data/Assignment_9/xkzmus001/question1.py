""" Program to analyse student marks and determine which students need to see a student advisor
Author : Musa Xakaza
Date : 11/05/2014"""
import math
def getMean(marks):
    #calc average
    sum = 0.0
    for num in marks:
        sum += num
    return sum/len(marks)

def getStdDev(marks, mean):
    #calc standard deviation
    sumOfSquares = 0.0
    for num in marks:
        sumOfSquares += (num - mean)**2
    return math.sqrt(sumOfSquares/len(marks))

def getStdAdv(students, marks, stdDev1, stdList):
    #return list of student(s) who need to see student advisor
    for i in range(len(marks)):
        if marks[i] < stdDev1:
            stdList.append(students[i])
    return stdList 

def main():
    names = []
    marks = []
    filename = input("Enter the marks filename:\n")
    f = open(filename,"r")
    for line in f:
        tmpList = line.split(',')
        names.append(tmpList[0])
        marks.append(int(tmpList[1]))    
    f.close()
    
    decimals = "{0:0.2f}"
    avg = getMean(marks)
    std = getStdDev(marks, avg)
    print("The average is:",decimals.format(avg))
    print("The std deviation is:",decimals.format(std))
    stdList = []
    stdList = getStdAdv(names, marks, avg - std, stdList)
    if stdList:
        print("List of students who need to see an advisor:")
        for learner in stdList:
            print(learner)

main()