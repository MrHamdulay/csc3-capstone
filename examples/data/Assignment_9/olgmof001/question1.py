"""Tofunmi Olagoke
OLGMOF001
Programme on average an standard deviation"""

import math

f=input("Enter the marks filename:\n")
thefile=open(f,"r")
lines=thefile.readlines()
thefile.close()

names=[]
sumofmarks=0
no_marks=0
deviation=0

#finding the components to find standard deviation and mean
for p in lines:
    y=p.index(",")
    name=p[0:y]
    names=names+[name]
    mark=p[y+1:]
    sumofmarks+=int(mark)
    no_marks+=1



for t in lines:
    y=t.index(",")
    mark=t[y+1:]
    deviation+=(int(mark)-(sumofmarks/no_marks))**2

    
average=sumofmarks/no_marks
print("The average is:",'{:.2f}'.format(average))
standard_deviation=math.sqrt(deviation/no_marks)
print("The std deviation is:", '{:.2f}'.format(standard_deviation))


#finding the dvisor names
names=[]
for i in lines:
    y=i.index(",")
    pre=i[y+1:] 
    mark=int(pre)
    name=i[0:y]
    if mark<(average-standard_deviation):
        names=names+[name]
print("List of students who need to see an advisor:")
for l in names:
    print(l, end=" ")

