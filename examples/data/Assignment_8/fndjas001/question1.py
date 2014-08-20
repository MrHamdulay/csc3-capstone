"""A program to determine if a string is a palindrome or not
Jason Findlay
07/05/2014"""

s=input("Enter a string:\n")

def palindrome(s):
    #Base case
    if len(s)==1 or len(s)==0:
        return True
    else:
        k=s[0]
        l=s[-1]
        #Checks if paired letters match
        if k==l:
            return palindrome(s[1:-1])
        else:
            return False

if palindrome(s):
    print("Palindrome!")
else:
    print("Not a palindrome!")
