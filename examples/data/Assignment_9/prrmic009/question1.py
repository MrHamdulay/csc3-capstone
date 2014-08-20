"""Program to calculate the mean and standard deviation of marks obtained by students from an input
file, and to calculate and list which of those students should see a student advisor
Mick Perring
16 May 2014"""

import math

file = input("Enter the marks filename:\n")  # user inputs a filename (of file that contains student names and marks)

f = open(file, "r")    # program opens input file, records data from file and closes file
lines = f.readlines()
f.close()

list_marks = []
list_names = []

for i in range(len(lines)-1):  # removes trailing carriage returns from end of each line
     lines[i] = lines[i][:-1]
     
for i in range(len(lines)):  # splits original list into seperate strings and appends marks to marks list and names to names list
     list_temp = lines[i].split(",")
     list_marks.append(int(list_temp[1]))
     list_names.append((list_temp[0]))
     
sumM = 0

for i in list_marks:  # calculates sum of marks
     sumM += i
     
aveM = sumM/len(list_marks)  # calculates average of marks

print("The average is: {0:.2f}".format(aveM))  # prints average of marks to 2 decimal places

stdDev_pre = 0

for i in list_marks:   # calculates 'first part' of standard deviation 
     stdDev_pre += (i - aveM)**2
     
stdDev = math.sqrt(stdDev_pre/len(list_marks))  # calculates standard deviation, using 'first part'

print("The std deviation is: {0:.2f}".format(stdDev))  # prints standard deviation to 2 decimal places

advise = aveM - stdDev  # calculates min mark to obtain to avoid student advisor

count_advise = 0

for i in range(len(lines)):  # counts number of students requiring advisor
     if list_marks[i] < advise:
          count_advise += 1

if count_advise > 0: 
     print("List of students who need to see an advisor:")

for i in range(len(lines)):  # prints out student names needing advisor
     if list_marks[i] < advise:
          print(list_names[i])