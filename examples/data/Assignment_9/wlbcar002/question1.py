"""Program to determine when marks are less than one standard deviation below the mean using files
Carla Wilby
10th May 2014"""

import math

filename = input("Enter the marks filename:\n") #Open file to read
file = open(filename, "r")
lines = file.readlines()
file.close()

marks = []

for i in range (len (lines)-1): #Removing newline character
    lines[i] = lines[i][:-1]

for i in range(len(lines)):
    x = lines[i].split(",")    
    marks.append(x[0])  #Appending names and marks to an array
    marks.append(eval(x[1]))
    
total = 0

for i in range(1,len(marks),2): #Adding all marks together
    total += marks[i]
    
mean = total/(len(marks)/2) #Finding average

sum_nth_value = 0
for i in range(1,len(marks),2): #Finding the sum of all marks minus the average
    sum_nth_value += (marks[i] - mean)**2

std_dev = math.sqrt(sum_nth_value/(len(marks)/2)) #The standard deviation

print("The average is: "+"{0:.2f}".format(mean))
print("The std deviation is: "+"{0:.2f}".format(std_dev))


for i in range(1,len(marks),2): #Finding if there are students with marks less than one standard deviation below the mean
    if marks[i] < (mean - std_dev):
        print("List of students who need to see an advisor:")
        break

for i in range(1,len(marks),2): #Finding students with marks less than one standard deviation below the mean
    if marks[i] < (mean - std_dev):
        print(marks[i-1])
    
