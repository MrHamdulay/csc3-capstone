def is_palindrome(s):
    if s == '':
        return "Palindrome!"
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
        
            return is_palindrome(s[1:len(s)-1])
        else:
            return "Not a palindrome!"

s= input("Enter a string:/n")
print(is_palindrome(s))