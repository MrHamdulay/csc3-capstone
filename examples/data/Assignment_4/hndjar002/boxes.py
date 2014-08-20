# Assignment 4
# Jaren Hendricks
# 02 April 2014

# Function to print a square
def print_square ():
    for k in range(5):
        for i in range(5):
            if (k == 0) or (k == 4) or  (i == 0)  or (i == 4): # Checks for the highest and lowest values. 
                print ("*", end = "")
            else:
                print(" ",end ="")
        print() 

# Outputs the code written in function get_rectangle
def print_rectangle (width, height):
    print (get_rectangle (width, height))
     
# Function to process the rectangle that's output in function print_rectangle
def get_rectangle (width, height): 
    x = ""    
    for k in range(height):
        for i in range(width):
            if (k == 0) or (k == height-1) or (i == 0) or (i == width-1):
                x += "*"
            else:
                x += " "
        if k!= height-1:
            x += "\n"
    return x