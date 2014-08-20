def rect(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end="")
        print()

if __name__ == '__main__':

    x = eval(input("Enter the height of the rectangle: \n"))
    y = eval(input("Enter the width of the rectangle: \n"))
    rect(x, y)
