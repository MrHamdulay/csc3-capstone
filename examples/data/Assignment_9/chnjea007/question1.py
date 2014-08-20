# a9 q1
import math 
from collections import OrderedDict
filename = input("Enter the marks filename:\n")
f = open(filename, "r")
try:    
    data = OrderedDict([])
    count = 0
    total = 0
    ave = 0.0
    dev = 0.0
    for line in f:
        line = line.split(",")
        data[line[0]] = eval(line[1].rstrip("\n"))
        count += 1
    for mark in data.values():
        total += mark
    ave = total/count
    for mark in data.values():
        dev += (mark - ave)**2
    dev = math.sqrt(dev/count)
    print("The average is:", "{0:.2f}".format(ave))
    print("The std deviation is:", "{0:.2f}".format(dev))
    count = 0
    for name, mark in data.items():
        if mark < ave - dev:
            if count == 0:
                print("List of students who need to see an advisor:")
                count+=1
            print(name)
except:
    print("File not found")
f.close()
    