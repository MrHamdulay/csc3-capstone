
def triangle(height, width):
    for j in range(height):
        i = 0
        for i in range(width):
            print("*", end = "")
        print("")
xinput = eval(input("Enter the height of the rectangle:\n"))
yinput = eval(input("Enter the width of the rectangle:\n"))
triangle(xinput,yinput)