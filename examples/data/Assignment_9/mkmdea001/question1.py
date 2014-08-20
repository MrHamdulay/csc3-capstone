'''program for determining studednt who need to see a student 
advisor on the basis of their marks
dean makambwa
11/05/14'''
import math
file_input = input('Enter the marks filename:\n')
f = open(file_input,'r')
marks=[]
names=[]
mark_tot=0
counter=0
lines = f.readlines()
for i in lines:
    counter+=1
    position = i.find(',')
    mark = int(i[position+1:])
    marks.append(mark)
    mark_tot+=mark
meanform ='%.2f'%(mark_tot/counter)
mean = (mark_tot/counter) 
print('The average is:',meanform)

mew=0
for j in marks:
    mew += (((j-mean)**2)/counter)
standform = '%.2f'%(math.sqrt(mew)) 
stand_dev = math.sqrt(mew)
print('The std deviation is:',standform)  

for m in lines:
    stand = int(math.sqrt(mew))
    mean1=int(mean)
    position1 = m.find(',')
    name = m[:position1]
   # names.append(name)
    mark1 = int(m[position1+1:])
    if (mark1)<(mean-stand):
        names.append(name)
if len(names)>0:
        print('List of students who need to see an advisor:\n',end='')  

for m in lines:
    stand = int(math.sqrt(mew))
    mean1=int(mean)
    position1 = m.find(',')
    name = m[:position1]
   # names.append(name)
    mark1 = int(m[position1+1:])
    if (mark1)<(mean-stand):
        print(name)


f.close()
