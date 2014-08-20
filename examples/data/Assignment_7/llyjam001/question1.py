"""Assignment 7 Question 1
James Lloyd
28 April 2014"""

#retrieving the list of strings
list = []
inp = input ("Enter strings (end with DONE):\n")

#Filling list with non repeating variables
while inp != "DONE":
    #Adding new names to list
    if inp not in list: 
        list.append (inp)
    inp = input ()

#Iterating through string to print
print ()
print ("Unique list:")
for i in list:
    print (i)
    
        