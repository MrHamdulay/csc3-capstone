#Kiuran Naidoo
#Assignment 9
#Question 1
import math

filename = input("Enter the marks filename:\n")
markFile = open(filename,"r")

names =[]
grade =[]
count = 0
total = 0
deviation =0

for line in markFile:
 current = line.split(",")
 names.append(current[0])
 grade.append(eval(current[1]))

markFile.close() 
 
for i in range(len(grade)):
 count +=1
 total +=grade[i]

mean = total/count

for i in range(len(grade)):
 deviation+= (mean-grade[i])**2

standardDev = math.sqrt(deviation/count)

print("The average is: {0:<6.2f}".format(mean))
print("The std deviation is: {0:<6.2f}".format(standardDev))

printSAdvisior = False

for i in range(len(grade)):
 if grade[i]+ standardDev < mean:
  if printSAdvisior == False:
   print("List of students who need to see an advisor:")
   printSAdvisior = True
  print(names[i])
  
  


 


