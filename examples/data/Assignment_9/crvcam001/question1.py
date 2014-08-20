# question1.py
# program to analyse student marks read in from a file and determine which students need to see a student advisor
# camilla craven
# 12 may 2014

# import maths library so can use its functions
import math

# get filename from user and open it
filename = input("Enter the marks filename:\n")
f = open(filename, "r")
# read all lines into list and close file
lines = f.readlines()
f.close()

# strip "\n" from each person/mark in list 
for i in range(len(lines)):
    lines[i] = lines[i][:-1]

List = []
Total = 0
marks = []

# split person from mark - creating lists within list
for i in lines:
    List.append(i.split(","))

# add all the numbers to a list called marks       
for i in range(len(lines)):
    marks.append(List[i][1])  

# find the sum of all the marks
for i in marks:
    Total += eval(i)
    
# calculate the mean by dividing total by the number of marks
mean = round(Total/len(List), 2)

# calculate standard deviation by definition given, and round to 2 dec pl
sd_total = 0
for i in marks:
    sd_total += ((eval(i)-mean)**2)
sd = round(math.sqrt(sd_total/len(List)),2)

# print out mean and sd
print("The average is:", format(mean, ".2f"))
print("The std deviation is:", format(sd, ".2f"))

if sd > 0:    
    print("List of students who need to see an advisor:")
    # if a pupil's mark is less than one sd below the mean, print out their name
    for i in range(len(marks)):   
        if eval(List[i][1]) < (mean - sd):
            print(List[i][0])
        else:
            None