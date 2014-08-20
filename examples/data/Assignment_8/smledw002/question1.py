#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014 - 05 - 09
#Function       : Checks for palindromes
#Title          : Question 1


def string_reverse(string, length):
    """reverses a string"""
    if length < 0:
        return ""
    return string[length] + string_reverse(string, length - 1)


def palindrome(string):
    """checks if a string is a palindrome"""
    if string == string_reverse(string, len(string)-1):
        return True
    return False

test_value = input("Enter a string:\n")

if palindrome(test_value):

    print("Palindrome!")

else:

    print("Not a palindrome!")









