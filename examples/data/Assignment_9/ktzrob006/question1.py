#AMNTAS003  #Tashfia Amin   #Due Date: 16 May 2014
#Question 1: Assignment 9   #Check file of student marks to send to advisor

import math

#Ask user for input for which file to open
marks = input("Enter the marks filename: \n")

#Open input file to read and then close file
f = open(marks, "r")
grades = f.readlines()
f.close()

#Remove "\n" from the list
for line in range(len(grades)):
    if grades[line] == grades[-1]:
        grades[line] = grades[line]
    else:
        grades[line] = grades[line][:-1]
#Pick out only the grades from the list
grade = []
for line in grades:
    if line[-2] == ",":
            grade.append(line[-1])
    elif grades[-1]:
        grade.append(line[-2:])
    else:
        grade.append(line[-3:])
   
#Get the average of the marks
avg = 0
mark = 0
count = 0
for i in grade:
    mark += eval(i)
    count+=1
    avg = round(mark/count, 2)
    
#Get the inner part of the standard deviation
def temp():
    dev = 0
    for i in range(len(grade)):    
        dev1 = round((eval(grade[i]) - avg)**2, 2)                  #Calculate (x-avg)**2 for every value in the list of marks
        dev+=dev1
        dev=round(dev, 2)
    return dev

#calculate the standard deviation of the mean
def stnd_dev():
    dev2 = temp()/len(grade)                                        #Use the inner value from temp() function to calculate the standard deviation
    deviation = round(math.sqrt(dev2), 2)
    if len(str(deviation))<5:
        deviate = "{:0<4}".format(deviation)
    else:
        deviate = "{:0<5}".format(deviation)
    return deviate

#Get names of the students into a list
names=[]
for line in grades:
    if line[-2] == ",":
        names.append(line[:-2])
    elif grades[-1]:
        names.append(line[:-3])
    else:
        names.append(line[:-4])    

print("The average is:", end=" ")
print("{0:.2f}".format(avg))
print("The std deviation is:", end=" ")
print("{0:.2f}".format(eval(stnd_dev())))

#Check for students with marks less than one standard deviation of the mean
adv = 0
for i in range(len(grade)):
    if eval(grade[i]) < (avg - eval(stnd_dev())):
        adv+=1
if adv > 0:
    print("List of students who need to see an advisor:")
    
for i in range(len(grade)):
    if eval(grade[i]) < (avg - eval(stnd_dev())):
        print(names[i])