'''Program to analyse student marks and determine whether they need to see a student advisor or not
Simangaliso Mlangeni
15 May 2014'''

#import math module
import math

#get file from user and read off the the file 
filename = input('Enter the marks filename:\n')
f = open(filename,'r')
fileLines = f.readlines()#read document and store lines in a list
f.close()

#get rid of new line characters in items in the list
lines = fileLines
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]

#find the average value
Sum = 0
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    Sum += int(lines[i][-1])
avg = Sum/len(lines)

Sum = 0
#calculates the standard  deviation

for j in range(len(lines)):
    Sum += (int(lines[j][-1])-avg)**2

    
var = Sum/len(lines)  
standardDev = math.sqrt(var)
 
#Print out the avg and standard dev as requested by user/AM
print('The average is: {:.2f}'.format(avg))
print('The std deviation is: {:.2f}'.format(standardDev))

for i in range(len(fileLines)-len(lines)):
    fileLines[i] = fileLines[i][:-1]
    
y = 1
p = avg - standardDev
#checks if the student needs to see the student advisor if marks are very low 
for i in range(len(fileLines)):
    fileLine = int(fileLines[i][-1])
    if fileLine < p:#checks if students mark is less than one standard deviation below the mean 
        for j in range(y):
            print('List of students who need to see an advisor:')
            y = 0
        print(fileLines[i][0])
        
