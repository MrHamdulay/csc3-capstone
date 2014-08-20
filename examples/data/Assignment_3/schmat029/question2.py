#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     19-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    height = eval(input("Enter the height of the triangle: \n"))
    for i in range(height):
        print(" "*(height-1-i) + "*"*(2*i+1) + " "*(height-1-i))

if __name__ == '__main__':
    main()
