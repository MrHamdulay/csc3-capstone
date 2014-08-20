"""This program checks whether or not a string is a palindrome
Hebert Tema
TMXTHA006
04 May 2014"""


def reverse(string):
    """recursive function that reverse the string"""
    if string=="": return ""
    else:
        return reverse(string[1:]) + string[0]
    
def palindrome(string):
    """this function checks whether the string is a palindrome or not"""
    if string==reverse(string):
        print("Palindrome!")
    else: print("Not a palindrome!")

#get input from the user
string=input("Enter a string:\n")

#call the palindrome function
palindrome(string)