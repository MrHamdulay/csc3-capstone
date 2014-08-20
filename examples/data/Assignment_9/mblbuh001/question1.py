# question1.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 13 May 2014

from math import *
infileName = input("Enter the marks filename:\n")                   #user enters marks filename

def mean_mark():                                                    #define function mean_mark()
    infile = open(infileName, "r")                                  #open original file for reading
    sum_num = 0.0                                                   #initialize sum to 0.0
    count = 0                                                       #initialize count to 0
    for line in infile:
        stud_num , mark = line.split(",")                           #simultaneous assignment
        sum_num += eval(mark)                                       #increment sum with each mark
        count+=1                                                    #increment count by 1 to count number of marks
    infile.close()                                                  #close original file
    mean = sum_num/count                                            #calculate the average
    return mean                                                     #return the average

mean = mean_mark()

def std_dev():                                                      #define function std_dev()
    infile = open(infileName, "r")                                  #open original file for reading
    sq_sum = 0.0                                                    #initialize the sq_sum to 0.0
    count = 0                                                       #initialize count to 0
    for line in infile:
        stud_num , mark = line.split(",")                           #simultaneous assignment
        sq_sum += (eval(mark)-mean)**2                              #increment sq_sum by the square of the difference between each mark and the average
        count+=1                                                    #increment count by 1 to count number of marks
    infile.close()                                                  #close original file
    return sqrt(sq_sum/count)                                       #return the standard deviation

std_deviation = std_dev()

print("The average is: {0:0.2f}".format(mean))                      #prints average mark in a specific format
print("The std deviation is: {0:0.2f}".format(std_deviation))       #prints standard deviation  in a specific format

if std_deviation == 0:
    pass                                                            #passes if standard deviation is 0
else:
    print("List of students who need to see an advisor:")           #print statement
    infile = open(infileName, "r")                                  #open original file for reading
    for line in infile:
        stud_num , mark = line.split(",")                           #simultaneous assignment
        if eval(mark) < mean-std_deviation:                         #if student mark is less than one standard deviation below the average mark
            print(stud_num)                                         #prints student number
    infile.close                                                    #close original file