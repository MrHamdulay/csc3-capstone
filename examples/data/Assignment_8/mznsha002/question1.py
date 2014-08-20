# 7 May 2014
# Shaun Muzenda
# Finding recursive functions using recursion

def palindrome(s):
    if s == '':     #base case which is an empty string
        return True
    else:
        if s[0] == s[-1]:   #checking string is a palindrome
            return palindrome(s[1:len(s)-1])    
        else:
            return False
        
        
s = input("Enter a string:\n")  #enter the palindrome

if palindrome(s):
    print("Palindrome!")    #prints palindrome if palindrome    
else:
    print("Not a palindrome!")  #prints not palindrome if not a palindrome