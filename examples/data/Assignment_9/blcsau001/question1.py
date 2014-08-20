#Program to producing a list of marks that are below one std. dev. from mean
#Saul Bloch
#14 May 2014

import math
fileName = input("Enter the marks filename:\n")

f = open(fileName, "r")
count = 0
tot = 0
stddevtot = 0
length = len(open(fileName).readlines())
names = []
marks = []
line = f.readline()
#Splitting names and marks into arrays
for i in range(length):
   split = line.split(",")
   names.append(split[0])
   marks.append(split[1])
   count += 1
   line = f.readline()

#Adding all marks
for i in range(len(marks)):
   tot = tot + int(marks[i])
avg = tot/count

#caculating standard deviation (First varience)
for i in range(len(marks)):
   stddevtot = stddevtot + (int(marks[i])-avg)*(int(marks[i])-avg)
#Now calculating std dev
stddev = math.sqrt(stddevtot/count)

#displaying the required information
print("The average is:","%0.2f" % (avg))
print("The std deviation is:","%0.2f" % (stddev))
NumberOfStudents = 0
for i in range(len(marks)):
   if int(marks[i]) < (avg-stddev):
      NumberOfStudents += 1
      
if NumberOfStudents != 0:
   print("List of students who need to see an advisor:")
   for i in range(len(marks)):
      if int(marks[i]) < (avg-stddev):
         print(names[i])