# Program to print out a rectangle
# Nevarr Pillay - PLLNEV006
# 20 March 2014

def rect(height,width):
    for i in range(height):
        for i in range(width):
            print("*",end="")
        print()    

def main():
    height = eval(input("Enter the height of the rectangle:\n"))
    width = eval(input("Enter the width of the rectangle:\n"))
    rect(height,width)           
    
main()  

