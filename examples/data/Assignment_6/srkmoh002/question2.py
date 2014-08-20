# Najeeb Sirkhoth
# SRKMOH002
# question2.py
# Assignment 6

# Program allowing user to do basic vector calculations of 3 dimensions
# Operations include; addition, dot product and normalisation

import math

# Get user input
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")


# Create Empty list
Alist = []
Blist = []



# Converting string to list
for i in A.split(" "):                  # Split string at blank space
    value = eval(i)                     # Covert digit to number
    Alist.append(value)                 # Append each number to emptylist
    
for i in B.split(" "):
    value = eval(i)
    Blist.append(value) 




# Vector Addition
addition = []                          # Create Empty list
for i in range(3):                     
    newvalue = Alist[i]+Blist[i]       # Add items of two list
    addition.append(newvalue)          # Append this value to emptylist
    
print ("A+B =", addition)    



# Vector dot product
dotproduct = []                        # Create Empty list
for i in range(3):                     
    newvalue = Alist[i]*Blist[i]       # Multiply items of two list
    dotproduct.append(newvalue)        # Append this value to emptylist

answer = dotproduct[0]+dotproduct[1]+dotproduct[2]      # Add each item
print("A.B =", answer)



# Vector normalisation
Asquares = []                                               # Create Empty List
for i in range(3):
    Asquares.append(Alist[i]**2)                            # Square each item and append to emptylist

Anorm = math.sqrt(Asquares[0]+Asquares[1]+Asquares[2])      # Square root sum of squares
print("|A| = {0:0.2f}".format(Anorm))


# Same process for B vector
Bsquares = []                                               
for i in range(3):
    Bsquares.append(Blist[i]**2)                            

Bnorm = math.sqrt(Bsquares[0]+Bsquares[1]+Bsquares[2])      
print("|B| = {0:0.2f}".format(Bnorm))