"""calculate whether or not a string is a palindrome 
barak setton
04/05/2014"""

def rev(s):
    if len(s)==1: # telling when to stop
        return s
    else:
        return (rev(s[1:])+s[:1]) # making issue smaller

s =input("Enter a string: \n")   
name = rev(s)
if name == s:
    print("Palindrome!")
else:
    print("Not a palindrome!")
