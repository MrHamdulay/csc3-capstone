""" Calculations with vectors
Kumaran Reddy
24 April 2014 """


import math
#To get two vectors
Vector_a=(input("Enter vector A:\n"))
Vector_b=(input("Enter vector B:\n"))

#To work with each calculation
#For addition
Add= []
i=0
while i in range(5):
               ADD =int(Vector_a[i]) + int(Vector_b[i])#to add corresponding positions
               Add.append(ADD)#add them to the list
               i+=2


print("A+B =", Add)

#For multiplication
value=0
i=0
while i in range(5):
               new=int(Vector_a[i])*int(Vector_b[i])#get multiplied value for each position in list
               value+=new#add this to total value
               i+=2
               
print("A.B =",value)

#To find norm

A=0
i=0
while i in range(5):
               New=int(Vector_a[i])**2
               A+=New
               i+=2
Aa=round(math.sqrt(A),2)
print("|A| =",Aa)

B=0
i=0
while i in range(5):
               New=int(Vector_b[i])**2
               B+=New
               i+=2
Bb=round(math.sqrt(B),2)
print("|B| =",Bb)

