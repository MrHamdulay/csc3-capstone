#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     07-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def leapyear():
    year = eval(input("Enter a year: \n"))
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == '__main__':
    leapyear()
