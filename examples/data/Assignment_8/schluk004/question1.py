def check_palindrome(s):
    if s=="":
        print("Palindrome!")
    
    elif s[0]==s[-1]:
        return(check_palindrome(s[1:-1]))
    
    else:
        print("Not a palindrome!")
    
s = input("Enter a string:\n")

check_palindrome(s)
        