"""Program to check whether a string is a palindrome or not (Question 1)
Jaren Hendricks
8 May 2014"""

string = input("Enter a string:\n").lower()

# Recursive function to reverse characters in a string
def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]

# Recursive function to remove spaces in a string
def remove_spaces(s):
    if s == '':
        return ''
    elif s[0] != ' ':                       
        return s[0] + remove_spaces(s[1:]) 
    else:                                   
        return '' + remove_spaces(s[1:])

# Recursive function to check whether the string equals its reverse.
def is_palindrome(s):
    if s == reverse(s): 
        return "Palindrome!"
    else:
        return "Not a palindrome!"

# Output statement
print(is_palindrome(string))