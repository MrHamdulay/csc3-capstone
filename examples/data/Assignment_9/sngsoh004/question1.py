#Soham Singh
#SNGSOH004
#Assignment 9
#Question 1

import math
filename = input("Enter the marks filename:\n") #Asking for the name of the text file

f = open(filename,"r")
contents = f.readlines()
f.close() #Storing all the lines of the text file in a list
grades=[]
total=0

for i in range(len(contents)): #Storing all the grades in a seperate list
    index = contents[i].index(",")
    if "\n" in contents[i]:
        grades.append(eval(contents[i][index+1:contents[i].index("\n")]))
    else:
        grades.append(eval(contents[i][index+1:])) 
    
    
    
for i in range(len(grades)): #Adding up the grades
    total+=grades[i]
    
average = "{0:.2f}".format(total/len(grades))#Calculating the average
std=0

for i in range(len(grades)):
    std += (grades[i]-eval(average))**2
std = round(math.sqrt(std/len(grades)),2) #calculating the standard deviation

target = eval(average)-std #calculating the target value
advisors = []

for j in range(len(contents)):
    student = contents[j][:contents[j].index(",")]
    if (grades[j]<target):
        advisors.append(student)
        
def strip_quotes (array):    
    for i in range (len (array)):
        if array[i] != "":
            if array[i][0] == '"':
                array[i] = array[i][1:]
            if array[i][-1] == '"':
                array[i] = array[i][:-1]
                
strip_quotes(advisors) #taking all quotation marks off of the strings in the list

print("The average is:",average)
print("The std deviation is:","{0:.2f}".format(std))

if (len(advisors)!=0):
    print("List of students who need to see an advisor:")
    for k in range (len(advisors)):
        print(advisors[k])