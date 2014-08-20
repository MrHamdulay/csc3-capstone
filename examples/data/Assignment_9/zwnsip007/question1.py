'''Siphesihle Zwane
standard devition and average programme 
15/05/14'''
import math

name = input("Enter the marks filename:\n") #reading file
f = open(name, "r")
lines = f.readlines()
f.close()

grade = len(lines)
total = 0

for i in range(grade):
 #   total+=
    indtot= eval(lines[i][lines[i].find(",")+1:]) #getting all the marks
    total+=indtot
average = total/grade
sumsquares = 0

for i in range(grade):
    sumsquares += (eval(lines[i][lines[i].find(",")+1:]) - average)**2
    
sdeviation = math.sqrt(sumsquares/grade) #getting standard deviation

f = "{0:.2f}"

print("The average is:", f.format(average))
print("The std deviation is:", f.format(sdeviation))


advisor = False # setting initial

for i in range(grade):
    if (eval(lines[i][lines[i].find(",")+1:]) < average-sdeviation):
        advisor = True
        
if advisor:
    print("List of students who need to see an advisor:")
    for i in range(grade):
        if (eval(lines[i][lines[i].find(",")+1:]) < average-sdeviation):
            print(lines[i][:lines[i].find(",")]) #printing names below