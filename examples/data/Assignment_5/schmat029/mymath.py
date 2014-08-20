#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     13-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def get_integer(s):
    number = ""
    while not number.isdigit():
        number = input("Enter " + s + ":\n")
    return eval(number)

def calc_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

if __name__ == '__main__':
    main()
