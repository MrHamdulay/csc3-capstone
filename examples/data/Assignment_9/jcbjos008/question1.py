'''Joshen Credelio Jacob
Reading marks from a file
13/05/2014'''

import math
x=input('Enter the marks filename:\n')

#reading the file
f=open(x,'r')
l=f.readlines()
f.close()

list1=[]
marks=[]

#removing the carriage character
for i in l:
    if i[-1]=='\n':
        i = i[:-1]
        list1.append(i)
        
#getting the marks from the file
for i in range(len(list1)):
    list1[i] = list1[i].split(',')
    list1[i][1] = int(list1[i][1])

for i in range(len(list1)):
    marks.append(list1[i][1])

#calculating the average and stadard deviation
avg = sum(marks) / len(marks)
std=0
for i in range(len(marks)):
    std+=(marks[i] - avg)**2
    
#giving back the average and standard deviation  
print('The average is:','{0:.2f}'.format(round(avg,2))  )

std=math.sqrt(std/(len(marks)))       
print('The std deviation is:','{0:.2f}'.format(round(std,2)) )

#students who need to see the advisor

for i in range(len(marks)):
    if marks[i]<(avg-std):
        print('List of students who need to see an advisor:')
        break 
    
for i in range(len(marks)):
    if marks[i]<(avg-std):
        print(list1[i][0])