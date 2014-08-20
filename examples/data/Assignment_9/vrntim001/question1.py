''' student advisors
Tim Mostert
13.05.14'''

import math

filename = input("Enter the marks filename:\n")
f = open(filename,"r")
namearray = f.readlines()
f.close()
numbers = []
names = []
total = 0
for i in range(len(namearray)):
    a = namearray[i].split(",")
    numbers.append(eval(a[1]))
    names.append(a[0])
    total += eval(a[1])
average = ("{0:.2f}".format(total/len(numbers)))
averagenum = eval(average)
stddev = 0
for i in numbers:
    stddev += ((i)-averagenum)**2
stddev = ("{0:.2f}".format(math.sqrt((stddev)/len(numbers))))
stddevnum = eval(stddev)
needadv = []
for i in range(len(numbers)):
    if numbers[i] < averagenum-stddevnum:
        needadv.append(names[i])
print("The average is:", average)  
print("The std deviation is:", stddev)
if len(needadv) > 0:
    print("List of students who need to see an advisor:")
for i in needadv:
    print(i)