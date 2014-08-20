def rectangle():
    x = eval(input("Enter the height of the rectangle:\n"))
    y = eval(input("Enter the width of the rectangle:\n"))
    z = (y*"*")
    print ((z+"\n")*x)
rectangle()