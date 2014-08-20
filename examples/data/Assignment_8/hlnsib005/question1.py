"""Name: Sibulele Hlongwane
Date: 06 May 2014
Assignment: To Check if word is a palindrome using recursion"""
s=input("Enter a string:\n")

def Palindrome(s):
    #Base Case
    if len(s)<=1:
        return "Palindrome!"
    else:
        #Checks to see if first character of string equals last chatacter of string
        if s[0]==(s[-1]): 
            #"new" string is put into palindrome function i.e: first and last characters are removed and palindrome function is recalled 
            return Palindrome(s[1:-1])
        #else if they do not match return false
        else:
            return "Not a palindrome!"
#prints result of recursive function
print(Palindrome(s))        
        
