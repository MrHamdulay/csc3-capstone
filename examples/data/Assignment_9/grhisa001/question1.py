"""Bella Gorham
makr checker
15/05/14"""


import math
#input of filename
file = input("Enter the marks filename:\n")
names = []
marks = []
sum = 0
num = 0

#create list of lines from marks file
f = open(file, 'r')
lines = f.readlines()
f.close()

#seprate the lines by ,
for i in range(len(lines)):
    lines[i] = lines[i].split(",")


#make a names list and a marks list    
for i in range(len(lines)):
    names.append(lines[i][0])
    marks.append(lines[i][1])
    
marks[len(marks)-1] = marks[len(marks)-1]+"\n"
    

#remove all \ns
for i in range(len(marks)):
    marks[i] = int(marks[i][:-1])
    

#work out average by summing marks and div them
for i in range(len(marks)):
    sum += marks[i]
mean = round(sum/len(marks),2)

#work out std dev

for i in range(len(marks)):
    num += (marks[i] - mean)**2

stddev = round(math.sqrt(num/len(marks)),2)
    
print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % stddev)

risk = mean - stddev

# work out who needs to see an advisor
for i in range(len(marks)):
    if marks[i] < risk:
        print("List of students who need to see an advisor:")
        break
    
for i in range(len(marks)):
    if marks[i] < risk:
        print(names[i])