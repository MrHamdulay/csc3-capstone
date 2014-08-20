"""Tevin Chetty
22 April 2014
Program to align a list of names"""

import math #for squareroot

vectors_A=input("Enter vector A: \n")
vectors_B=input("Enter vector B: \n")

#splits the string input up and makes a list
list_a=vectors_A.split(" ")
list_b=vectors_B.split(" ")

new_list=[]
#creates a list with each vector added together
x=0
while x<=2:
    position=eval(list_a[x])+eval(list_b[x])
    new_list.append(position)
    x+=1
print("A+B =", new_list)

#Muliplies each vector and then adds them together
y=0
multiplication=0
while y<=2:
    multiplication+=(eval(list_a[y]))*(eval(list_b[y]))
    y+=1
print("A.B =", multiplication)

#finds the squareroot of the sum of each vector squared for a and b
absolute_a=(math.sqrt((eval(list_a[0]))**2+(eval(list_a[1]))**2+(eval(list_a[2]))**2))
print("|A| =","{0:.2f}".format(absolute_a)) #.2f shortens it to 2 decimal places while round would make 0.00 to 0.0

absolute_b=(math.sqrt((eval(list_b[0]))**2+(eval(list_b[1]))**2+(eval(list_b[2]))**2))
print("|B| =","{0:.2f}".format(absolute_b)) 