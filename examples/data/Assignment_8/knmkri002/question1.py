"""Palindrome calculator
Kristin Kinmont
4 May 2014"""

def palindrome(s):       
    if s[0] == s[-1]:
        if len(s) <= 3: # if s is 3 or less and the first and last charactures are equal, it has to be a palindrome
            print( "Palindrome!")
        else:
            palindrome(s[1:-1])         
           
    else:
        print( "Not a palindrome!")

s = input("Enter a string:\n")
palindrome(s)