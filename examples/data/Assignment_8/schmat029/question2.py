#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     checks for repeated characters recursively
#
# Author:      Matthias
#
# Created:     04-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def repeat_char(string):
    if len(string) <= 1:
        # basecase if the string has no more pairs left
        return 0
    if string[0] == string[1]:
        return 1 + repeat_char(string[2:])
    else:
        return 0 + repeat_char(string[2:])

string = input("Enter a message: \n")
print("Number of pairs:", repeat_char(string))