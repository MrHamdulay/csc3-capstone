#HLNCEC001
#Assignment9
#Question1
#Files

text = input("Enter the marks filename:\n")
f = open(str(text),"r")
lines = f.readlines()
f.close()

for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]
    
L = []    
for j in range(len(lines)):
    fields = lines[j].split(',')
    L.append(fields)
    
total = 0    
for x in range(len(L)):
    mark = L[x][1]
    total+=int(mark)
avg = total/len(L)
print('The average is:','{0:1.2f}'.format(avg))

import math
std = 0
for y in range(len(L)):
    mark = L[y][1]
    stdv = (int(mark)-avg)**2
    std+=stdv
std = math.sqrt(std/len(L))
print('The std deviation is:','{0:1.2f}'.format(std))

nV = 0
lN = []
for z in range(len(L)):
    Ostd = avg - std
    if int(L[z][1]) < Ostd:
        lN.append(L[z][0])
        nV = 1
if nV == 1:
    print("List of students who need to see an advisor:")
    for p in lN:
        print(p)