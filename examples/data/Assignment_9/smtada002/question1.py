'''Assignment 9 question 1 Mark read in
Adam Smith
12 May 2014'''

import math
FName = input("Enter the marks filename:\n")

f = open(FName, "r")

Student_Marks = []
Problem_Students = []

for line in f: #read the file into the Student_Marks list
    Student_Marks.append(line.split(","))    
f.close()

total = 0
for i in range (len(Student_Marks)):  #calculate the average
    total = total + int(Student_Marks[i][1])    
average = round(total/(len(Student_Marks)),2)

devitaion_sum = 0
for i in range (len(Student_Marks)):  #calculate the standard deviation
    devitaion_sum = devitaion_sum + (abs(int(Student_Marks[i][1]) - average))**2
Std_deviation = round(math.sqrt(devitaion_sum/(len(Student_Marks))),2)

for i in range (len(Student_Marks)): # check which students fall 1 standard deviation below the average
    if int(Student_Marks[i][1]) < (average - Std_deviation):
        Problem_Students.append(Student_Marks[i][0])
        
average = '{:.2f}'.format(average) #format to 2 decimal places
Std_deviation = '{:.2f}'.format(Std_deviation)

print("The average is: " + str(average)) # print out resulat
print("The std deviation is: " + str(Std_deviation))
if Problem_Students != []:
    print("List of students who need to see an advisor:")
    for i in range (len(Problem_Students)):
        print(Problem_Students[i])