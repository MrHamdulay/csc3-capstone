'''question1.py
determine which students need to seen an advisor based on marks and stats
douglas newton NWTDOU001
15 may 2014'''

import math

# get filename from user
filename = input('Enter the marks filename:\n')

# for mapping marks to names
marks = {}

# also, a name list to keep names in the correct order later on
names = []

# open/close file and extract names and marks to dictionary
file = open(filename,'r')
for line in file.readlines():
    # eliminate double-spacing:
    for i in range(len(line)-1):
        if line[i:i+2]==' '*2:
            line = line[:i+1]+line[i+2:]
    
    data = line.split(',')
    # [0] is the name, [1] is the mark
    names.append(data[0])
    marks[data[0]] = eval(data[1])
file.close()

# calculate mean
total = 0
for name in names:
    total += marks[name]
mean = total/len(names)
print('The average is:','%.2f' % round(mean,2))

# calculate std deviation
total = 0
for name in names:
    total += (marks[name] - mean)**2
std_dev = math.sqrt(total/len(names))
print('The std deviation is:','%.2f' % round(std_dev,2))

# first create a list of those that need help (so we can check if there are 0)
need_help = []
for name in names:
    if marks[name] < mean - std_dev:
        need_help.append(name)
        
# now print the names of the people that need help (if there are any)
if len(need_help)>0:
    print('List of students who need to see an advisor:')
    for name in need_help:
            print(name)