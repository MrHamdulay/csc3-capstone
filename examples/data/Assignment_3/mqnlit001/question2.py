#Program to output a triangle
# 26 March 2014
# Author: Litha Maqungo

def triangle():
    print("Enter the height of the triangle:")
    height=eval(input())
    gap= height
    for i in range(0,height):
        print(" "*(gap-1),end =''*(gap-1), sep='')
        print("*"*(i+1) + "*"*(i), sep='')
        gap= gap-1
    
triangle()
    
            