#creating a rectangle
#created by tafara mtutu
#21 march 2013
def rectangle(height, width):
    for j in range(height):
        i = 0
        for i in range(width):
            print("*", end = "")
        print("")
x = eval(input("Enter the height of the rectangle:\n"))
y = eval(input("Enter the width of the rectangle:\n"))
rectangle(x,y)