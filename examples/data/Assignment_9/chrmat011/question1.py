##Mathew Cherry
##13/05/14
##Finds the mean and standard deviation of a set of grades,
##also lists students who need help

import math

filename = input('Enter the marks filename:\n')
file = open(filename, 'r')

total = 0
count = 0
marks = []
students = []

for line in file:
    mark = int(line.split(',')[1]) #get the mark
    students.append(line.split(',')[0]) #get the student name
    count += 1
    total += int(mark)
    marks.append(mark)

mean = total/count
deviations = []
for i in marks:
    deviations.append((i-mean)**2)

standard_deviation = math.sqrt((sum(deviations))/count)

mean_print = str(round(mean,2))
#appends an extra 0 to the final value so that it always shows in the form xx.xx
while len(mean_print.split('.')[1])<2:
    mean_print += "0"

std_print = str(round(standard_deviation,2))
#appends an extra 0 to the final value so that it always shows in the form xx.xx
while len(std_print.split('.')[1])<2:
    std_print += "0"

print('The average is:',mean_print)
print('The std deviation is:',std_print)

bad_students = []
for i in range(len(marks)):
    if mean - standard_deviation > marks[i]: #if the student is further than one standard deviation from the mean he needs help
        bad_students.append(students[i])

if len(bad_students) > 0:
    print('List of students who need to see an advisor:')
    for i in bad_students:
        print(i)

file.close()
