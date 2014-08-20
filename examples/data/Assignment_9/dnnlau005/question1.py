"""analyse student marks read in from a file
Lauren Denny
11 May 2014"""

import math

filename=input("Enter the marks filename:\n") #get filename

f=open(filename, "r")
lines=f.readlines() #read file into lines as a list of strings
f.close()

for i in range(len(lines)):
    lines[i]=lines[i][:-1] #get rid of "\n" at end of each line
    lines[i]=lines[i].split(",") #split name and mark which are separated by a ","

SUM=0
for i in range(len(lines)):
    SUM+=eval(lines[i][1]) #add up all marks i.e. all the elements in poisition [i][1] of lines
average=SUM/len(lines)

SD_sum=0
for i in range(len(lines)):
    SD_sum+=(eval(lines[i][1])-average)**2 #add up the squares of the differences between each mark and the average
SD =math.sqrt(SD_sum/len(lines))

f_string="{0:.2f}" #format string to print out a number to 2 decimal places

print("The average is:",f_string.format(average))
print("The std deviation is:",f_string.format(SD))

problem_students=[]
for i in range(len(lines)):
    if eval(lines[i][1])<(average-SD):#if the mark is less than 1 standard of the mean below the average
        problem_students.append(lines[i][0])#append the name of the person with that mark to problem_students

if len(problem_students)!=0: #if there are any problem students
    print("List of students who need to see an advisor:")
    for i in range(len(problem_students)):
        print(problem_students[i])