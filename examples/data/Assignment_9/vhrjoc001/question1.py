#VHRJOC001
#finding out which student needs to see a counsellor
import math

file=input("Enter the marks filename:\n")
action=open(file,"r")
marks=action.readlines()
action.close()

for i in range(len(marks)):
    marks[i]=marks[i][:-1]
    marks[i]=marks[i].split(",")
    marks[i][1]=int(marks[i][1])
   
#calculations
#average
add=0
for i in range(len(marks)):
    add+=marks[i][1]
average=add/len(marks)    
print("The average is: {0:.2f}".format(average))

#std deviation
stddev=0
for i in range(len(marks)):
    stddev+=((marks[i][1])-average) **2
stddev=stddev/len(marks)
stddev=math.sqrt(stddev)
print("The std deviation is: {0:.2f}".format(stddev))

#who needs counselling
for i in range(len(marks)):
    if marks[i][1]<(average-stddev):
        print("List of students who need to see an advisor:")
        break
    
        
for i in range(len(marks)):
    if marks[i][1]<(average-stddev):
        print(marks[i][0])
