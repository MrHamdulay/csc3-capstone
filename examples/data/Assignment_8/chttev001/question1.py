"""Tevin Chetty
8 May 2014
Program to check palindrome using recursion"""


def is_palindrome(check):
    if len(check)<2: #if single digit then palindrome
        return print("Palindrome!")
    else:
        if check[0]==check[-1]: #checks if the first and the last are equal
            return is_palindrome(check[1:-1]) #removes the first and the last letters to be compared again 
        else:
            return print("Not a palindrome!")

check=input("Enter a string:\n")
is_palindrome(check)