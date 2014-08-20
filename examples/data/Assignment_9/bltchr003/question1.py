"""question 1 Assignment 9
CHRIS BOLTON
File reading"""


import sys

filename = input("Enter the marks filename:")

try:
f = open (filename , “r”)

except IOError as errno:
   print ("Could not read file")
   print ("Error number:",errno)
finally:
   print ("cleaning up")











f.close ()











print ("The average is:" ,  avg)
print ("The std deviation is:" , sd)
print ("List of students who need to see an advisor:" , students)
