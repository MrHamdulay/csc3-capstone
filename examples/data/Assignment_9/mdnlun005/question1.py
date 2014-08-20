#-------------------------------------------------------------------------------
# Name:        question1
# Purpose:
#
# Author:      Lungelo
#
# Created:     10/05/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import math


filename=input("Enter the marks filename:\n")

f=open(filename,'r')
lst=f.readlines()

f.close()


lines=[]
for i in range(len(lst)):
    lst[i]=lst[i].split(',')
    lines+=lst[i]

for i in range(len(lines)):
    if lines[i][-1::]=='\n':
        lines[i]=lines[i][:-1]


count_of_nums=0
sum_of_nums=0
for i in range(1,len(lines),2):
    count_of_nums+=1
    lines[i]=int(lines[i])
    sum_of_nums+=lines[i]
mean=sum_of_nums/count_of_nums

standard_dev=0
for i in range(1,len(lines),2):
        standard_dev+=((lines[i]-mean)**2)
standard_dev=math.sqrt(standard_dev/count_of_nums)

print("The average is:","{0:.2f}".format(mean))
print("The std deviation is:","{0:.2f}".format(standard_dev))



l=[]
for i in range(1,len(lines)+1,2):
    if lines[i]<mean-standard_dev:
        l.append(lines[i-1])

if len(l)>0:
    print("List of students who need to see an advisor:")
    for i in range(len(l)):
        print(l[i])








