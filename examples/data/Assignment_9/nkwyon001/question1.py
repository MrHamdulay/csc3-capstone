"""a Python program to analyse student marks read in from a file 
Yondela Nkwali
15 May 2014"""

name=input("Enter the marks filename:\n")

import math

listmarks=[]
file=open(name,"r")
line=file.readlines()
file.close()
newlist=[]
list2=[]
listn=[]
for i in range(len(line)):
    eachline=line[i]
    sline=eachline.split(",")
    marks=sline[1]
    names=sline[0]
    listnames=names.split()
    listn.append(listnames)
    listmarks=marks.split()
    newlist.append(listmarks)
for i in newlist:
    for j in i:
        list2.append(int(j))
no=(len(list2))
count=0
for i in list2:
    count+=i
av=(count/no)
partstd=0
for k in range(len(list2)):
    partstd+=(list2[k]-av)**2
std=math.sqrt(partstd//no)
required=av-std
print("The average is:","%1.2f " % av)
print("The std deviation is:","%1.2f " %std)
student=0
value=False

for mark in list2:
    if mark<required:
        x=list2.index(mark)
        student =listn[x][0]
        value=True
if value:
    print("List of students who need to see an advisor:")
for mark in list2:
    if mark<required:
        x=list2.index(mark)
        student =listn[x][0]
        print(student)
