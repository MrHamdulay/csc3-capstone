__author__ = 'TMPSTE002'

def printRectangle(h, w):
    for i in range(h):
        print('*'*w)

if __name__ == '__main__':
    h = eval(input("Enter the height of the rectangle:\n"))
    w = eval(input("Enter the width of the rectangle:\n"))
    printRectangle(h, w)