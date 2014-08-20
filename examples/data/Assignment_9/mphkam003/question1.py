"""progam to determine which students need to see an advisor
kamogelo mphela
11 may 2014"""

import math
file = input("Enter the marks filename:\n")
f = open(file,"r")
file = f.readlines()
f.close()    
sum = 0
N = 0
list = []
for line in  file:
    mark = eval(line[line.find(',')+1:])
    sum += mark
    N += 1
    list .append(mark)

mean = round(sum/N,2)
print("The average is:", "{0:0<5}".format(mean))
def inside(list):
    """return the inside of the Starndard deviation formula bracket"""
    if len(list)==1:
        return (list[0]-mean)**2
    else:
        return (list[0]- mean)**2 + inside(list[1:])

inside(list)

SD = math.sqrt(inside(list)/N)
std = round(SD,2)
print ("The std deviation is:","{0:0<4}".format(std))

if min(list)< (mean- std):
    
    print ("List of students who need to see an advisor:")

n = 0
for i in list:
    if i < mean - std:
        print(file[n][:file[n].find(',')])
    n += 1
    
