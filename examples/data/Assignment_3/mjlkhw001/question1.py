# Program to create a rectangle
# Khwezi Majola
# MJLKHW001
# 20 March 2014
def rec():
    h = eval(input('Enter the height of the rectangle:\n'))
    w = eval(input('Enter the width of the rectangle:\n'))
    for i in range(h):
        print('*' * w)
rec()