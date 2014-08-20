"""Check if the string is palindrome using recursion.
Name: Thubelihle Mdlalose
Student Number: MDLTHU011"""

def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]

def isPalindrome(s):
    if s == reverse(s):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        
x = input("Enter a string:\n")
isPalindrome(x)