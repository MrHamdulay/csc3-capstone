"""Program to determine which students from a file need to see a student advisor
Tamsin Kantor
May 2014"""

import math 

file = input("Enter the marks filename:\n") 

f = open(file, "r") # opening the file with the marks
lines = f.readlines()
f.close() # closing the file

# getting the marks of each student as a list of integers
marks = [] 
for n in lines:
    if n[len(n)-1] == "\n":
        mark = n[n.index(",") + 1:len(n)]
        mark = int(mark)
        marks.append(mark)
    else:
        mark = n[n.index(",") + 1:len(n) +1]
        mark = int(mark)
        marks.append(mark)        

# getting the names of each student as a list of strings
names = []
for n in lines:
    name = n[0:n.index(",")]
    names.append(name)

# getting the average mark
total = 0
for n in marks:
    total += n
average = total/len(marks)

#getting the standard deviation
step1 = 0
for n in marks:
    step1 += (n - average)*(n - average)
step2 = step1/len(marks)
std_dev = math.sqrt(step2)
        
print("The average is: ",end="")
print("{0:.2f}".format(average))
print("The std deviation is: ",end="")
print("{0:.2f}".format(std_dev))

#do any students need an advisor?
advisor = 0
for i in range(len(marks)):
    if marks[i] < (average - std_dev) :
        advisor += 1
if advisor > 0:
    print("List of students who need to see an advisor:")

# printing the names of the students who need an advisor
for i in range(len(marks)):
    if marks[i] < (average - std_dev) :
        print(names[i])

