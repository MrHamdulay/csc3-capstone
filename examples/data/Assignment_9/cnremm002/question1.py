"""Check which students are failing/doing badly
Emmanuel Conradie
16 May 2014"""

import math

#Enter file
filename = input("Enter the marks filename:\n")

#Read file
f = open (filename, "r")
lines = f.readlines()
f.close()

#Temp list
alist = []

#New list
clist = []

#Fail list
elist = []

#Create temp list
for i in lines:
    alist.append(i)

#Chop off \n
for i in range (len(alist[:-1])):
    alist[i] = alist[i][:-1]

#Create new list
for i in alist:
    blist = i.split(",")
    clist.append(blist)

#Calculate mean
mean = 0
for i in clist:
    x = int(i[1])
    mean += ((x)/len(clist))

#Calculate standard eviation and add calculations within squareroot
s = 0
for i in clist:
    y = int(i[1])
    s += (((y-mean)**2)/len(clist))

#Square answer
sd = math.sqrt(s)

#Print results
print ("The average is:", ("%.2f" % mean))
print ("The std deviation is:", ("%.2f" % sd))

#Create failure list
for i in clist:
    if int(i[1]) < (mean - sd):
        elist.append(i[0])

#Check for failures
if len(elist) != 0:
    print ("List of students who need to see an advisor:")

#Print failures
for i in elist:
    print (i)