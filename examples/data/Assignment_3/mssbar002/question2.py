# Assignment 3. Question 2
# Write a program to draw an isoceles triangle of a given height using the * character

# Author: Barnett msiska(MSSBAR002)
# Date: 20/03/2014

def main():
    # request user input
    height = eval(input("Enter the height of the triangle:\n"))
    
    if height > 0:
    # print rectangle
        width = (height * 2) - 1
        characters = 1
        while height > 0:
            #characters = height - (height - 1)
            #while characters > 0:
            row = "{0:^{width}}"
            print(row.format('*'*characters, width = width))
            height -= 1
            characters += 2
        
main()