"""Question 1 of Assignment 4"""
"""Mick Perring"""
"""3 April 2014"""

def print_square ():
    print (5*"*")
    for i in range (0, 3):
        print ("*" + 3*" " + "*")
    print (5*"*")

def print_rectangle (width, height):
    w = width - 2
    h = height - 2    
    print (width*"*")
    for i in range (0, h):
        print ("*" + w*" " + "*")
    print (width*"*")    

def get_rectangle (width, height):
    w = width - 2
    h = height - 2    
    x = width*"*" + "\n"
    for i in range (0, h):
        x += "*" + w*" " + "*" + "\n"
    x += width*"*"
    return x
