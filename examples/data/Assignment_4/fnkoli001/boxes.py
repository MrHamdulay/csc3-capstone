# coding=utf-8

def print_square ():
    print('*'*5+"\n"+('*'+' '*3+'*'+"\n")*3+'*'*5)

def print_rectangle (width, height):
    print('*'*width+"\n"+('*'+' '*(width-2)+'*'+"\n")*(height-2)+'*'*width)

def get_rectangle (width, height):
    return '*'*width+"\n"+('*'+' '*(width-2)+'*'+"\n")*(height-2)+'*'*width