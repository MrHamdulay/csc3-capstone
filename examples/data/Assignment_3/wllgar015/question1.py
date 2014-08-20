#question 1
#constructing a rectangle according to the specifics of the user

def rb(width,height):    
    for i in range(height):
        print(width*"*")
height=eval(input("Enter the height of the rectangle: \n"))
width=eval(input("Enter the width of the rectangle: \n"))

rb(width,height)