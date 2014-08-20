# Mathew Finlayson - FNLMAT001
# Assignment 8 - Question 1
# 04/05/2014

def isPalindrome (s):
    """recursive function that calculates whether or not a string is a palindrome"""
    if (len(s) == 0): # end case
        return True
    
    if(s[0] == s[-1]): # if the first letter is the same as the last letter
        return (isPalindrome(s[1:-1])) # re-calls isPalindrome with inside string
    else:
        return False
        
# prompts user for input and checks whether or not the inputted string is a palindrome
if isPalindrome(input("Enter a string:\n")): 
    print("Palindrome!")
else:
    print("Not a palindrome!")