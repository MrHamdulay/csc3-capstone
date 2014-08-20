#-------------------------------------------------------------------------------
# Name:        question2
# Purpose:     program that uses a recursive function to count the number of
#              pairs of repeated characters in a string
#
# Author:      Lungelo Mdunge
#
# Created:     04/05/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

string=input("Enter a message:\n")

def pairs(string):
    if len(string)==1 or string=='':
        return 0
    elif string[0]==string[1]:
        return 1 + pairs(string[2::])
    else:
        return pairs(string[1::])

pairs=pairs(string)

print("Number of pairs:",pairs)