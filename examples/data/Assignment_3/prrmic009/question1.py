# program to print a rectangle of input height and width
# Mick Perring
# 27 arch 2014

x = eval(input("Enter the height of the rectangle:""\n")) # Allows user to input rectangle height
y = eval(input("Enter the width of the rectangle:""\n"))  # Allows user to input rectangle width

def rec(R):                   # Function of rectangle, prints rectangle of input height and width
    for i in range (R):
        print ('*'*y)
        
rec(x)