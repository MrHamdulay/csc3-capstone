#kereshnee pillay
#13 may 2014
#reading a text file

import math

filename = input("Enter the marks filename:\n")

f = open(filename, "r")
lines = f.readlines()
f.close()

learners = len(lines)
total = 0

#calculate sum 
for i in range(learners):
#data after comma is mark
    total += eval(lines[i][lines[i].find(",")+1:])

#calculate average
average = total/learners
sum_squares = 0

#sum of the square of the difference between students mark and the average
for i in range(learners):
    sum_squares += (eval(lines[i][lines[i].find(",")+1:]) - average)**2
  
#calculate standard deviation    
deviation = math.sqrt(sum_squares/learners)

f = "{0:.2f}"

print("The average is:", f.format(average))
print("The std deviation is:", f.format(deviation))


advisor = False
#check to see who needs the advisor
for i in range(learners):
    if (eval(lines[i][lines[i].find(",")+1:]) < average-deviation):
        advisor = True
        
if advisor:
    print("List of students who need to see an advisor:")
    for i in range(learners):
#print names of students who are one deviation from average
        if (eval(lines[i][lines[i].find(",")+1:]) < average-deviation):
            print(lines[i][:lines[i].find(",")]) 