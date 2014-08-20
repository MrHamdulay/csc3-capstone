"""danson masuka
a recursive function to calculate whether or not a string is a palindrome 
5 may 2014"""


def palindrome(s):
    if len(s) <= 1:
        return "Palindrome!"
    elif s[0] == s[-1]:
        return palindrome(s[1:len(s)-1])
    else:
        return "Not a palindrome!"
print (palindrome(input("Enter a string:\n")))