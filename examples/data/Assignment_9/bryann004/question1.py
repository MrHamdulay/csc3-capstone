"""analyse student marks to determine who needs to see a student advisor
anna borysova
2014-05-12"""

import math


advisor = [] 

# create list of info from file
infilefile = open(input("Enter the marks filename:\n"), "r")
infile = infilefile.readlines()
infilefile.close()

#create list of marks + count number of marks
marks_list = []
N = 0
for line in infile:
    split = line.split(",")
    #remove newline character
    marks_list.append(int(split[1][:len(line)]))
    N += 1

# calculate mean
mean = sum(marks_list)/N

#calculate standard deviation
stand_dev = 0
for mark in marks_list:
    stand_dev += (mark - mean)**2
stand_dev = math.sqrt(stand_dev/N)

# check what students need advisor
for line in infile:
    split = line.split(",")
    if int(split[1][:len(line)])< mean - stand_dev:
        advisor.append(split[0])


print("The average is:", "{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(stand_dev))
if advisor:
    print("List of students who need to see an advisor:")
    for name in advisor:
        print(name)