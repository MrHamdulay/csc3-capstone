"""calculate class average, standard deviation, and list student who need to see an advisor
blessings hadebe
15 may 2014"""

import math
filename=input("Enter the marks filename:\n")

f=open ( filename, "r")
list= f.readlines()
f.close

names=[]
marks=[]
for i in range(len(list)):
    entry=list[i].split(",")
    names.append(entry[0])
    marks.append(eval(entry[1])) 
    
def mean(marks):
    sum=0
    for i in range(len(marks)):
        sum+=marks[i]
    mean=sum/len(marks)
    return "{0:.2f}".format(mean)

def stdDev(marks):
    variance=0
    for i in marks:
        variance+=((i - eval(mean(marks))))**2
    dev=math.sqrt(variance/len(marks))
    return "{0:.2f}".format(dev)

def need_advice(names,marks):
    list=[]
    for i in range(len(marks)):
        if marks[i] < (eval(mean(marks)) - eval(stdDev(marks))):
            list.append(names[i])
    return list
   
print("The average is:", mean(marks))
print("The std deviation is:", stdDev(marks))
if need_advice(names,marks):
    print("List of students who need to see an advisor:")
    for i in need_advice(names,marks):
        print(i)

