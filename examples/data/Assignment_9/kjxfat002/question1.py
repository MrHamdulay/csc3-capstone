"""
Created on May 15th 2014
A program to analyse students marks and read it from a file
KJXFAT002

"""
import math

filename = input("Enter the marks filename: \n")

marksFile = open(filename,"r")


# file read into a list
x = marksFile.readlines()
studentMarks = []
studentNames = []

#marks and names are seperated. The key of the one corresponds to key in other
for i in x:
    
    if i == "\n":
        break
    
    perLine = i.split(",")
    studentNames.append(perLine[0])
    studentMarks.append(perLine[1])
    
# converting each mark to an int such as to manipulate mathematically
for i in range(len(studentMarks)):
    studentMarks[i] = int(studentMarks[i])
    
# adding all marks together   
sum_of_marks = 0     
for i in studentMarks:
    sum_of_marks = sum_of_marks + i
    
#finding average
average = sum_of_marks/(len(studentMarks))
average = round(average,2)


#finding delta
delta = 0
for i in range(len(studentMarks)):
    delta = delta + (studentMarks[i] - average)*(studentMarks[i] - average)
    
delta = math.sqrt(delta / (len(studentMarks)))
delta = round(delta,2)


#evaluating which students should see an advisor


if average/(int(average)) == 1:
    average = str(average)
    average = average + "0"
    print("The average is:",average)
        
else:
    print("The average is:",average)


if delta == 0:
    delta=str(delta)
    delta = delta + "0"
    print("The std deviation is:",delta)

elif delta/(int(delta)) == 1:
    delta = str(delta)
    delta = delta + "0"
    print("The std deviation is:",delta)
    print("List of students who need to see an advisor:")
    
else:
    print("The std deviation is:",delta)
    print("List of students who need to see an advisor:")




average = float(average)
delta = float(delta)

for i in range(len(studentMarks)):
    if studentMarks[i] < average - delta:
        print(studentNames[i])

marksFile.close()


