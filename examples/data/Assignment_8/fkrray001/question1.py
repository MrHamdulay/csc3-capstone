# Author : Rayaan Fakier FKRRAY001
# Date : 05 - 05 - 2014
# question1.py


def recursive_palindrome(string):
    '''Python program to check whether a string is a palindrome'''
    # Base Case - stop when 1 letter left
    if string == "":
        return "Palindrome!"
    # Recursive case - prints not palindrome 
    else:
        if string[0] == string[-1]:
            return recursive_palindrome(string[1:-1])
        else:
            return "Not a palindrome!"

if __name__ == '__main__':
    string = input("Enter a string:\n")
    #recursive_palindrome(string)
    print(recursive_palindrome(string))
