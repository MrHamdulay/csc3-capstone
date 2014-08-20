# Program to print out a triangle
# Nevarr Pillay - PLLNEV006
# 8 March 2014

import math

def tri(height):
    for i in range(1,height+1):
        for j in range(height-i):
            print(end=" ")
        for star in range(i*2-1):
            print("*",end="")
        print()    

def main():
    height = eval(input("Enter the height of the triangle:\n"))
    tri(height)
    
main()  

