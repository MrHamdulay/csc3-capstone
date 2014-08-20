"""a program to analyse student marks read from a file and determine which students need to see a student advisor
Zikho Godana
13 May 2014"""

import math

filename=input("Enter the marks filename:\n")
file=open(filename,"r")
lines=file.readlines()
file.close()
marks_list=[]
names=[]
positions=[]

#create lists of important parameters to be used 
for i in range (len(lines)):
    lines[i] = lines[i][:-1] #get rid of the "\n" character printed at the end of each item in lines
    if "," in lines[i][len(lines[i])-2:]:
        mark=lines[i][len(lines[i])-1:]
        name=lines[i][:len(lines[i])-2]
    else:
        mark=lines[i][len(lines[i])-2:]
        name=lines[i][:len(lines[i])-3]
    marks_list.append(mark)
    names.append(name)

#calculate the mean and the standard  deviation
sum=0
sum_a=0

for j in marks_list:
    sum+=int(j)
average=sum/len(marks_list)

for k in marks_list:
    a=(int(k)-average)**2
    sum_a+=a
stdev=math.sqrt(sum_a/len(marks_list))

limit=average-stdev

output="{name:.2f}"#format the answers to two decimal places
print("The average is:",output.format(name=average))
print("The std deviation is:",output.format(name=stdev))
if len(marks_list)>1:
    print("List of students who need to see an advisor:")
    
for mark in marks_list:
    if int(mark)<limit: 
        position=marks_list.index(mark)
        positions.append(position)
        for ind in positions:
            student=names[ind]
        print(student)