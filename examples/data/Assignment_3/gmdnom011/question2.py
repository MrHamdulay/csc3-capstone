# 23 March 2014
# Program to draw an isoceles triangle of input height
# by Nomsa Gamedze

def isoc_triangle():
    height = eval(input("Enter the height of the triangle:"'\n'))
    j = height
    o = 1
    for i in range(height):
        print(" "*(j-1), "*"*o, sep="")
        j-=1
        o+=2
        
isoc_triangle()