#Assignment 9 - Question 1
#Determines which students in a file are below one deviations from the mean
#Aidan de Nobrega DNBAID001
#10/05/2014

from math import sqrt

filename = input("Enter the marks filename:\n")

with open(filename, "r") as f: #file closes automatically after .readlines()
    lines = f.readlines()
    
pairs = []

#name and mark have separate indices within list of pairs
for line in lines:
    pair = line.split(',')
    pairs.append(pair)
    
marks = []

#makes a separate list of marks only (for calculating mean, etc.)
for i in pairs:
    marks.append(eval(i[1]))

#adds marks and divides by number of marks
mean = sum(marks)/len(marks)

#stddev is a composition of two function. Stdtemp is inner function Easier to work with
stdtemp = 0

#inner function of standard deviation formula
for mark in marks:
    stdtemp += (mark - mean)**2
    
#stddev makes use of inner function above. Result is rounded to 2 places.
stddev = round(sqrt(stdtemp/len(marks)), 2)
    
#answers are formatted to two decimal places for consistency
print("The average is:", "{0:.2f}".format(mean))
print("The std deviation is:","{0:.2f}".format(stddev))
for mark in marks:
    #if there are any students who are below the threshold, default line is printed
    if mark < mean - stddev:
        print("List of students who need to see an advisor:")
        break
    
#every student mark below the threshold has it's paired string (student name) printed
for mark in marks:
    if mark < mean - stddev:
        i = marks.index(mark)
        print(pairs[i][0])
           
   
        
    




