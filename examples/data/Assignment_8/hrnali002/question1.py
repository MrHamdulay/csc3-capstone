"""A recursive program to determine of a word/sentence is a palendrome
Alison Hoernle
HRNALI002
4 May 2014"""

def palindrome(string):
    
    # Base case is if length of the string is one:
    if len(string) == 1:
        return string
    
    else:
        
        return string[-1] + palindrome(string[0:len(string)-1])
    
string = input("Enter a string:\n")
string_rev = palindrome(string)
if string_rev == string:
    print("Palindrome!")
else:
    print("Not a palindrome!")