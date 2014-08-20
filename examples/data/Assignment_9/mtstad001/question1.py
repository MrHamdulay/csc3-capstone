

import math
count = 0
temp = 0
grades =[]
list1 = []

name = input("Enter the marks filename:\n")
x = open (name, "r")
lists = x.readlines()
x.close()

for i in range(len(lists)):
    y = lists[i].split(",")
    
    grades.append(y[1])
    count  += eval(y[1])
    
average = count/len(lists)
if average - int(average) == 0:
    print("The average is:", str(round(average, 2))+"0")
else:
    print("The average is:", round(average, 2))
for j in range(len(grades)):
    temp += (eval(grades[j]) - average)**2
deviation = math.sqrt(temp/len(grades))
if deviation - int(deviation) == 0:
    print ("The std deviation is:", str(round(deviation, 2))+"0")
else:
    print ("The std deviation is:", round(deviation, 2))

for i in range(len(lists)):
    y = lists[i].split(",")
    if eval(y[1]) < (average - deviation):
        list1.append(y[0])
if len(list1) > 0:
    print("List of students who need to see an advisor:")
    for i in list1:
        print(i)
    
