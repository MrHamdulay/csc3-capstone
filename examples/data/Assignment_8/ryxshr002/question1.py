"""Shriya Roy
7 May 2014
palindrome program"""
def palindrome(n):
    
    
    
    if len(n)<2:#checks if length is less than 2
        return print("Palindrome!")#palindrome is length is one
    else:
        if n[-1]==n[0]:#if the last character is equal to the first character
            return palindrome(n[1:-1])
        
        else:
            return print("Not a palindrome!")#returns not a palindrome if the forward string doesnt equal the backward string 
        
n=input("Enter a string: \n")        
palindrome(n)       
        



    
        
        
        
        
        
    