"""PRIYANKA GOBERDHAN
ASSIGNMENT 9 - QUESTION ONE
14/05/14"""

import math

file_name=input("Enter the marks filename:\n")
f = open(file_name,"r")
lines = f.readlines()

grade = []
names = []
mean = 0

for i in range(len(lines)):
    grade.append(lines[i].split(',')[1].split("\n")[0])
    names.append(lines[i].split(',')[0])
    grade[i] = int(grade[i])
    mean += grade[i]
    
mean = mean/len(grade)
stan_dev = 0

for i in range(len(grade)):
    stan_dev += (grade[i]-mean)**2
stan_dev = math.sqrt(stan_dev/len(grade))
print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(stan_dev))

student = False

for i in range(len(grade)):
    if(grade[i] < (mean-stan_dev)):
        student=True
        
if(student):
    print("List of students who need to see an advisor:")
    for i in range(len(grade)):
        if(grade[i] < (mean-stan_dev)):
            print(names[i])
