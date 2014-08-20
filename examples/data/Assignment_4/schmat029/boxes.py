#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     28-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def print_square():
    print("*****")
    print("*   *\n" * 3, end="")
    print("*****")

def print_rectangle(width, height):
    print("*" * width)
    print(("*" + " "*(width-2) + "*\n") * (height-2), end="")
    print("*" * width)

def get_rectangle(width, height):
    return("*" * width + "\n" + (("*") + " "*(width-2) + "*\n") * (height-2) + "*" *width)
