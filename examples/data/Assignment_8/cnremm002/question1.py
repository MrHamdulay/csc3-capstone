"""Check for palindrome
Emmanuel Conradie
09 May 2014"""

#Check if first half = second half of string
def palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:len(s)-1])
        else:
            return False
        
#Enter string
s = input("Enter a string:\n")

if palindrome(s):
    print("Palindrome!")
else:
    print("Not a palindrome!")