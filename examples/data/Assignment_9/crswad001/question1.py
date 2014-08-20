'''Wade Cresswell
Question1'''
import math
print('Enter the marks filename:')
filename = input()
f1 = open(filename,'r')
stringfile = f1.readlines() #reads all lines into a list
f1.close
listm = []
N=0
for i in stringfile:
    listm.append(eval(i.split(',')[1])) #creates a list of just the marks
    N+=1
average = 0
variance = 0
for i in listm:
    average += i #calculates sum of marks
average = average/N #calculates average
for i in listm:
    variance += (i-average)*(i-average) #calculates variance
standardDev = math.sqrt(variance/N)
print('The average is:','{:.2f}'.format((round(average,2))))
print('The std deviation is:','{:.2f}'.format(round(standardDev,2)))
x=''
for i in stringfile:
    if eval(i.split(',')[1])<(average-standardDev): #if their mark is less than one standard dev below average, add their name to x.
        x+='\n'+i.split(',')[0]
if x: #if there are names, print them
    print('List of students who need to see an advisor:',x,sep='')