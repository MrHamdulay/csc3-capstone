"""palindrome recursive function 
Author: Onalerona Mosimege
04 May 2014"""


def palindrome(s):
    """calculate whether or not a string is a palindrome (reads the same if reversed)"""
    #output if the string is a palindrome
    string1 = 'Palindrome!' 
    #output if the string is not a palindrome
    string2 = 'Not a palindrome!'
    #base case - if only one letter, automatically a palindrome
    if len(s) <= 1:
        print(string1)
    #recursive step
    elif s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return print(string2)
    
s= input('Enter a string:\n')
palindrome(s)