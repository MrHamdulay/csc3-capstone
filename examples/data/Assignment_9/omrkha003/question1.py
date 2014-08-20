# program to analyse student marks read in from a file and determine which students need to see a student advisor
# khadeejah omar
# 11 may 2014

import math

filename = input("Enter the marks filename: \n")

f = open(filename, "r")
file_lines = f.readlines() # creates a list of strings with each name,mark
f.close


names = []
marks = []
for line in file_lines :
    
    # determines position of the comma seperating each name and its corresponding mark
    comma_index_value = line.index(",") 
    
    # seperate name and mark and add to seperate lists
    name, mark = line[:comma_index_value], line[(comma_index_value + 1) : -1] # to extract mark, exclude last value in line to slice off newline character
    names.append(name)
    marks.append(mark)
        
    
# determine the average mark
numerator = 0
denominator = 0
for mark in marks :
    mark = eval(mark)
    numerator += mark
    denominator += 1
mean = (numerator/denominator)

# determine the standard deviation
variance = 0
for mark in marks :
    mark = eval(mark)
    squares = (mark - mean)**2
    variance += squares
std_deviation = round(math.sqrt(variance/denominator),2)

# get list of student names who need to see a student advisor
students = []
for mark in marks :
    mark = eval(mark)
    if mark < (mean - std_deviation) : # if the mark is lower than one standard deviation from the mean
        index_value = marks.index(str(mark))
        students.append(names[index_value]) # index value of the mark corresponds to the index value of the student name

print("The average is: " + "{0:.2f}".format(mean))
print("The std deviation is:", "{:.2f}".format(std_deviation))
if students != [] :
    print("List of students who need to see an advisor:")
    for student in students :
        print(student)