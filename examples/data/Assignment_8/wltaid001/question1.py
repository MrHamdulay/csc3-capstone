"""Aiden Walton
WLTAID001
Question 1 - Assignment 8"""

def palindrome(s):
    if s=="":
        print("Palindrome!")
    elif s[len(s)-1]==s[0]:
        return palindrome(s[1:len(s)-1])
    else:
        print("Not a palindrome!")
s=input('Enter a string:\n')
palindrome(s)
                          