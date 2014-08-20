# Yentl Naidu (NDXYEN001)
# 8 May 2014
# Assignment 8
# Question 1 - Is a string a palindrome?

def is_palindrome(s):
    # Using recursion to determine whether a string is a palindrome
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            return is_palindrome(s[1:len(s)-1])
        else:
            return False
        
if __name__ == "__main__":
    # Get the input 
    x = input("Enter a string:\n")
    
    # Determine whether string is a palindrome
    result = is_palindrome(x)
    
    # The response saying whether it is a palindrome or not
    if not result:
        print("Not a palindrome!")
        
    else:
        print("Palindrome!")