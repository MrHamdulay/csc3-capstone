'''Daniel Feinstein FNSDAN001
Assignment 9
Read marks from file and print std deviation and mean'''

import sys
import math

file = input("Enter the marks filename:\n")

f = open(file, "r")

#initialisation
lines = f.readlines()
mean = 0
sd = 0
students = []

#determine mean
for line in lines:
   
    mean+=int((line.split(",")[1].replace("\n", "")))

mean= round(mean/len(lines),2)

#if mean has only one zero (.0 instead of .00) add the 0
if len(str(mean).split(".")[1])<2:
    meana = (str(mean)+"0")
else:
    meana = mean


#determine standard deviation
for line in lines:
    sd += (int((line.split(",")[1].replace("\n", "")))-(mean))**2
sd = round(math.sqrt(sd/len(lines)), 2)
#if there is only one zero printed (rounding in python prints .0 not.00) add a zero
if len(str(sd).split(".")[1])<2:
    sda = (str(sd)+"0")
else:
    sda = sd
#print the results
print("The average is:", meana)
print("The std deviation is:", sda)

#print list of students who need help
for line in lines:
    #split the line to get their name and marks
    if int((line.split(",")[1].replace("\n", ""))) < ((mean)-(sd)):
        #append the students name to a list to print later
         students.append((line.split(",")[0]))
#print the list of students who need assistance if the len of list is not 0
if len(students)!= 0:
    print("List of students who need to see an advisor:")
print("\n".join(students))




f.close()
