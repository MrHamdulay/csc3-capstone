#Lauren de Bruyn DBRLAU003
#Analyse student marks read in from a file and determine which students with marks less than one standard deviation below the mean.
#10 May 2014

import math
marks=[]

filename= input("Enter the marks filename: \n")

f = open (filename, "r")
lines = f.readlines ()
f.close ()

#strip lines of "\n"
for i in range (len (lines)):
    if lines[i][-1]== "\n":
        lines[i] = lines[i][:-1]

#create list for each student and their respective mark
for i in range (len (lines)):
    lines[i]=(lines[i].split (','))

#create list of marks to calculate mean and standarddev
for i in range(len(lines)):
    marks.append(eval(lines[i][1]))

#calculate the mean
averagemark=sum(marks)/len(marks)

#calculate the variation
variation=0
for i in marks:
    variation += (i-averagemark)**2

#calculate the standard deviation
standarddev = math.sqrt(variation/len(marks))

print("The average is:","{0:.2f}".format(averagemark))
print("The std deviation is:","{0:.2f}".format(standarddev))

#check to see which students have marks more than one standard deviation below the mean
students=[]
for i in range(len(lines)):
    if eval(lines[i][1])< averagemark-standarddev:
        students.append(lines[i][0])
        
if len(students)>0:
    print("List of students who need to see an advisor:")

for i in students:
    print(i)
