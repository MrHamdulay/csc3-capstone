"""question1.py :- checks whether or not a string is a palindrome
Author : Musa Xakaza
Date : 07/05/2014"""

def isPalindrome(s):
    # if string has one character, then it is a palindrome
    if len(s) == 1:
        return "Palindrome!"
    elif len(s) > 1 and s[0] == s[-1]:
        #if the first and last character match then continue recusing 
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