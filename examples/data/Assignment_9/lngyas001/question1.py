"""program to determine whether students need to see an advisor based on mean and standard deviation
yasha longstaff
13 may 2014"""

import math

filename = input('Enter the marks filename:\n')

file = open(filename, "r")
marks = file.readlines()
file.close()

aggregate = 0
for item in marks:
    position = item.find(',')
    aggregate += eval(item[position+1:])
mean = "{0:.2f}".format(aggregate/len(marks))

deviation = 0
variance_squared = 0
for item in marks:
    position = item.find(',')
    deviation = (float(item[position+1:])- float(mean))**2
    variance_squared += deviation
variance = math.sqrt((variance_squared)/len(marks))

print('The average is:', mean)
print('The std deviation is:', "{0:.2f}".format(variance))

iter = False

for item in marks:
    if iter == False:
        print('List of students who need to see an advisor:')
        iter = True

    position = item.find(',')
    if eval(item[position+1:]) < (float(mean) - float(variance)):
        print(item[:position])
    else:
        continue
 


