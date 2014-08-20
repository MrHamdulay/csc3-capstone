# program  that draws a rectangle of supplied length and breadth using "*"
# Xola Bilose
# 20/03/2014

rectangle_height = eval(input("Enter the height of the rectangle:\n"))
breadth = eval(input("Enter the width of the rectangle:\n"))
for i in range (rectangle_height):
    print('*'*breadth)