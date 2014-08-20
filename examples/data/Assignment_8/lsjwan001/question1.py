# Program calculates whether or not a string is a palidrome
# Wandile Lesejane
# 8 May 2014

def palindrome(string):
    if string=="":
        return string
    else:
        return palindrome(string[1:])+string[0]
    
string=input("Enter a string:\n")
if string==palindrome(string[1:])+string[0]:
    print("Palindrome!")
    
else:
    print("Not a palindrome!")
