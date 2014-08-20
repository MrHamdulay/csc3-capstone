# Assignment 3
# Question1 ( Drawing a rectange )
# Ntuthuko Mthiyane
# 20 March 2014

def rectangle():
    x = eval(input("Enter the height of the rectangle:\n"))
    y = eval(input("Enter the width of the rectangle:\n"))
    
    count = 0
    while count < x:
        print("*" * y,)
        count+=1
rectangle()            