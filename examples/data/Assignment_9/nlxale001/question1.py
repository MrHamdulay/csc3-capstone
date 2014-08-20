#Author: NLXALE001
#Date: 13 May 2014
#Assignment 9


import math

filename = input("Enter the marks filename:\n")

#separate file into names and marks
names = []
marks = []
f = open(filename, "r")
for line in f:
    both = line.split(",")
    names.append(both[0])
    marks.append(both[1])
f.close()

#find total amount of marks to find average
total = 0
for i in marks:
    total += eval(i)

#calculate average
average = total/len(marks)
average = round(average, 2)

print ("The average is: %.2f" % average)

#calculate sd
sdcalc = 0
for i in marks:
    sdcalc += (eval(i)-average)*(eval(i)-average)

sdcalc = sdcalc/len(marks)

sdcalc =  math.sqrt(sdcalc)
sdcalc = round(sdcalc, 2)

print ("The std deviation is: %.2f" % sdcalc)

#find who needs to bwe worried or not
worry = average-sdcalc
worrylist = []

for i in marks:
    if eval(i)<worry:
        index = marks.index(i)
        worrylist.append(names[index]) 

if (len(worrylist) > 0):
    print("List of students who need to see an advisor:")
for i in worrylist:
    print(i)
            
            
