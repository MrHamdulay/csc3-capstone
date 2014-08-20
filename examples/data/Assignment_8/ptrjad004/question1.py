"""Finding recursive functions using recursion
Jade Petersen
7 May 2014"""

def palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:len(s)-1])
        else:
            return False
        
        
s = input("Enter a string:\n")

if palindrome(s):
    print("Palindrome!")
else:
    print("Not a palindrome!")