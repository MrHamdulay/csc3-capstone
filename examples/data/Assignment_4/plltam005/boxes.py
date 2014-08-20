# Assignment 4, question 1-module
# Tameryn Pillay
# April 2014

def print_square():
    print("*"*5)
    for i in range(1,4):
        print("*","   ","*",sep="")
    print("*"*5)

def print_rectangle(width, height):
    print("*"*width)
    for i in range(1,height-1):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)

def get_rectangle(width,height):
    figure = (width*"*")
    for i in range(height-2):
        figure = figure + ("\n*"+(width-2)*" "+"*")
    figure = figure + ("\n"+width*"*")
    return figure

    

    
