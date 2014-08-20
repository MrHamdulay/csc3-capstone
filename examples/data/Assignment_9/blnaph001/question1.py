#aphiwe baleini
#16 may 2014
#program to check if students should see a student advisor
import math

filename = input("Enter the marks filename:\n")
f = open(filename, "r")
lines = f.readlines()
f.close()

num_learners = len(lines)
total = 0

for i in range(num_learners):
    total += eval(lines[i][lines[i].find(",")+1:])

average = total/num_learners
sum_of_squares = 0

for i in range(num_learners):
    sum_of_squares += (eval(lines[i][lines[i].find(",")+1:]) - average)**2
    
standard_deviation = math.sqrt(sum_of_squares/num_learners)

f = "{0:.2f}"

print("The average is:", f.format(average))
print("The std deviation is:", f.format(standard_deviation))


advisor = False

for i in range(num_learners):
    if (eval(lines[i][lines[i].find(",")+1:]) < average-standard_deviation):
        advisor = True
        
if advisor:
    print("List of students who need to see an advisor:")
    for i in range(num_learners):
        if (eval(lines[i][lines[i].find(",")+1:]) < average-standard_deviation):
            print(lines[i][:lines[i].find(",")])