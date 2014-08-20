"""A program to test if a string is a palindrome, using recursion
By Jeremy Smith SMTJER002
4 May 2014"""

def reverse(string):
    """reverses a string"""
    #stopping point is if there is no string left
    if len(string) == 0:
        return ""
    #return the last letter, plus the last letter of the rest of the string
    else:
        return string[-1] + reverse(string[0:-1])

#input a string
string = input("Enter a string:\n")

#reverse the string using a recursive function
palindrome = reverse(string)

#test if the reverse string is the same as the original string
if string == palindrome:
    print("Palindrome!")
else:
    print("Not a palindrome!")