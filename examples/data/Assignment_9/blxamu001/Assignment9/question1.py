
import math
#Opens the file
filename = input("Enter the marks filename:\n")
f = open(filename, "r")
lines = f.readlines()
f.close()

no_learners = len(lines)
total = 0

for i in range(no_learners):
    total += eval(lines[i][lines[i].find(",")+1:])

ave = total/no_learners
sum_of_sqs = 0
#Calcuates number of learners

for i in range(no_learners):
    sum_of_sqs += (eval(lines[i][lines[i].find(",")+1:]) - ave)**2
    
stand_dev = math.sqrt(sum_of_sqs/no_learners)

f = "{0:.2f}"

print("The average is:", f.format(ave))
print("The std deviation is:", f.format(stand_dev))


running = False

for i in range(no_learners):
    if (eval(lines[i][lines[i].find(",")+1:]) < ave-stand_dev):
        running = True
 #Determining the learners who should see an advisor       
if running:
    print("List of students who need to see an advisor:")
    for i in range(num_learners):
        if (eval(lines[i][lines[i].find(",")+1:]) < ave-stand_dev):
            print(lines[i][:lines[i].find(",")])