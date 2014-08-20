def is_palindrome(s):
    if s == '':
        return 'Palindrome!'
    else:
        if s[0] == s[-1]:       # check if first element is the same as last
            return is_palindrome(s[1:-1])              
        else:
            return 'Not a palindrome!'
        
        
def main():
    string = input("Enter a string:\n")
    print(is_palindrome(string))
main()