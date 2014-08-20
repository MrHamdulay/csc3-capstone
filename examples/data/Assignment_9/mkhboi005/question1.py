""" Tumi Mkhawana
14 May 2014
Assignment 9 Question 1"""

from math import *

filename = input("Enter the marks filename:\n")
f= open (filename, "r" )
lines= f.readlines()
f.close()

#remove \n at ends
for i in range(len(lines)):
   lines[i]= lines[i][:-1]
   
#split names and marks into seperate lists
mark_list= []
name_list= []
for line in lines:
   name, mark = line.split(",")
   mark_list.append(eval(mark))
   name_list.append(name)
   
#create a new variable to add all marks
marks = 0
#m is the mark            
for m in mark_list:
   marks= marks+ (m)

mean= (marks/len(lines))
print("The average is:" ,"{0:.2f}".format(mean))

std_dev= 0

for t in range (len(lines)):
   std_dev+= (mark_list[t] - mean) **2
         
std_dev = sqrt(std_dev/len(lines))

print("The std deviation is:" ,"{0:.2f}".format(std_dev))

x=[]
for n in range(len(lines)):
   if mark_list[n] < mean - std_dev:
      x.append(name_list[n])
if len(x)>0:
   print("List of students who need to see an advisor:")
for h in x:
   print(h)