#nasha meoli
#21st march 2013
#program to print rectangle
height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))

def rectangle(ch):
    for i in range(height):
        print(ch*width)
        
rectangle("*")