""" Question 1 / Assignment 8: Palindrome checker
Shaheel Kooverjee - KVRSHA004
8 May 2014 """

def palindrome(string):
    if string == "": #base case where string is empty
        return True
    else:
        if string[0] == string[-1]: #if first and last characters are the same:
            return palindrome(string[1: -1]) #repeat function without first and last characters of string
    return False #not a palindrome if none of above are fully carried through
        
userstring = input("Enter a string:\n") #string given by user

if palindrome(userstring) == True:
    print("Palindrome!")
if palindrome(userstring) == False:
    print("Not a palindrome!")