"""Cherise Dube
06 May 2014
Program to check if string is a palindrome using recursion"""

#Makes the input string a string with no spaces
s=input("Enter a string:\n")
#s=s_original.split(" ")
#s="".join(s) #s=spaceless string

def reverse(s):
    """reverses the string"""
    if len(s)==0:
        return ""
    elif s[0]==" ":
        return reverse(s[1:])+s[0]
    else:
        return reverse(s[1:])+s[0]
    
r=reverse(s) #r=reversed string 
    
if r==s:
    print("Palindrome!")
else:
    print("Not a palindrome!")
    
    