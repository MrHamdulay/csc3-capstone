"""program to check if a string is palindrome recursively
Zikho Godana
08 May 2014"""

s=input("Enter a string:\n")

def reverse(s):
    """reverses a string"""
    #base case, s="", do nothing
    if s!="":
        s_rev=s[:-len(s):-1]+s[0]
        if s_rev==s:
            print("Palindrome!")
        else:
            print("Not a palindrome!")         
reverse(s)
