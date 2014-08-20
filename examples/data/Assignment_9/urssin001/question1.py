'''
Write a Python program to analyse student marks read in from a file and determine which students need to see a student advisor.
The students who (hypothetically!) need to see a student advisor are those with marks less than one standard deviation below the mean.
The marks file is composed of lines of text, where each line contains a student number and mark separated by a comma.
Before the list of student names, print out the average and standard deviation with 2 decimal points of precision.
Sinead Urisohn
14 May 2014
'''
#to use math functions
import math

#get filename and read its content
filename=input("Enter the marks filename:\n")
f=open(filename,"r")
#get each line as an element in a list
lines=f.readlines()
#close file
f.close ()


#set average, number of students and lists of marks and student names/numbers
average=0
countStudents=len(lines)#number student equivalent to number of lines
studentNoList,markList=[],[]
#loop though each line
for line in range(countStudents):
    #get student number and mark by splitting at comma
    studentNo,mark=lines[line].split(",")
    #appent student number/name to student list
    studentNoList.append(studentNo)
    #append mark to mark list and strip the newline character
    markList.append(eval(mark.strip()))
    #increment average
    average+=eval(mark)/countStudents

def standard_dev(mean):
    '''Function that receives mean as parameter and returns standard deviation
    of marks'''
    sd=0
    for line in range(countStudents):
        sd+=(markList[line]-average)**2
    return math.sqrt(sd/countStudents)
#print average and std deviation results formated to 2 dec places
print("The average is: {0:.2f}".format(average))
print("The std deviation is: {0:.2f}".format(standard_dev(average)))
standardDeviation=standard_dev(average)

def advisor():
    '''Function that checks if there are marks less than one standard deviation
    below the mean and returns True if so or False'''
    check=False
    for student in range(countStudents):
        if markList[student]<(average-standardDeviation):
            check=True  
    return check
#if there are students that need to see advisor print their names
if advisor()==True:
    print("List of students who need to see an advisor:")
    for student in range(countStudents):
        if markList[student]<(average-standardDeviation):
            print(studentNoList[student])