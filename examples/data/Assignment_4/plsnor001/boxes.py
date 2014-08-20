#-------------------------------------------------------------------------------
# Name:        boxes
# Purpose:
#
# Author:      Pilusa
#
# Created:     02-04-2014
# Copyright:   (c) Pilusa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_square ():
    s='*'
    e=' '
    print(s*5)              #prints first line of box
    for i in range (3):
        print(s+e*3+s)
    print(s*5)              #prints the sides of box



def print_rectangle (width, height):
    s='*'
    e=' '
    width=int(width)
    height=int(height)

    print(s*width)          #prints first line of box
    for i in range (height-2):
        print(s+e*(width-2)+s)
    print(s*width)          #prints the sides of box




def get_rectangle(width,height):
    s='*'
    e=' '
    latter='\n'
    first_last='*'*width+latter
    middle=(s+e*(width-2)+s+latter)*(height-2)

    return first_last+middle+first_last

