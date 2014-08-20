'''Ednecia Matlapeng
Reading the values from a text file into a list and then manipulating the string
9 May 2014'''
import math
filename = input('Enter the marks filename:\n')
f = open(filename, 'r')
mylist = f.readlines()
f.close()
#print(mylist) contains \n
#Remove the newlines
for  i in range(len(mylist)):
    mylist[i]=mylist[i].replace('\n','')
#print(mylist)
#separate the list into 2D for names and marks
for  k in range(len(mylist)):
    breakpoint = mylist[k].index(',')
    temp = mylist[k]
    mylist[k] = [temp[:breakpoint], int(temp[breakpoint+1:])]
#print(mylist)
#Getting the average and the number of marks
avg,n,marklist =0,0,[]

for k in range(len(mylist)):
    n+=1
    avg+=mylist[k][1]
    #print(avg)
    marklist.append(mylist[k][1])
avg = avg/n
#test1.txt
#The standard deviation
#print(n)
std = 0
for i in marklist:
    std+= (i-avg)**2
std =round( math.sqrt(std/n),2)
avg=round(avg,2)
if avg%1==0 and std%1==0:
    print('The average is: ',avg,'0\nThe std deviation is: ',std,'0' ,sep='')
elif avg%1==0:
    print('The average is: ',avg,'0\nThe std deviation is: ',std ,sep='')
elif std%1==0:
    print('The average is: ',avg,'\nThe std deviation is: ',std ,'0',sep='')
else:
    print('The average is:',avg,'\nThe std deviation is:',std)

advice = ''

for f in range(len(mylist)):
    if marklist[f]<(avg-std):
        advice+=(mylist[f][0])+'\n'
if advice!='':
    print('List of students who need to see an advisor:')
    print(advice)
    


