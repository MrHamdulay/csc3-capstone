def rectangle (width, height):
    if height != 0:
        x = height//height
        y = height+1
        for i in range (x,y):
            print("*"*width)
        
height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))
rectangle(width, height)