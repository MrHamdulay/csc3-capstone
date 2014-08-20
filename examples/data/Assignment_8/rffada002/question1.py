"""07/05/2014
Adam Ruff RFFADA002
Assignment 8 Question 1
Use recursion to find palindromes"""

string = input("Enter a string:\n")

def palin(string):
    if len(string) == 0 or len(string) == 1:
        print ("Palindrome!")
    elif string[0] != string[len(string)-1]:
        print ("Not a palindrome!")
    elif string[0] == string[len(string)-1]:
        return palin(string[1:len(string)-1])
    
palin(string)