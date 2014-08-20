"""program to analyse student marks with marks less than one standard deviation below the mean
Onalerona Mosimege
13 May 2014"""

import math

myfile= input("Enter the marks filename:\n")

# open and load the data from the file
f= open(myfile,"r")
lines= f.readlines()
f.close()

array= []
names = []

# chop off the trailing carriage returns and get marks from lines
for i in range (len (lines)):
    new = lines[i].split(',')
    array.append(new[1])
    names.append(new[0])
    lines[i] = lines[i][:-1]
    array[i] = array[i][:-1]
    array[i] = int(array[i])

#funtions for calculating the average and standard deviation
def mean(array):
        return sum(array)/len(array)
    
def deviation(array):
        n = len(array)
        m = mean(array)
        total = 0
        for i in range(n):
            total += (array[i]-m)**2
        return math.sqrt(total/n)

average= mean(array)
std_dev= deviation(array)
req = average-std_dev

#check for names below requirement
arrNames = []
for k in range(len(array)):
    if array[k] < req:
        arrNames.append(names[k])

#print results    
r = '{0:0.2f}'
print("The average is:",r.format(average))
print("The std deviation is:",r.format(std_dev))
if len(arrNames) > 0:
    print("List of students who need to see an advisor:")
    for b in range(len(arrNames)):
        print(arrNames[b])
