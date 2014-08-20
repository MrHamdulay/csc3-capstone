#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lungelo
#
# Created:     29/03/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_square():
    print("*****")
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')

def print_rectangle(width,height):
    print('*'*width)
    gaps=width-2
    for i in range(height-2):
        print('*'+' '*gaps+'*')
    print('*'*width)

def get_rectangle(width,height):
    box_string='*'*width+'\n'
    for i in range(height-2):
        box_string+='*'
        for i in range(width-2):
            box_string+=' '
        box_string+='*\n'
    box_string+='*'*width

    return box_string


