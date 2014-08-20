"""Question one
Recursive Function for Palindromic characters
4 May 2014
yuan-Yow Wu
"""


def palindrome (string):
    s1 = ""
    s2 = ""                 #palindrome or not (-1 means not, 1 means it is. 0 means nothing)
    if len(string) == 0: #if string manages to get to nothing.
        return ("Palindrome!")
        
    elif len(string) == 1: #if its a single character then it must be a palindrome
        return ("Palindrome!")
    
    elif string[0] == string[-1]:        
        return palindrome(string[1:len(string)-1])
    
    else:
        return ("Not a palindrome!")       
        
    
    
string = input("Enter a string: \n")
if string != "":
    print(palindrome(string))
        
#palindrome(string)
#if palindrome(string) == 1:
#    print ("Palindrome!")
#elif palindrome(string) == 0:
#    print ("Palindrome")