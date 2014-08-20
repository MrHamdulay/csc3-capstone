'''Student marks analyzer
Sbongakonke Mlangeni
13 April 2014'''

from math import sqrt


filename = input('Enter the marks filename:\n')
fob = open(filename,'r')
listfile = fob.readlines()
fob.close()
#print(listfile)


for i in range(len(listfile)):
    if '\n' in listfile[i]:
        listfile[i] = listfile[i].rstrip('\n')
#print(listfile)

newfilelist = []
for i in listfile:
    a = i.split(',')
    newfilelist += a
#print(newfilelist)

marks = []
for i in newfilelist:
    if i.isdigit():
        marks.append(i)
#print(marks)

avsum = 0
for i in marks:
    avsum += int(i)
#print(avsum)
        
count = len(marks)
average = avsum/count
print('The average is: {0:.2f}'.format(average))

d = 0

for i in marks:
    a = (int(i) - average)**2
    d += a
sd = round(sqrt(d/count),2)

names = []
for i in newfilelist:
    if not i.isdigit():
        names.append(i)
#print(names)        
        

print('The std deviation is: {0:.2f}'.format(sd))

print('List of students who need to see an advisor:')
for i in marks:
    if int(i) < (average - sd):
        print(names[marks.index(i)])

