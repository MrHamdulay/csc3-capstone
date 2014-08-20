#print a * isos triangle of a given height
#Assignment 3 Question 2
#Brandon Pickup - PCKBRA002
#19 March 2014
height = eval(input("Enter the height of the triangle:\n"))
for i in range(1,height+1):
    print(" "*(height-(i)),"*"*(2*i-1),sep="")
    