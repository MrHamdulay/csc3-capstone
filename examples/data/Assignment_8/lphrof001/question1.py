"""program to find whether a string is a palindrome
Rofhiwa Liphauphau
5 May 2014"""
#prompts user to enter a string
s=input("Enter a string:\n")
#recurve function to reverse a string
def palindrome(s):
    if s == "":
        return s
    else:
        return palindrome(s[1:]) + s[0]  
#if the reversed string is equal to the original input then we have a palindrome
if palindrome(s)==s:
    print("Palindrome!")
else:
    print("Not a palindrome!")

