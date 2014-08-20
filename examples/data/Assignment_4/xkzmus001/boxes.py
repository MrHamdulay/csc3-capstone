# Description
# Name: Musa Xakaza
# Student Number: XKZMUS001
# Date:

def print_square ():
    W , H = 5 , 5
    print('*'*W)
    for i in range(1, (H-1)):
        print('*', ' '*(W-2), '*', sep = '')
    print('*'*W)

def print_rectangle (width, height):
    W , H = width , height
    print('*'*W)
    for i in range(1, (H-1)):
        print('*', ' '*(W-2), '*', sep = '')
    print('*'*W)

def get_rectangle (width, height):
    W , H = width , height
    box = '*'*W+ '\n'
    for i in range(1, (H-1)):
        box +='*'+' '*(W-2)+'*'+'\n'
    box += '*'*W
    return box