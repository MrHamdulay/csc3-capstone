# question1.py
# a program to draw a rectangle of a given height and width using the * character.
# Thomas Konigkramer
# 19 March 2014


def rect():
    # program inquiring user for inputs (height and width of rectangle)
    h = eval(input("Enter the height of the rectangle: \n"))
    w = eval(input("Enter the width of the rectangle: \n"))
    
    for i in range(h):
        print("*" * w)
        
rect()