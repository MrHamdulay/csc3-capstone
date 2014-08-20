
"""Question 1 - Assignment 8- check if string is a palindrome using recursion
GVNPRI022- Prinesan Govender
09 May 2014"""
word= input("Enter a string:\n") #input initial word


def check_palindrome(word):
    if len(word)<=1: #base case
        return True
    
    else:
        if word[0]==word[-1]: #if first and last letters equal
            return check_palindrome(word[1:-1]) #call function again
        
        else:
            return False #if not equal - not a palindrome
        
                  

if(check_palindrome(word)==True):
    print("Palindrome!")

else:
    print("Not a palindrome!")

    
            