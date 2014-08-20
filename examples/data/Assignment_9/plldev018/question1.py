# student marks below the mean by one standard deviation
# Devaksha Pillay
# 10 May 2014

#required to work out standard deviation
import math

#open and close file and store the data in a list
file_name = input("Enter the marks filename:\n")
f = open (file_name, "r")
names_and_marks = f.readlines()
f.close ()

for char in range(len(names_and_marks)):
    #remove \n
    names_and_marks[char] = names_and_marks[:-1]

marks = []
names = []

#splits student names and marks
for line in names_and_marks:
    for item in range(len(line)):
        if line[item] == ",":
            names.append(line[:item])
            marks.append(line[item + 1:])
    
#calculate the standard deviation        
average = 0
total = len(marks)
for mark in marks:
    marks[mark] = eval(marks[mark])
    average = average + marks[mark]
average = average/total
print("The average is:","{:.2f}".format(average))

standard_deviation = 0
for mark in marks:
    marks[mark] = eval(marks[mark])
    standard_deviation = standard_deviation + (mark - mean)**2
standard_deviation = math.sqrt(standard_deviation/total)
print("The standard deviation is:","{:.2f}".format(standard_deviation))

list_names = []
#printing out the corresponding name in the list names
for student in range(len(marks)):
    if marks[student] < average - standard_deviation:
        list_names.append(names[student])

if list_names != "":
    print("List of students who need to see an advisor:\n")
    for name in list_names:
        print(list_names[name],sep = "")        