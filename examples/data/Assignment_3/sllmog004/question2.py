# SLLMOG004
#Question 1 of Assignment 3

height=eval(input("Enter the height of the triangle:\n"))
for i in range(0,height):
    print(" "*(height-(i+1)),end="")
    print("*"*(2*i+1))