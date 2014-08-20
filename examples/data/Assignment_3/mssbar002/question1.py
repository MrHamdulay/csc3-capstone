# Assignment 3. Question 1
# Write a program to draw a rectangle of a given height and width 
# using the * character. 

# Author: Barnett msiska(MSSBAR002)
# Date: 20/03/2014

def main():
    # request user input
    height = eval(input("Enter the height of the rectangle:\n"))
    width = eval(input("Enter the width of the rectangle:\n"))
    
    if height > 0 and width > 0:
        # print rectangle
        while height > 0:
            w = width
            while w > 0:
                print("*", end='')
                w -= 1
            print("\n", end='')
            height -= 1
            
main()