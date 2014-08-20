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
    height = eval(input("Enter the height of the rectangle: \n"))
    width = eval(input("Enter the width of the rectangle: \n"))
    for i in range(height):
        print("*"*width)

if __name__ == '__main__':
    main()
