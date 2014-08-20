"""this program checks if a phrase or word is a palindrome
quincy cele
9 may 2014"""
x=input("Enter a string:\n")
def palindrome(string):
    """function reverses a string"""
    if len(string)==0:
        return ""
    elif len(string)>=0:
        return palindrome(string[1:])+ string[0]

y= palindrome(x)
#check if the reverse of the string is the same as the original string
if x==y:
    print("Palindrome!")

else:
    print("Not a palindrome!")
        
