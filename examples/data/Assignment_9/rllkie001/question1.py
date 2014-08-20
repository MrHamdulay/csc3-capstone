'''Assign9,Q1 reading marks finding standard diviation printing results
Kieran Reilly, RLLKIE001
12/04/14'''

import math
import decimal

fileName = input("Enter the marks filename:\n")
lines = []      #empty array to store lines in txt file

#open, reads and stores, and closes the textfile
f = open (fileName, "r")
lines = f.readlines()
f.close

#just used to take away the "\n"
for i in range(len(lines)):
    if i+1 < len(lines):
        lines[i] = lines[i][:-1]
        
    
marks = []      #used to store the marks of each student
names = []
line = ""
index = 0           #used to get the position of the "," char

#used to store the marks in marks[]
for i in range(len(lines)):
    line = lines[i]
    index = line.index(",")
    marks.append(line[index+1:])
    names.append(line[:index])
    

#getting the sum of all the marks as total
total = 0    
for i in range(len(lines)):
    total = total + int(marks[i])
    
#calculating the mean
mean = round(total/len(marks),2)
print("The average is: "+str("%0.2f" % mean))


#standard deciation = sqrt(((Xi-u)**2+...(Xn-1-u)**2)/n)
#getting the inner brakets of the formula: (Xi-u)**2+...(Xn-1-u)**2
sumSquares = 0.00
innerSquare = 0.00
for i in range(len(lines)):
    innerSquare = round((float(marks[i]) - mean)**2,2)
    sumSquares = sumSquares + innerSquare

#calculating the variance: ((Xi-u)**2+...(Xn-1-u)**2)/n
variance = round(sumSquares/len(marks),2)

#calculating std deviation: sqrt(variance)
standardDeviation = round(math.sqrt(variance),2)
print("The std deviation is: "+str("%0.2f" % standardDeviation))

oneStdDeviat = round(mean - standardDeviation,2)

#printing out
fails = False
for i in range(len(marks)):
    if float(marks[i]) < oneStdDeviat:
        fails = True
        
if fails == True:
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if float(marks[i]) < oneStdDeviat:
            print(names[i])
    
