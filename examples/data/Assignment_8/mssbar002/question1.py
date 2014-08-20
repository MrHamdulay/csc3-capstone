"""a Python program with a recursive function to calculate whether or not a 
string is a palindrome
Barnett Msiska
05/05/2014"""
def main():
    s = input("Enter a string:\n")
    if isPalindrome(s):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
def isPalindrome(s):
    """return true if s is a palindrome"""
    if len(s)== 0:
        return True
    elif len(s) == 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])
main()