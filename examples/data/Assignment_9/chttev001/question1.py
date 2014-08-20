"""Tevin Chetty
14 May 2014
Program to find the standard deviation and average if a list of marks"""

import math

filename=input("Enter the marks filename: \n")
marks=open(filename, "r")
list_lines=marks.readlines()
marks.close()

names=[]
list_marks=[]
for i in (list_lines):
    for j in range(len(i)):
        if i[j]==",":
            position_comma=j
            names.append(i[0:position_comma])
            list_marks.append(i[position_comma+1:len(i)])
sum_marks=0           
for i in list_marks:
    sum_marks+=eval(i)
average=sum_marks/len(list_marks)

standard=0
for i in range(len(list_marks)):
    x=eval(list_marks[i])
    standard+=(x-average)**2
    n=len(list_marks)
standard_deviation=math.sqrt(standard/n)

print("The average is: {0:.2f}".format(average))
print("The std deviation is: {0:.2f}".format(standard_deviation))
count=0
for i in range (len(list_marks)):
    check=eval(list_marks[i])
    if check<(average-standard_deviation):
        count+=1
if count>0:
    print("List of students who need to see an advisor:")

for i in range (len(list_marks)):
    check=eval(list_marks[i])
    if check<(average-standard_deviation):
        print(names[i])