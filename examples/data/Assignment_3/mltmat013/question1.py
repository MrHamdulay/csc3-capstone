sHeight = eval(input("Enter the height of the rectangle:\n"))
sWidth = eval(input("Enter the width of the rectangle:\n"))
def rectangle(height,width):
    for i in range(height):
        print('*'*width)
rectangle(sHeight,sWidth)