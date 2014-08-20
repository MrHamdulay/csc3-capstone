'''
Prashanth Sridharan
SRDPRA001
Assignment 06
Question 01
'''
n = [] #creating an array or a list for values to be read into
print ("Enter strings (end with DONE):")
name = "" #initialising name
longest = 0 #initialising longest
while name != "DONE": # loop condition
   name = input ("")
   if name != "DONE": 
      n.append (name)
      if len(name) > longest:
         longest = len(name)
      
print ("\nRight-aligned list:")
for name in n:
   print (("{:>"+str(longest)+"}").format(name)) #outputs right aligned list
