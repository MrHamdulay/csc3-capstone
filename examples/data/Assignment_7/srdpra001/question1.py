"""
Prashanth Sridharan
SRDPRA001
Assignment 07
Question 01
"""
print ("Enter strings (end with DONE):")

i = []

string = input ("") #input a string
while string !="DONE": #loop the inputs until user inputs 'DONE'
   if not string in i:
      i.append (string) #strings added to list 'i'
   string = input ("")
   
print ("")

print ("Unique list:")
for word in i:
   print (word)
          
   
