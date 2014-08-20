""" Assignment 4 Questiosn 1 by Jonathan Ovadia
on the 31st of Marth 2014"""
def print_square():
    print("*"*5)
    for i in range(3):
        print("*" + " "*3 + "*")
    print("*"*5)
    
    
def print_rectangle (width, height):
    print("*"*width)
    for i in range(height-2):
        print("*" + " "*(width-2) + "*")
    print("*"*width)
    
    
def get_rectangle (width, height):
    box = ""
    box+=("*"*width + "\n")
    for i in range(height-2):
        box+=("*" + " "*(width-2) + "*" +"\n")
    box+=("*"*width +"\n")
    return box
