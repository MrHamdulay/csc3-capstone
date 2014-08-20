"""student advisor list
rama raphalalani
12-05-2014"""

import math

#Opens and reads through the lines of the file with the student marks
fileName = input("Enter the marks filename:\n")
file = open(fileName,"r")
lines = file.readlines()
list1 = []
total = 0
std2 = 0

#creates a list with the marks and then works out the avearge of the students.
for line in lines:
    x = line.split(",")
    y = eval(x[1])
    total += y
    list1.append(y)
average = total/len(lines)
print("The average is: {0:.2f}".format(average))  

#uses the average to work out the standard deviation for each students mark
for j in (list1):
    z = j
    std = (z-average)**2
    std2 += std
deviation = (math.sqrt(std2/len(list1)))
deviation = round(deviation,2)

print("The std deviation is: {0:.2f}".format(deviation))
if deviation>0:
    print("List of students who need to see an advisor:")

#goes throught the list and looks at who should see the student advisor
for line in lines:
    x = line.split(",")
    y = eval(x[1])
    if y<(average-deviation):
        print(x[0])
file.close()         