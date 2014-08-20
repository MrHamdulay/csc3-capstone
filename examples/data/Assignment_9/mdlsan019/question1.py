#-------------------------------------------------------------------------------
# Assignment:  9
# Purpose:     Analyses students marks read in from a file
#
# Author:      S.C.MDLALOSE
#
# Created:     13/05/2014
# Copyright:   (c) S.C.MDLALOSE 2014
#
#-------------------------------------------------------------------------------

filename = input("Enter the marks filename:\n")

f = open(filename, 'r')

items = f.readlines()
values = []
names = []

for line in items:
    x = line.find(',')
    values.append(line[x+1:-1])
    names.append(line[:x])
def mean (values):
    count = 0.0
    total = 0.0
    for num in values:
        num = eval(num)
        total+=num
        count+=1
    x_bar = total/count
    return x_bar
x_bar = mean (values)
print("The average is:","%.2f"%x_bar)

def std_dev(values, x_bar):
    N = 0.0
    total = 0.0
    for num in values:
        num = eval(num)

        dev = x_bar-num
        total+=dev**2
        N+=1
    std_dev=(total/N)**0.5
    return std_dev
stdev=std_dev (values, x_bar)
print("The std deviation is:", "%.2f"%stdev)

students=[]
student=False
for i in range (len(names)):
    
    if eval(values[i]) < (x_bar-stdev):
        students.append(names[i])
        student=True
if student==True:
    print("List of students who need to see an advisor:")
    for j in students:
        print(j)    

f.close()