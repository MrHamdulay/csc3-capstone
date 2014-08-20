'''Program for length adjustment to a text file
Julian Albert
16-05-2014'''

import math
input_file = input('Enter the marks filename:\n') #user input
#mean calculation
def mean(l):
	output = 0
	for i in l:
		output += i
	return (output/len(l))
#standard deviation calculation
def std_dev(l):
	output = 0
	average = mean(l)
	for i in l:
		output += (i-average)*(i-average)
	return math.sqrt(output/len(l))

f = open(input_file,"r");
lines = f.readlines();
f.close()

names = []
marks = []

for i in lines:
	names.append(i.split(",")[0])
	marks.append(int(i.split(",")[1].replace('\n','')))
average = mean(marks)
std = std_dev(marks)

print('The average is: %0.2F' %average) #print average
print('The std deviation is: %0.2F' %std) #print standard deviation
output = 'List of students who need to see an advisor:'
#check below mean
for i in range(len(marks)):
	if marks[i]<(average - std):
		output += '\n' + names[i]

if output != 'List of students who need to see an advisor:':
	print(output)


