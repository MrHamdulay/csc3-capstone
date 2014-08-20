"""Python program to analyse student marks read in from a file and determine which students need to see a student advisor.
John Odetokun
11 May 2014"""

import math


filename= input("Enter the marks filename:\n")
f = open( filename, "r")
list = []
for line in f:
    list.append(line)
f.close()

nlist = [] 
for i in range(len(list)):
    lin  = list[i].split(",")
    nlist.append(lin)

marks = 0
for j in range(len(nlist)):
    marks += eval(nlist[j][1])

average = marks / len(list)
print("The average is:", "{0:.2f}".format(average))

meansum = 0
for k in range(len(list)):
    meansum += (eval(nlist[k][1]) - average)**2

meansum = meansum / len(list)
dev = math.sqrt(meansum)
print("The std deviation is:", "{0:.2f}".format(dev))
     
minmark = average - dev
studentadvlist = []
for a in range(len(list)):
    if (eval(nlist[a][1]) < minmark):
        studentadvlist.append(nlist[a][0])
if len(studentadvlist) != 0:
    print("List of students who need to see an advisor:")
    for k in studentadvlist:
        print(k)
    