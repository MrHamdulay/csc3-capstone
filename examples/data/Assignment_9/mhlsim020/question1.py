"""program to analyse student marks read in from a file
Simlindile Mahlaba
14 May 2014"""

import math
fname=input("Enter the marks filename:\n")
sum=0
count=0
my_marks=[]
total=0
names_lst=[]
ifstate=0
try:
    o=open(fname,"r") 
    for line in o:
        mark=eval(line[line.index(",")+1:line.index(",")+3])
        fname1=line[:line.index(",")]
        names_lst.append(fname1)
        my_marks.append(mark)
        sum=sum+mark
        count+=1
    average=round((sum*100/count)/100, 2)
    for i in range(count):
        total=total+((my_marks[i]-average)**2)
    sd=round(math.sqrt(total/count), 2)
    print("The average is:",average)
    print("The std deviation is:",sd)
    for b in range(count):
        if my_marks[b]<sd: 
            ifstate+=1
    if ifstate>0:
        print("List of students who need to see an advisor:")
    for a in range(count):
        if my_marks[a]<sd:
            print(names_lst[a])
except IOError as err:
    print("({})".format(err))