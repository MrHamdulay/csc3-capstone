""" a program that checks if a sentence is a palindrome using recursion
nelisile mkhwebane
07 May 2014"""

""" initialising the list"""
#list_words = []

""" getting the string from the user"""
s = input ("Enter a string:\n")

def palidro (s):
    """ base case """
    palidrome = True
    if len(s) < 1:
        palidrome = True
    else:
        if s[0] == s[-1]:
            return palidro (s[1:-1])
        else:
            palidrome = False
    if palidrome:
            print ("Palindrome!")
    else:
        print("Not a palindrome!")
palidro(s)
