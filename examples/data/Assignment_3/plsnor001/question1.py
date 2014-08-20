#-------------------------------------------------------------------------------
# Name:    question1
# Purpose: draws a rectangle of a given height and width using the '*' character
#
# Author:  Pilusa
#
# Created:    19/03/2014
# Copyright:  (c) Pilusa 2014
#-------------------------------------------------------------------------------

def main():
    height=eval(input('Enter the height of the rectangle:\n'))
    width=eval(input('Enter the width of the rectangle:\n'))
    for i in range(height):
        print('*'*width)

if __name__ == '__main__':
    main()
