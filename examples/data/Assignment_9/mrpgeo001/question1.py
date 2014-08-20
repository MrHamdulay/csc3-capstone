"""Program to check for student advisor requirement
Geoff Murphy
MRPGEO001
11 May 2014"""

from math import *

file_name = input("Enter the marks filename:\n")

f = open(file_name,"r")

lines = f.readlines()
f.close ()

#-------------------------------------------------------------------------------

for i in range (len (lines)-1): #Removes the \n after each item
    lines[i] = lines[i][:-1]
    

names = []
marks = []

for i in lines:                #Adds the names and marks to different lists
    split = i.split(',')       
    names.append(split[0])
    marks.append(split[1])
    
#-------------------------------------------------------------------------------


average = 0

def average(l):                #Function for calculating average
    global average
    total = 0
    number = 0
    for i in l:
        total += eval(i)
        number += 1
    
    ave = total / number
    average = ave
       
average(marks)
print("The average is:",'{0:.2f}'.format(average))

#-------------------------------------------------------------------------------
  
standard_dev = 0

def std_dv(marks,average):          #Function to calculate the standard deviation, step-by-step
    global standard_dev
    mark_1 = 0
    N = 0
    for i in marks:
        a = (eval(i) - average)**2  #Subtracts the subtract from the mark and squares it
        mark_1 += a                 #Adds this to a certain variable
        N += 1                      #And adds one to the total number of items
        
    std_dev = sqrt(mark_1 / N)      #Then calculates the standard deviation
    standard_dev = std_dev
    
    
std_dv(marks,average)
print("The std deviation is:", '{0:.2f}'.format(standard_dev))
        
#-------------------------------------------------------------------------------

number_students = 0                 #Used to count the number of students who need to see an advisor

below_std_dev = average - standard_dev  #Calculates one std. dev. below the mean

for j in marks:                     
    if eval(j) < below_std_dev:
        number_students += 1        #Adds to the 'number_students' counter
        
if number_students > 0:
    print("List of students who need to see an advisor:")



position = 0

for i in marks:                     #Finally, checks who has marks one std. dev. below the mean and prints their names
    if eval(i) < below_std_dev:
        print(names[position])
        position += 1               #Position is the name's position in the 'names' list
    else:
        position += 1

#-------------------------------------------------------------------------------





