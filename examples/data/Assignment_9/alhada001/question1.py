#Adam Alhadeff

import math
file = input("Enter the marks filename:\n")

f = open(file, "r")

length = len(open(file).readlines())
names = []
marks = []
line = f.readline()

count = 0
for i in range(length):
   split = line.split(",")
   names.append(split[0])
   marks.append(split[1])
   count += 1
   line = f.readline()


total = 0
for i in range(len(marks)):
   total = total + int(marks[i])
average = total/count


SDT = 0
for i in range(len(marks)):
   SDT = SDT + (int(marks[i])-average)*(int(marks[i])-average)

SD = math.sqrt(SDT/count)


print("The average is:","%0.2f" % (average))
print("The std deviation is:","%0.2f" % (SD))
NumStudents = 0
for i in range(len(marks)):
   if int(marks[i]) < (average-SD):
      NumStudents += 1
      
if NumStudents != 0:
   print("List of students who need to see an advisor:")
   for i in range(len(marks)):
      if int(marks[i]) < (average-SD):
         print(names[i])