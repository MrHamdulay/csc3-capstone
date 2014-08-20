# Zikho Godana
#24 March 2014
#Program to draw a rectangle of a given height and width using the '*' character.

height=eval(input("Enter the height of the rectangle:\n"))
width=eval(input("Enter the width of the rectangle:\n"))
def Rectangle(height,width):
    print(('*'*width+'\n')*height)
            
Rectangle(height,width)