#Program that analyses student marks read from a file and determines which students need to see a student advisor
#Ashton Singh
#10 May 2014

import math

filename = input("Enter the marks filename:\n")

#populate array from read file
f = open(filename, "r")
lines = f.readlines()
f.close()

learners_num = len(lines)
total = 0

#calculate sum of total marks
for i in range(learners_num):
    total += eval(lines[i][lines[i].find(",")+1:])

#calculate average
average = total/learners_num
sum_of_squares = 0

#calculate sum of the square of the difference between each student's mark and the mean
for i in range(learners_num):
    sum_of_squares += (eval(lines[i][lines[i].find(",")+1:]) - average)**2
  
#calculate standard deviation    
standard_deviation = math.sqrt(sum_of_squares/learners_num)

f = "{0:.2f}"

print("The average is:", f.format(average))
print("The std deviation is:", f.format(standard_deviation))


advisor = False
#test which students need to see advisor
for i in range(learners_num):
    if (eval(lines[i][lines[i].find(",")+1:]) < average-standard_deviation):
        advisor = True
        
if advisor:
    print("List of students who need to see an advisor:")
    for i in range(learners_num):
        if (eval(lines[i][lines[i].find(",")+1:]) < average-standard_deviation):
            print(lines[i][:lines[i].find(",")]) #print names of students who need to see an advisor