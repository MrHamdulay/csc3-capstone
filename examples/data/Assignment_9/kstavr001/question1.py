#Assignment 9, Question 1
#Avreyna Kistensamy
#10 May 2014

import math

markfile = input("Enter the marks filename:\n")

f = open (markfile, "r")
students = f.readlines()
f.close()

marks = []
for line in students:
    x = line.find(",")
    learner_mark = line[x+1:x+3]
    marks.append(eval(learner_mark))

#Calculating the average of the marks
total = 0
n = 0
for i in marks:
    total += i
    n += 1
xbar = total/n

#Calculating stdev
sq = 0
for i in marks:
    sq += (xbar-i)**2
stdev = math.sqrt(sq/n)

#Finding problem marks
counsellor = []
for i in marks:
    if i < xbar-stdev:
        y = students[marks.index(i)].find(",")
        counsellor.append(students[marks.index(i)][:y])

print("The average is:", "{0:.2f}".format(xbar))
print("The std deviation is:", "{0:.2f}".format(stdev))
if counsellor != []:
    print("List of students who need to see an advisor:")
    for i in counsellor:
        print(i)




    