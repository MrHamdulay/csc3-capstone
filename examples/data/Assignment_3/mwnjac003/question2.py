def pyramid():
    x=eval(input("Enter the height of the triangle:\n"))
    y = x * 2
    for i in range(1, y, 2):
        print("{0:^{1}}".format("*" * i, y))
pyramid()