#MDLKUR001
#Assignment 3
#Question 2

x=eval(input("Enter the height of the triangle: \n"))
y=" "
z=1
while x>=1:
    print(y*(x-1),z*"*", sep="")
    z+=2
    x=x-1