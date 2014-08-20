#Keanon Fell
#Computer Science assignment 9 
#11 May 2014
#Reads text and prints the names of those who need to see a studenta advisor

import math

names = []
newList = []
studentNames = []
sum = 0 

#=========================================================================
def stndDev(x):
    variance = 0 
    for a in range(len(newList)):
        factor = (newList[a] - x)**2
        variance += factor
    variance = variance/ len(newList)
    deviation = math.sqrt(variance)
    return deviation
#=======================================================================

print("Enter the marks filename:")
filename = input()
infile = open(filename,"r")
names = infile.readlines()#Reading data from text file into an array of strings
infile.close()

#For loop used to store the scores in a loop 
for i in range(len(names)):
    line = names[i]
    index = int( line.find(",") )
    length = len(line)
    number = int( line[index + 1:length-1] )
    newList.append(number)
    
for k in range(len(newList)): 
    sum += newList[k]#Calculating the sum of all of the marks in the list
average = sum/ len(newList)#Calculating the average of all the marks

std = stndDev(average)#Using the function to calculate the standard deviation using the average

#Printing the desired output
print("The average is: {0:0.2f}".format(average))
print("The std deviation is: {0:0.2f}".format(std))
print("List of students who need to see an advisor:")

#For loop used to store the names in a loop
for i in range(len(names)): 
    line = names[i]
    index = int( line.find(",") )
    name = line[0:index]
    studentNames.append(name)

#Printing out the names that need to see a student advisor
for g in range(len(names)):
    if newList[g] < (average - std):
        print(studentNames[g])