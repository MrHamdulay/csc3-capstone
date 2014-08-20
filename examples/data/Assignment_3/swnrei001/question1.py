def rectprint(height, width):
    for i in range(height):
        print('*'*width)


if __name__ == '__main__':
    h = eval(input("Enter the height of the rectangle:\n"))
    w = eval(input("Enter the width of the rectangle:\n"))
    rectprint(h, w)