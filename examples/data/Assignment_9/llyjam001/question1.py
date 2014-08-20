"""Assignment 9 Question 1
James Lloyd
10 May 2014"""

#Importing math library for sqrt and defining variables for later use
import math
advisor_list = []
totalav = 0
totaldev = 0

#Obtaining file name
filename = input ("Enter the marks filename:\n")

#Creating list of file names from given file
f = open (filename, "r")
lists = f.readlines ()
f.close ()

#Removing \n
for i in range (len (lists)):
    lists [i] = lists [i] [0:-1]

#Calculating Average   
for i in range (len (lists)):
    position = lists [i].find (",")
    mark = eval (lists [i] [position + 1:])
    totalav += mark
average = round (totalav / len (lists), 2)

#Calculating std deviation
for i in range (len (lists)):
    position = lists [i].find (",")
    mark = eval (lists [i] [position + 1:])
    totaldev += (mark - average)**2
deviation = round (math.sqrt (totaldev / len (lists)), 2)

#Creating list of students who need to see advisor
for i in range (len (lists)):
    position = lists [i].find (",")
    mark = eval (lists [i] [position + 1:])
    too_low = average - deviation
    if mark < too_low:
        advisor_list.append (lists [i] [0:position])

average = str (average)
if average [-1] == '0':
    average = average + '0'
    
deviation = str (deviation)
if deviation [-1] == '0':
    deviation = deviation + '0'

print ("The average is: " + average)
print ("The std deviation is: " + deviation)
if advisor_list != []:
    print ("List of students who need to see an advisor:")
    #Printing list
    for i in advisor_list:
        print (i)
