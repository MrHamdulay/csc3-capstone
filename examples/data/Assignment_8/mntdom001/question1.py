""" a Python program with a recursive function to calculate whether or not 
a string is a palindrome (reads the sa me if reversed).
Dominic Manthoko
05 May 2014"""


def reverse(s):
    """ a function that returns the reverse of a string"""
    
    if s == '':
        return ''
    
    else:
        return reverse(s[1:]) + s[0]
    
if __name__ == '__main__':
    # prompt the user to enter string
    s = input("Enter a string: \n")
    
    # check if the reversed string if the same as the original string
    if s == reverse(s):
        print("Palindrome!")
    else:
        print("Not a palindrome!")