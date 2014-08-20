"""program to check if a string is a palindrome
Runako Muzwidzwa
03/05/2014"""
x=input("Enter a string:\n")

def palindrome(x):
    
    if len(x)<1:
        print("Palindrome!")
    elif x[0]==x[-1]:#checks first and last letters for quality
        x=x[1:-1] #slices the string
        return palindrome(x)
    else:
        print("Not a palindrome!")

palindrome(x)