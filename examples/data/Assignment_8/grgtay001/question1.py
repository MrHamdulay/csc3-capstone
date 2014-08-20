"""Calculating whether or not a string is a palindrome - recursive functions
tayla george
9 May 2014"""

def palindrome(s):
    if s == '': #empty string
        return True
    else:
        if s[0] == s[-1]: #checking if it is a palindrome
            return palindrome(s[1:len(s)-1])
        else:
            return False
        
        
s = input("Enter a string:\n")

if palindrome(s):
    print("Palindrome!")
else:
    print("Not a palindrome!")