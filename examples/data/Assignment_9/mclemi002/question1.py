"""emile mclennan
11/5/14
q1 A9"""
import math
i=1
sd=0
marks=[]
names=[]
fileName = input('Enter the marks filename:\n')
f = open(fileName,'r')
lines = f.read() #get data from file
f.close()
items=lines.replace(',',' ').split() #replace , with <space> so that we can split items individually
num=len(items) #get length of list
while i <= num:
    a = eval(items[i])
    marks.append(a) #add marks to array
    i=i+2

numMarks = len(marks) #get number of marks
mean =0
for i in range(numMarks): #calculate mean of marks
    mean = mean+marks[i]
mean = round(mean/numMarks,2)
fMean="The average is: {0:0.2f}".format(mean)
#calculate the standard deviation
for i in range (numMarks):
    sd = sd+ ((marks[i]-mean)**2)
sd=sd/numMarks
sd = round(math.sqrt(sd),2)
fsd="The std deviation is: {0:0.2f}".format(sd)

oneSD = mean-sd #calculate value of 1 standard deviation
for i in range(numMarks): #check to see who has a mark below 1 standard deviation
    if  oneSD > marks[i]:
        pos = items.index(str(marks[i]))
        pos=pos-1
        names.append(items[pos])

print(fMean)
print(fsd)
nameLength = len(names)

if nameLength >0:
    print('List of students who need to see an advisor:')
    for name in names:
        print(name)