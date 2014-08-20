"""Program to check whether a student needs a student adviser or not
Jaren Hendricks
15 May 2014"""

import math

# function to calculate the mean(average)
def average (Marks):
    return sum(Marks)/len(Marks)

# function to calculate the standard deviation
def stanDev (values):
    length = len(values)
    avg = average (values)
    count_sum = 0
    for i in range(length):
        count_sum += (values[i]-avg)**2
    ans = count_sum/length
    return math.sqrt(ans)


# Gets the file, opens and reads it
file_name = input('Enter the marks filename:\n')
arrMarks = []
names= ''
arrNames = []
avg = 0
myFile= open(file_name,'r')

# loop to split the values and add it to an array # checks whether a student needs a student advisor or not
for line in myFile:
    name, marks = line.split(',')
    marks = eval(marks)
    arrMarks.append(marks)
    arrNames.append(name)
    avg = average(arrMarks)
    std = stanDev (arrMarks)
    
# output code
print ('The average is:', '{0:0.2f}'.format(avg))
print ('The std deviation is:', '{0:0.2f}'.format(std))

# checks for students who need an adviser
if std > 0:
    print ('List of students who need to see an advisor:')
    for i in arrMarks:
        if i < avg-std:
            advisor = arrNames[arrMarks.index(i)]
            print(advisor)
