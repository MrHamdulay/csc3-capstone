#ASSIGNMENT 9
#QUESTION 1
#NLTWES001

fname=input("Enter the marks filename:\n")

f=open(fname,"r")
lines=f.readlines()
for i in range(len(lines)):
    if "\n" in lines[i]:
        lines[i]=lines[i][:-1]
    for k in lines[i]:
        if k!=",":
            lines[i]=lines[i][1:]
        else:
            lines[i]=lines[i][1:]
            break

import math
sum=0
count=0
for j in lines:
    sum+=eval(j)
    count+=1
average=(sum/count)

variance=0
for c in lines:
    variance+=(eval(c)-average)**2
stddev=math.sqrt(variance/count)

print("The average is:","%.2f"%round(average,2))
print("The std deviation is:","%.2f"%round(stddev,2))

f.close()
f=open(fname,"r")
newlines=f.readlines()
names=[]
for j in newlines:
    line = j.split(",")
    if eval(line[1])<(average-stddev):
        names.append(line[0])

if names!=[]:
    print("List of students who need to see an advisor:")
    for k in names:
        print(k)
        
f.close()