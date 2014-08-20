"""program to print a list right-aligned
author: Divan Jagers
254 April 2014"""
x = []     #creates an empty list
a =""
a= input("Enter strings (end with DONE):\n")
while a != "DONE": #adds each item to the list
    x.append(a)
    a= input("")
long = 0             #the longest item in the list
for item in x :      #looks for longest item in list
    length = len(item)
    if length >= long:
        long = length
    else:
        break
print("")
print("Right-aligned list:")
for word in x:
    print(" "*(long-len(word))+word)     #prints  " " depending on how long the longest item in the list is
          
        