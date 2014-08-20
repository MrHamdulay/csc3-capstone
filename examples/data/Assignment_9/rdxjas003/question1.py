#Alan, 35
#Siobhan,23
#Mmberengeni,38
import math
marks = {}
namenumber = []
filename = input('Enter the marks filename:\n')
#connect to text file

file = open(filename,'r')
for line in file:
        info = line.split(',')
        marks[info[0]] = eval(info[1])
        namenumber.append(info[0])
file.close


# work out average
sum = 0
num = 0
for name in marks.keys():
        num+=1
        sum+=marks[name]
average = sum/num

print('The average is: %.2f' % (average) )
# standard deviation
SD = 0
for name in marks.keys():
        SD+=((marks[name]-average)**2)
SD = math.sqrt(SD/num)
print('The std deviation is: %.2f' % (SD) )
# list students who need to see advisor (less than 1 SD from average)
atRisk = []
for name in marks.keys():
        if marks[name]<(average-SD):
                atRisk.append(name)
if len(atRisk)>0:
        #atRisk = sorted(atRisk)
        print('List of students who need to see an advisor:')
        i = 0
        while i < len(namenumber):
                x = 0
                while x < len(atRisk):
                        if namenumber[i]==atRisk[x]:
                                print(atRisk[x])
                        x+=1
                i+=1
                
