# Python program to analyse student marks read in from a file and determine which students need to see a student advisor.
# Badugela Mulisa
# 12 May 2014

import math
name=input('Enter the marks filename:\n')            # user inputs file name
f=open(name,'r')                                     # open file
shedule = {}                                         # create new student, mark dictionary
for line in f:
    k, v = line.strip().split(',')                   # line 10 - 12 converts the string file into a dictionary
    shedule[k.strip()] = v.strip()
    dict((k, int(v)) for k, v in shedule.items())
f.close()                                            # close file

add=0
add2=0
for i in shedule:                                    # add each value of dictionary to find sum
    add+=int(shedule[i])
average = add/len(shedule)                           # get average/mean by dividing sum of all values by nummber of values
for j in shedule:                                    
    add2 += (int(shedule[j])-average)**2             # finds the sum of (x-mean)^2 for each x value
std = math.sqrt(add2/len(shedule))                   # find the standard deviation

print('The average is:',"{:.2f}".format(average))
print('The std deviation is:',"{:.2f}".format(std))
if std == 0.00:
    print('',end='')
else: 
    one_std = average - std                                              
    shedule2={}                                          # line 28 - 30 creates new dictionary with reversed key-value pair of 1st dictionary
    print('List of students who need to see an advisor:')
    for k in shedule:
        shedule2[shedule[k]]=k
        if int(shedule[k]) < one_std:                    # find the name of the leaner who must see student advisor
            print(shedule2.get(k,k))  