#Question1.py
#A program to draw the triangle of a given height and width using the "*" character
#Author: Michelle Njoroge

def main():
    height=eval(input("Enter the height of the rectangle:\n"))
    width=eval(input("Enter the width of the rectangle:\n"))
    for i in range(height):
        print("*"*width)
            
main()

    
    