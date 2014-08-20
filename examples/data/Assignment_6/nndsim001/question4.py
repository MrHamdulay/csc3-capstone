# This program takes in a list of marks (separated by spaces) and outputs
# a histogram representation of the marks according to the mark categories at UCT:
#        fail < 50%
#        50% <= 3rd < 60%
#        60% <= lower 2nd < 70%
#        70% <= upper 2nd < 75%
#        1st >= 75%

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 22 April 2014

marks = input("Enter a space-separated list of marks:\n").split(" ")
gradedict = {'1':0,'2+':0,'2-':0,'3':0,'F':0}
grades = []
labels = ['1','2+','2-','3','F']

# categorize the marks into their correct grades
for mark in marks:
    if int(mark) < 50:
        grades.append("F")
    elif int(mark) >= 50 and int(mark) < 60:
        grades.append("3")
    elif int(mark) >= 60 and int(mark) < 70:
        grades.append("2-")
    elif int(mark) >= 70 and int(mark) < 75:
        grades.append("2+")
    else: grades.append("1")

# store marks grade counts to the dictionary
for i in grades:
    gradedict[i] += 1

# print the histogram
for label in labels:
    print("{0:<2}|{1}".format(label,"X"*gradedict[label]))

#Sample I/O:

#Enter a space-separated list of marks:
#12 23 34 45 56 67 78 89 90
#1 |XXX
#2+|
#2-|X
#3 |X
#F |XXXX