__author__ = 'George de Kock'
"""Program to analyse student marks read in from a file and determine which students need to see a student advisor.
2014-05-12"""

import math

filename = input("Enter the marks filename:\n")
studentnos = []
marks = []
f = open(filename,"r")
count = 0
total = 0
for line in f:
    comma = line.find(",")
    studentnos.append(line[0:comma])
    marks.append(eval(line[comma+1:comma+3]))
    total += marks[count]
    count += 1
f.close()
avg = total/count
print("The average is: {:.2f}".format(round(avg,2)))
sumsqrt = 0
for mark in marks:
    sumsqrt += (mark-avg)**2
sd = math.sqrt(sumsqrt/count)

print("The std deviation is: {:.2f}".format(round(sd,2)))

advisor = []
for i in range(len(marks)):
    if marks[i] < (avg-sd):
        advisor.append(studentnos[i])

if len(advisor) != 0:
    print("List of students who need to see an advisor:")
    for a in advisor:
        print(a)
