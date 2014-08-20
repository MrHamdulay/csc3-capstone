# Student Number: PRTNIC017
# Date: 5/11/14
# Description: A python program to analyse student marks read in from
#              a file and determine which students need to see a student
#              adviser.

# Imports
import math

# Input
text_file = input('Enter the marks filename:\n')

# File to read from
file = open(text_file)
# Variables
data = []
ave = 0.0  # Average
dev = 0.0  # Standard Deviation

# Read data from file
for l in file.readlines():
    l = l.replace('\n', '').split(',')
    data += [[l[0], int(l[1])]]

# Get average
for el in data:
    ave += el[1]
ave /= len(data)

# Get standard deviation
for el in data:
    dev += (el[1] - ave) ** 2
dev = math.sqrt(dev / len(data))

# List students needing advise
advise_students = []
for el in data:
    if el[1] < (ave - dev):
        advise_students.append(el[0])

# Output
print('The average is:', '{0:0.2f}'.format(ave))
print('The std deviation is:', '{0:0.2f}'.format(dev))
if len(advise_students) != 0:
    print('List of students who need to see an advisor:')
    for s in advise_students:
        print(s)