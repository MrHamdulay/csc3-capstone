#Riya Desai
#Assignment 9 - Question 1
#15 May 2014


import math

marksfile=input("Enter the marks filename:\n")

#open file to read only
f = open(marksfile,"r")

#read lines in the file
lines=f.readlines()

marks=[]

names=[]
average=0


for i in range(len(lines)):
    marks.append(lines[i].split(',')[1].split("\n")[0])
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    average+=marks[i]

average=average/len(marks)

#set the standard deviation to 0
standard_deviation=0


#work out the standard deviation
for i in range(len(marks)):
    standard_deviation+=(marks[i]-average)**2
standard_deviation=math.sqrt(standard_deviation/len(marks))



print("The average is:","{:.2f}".format(average))
print("The std deviation is:","{:.2f}".format(standard_deviation))

check=False

#check if the mark is lower than the standard deviation
for i in range(len(marks)):
    if(marks[i]<(average-standard_deviation)):
        check=True


if(check):
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if(marks[i]<(average-standard_deviation)):
            print(names[i])
