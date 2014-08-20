"""Assignment 9 question 1 Determine which students need to see an advisor
Ross van der Heyde VHYROS001
10 May 2014"""
import math

def average(data):
    """Calculates the average of the data supplied"""
    sum =0
    for i in data:
        sum+=i
    return sum/len(data)

def stdDev(data):
    """Calculates standard deviation of data in list supplied"""
    sum = 0
    ave = average(data)
    for i in data:
        sum += (i-ave)**2
    return math.sqrt(sum/len(data))    
    
def advisor(names, marks, ave, sDev):
    """Returns list containing indices of students who need to see an advisor"""
    boundary = ave-sDev
    indexes= []
    for i in range(len(names)):
        if marks[i]<boundary:
            indexes.append(i)
    return indexes

#MAIN
fName = input("Enter the marks filename:\n")
#fName = "test1.txt"
names = []# array to store names of students
marks = []# array to store students' marks

#read in file 1 line at a time, split line into arrays for names and marks
f = open(fName, "r")
line = f.readline()
while line != "":
    temp = line.split(",")
    names.append(temp[0])
    marks.append(eval(temp[1]))
    line = f.readline()
f.close()

output = "{:.2F}"
ave = average(marks)
print("The average is:", output.format(ave))
sDev = stdDev(marks)
print("The std deviation is:", output.format(sDev))

#Determine studente that need to see an advisor
students = advisor(names, marks, ave, sDev)
if len(students) >0:
    print("List of students who need to see an advisor:")
    for i in students:
        print(names[i])