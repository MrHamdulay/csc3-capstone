#program to draw a rectangle given height and width
#24/03/2014

def rectangle(height,width):
    for i in range(height):
        print("*"*width)

height=eval(input("Enter the height of the rectangle:\n"))
width=eval(input("Enter the width of the rectangle:\n"))
rectangle(height,width)