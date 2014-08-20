'''Question1 
Aaron Daniels
13 May 2014'''

import math

filename=input('Enter the marks filename:\n')
f=open(filename,'r')
line=f.readlines()
f.close()

for i in range(len(line)):
    line[i]=line[i][:len(line[i])-1]
   
names=[]

for q in range(len(line)):
    names.append(line[q])

for i in range(len(line)):
    for c in range(len(line[i])):
        if line[i][0].isalpha() or line[i][0]=='-':
            line[i]=line[i][1:]
            
for w in range(len(names)):
    names[w]=names[w][::-1]

for t in range(len(names)):
    for j in range(len(names[t])):
        if names[t][0].isdigit():
            names[t]=names[t][1:]

for i in range(len(line)):
    line[i]=line[i][1:]
    names[i]=names[i][1:]

for h in range(len(names)):
    names[h]=names[h][::-1]

total=0
for g in range(len(line)):
    total+=eval(line[g])

mean=round(total/len(line),2)
am=total//len(line)
v=str(mean-am)
x=str(mean)
if v=='0.0':
    x+='0'
print('The average is:',x)

variance=0
for b in range(len(line)):
    variance+=(eval(line[b])-mean)**2
    
sd=math.sqrt(variance/len(line))
ma=round(sd,0)
bb=str(sd-ma)
cc=str(round(sd,2))
if bb=='0.0':
    cc+='0'
print('The std deviation is:',cc)

lower=mean-sd
z=''
for n in range(len(line)):
    if eval(line[n])<lower:
        z+=names[n]+'\n'
if len(z)>0:
    print('List of students who need to see an advisor:')
    print(z)
