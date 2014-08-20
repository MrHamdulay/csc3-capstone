'''Gather information from a text file and determine if students need see advisors based on their marks
Gareth Lategan
16-05-2014'''

import math

filename = input("Enter the marks filename:\n") # Find out the name of the text file
test = open(filename,'r') # Open the text file
file=test.read()
catelog = file.split('\n') # Make a list out of the contents of the file
test.close() # Always close the file ASAP
a=[] # Empty list for the students and their respective marks
for i in range(len(catelog)):
    a.append(catelog[i].split(', ')) # This is to make lists within lists in order to keep the student and his mark in the same list
for i in range(len(a)):
    a.append(a[0][0].split(',')) # This splits the student from his mark, making them different items in the same 'mixed' list
    a.remove(a[0]) # Removes the information that has already been sorted
    
sum_marks=0 # Add up the total of all their marks together
for i in range(len(a)):
    sum_marks += eval(a[i][1])

mean=(sum_marks/len(a)) # Get the average
mean="%.2f" % mean # This is necessary to get that second decimal place when the number is equal to a less specific number

print("The average is:",mean)

x=0
for i in range(len(a)):
    x+=(eval(a[i][1])-eval(mean))**2 # Total the difference between the average and each students number
x=x/len(a) # Divide that total by the amount of students
std=round(math.sqrt(x),2) # This is the standard deviation accurate to two decimal places
print("The std deviation is:",std)
risk_mark=eval(mean)-std # Determine the value below one standard deviation of the average
risk_list=[]
for i in range(len(a)):
    if eval(a[i][1])<risk_mark:
        risk_list.append(a[i][0]) # Make a list of all students whose marks are below one standard deviation of the average
print("List of students who need to see an advisor:")
for i in range(len(risk_list)):
    print(risk_list[i])