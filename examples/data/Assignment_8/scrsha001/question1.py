#Shaaheen Sacoor SCRSHA001
#Program to find palidromes
# 8 may 2014


def check_palindrome(s):
    if s == '':
        return True
    else:
        #if (ord(s[0]) - ord(s[len(s)-1])) == 0:
        if s[0] == s[-1]:
            return check_palindrome(s[1:-1])
        else:
            return False
        
def main():
    s = input("Enter a string:\n")
    x = check_palindrome(s)
    if x is True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
main()