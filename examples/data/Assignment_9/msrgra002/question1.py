#MSRGRA002
#Grant Meeser
#15/05/2014

import math
inputFile=input('Enter the marks filename:\n')

def mean(l):
	output=0
	for i in l:
		output+=i
	return (output/len(l))

def sd(l):
	output=0
	ave=mean(l)
	for i in l:
		output+=(i-ave)*(i-ave)
	return math.sqrt(output/len(l))

f = open(inputFile,"r");
lines = f.readlines();
f.close()

names=[]
marks=[]

for i in lines:
	names.append(i.split(",")[0])
	marks.append(int(i.split(",")[1].replace('\n','')))
ave=mean(marks)
std=sd(marks)

print('The average is: %0.2F' %ave)
print('The std deviation is: %0.2F' %std)
output='List of students who need to see an advisor:'

for i in range(len(marks)):
	if marks[i]<(ave-std):
		output+='\n'+names[i]

if output != 'List of students who need to see an advisor:':
	print(output)


