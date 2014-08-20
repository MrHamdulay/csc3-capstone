#Thea Sitek, STKTHE002
#16.05.2014
#Find out who needs compsci help based on gradelist

import math 
file = input('Enter the marks filename: \n')

#read file
f = open(file, "r")
grades = f.readlines()
f.close()

#create variables
sumave = 0
count = 0
gradelist = []

#read grades and calcualte average
for i in range(len(grades)):
    grade = grades[i].split(',')
    grade = eval(grade[-1])
    
    count += 1
    sumave += grade
    gradelist.append(grade)

average = sumave/count

#calculate standard deviasion
sumstd = 0
for j in gradelist:
    sumstd += ((j - average)**2)
    
std = math.sqrt(sumstd/count)

#output    
print('The average is:', "%.2f" %average)
print('The std deviation is:', "%.2f" %std)  

#locate students matching grades
grade = 0
count = 0
for i in range(len(grades)):
    person = grades[i].split(',')
    grade = eval(person[-1])
    if grade < (average - std):
        if count == 0:
            #print this line only once and only if any students need advisor
            print('List of students who need to see an advisor:')    
            count += 1
        #print all names
        print(person[0])