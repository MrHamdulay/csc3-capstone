'''dario pillay
10/05/14'''

from math import sqrt

file=input("Enter the marks filename:\n")

#Open file, access required content, then close
f=open(file, "r")
lines=f.readlines()
f.close()

indivmark=''
names=[]
marks=[]

#split marks and names into separate lists to be evaluated.
for part in lines:
    part=part.split(",")
    names.append(part[0])
    for i in part[1]:
        if i.isdigit():
            indivmark+=i
    indivmark=int(indivmark)
    marks.append(indivmark)
    indivmark=''

#Calculate average of marks then print
tot,n=0,0
for m in marks:
    tot+=m
    n+=1
average=tot/n

print("The average is:",'{0:.{1}f}'.format(average, 2))

#Calculate then print standard deviation of marks
stdev=0
for m in marks:
    stdev+=(m-average)**2
stdev=sqrt(stdev/n)

print("The std deviation is:",'{0:.{1}f}'.format(stdev, 2))

#Determine which students must be advised then print
adv_stud=[]
for i in range(len(marks)):
    if marks[i]<(average-stdev):
        adv_stud.append(names[i])

if adv_stud!=[]:    
    print("List of students who need to see an advisor:")
for i in adv_stud:
    print(i)