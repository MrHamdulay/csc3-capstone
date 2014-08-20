#Assignment 6, Question 4
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 21/04/2014

#This program is designed to make a histogram of the marks of a student.
#Pre-condition: Input marks, separated by space.
#Post-condition: Output histogram.
marks = input("Enter a space-separated list of marks:\n")
marks = marks.split() #Split marks into a list.

#Initializing counters.
failCount = 0
thirdCount = 0
lowerSecondCount = 0
upperSecondCount = 0
firstCount = 0

#Counting number of marks.
#.#Pre-condition: Convert mark to a value. Check grade for mark .
#.#Post-condition: Update mark counter accordingly.
for mark in range(len(marks)):
    mark = eval(marks[mark]) #Converting mark to a value(integer).
    
    #Checking marks and updating counters.
    if(mark < 50):
        failCount += 1        
    elif(mark >= 50 and mark < 60):
        thirdCount += 1
    elif(mark >= 60 and mark < 70):
        lowerSecondCount += 1
    elif(mark >=70 and mark < 75):
        upperSecondCount += 1
    else:
        firstCount += 1

#Print Histogram.
print("1 |", "X"*firstCount, sep="")
print("2+|", "X"*upperSecondCount, sep="")
print("2-|", "X"*lowerSecondCount, sep="")
print("3 |", "X"*thirdCount, sep="")
print("F |", "X"*failCount, sep="")