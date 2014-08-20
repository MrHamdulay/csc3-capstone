# Assignment 9
# Question 1
# 12 May 2014
# Richard van Gysen
import math
# create empty lists
names = []
marks = []

# get the file
filename = input("Enter the marks filename:\n")
# open and read
f = open(filename, 'r')
lines = f.readlines()
# remove \n
for j in range (len (lines)-1):
    lines[j] = lines[j][:-1]
    
# split lines
for i in range(len(lines)):
    lines[i] = lines[i].split (',')
# append marks and names to each separate list
for i in range(len(lines)):
    names.append(lines[i][0])
    marks.append(lines[i][1])
# find average of marks
total = 0
count = 0
for i in marks:
    total+= eval(i)
    count += 1
if count != 0:
    average = (total/count)
else:
    average= 0
# find standard deviation
sd1= 0
sd2 = 0
for i in marks:
    sd1 += ((eval(i) - average)**2)
    sd2 = math.sqrt(sd1/count)
# print the requirements and results
print("The average is: {:.2f}".format(average))
print("The std deviation is: {:.2f}".format(sd2))
x = False
for i in range(len(marks)):
    if eval(marks[i]) < (average-sd2):
        if x == False:
            print("List of students who need to see an advisor:")
            x = True
        print(names[i])
f.close()