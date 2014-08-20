#Ikhlaas Pohplonker
#8 May 2014
#a Python program to calculate whether or not a string is a palindrome
def palindrome(s):# a recursive function to calculate whether or not a string is a palindrome
    if len(s)==1 or len(s)==0:#prints palindrome if the length of the string is zero or one
        print("Palindrome!")
    elif s[0]!=s[-1]:#prints not a palindrom if the character at the beginning is not the same as the character at the end
        print("Not a palindrome!")
    else:
        return palindrome(s[1:-1])#returns the function if the character at the beginning is the same as the character at the end
s=input("Enter a string:\n")
palindrome(s)
