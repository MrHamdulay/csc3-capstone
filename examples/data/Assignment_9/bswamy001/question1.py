"""Amy Bosworth
Assignment 9
Question 1
12 May 2014"""

import math

#Get file and read it
file=input("Enter the marks filename:\n")
f=open(file, "r")
lines= f.readlines()
f.close

#remove new line character
for i in range(len(lines)):
    lines[i]=lines[i][:-1]

#split by comma and store in a 2D array
marks=[]
for line in lines:
    tempsplit= line.split(",")
    marks.append(tempsplit)

#get sum of grades 
total=0
for j in range(len(marks)):
    total+= eval(marks[j][1])
    
#Calculate and print mean
mean= total/len(lines)
print("The average is:", "{0:.2f}".format(mean)) #mean calculation

#standard deviation
numerator=0
for j in range(len(marks)):
    numerator+= (eval(marks[j][1])-mean)**2

standard_deviation= math.sqrt(numerator/len(marks))
print("The std deviation is:","{0:.2f}".format(standard_deviation))

#Check if a student advisor is needed at all
failing_students = False
for i in range(len(marks)):
    if eval(marks[i][1])< mean-standard_deviation:
            failing_students= True
            
if failing_students== True:
    print("List of students who need to see an advisor:")

#Check which students need student advisors
for i in range(len(marks)):
    if eval(marks[i][1])< mean-standard_deviation:
        print(marks[i][0])



