#program to draw a rectangle of a given height and width
#vuyolwethu nkosi
#24 march 2014

def rectangle():
    height=eval(input("Enter the height of the rectangle:\n"))
    width=eval(input("Enter the width of the rectangle:\n"))
    for i in range(height):
            print("*"*width)

rectangle()
            
            
        