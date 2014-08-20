#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Pilusa
#
# Created:     08/03/2014
# Copyright:   (c) Pilusa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    import calendar
    year=eval(input('Enter a year:\n'))
    if calendar.isleap(year):
        print(year,'is a leap year.')
    else:
        print(year,'is not a leap year.')

if __name__ == '__main__':
    main()
