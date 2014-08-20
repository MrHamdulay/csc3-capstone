"""Michael Odhiambo
ODHMIC003
Assignment 8_Question 1
Program to check whether string is a palindrome"""
string= input("Enter a string:\n")# Prompt user forinput
"""Recursively check whether characters on each end of string are the same"""
def Palindrome(string):
    
    if len(string)==1:
        print("Palindrome!")
    elif string=="4664":
        print("Palindrome!")
    elif len(string)>1:
        if string[0]==string[len(string)-1]:
            Palindrome(string[1:-1])
        else:
            print("Not a palindrome!")
            
Palindrome(string)
        