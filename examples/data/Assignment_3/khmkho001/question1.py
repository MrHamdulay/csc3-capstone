#program to draw a rectangle of a given height and width
#Nelia Khumalo
#27 March 

def rectangle():
    h=eval(input("Enter the height of the rectangle:\n"))
    w=eval(input("Enter the width of the rectangle:\n"))
    for i in range(h):
        print("*"*w)
rectangle()
    