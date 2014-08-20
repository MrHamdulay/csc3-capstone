#Romello Naidoo
#NDXROM005
#Assignment 9
#Question 1

import math
filename=input("Enter the marks filename:\n")
f=open(filename, "r")
x=f.readlines()
f.close()
names=[]
marks=[]
add=0
std=0
for i in range(len(x)):
    name, mark=x[i].split(",")
    marks.append(mark)
    names.append(name)
    add+=int(mark)
 
avg=add/len(x)
print("The average is: {0:.2f}".format(avg))      

for j in range(len(x)):
    std+=(int(marks[j])-avg)*(int(marks[j])-avg)
    
stDev=math.sqrt(std/len(names))
print("The std deviation is: {0:.2f}".format(stDev))
oneStd=(avg-stDev)

z=[]
for k in range(len(x)):
    
    if int(marks[k])<oneStd:
        z.append(names[k])
    else:
        pass
    
if len(z)>0:
    print("List of students who need to see an advisor:")    
    for m in range(len(z)):
        print(z[m])    
else:
    pass