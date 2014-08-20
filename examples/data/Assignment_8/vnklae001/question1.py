# Assignment 8 (Q1)
# A program that tests to see if a string is a palindrome or not
# Written by: Laene van Niekerk
# VNKLAE001

def is_palindrome(s):
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            return is_palindrome(s[1:len(s)-1])
        else:
            return False
        
x = input("Enter a string:\n")
if is_palindrome(x) == True:
    print("Palindrome!")
else:
    print("Not a palindrome!")