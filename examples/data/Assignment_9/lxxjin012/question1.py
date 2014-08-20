#a Python program to analyse student marks read in from a file and determine which students need to see a student advisor
#Jenny Luo
#13 May 2014

import math

#open the text file and calculate the mean of the marks
file=input("Enter the marks filename:\n")
f=open(file, "r")

total=0
divisor=0
for line in f:
    for i in range(len(line)):
        if line[i]==",":
            total+=int(line[i+1:])
        else:
            pass
    divisor+=1
average=total/divisor
print("The average is:", "{0:.2f}".format(average))
f.close()  #close the file

#open the text file and get the marks separated to be worked with
f=open(file, "r")
marks=[]
for line in f:
    for i in range(len(line)):
        if line[i]==",":
            mark=int(line[i+1:])
            marks.append(mark)
        else:
            pass        
f.close()  #close the file

#open the text file and calculate the standard deviation
f=open(file, "r")
total1=0
for i in range(len(marks)):
    x=(int(marks[i])-average)**2
    total1+=x
deviation=math.sqrt((total1)/len(marks))
print("The std deviation is:","{0:.2f}".format(deviation) )
f.close()   #close the file


#open the file and find the name that mathches with the mark in the list
f=open(file, "r")
x=f.readlines()
name=[]
for i in range(len(x)):
    y=x[i].split(",")
    name.append(y[0])   #append all the students names into a list


alist=[]
for i in range(len(marks)):
    if marks[i]<(average-deviation):
        alist.append(name[i])
if deviation == "0.00":
    pass
else:
    if len(alist)>0:
        print("List of students who need to see an advisor:")
        for i in alist:
            print(i)

f.close()  #close the file