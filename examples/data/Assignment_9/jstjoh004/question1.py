# Program to determine how student are doing in a subject
# Hendrik Joosten
# 16/05/2014

import math

lines = []
names = []
marks = []

filename = input("Enter the marks filename:\n")
f = open(filename,"r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    pos_comma = lines[i].index(",")
    names.append((lines[i])[:pos_comma])

for j in range(len(lines)):
    pos_comma = lines[j].index(",")
    marks.append((lines[j])[pos_comma+1:])
    if marks[j].count("\n") == 1:
        marks[j] = (marks[j])[:-1]
    marks[j] = int(marks[j])
    
ave = (sum(marks)/len(marks))
print("The average is: {0:.2f}".format(ave))

sd = 0
for k in range(len(marks)):
    sd = sd + (marks[k] - ave)**2
sd = sd/len(marks)
sd = math.sqrt(sd)
print("The std deviation is: {0:.2f}".format(sd))

if sd > 0:
    print("List of students who need to see an advisor:")
    for l in range(len(marks)):
        if ave - marks[l] > sd:
            print(names[l])