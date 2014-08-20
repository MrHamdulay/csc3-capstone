def rectangle(s):
    height=eval(input("Enter the height of the rectangle: \n"))
    width=eval(input("Enter the width of the rectangle: \n"))
    for i in range(height):
        print(s*width)
rectangle("*")