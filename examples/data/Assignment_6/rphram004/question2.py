"""programme that adds and multiplies arrays
#rama raphalalani
#19-04-2014"""

import math #importing maths library
#getting inputs and splitting those up into indiviual strings
vector_a = input("Enter vector A:\n")
vector_b = input("Enter vector B:\n")
a = vector_a.split(" ")
b = vector_b.split(" ")

#assigning each string a variable and creating a list for the add function
a0,a1,a2,b0,b1,b2 = a[0],a[1],a[2],b[0],b[1],b[2]
c,d,e,f,g,h = int(a0),int(a1),int(a2),int(b0),int(b1),int(b2)
add = [c+f,d+g,e+h]
mult = (c*f)+(d*g)+(e*h)

#doing all the maths required for the required output
sq_a = math.sqrt((c**2)+(d**2)+(e**2))
sq_a = round(sq_a,2)
sq_b = math.sqrt((f**2)+(g**2)+(h**2))
sq_b = round(sq_b,2)

#various print statements for each line
print("A+B = ",add,sep='')
print("A.B = ",mult,sep='')
print("|A| = ",sq_a,sep='')
print("|B| = ",sq_b,sep='')