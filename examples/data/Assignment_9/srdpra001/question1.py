'''
Prashanth Sridharan
SRDPRA001
Assignment 09
Question 01
'''
import math
file_name = input ("Enter the marks filename:\n")
i = open (file_name, "r") #variable name i declared as the variable which opens and reads the file
data = i.readlines () #variable data is declared to read the lines in the file to be assigned to this variable
i.close ()
sum_count = 0 #initialising the sum variable
count = 0 #initialising a count variable
for l in data: #variable l is the variable name for the list l.
   l = l[:-1]
   fields = l.split (",")
   if len (fields) == 2:
      count += 1
      sum_count += int (fields[1])
ave = sum_count/count #ave is the variable name for average
print ("The average is: {:.2f}".format (ave))
standard_deviation = 0 #the variable for standard deviation is initialised here.
for l in data:
   l = l[:-1] 
   fields = l.split (",") #splits the field variable into an array with a comma seperation.
   if len (fields) == 2:
      standard_deviation += (int (fields[1]) - ave)**2
standard_deviation = math.sqrt (standard_deviation / count) #formula to calculate standard deviation
print ("The std deviation is: {:.2f}".format (standard_deviation)) #prints the standard deviation to 2 decimal places.
heading = 0 #initialising the variable for heading.
for l in data:
   l = l[:-1]
   fields = l.split (",")
   if len (fields) == 2:
      if int(fields[1]) < ave-standard_deviation:
         if heading == 0:
            heading = 1
            print ("List of students who need to see an advisor:")
         print (fields[0])
