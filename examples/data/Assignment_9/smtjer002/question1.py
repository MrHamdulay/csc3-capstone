"""A program to determine the average and standard deviation from a list of marks in a file, and to print out a list of students who are below one standard deviation of the average
by Jeremy Smith SMTJER002
15 May 2014"""

import math

#input the file name and copy the contents of the file to a list
filename = input("Enter the marks filename:\n")
f = open(filename, "r")
lines = f.readlines()
f.close()

#count the number of marks in the list, excluding empty lines
count = 0
for line in lines:
    if line != "" or line != "\n":
        count += 1

names=[]
marks=[]
list_1=[]
#remove the \n that occurs at the end of each string in the list
for line in lines:
    if line[-1] == '\n':
        list_1.append(line[0:-1])
    else:
        list_1.append(line)
#split the list into two lists, a list of names and a list of the associated marks, so that each name index is associated with the correct mark index
for i in range(len(list_1)):
    x = list_1[i].split(',')
    names.append(x[0])
    marks.append(x[1])

#calculate the total marks and divide this by the number of marks to determine the average
total = 0
for i in marks:
    total+= int(i)
average = total / count
print("The average is:", '{0:.2f}'.format(average))

#calculate the standard deviation
std_dev = 0
for i in range(count):
    std_dev += (int(marks[i]) - average)**2
std_dev = math.sqrt(std_dev/count)
print("The std deviation is:", '{0:.2f}'.format(std_dev))

#print a list of students who's mark is below 1 std deviation of the average
mark_check = False
for i in range(count):
    if int(marks[i]) < (average-std_dev):
        mark_check = True
        
if mark_check:        
    print("List of students who need to see an advisor:")
    for i in range(count):
        if int(marks[i]) < (average-std_dev):
            print(names[i])