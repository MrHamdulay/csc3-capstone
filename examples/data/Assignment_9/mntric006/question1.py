import math
x = "{0:.2f}"
data = open (input("Enter the marks filename:\n"), "r")
array = []
for line in data:
    array.append(line.split(","))
data.close ()
total = 0
num = len(array)
for i in range(num):
    total += eval(array[i][1])
average = round(total/num,2)
print("The average is: " + x.format(average))
total = 0
for j in range(num):
    total += (float(array[j][1])-average)*(float(array[j][1])-average)
stddev = math.sqrt(total/num)
print("The std deviation is: " + x.format(stddev))
listoffail = []
for k in range(num):
    if eval(array[k][1]) < (average - stddev):
        listoffail.append(array[k][0])
if listoffail != []:
    print("List of students who need to see an advisor:")
    for l in range(len(listoffail)):
        print(listoffail[l])



    