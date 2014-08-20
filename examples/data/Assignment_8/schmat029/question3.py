#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     encrypts a given message
#
# Author:      Matthias
#
# Created:     05-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def encrypt(string):
    if string == "":
        # basecase where the string is empty
        return ""
    else:
        # convert the first character to its equivalent UNICODE number
        num = ord(string[0])
        if num < 122 and num >= 97:
            # if the character is between a and y, add one and convert back
            char = chr(num + 1)
        elif num == 122:
            # if the character is z, go back to a
            char = chr(97)
        else:
            # if the character is anything else, DO NOT add to the number
            char = chr(num)
        return char + encrypt(string[1:])

string = input("Enter a message: \n")
print("Encrypted message: \n" + encrypt(string))