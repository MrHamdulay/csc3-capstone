"""Assignement 9, Question 1
Tejasvin Bagirathi
Program to analyse standard deviation of marks"""
import math
#User inputs file name, file is opened read in and then closed
inFile = input('Enter the marks filename:\n')
f = open(inFile, 'r')
lines = f.readlines()
f.close

#Initialise 2 variables for sum of all marks and the number of marks
tot_mark = float(0)
mark_num = 0
marks = []
for line in lines:
    #Split up the lines individually to get marks on their own
    mark = line[line.find(',')+1:]
    #Convert mark to int, then add mark to total mark
    marks.append(int(mark))
    #Add one to number of marks
    mark_num += 1

#Calculate and print average
for i in marks:
    tot_mark += i
    
average = tot_mark/mark_num
print('The average is: {0:0.2f}'.format(average))

#Create new variable for deviation
tot_deviation = 0

#Calculate standard deviation
for i in marks:
    std_deviation = float(i-average)**2
    tot_deviation += std_deviation
    
#Divide above answer by number of marks to get standard deviation
final_deviation = math.sqrt(tot_deviation/mark_num)
print('The std deviation is: {0:0.2f}'.format(final_deviation))

#Deterimne if any students need to be on fail list
fail_list = []
for j in lines:
    mark = int(j[j.find(',')+1:])
    if mark < (average-final_deviation):
        fail_list.append(j[:j.find(',')])
#If fail list is not empty, then print out the students who need to see a student advisor
if len(fail_list) > 0:
    print('List of students who need to see an advisor:')
    for i in fail_list:
        print(i)