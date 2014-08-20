# Lehlogonolo Masetla


def isPalindrome(s):
    
    if len(s) == 1:
        return "Palindrome!"
    
    elif len(s) > 1 and s[0] == s[-1]:

        if len(s[1:-1]) != 0:
            return isPalindrome(s[1:-1])
        else:
            return isPalindrome(' ')
    else:
        return "Not a palindrome!"
        
def main():
    string = input("Enter a string:\n")
    print(isPalindrome(string))

if __name__=='__main__':
    main()