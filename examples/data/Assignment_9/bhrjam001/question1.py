# Assignment 9 Question 1
# James Behr
# 2014-05-12

import math

def formatline(line):
    '''Return a key-value pair from a csv style file'''
    key, val = line.rstrip().split(',')
    return (key, int(val))

# Open file to read
f = open(input('Enter the marks filename:\n'))

# Create a list of tuples to prevent arbitary sorting (characteristic of dictionaries)
marks = [formatline(line) for line in f]

# Use the sum function to derive a mean (we need the second element of the tuple only)
mean = sum(mark[1] for mark in marks) / len(marks)
print('The average is: {:.2f}'.format(mean))

# Use a generator and the sum function to get the standard deviation
stddev = math.sqrt(sum((i - mean) ** 2 for i in [mark[1] for mark in marks]) / len(marks))
print('The std deviation is: {:.2f}'.format(stddev))

# Create a list of sudents whose marks are one standard deviation below the mean
studentadvisor = [student for student, mark in marks if mark < mean - stddev]
if len(studentadvisor):
    # Only print this if there are students who need to see an advisor
    print('List of students who need to see an advisor:')
    for student in studentadvisor:
        print(student)
        
# Close the file
f.close()