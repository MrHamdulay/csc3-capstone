# Assignment 3
# Question2 (drawing an isoceles triangle)
# Ntuthuko Mthiyane
# 20 March 2014

def triangle():
    x = eval(input("Enter the height of the triangle:\n"))
    count = 0
    y = 1
    sep=" "
    q=x-1
    while count < x:
        
        print(sep*q,"*"*y, sep='')
        y+=2
        count+=1
        q-=1
triangle()
        
