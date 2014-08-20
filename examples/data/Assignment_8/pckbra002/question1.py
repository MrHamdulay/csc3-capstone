"""calculate whether or not a string is a palindrome using recursion"""
"""Brandon Pickup"""
"""3 May 2014"""
"""Assignment 8 Question 1"""
sent = input("Enter a string:\n")
def palindrome(s):
    if len(s)<=1:
        return "Palindrome!"
    elif s[0] == s[-1]:#checks to see whether the first and last letters are the same
        return palindrome(s[1:len(s)-1])#runs the function again on a string with either edge truncated
    else:
        return "Not a palindrome!"
print(palindrome(sent))
