#Ross van der Heyde VHYROS001
#Assignment 3 question 2

h = eval(input ("Enter the height of the triangle:\n"))

for i in range(1,h+1):   
    print(" "*(h-1),end="")
    h-=1
    print("*"*(i*2-1))