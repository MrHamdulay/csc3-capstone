"""Program to determine weather a student needs to see a student advisor based on marks from a read file
Dean Gracey
10 May2014"""

import math

file = input("Enter the marks filename:\n")
f = open(file,"r")
marks=f.readlines()
f.close()

for i in range (len(marks)-1):
    marks[i] = marks[i][:-1]

#calc avearge
avg = 0
num_marks=len(marks)
for student in marks:
    sepperate = student.split(",")
    avg = avg + int(sepperate[1])
avg = avg/num_marks

print("The average is:",("{0:.2f}".format(avg)))

#calc standard deviation
deviation = 0
for student in marks:
    sepperate = student.split(",")
    mark = int(sepperate[1])
    deviation = deviation + (mark-avg)**2

deviation = math.sqrt(deviation/num_marks)

print("The std deviation is:","{0:.2f}".format(deviation))




#students who need to see an advisor
advisor = False
advistudents = []
for student in marks:
    sepperate = student.split(",")
    if int(sepperate[1]) < avg-deviation:
        advisor = True
        advistudents.append(sepperate[0])
        
#Print students who need to see an advisor
if advisor:
    print("List of students who need to see an advisor:")
    for student in advistudents:
        print(student)

