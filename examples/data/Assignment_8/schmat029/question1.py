#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     checks recursively for palindromes
#
# Author:      Matthias
#
# Created:     04-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def is_palindrome(string):
    if string == "":
        # basecase if the string is empty - indicates a palindrome
        return True
    if string[0] != string[-1]:
        # second basecase if first and last characters are not equal - not a palindrome
        return False
    return is_palindrome(string[1:-1])

string = input("Enter a string: \n")

# checks for function output and prints the corresponding statement
if is_palindrome(string):
    print("Palindrome!")
else:
    print("Not a palindrome!")