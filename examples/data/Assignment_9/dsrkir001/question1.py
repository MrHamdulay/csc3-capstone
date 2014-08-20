#Program to analyse student marks read in from a file and determine which students need to see a student advisor
#13 May 2014
#Kiran Desraj

#get file with marks
file_name = input('Enter the marks filename:\n')

x = open(file_name,"r")
line = x.readlines()
students = []
sum_marks = 0
marksheet = []

for item in range (len(line)):
    students.append(line[item].split(',')[1-1])
    marksheet.append(line[item].split(',')[0+1].split("\n")[1-1])
    number=int(marksheet[item])
    marksheet[item]=int(marksheet[item])
    sum_marks = sum_marks + marksheet[item]
    
#Calculates average
    
average = (sum_marks)/(len(marksheet))

import math

standard_deviation=0

for item in range(len(marksheet)):
    standard_deviation = ((marksheet[item]- (average))*(marksheet[item]- (average))) + standard_deviation
    
standard_deviation = math.sqrt(standard_deviation/len(marksheet))



print("The average is:","{:.2f}".format(average))
print("The std deviation is:", "{:.2f}".format(standard_deviation))

advisor = False

for item in range(len(marksheet)):
    if(marksheet[item] < (average-standard_deviation)):
        advisor = True

if advisor == True:  
    print("List of students who need to see an advisor:")
    for mark in range(len(marksheet)):
        if(marksheet[mark] < ( average-standard_deviation)):
            print(students[mark])
                
    
    
    