#Q2 of Assignment 3
#KVRSHA004
#Q2 of Assignment 3
#KVRSHA004
#Triangle Builder

x = eval(input("Enter the height of the triangle: \n"))
gap = x-1
linewidth = 1
for i in range(x):
    print(" "*gap + "*"*linewidth)
    linewidth+=2
    gap-=1
    