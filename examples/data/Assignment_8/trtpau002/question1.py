"""check for palindrome
Paul Truter
06 May 2014"""

s2 = input("Enter a string:\n")
    
def isPalindrome(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])

if isPalindrome(s2):
    print("Palindrome!")
else:
    print("Not a palindrome!")