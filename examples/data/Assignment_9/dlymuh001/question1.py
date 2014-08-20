"""Program to read the marks of students from a text file and decide who should see an advisor
Muhammad Nabeel Dulymamode
11/05/2014"""
import math

filename = input("Enter the marks filename:\n")
studentfile = open(filename,"r")
studentmarks = {}
studentnames = []
summark = 0
sumsqmark = 0
for line in studentfile:
    studrec = line.split(",")
    name = studrec[0]
    mark = int(studrec[1])
    studentnames.append(name)
    studentmarks[name] = mark
studentfile.close()
#Calculate sum of marks and sum of squares of marks
N = 0
for name in studentnames:
    N += 1
    summark += studentmarks[name]
    sumsqmark += studentmarks[name]**2
#Calculate mean and standard deviation of marks
mean = summark/N
stdev = math.sqrt(sumsqmark/N - mean**2)
lowerlimit = mean - stdev
#Output mean and standard deviation
print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(stdev))
#Decide which students need to see an advisor
printmsg = True
for student in studentnames:
    if studentmarks[student] < lowerlimit:
        if printmsg:
            print("List of students who need to see an advisor:")
            printmsg = False
        print(student)