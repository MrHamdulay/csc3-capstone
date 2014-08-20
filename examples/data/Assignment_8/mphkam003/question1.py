"""check whether a string is palindrome
kamogelo mphela
6 may 2014"""
def check_palindrome(s):
    """return 0 if the first and last charcters are the same, otherwise return 1"""
    if len(s)==0:
        return 0
    elif s[0]!= s[-1]:
        return 1 + check_palindrome(s[1:-1])
    else:
        return 0 + check_palindrome(s[1:-1])
        
s = input("Enter a string:\n")
check_palindrome(s)


if check_palindrome(s)==0:
    print("Palindrome!")
elif check_palindrome(s)>=1:
    print ("Not a palindrome!")