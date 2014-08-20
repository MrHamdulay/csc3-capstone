"""program to analys marks in a file and determine which students have marks less than 1 standard deviation below mean
Kristin Kinmont
9 May 2014"""

import math

#get marks file name
filename = input("Enter the marks filename:\n")

# open file and convert contents to strings
f = open(filename, "r")
lines = f.readlines()
f.close()

# go through marks and calculate mean
total = 0
count = 0
for i in lines:
    line = i.split(",")
    mark = eval(line[1])
    total += mark
    count += 1
average = total/count
average_rounded ='{0:.2f}'.format(average)
print("The average is:", average_rounded)
    
# calculate standard deviation (SD)
add = 0
for i in lines:
    line = i.split(",")
    mark = eval(line[1])
    x = (mark - average)**2
    add += x
SD = math.sqrt(add/count)
SD_rounded ='{0:.2f}'.format(SD)
print("The std deviation is:", SD_rounded)

# print out students with marks less than 1 standard deviation
if SD != 0.00:
    print("List of students who need to see an advisor:")
    for i in lines:
        line = i.split(",")
        mark = eval(line[1])
        if mark < (average - SD):
            print(line[0])