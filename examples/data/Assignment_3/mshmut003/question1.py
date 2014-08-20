# This program uses the asterisk to draw the infamous RECTANGLE
# by MSHMUT003 (R)

def rect():
    h=eval(input('Enter the height of the rectangle:\n'))
    w=eval(input('Enter the width of the rectangle:\n'))
    if h>0 and w>0:
        for i in range(h):
            print('*'*w)
rect()