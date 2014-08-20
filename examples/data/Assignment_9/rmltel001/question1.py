"""Program to analyse student marks read in from a file and determine which students need to see a student advisor
Telisha Ramlall
10 May 2014"""

import math

filename = input("Enter the marks filename:\n")

#open file and read lines into an array
f = open(filename, "r")
lines = f.readlines()
f.close()

num_learners = len(lines)
total = 0

#get marks and calculate sum of total marks
for i in range(num_learners):
    total += eval(lines[i][lines[i].find(",")+1:])

#calculate average
average = total/num_learners
sum_of_squares = 0

#calculate the sum of the square of the difference between each student's mark and the mean
for i in range(num_learners):
    sum_of_squares += (eval(lines[i][lines[i].find(",")+1:]) - average)**2
  
#calculate standard deviation    
standard_deviation = math.sqrt(sum_of_squares/num_learners)

f = "{0:.2f}"

print("The average is:", f.format(average))
print("The std deviation is:", f.format(standard_deviation))


advisor = False
#Check if any students need to see advisor
for i in range(num_learners):
    if (eval(lines[i][lines[i].find(",")+1:]) < average-standard_deviation):
        advisor = True
        
if advisor:
    print("List of students who need to see an advisor:")
    for i in range(num_learners):
        if (eval(lines[i][lines[i].find(",")+1:]) < average-standard_deviation):
            print(lines[i][:lines[i].find(",")]) #print names