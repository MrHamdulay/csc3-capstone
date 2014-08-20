# program to determine whether a string is a palidrome o not
# mllgad001
# 6 April 2014

def is_palindrome(s): 
    if s == '':                     # base case- if string is empty, return palindrome
        return 'Palindrome!'
    else:                             # if string is not empty
        if s[0] == s[-1]:              # check if first letter is equal to last
            return is_palindrome(s[1:-1])         # recursive step- repeats from second character, up to but not including the last
    return 'Not a palindrome!'    # returns this if no palindrome is found

def string():
    s = input("Enter a string:\n")
    print(is_palindrome(s))
    
    
string()