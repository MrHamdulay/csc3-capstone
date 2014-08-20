# Assignment 3 Question 2
#Name: Shaheen Karodia
#Student Number: KRDSHA0036
#Date 2014-03-20
 

h=eval(input("Enter the height of the triangle:\n"))
t=1
space=h
for i in range (h):
    
    space=space-1
    print(space*" ","*"*t, sep="")
    t=t+2
    