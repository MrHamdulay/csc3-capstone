"""thrianka naidoo
ndxthr005
11 may 2014, assigment9, question 1: to see the student advisor or not to see the student advisor"""

import math
filename = input("Enter the marks filename:\n")#input for user
f = open(filename, "r")
lines = f.readlines()                    #creates list to save each line in textfile

count = 0                                #declaring varibles
total = 0
strd_dev = 0
marksList = []
namesList = []
studAdvisor = []

for i in range(len(lines)):              #iterates for each line in the textfile
   entries = lines[i].split(",")         #creates another array with each individual entry
   
   for mark in range(len(entries)):      #iterates to get mark for each entry
      names = entries[0]
      marks = entries[1]
   
      marks = float(marks)               #converts str(mark) to an integer
   total +=marks                         #adds required figures for each variable
   count +=1
   average = (total/count)               #calculates average
   marksList.append(marks)
   namesList.append(names)

for i in range(len(marksList)):          #calculated std deviation
   strd_dev +=((marksList[i] - average)**2)
d = math.sqrt(strd_dev/count)
mean_sd = average - d

for i in range(len(marksList)):          #checks for students below the one sd below average
   if marksList[i] < mean_sd:
      studAdvisor.append(namesList[i])
f.close()

print("The average is: %.2f"%average)    #output
print("The std deviation is: %.2f"%d)

if studAdvisor:
   print("List of students who need to see an advisor:")
   for i in range(len(studAdvisor)):
      print(studAdvisor[i])