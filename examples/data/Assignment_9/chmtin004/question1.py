'''Program to analyze marks and determine which student need to see the advisor
Tinotenda Chemvura
11 May 2014'''

import math
#___________________________PROGRAM STARTS HERE_________________________________
def marks(marks):
    
    #strip off the "\n" at the end of each string
    #insert fields in each line to seperate the name and mark
    for i in range(len(marks)):
        marks[i] = marks[i][:-1]
        marks[i] = marks[i].split(",")
        #print(marks[i][0],marks[i][1])
    return marks

#function to calculate the mean
def calc_mean():
    sum1 = 0
    count1 = 0
    for i in range (len(marks2)):
        sum1 += eval(marks2[i][1])
        count1 += 1
    mean = sum1/count1
    return mean
    
#function to calculate Standard Deviation of the student's marks
def calc_SD():
    mean = calc_mean()
    sum2 = 0
    n = 0
    #loop to calculate the sum
    for j in range(len(marks2)):
        diff = eval(marks2[j][1]) - mean
        sum2 += diff**2
        n += 1
    
    SD = math.sqrt((1/n)*sum2)
    return SD

def advisor():
    print('List of students who need to see an advisor:')
    border1 = mean_ - S_D
    for i in range(len(marks2)):
        if eval(marks2[i][1]) < border1:
            print(marks2[i][0])

#ask user for the name of marks file
filename = input("Enter the marks filename:\n")
#filename = "test1.txt"
#open file in read mode and make a list of all the lines in the text file
file1 = open (filename, "r")
marks1 = file1.readlines()
file1.close()

marks2 = marks(marks1)
S_D = calc_SD()
mean_ = calc_mean()

#printing the recquired results
print('The average is: {0:1.2f}'.format(mean_))
print("The std deviation is: {0:1.2f}".format(S_D))
if S_D > 0:
    advisor()
#___________________________END OF PROGRAM______________________________________