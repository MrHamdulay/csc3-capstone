#-------------------------------------------------------------------------------
# Name:        question2
# Purpose: Draws a triangle of given height using '*'
#
# Author:      Pilusa
#
# Created:     20/03/2014
# Copyright:   (c) Pilusa 2014
#-------------------------------------------------------------------------------

def main():
    t=1
    height=eval(input('Enter the height of the triangle:\n'))
    spacing=height-1
    for i in range(spacing,-1,-1):
        if t>=0:
            print(' '*i+'*'*t)
        t+=2
    
if __name__ == '__main__':
    main()
