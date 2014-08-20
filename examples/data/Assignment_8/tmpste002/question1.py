""" Recursive function to calculate whether or not a string is a palindrome """
__author__ = 'Stephen Temple'
__date__ = '2014/05/05'


def reverse(p) -> str:
    """ Reverse a string """
    return p if len(p) == 1 else p[-1] + reverse(p[:-1])


if __name__ == '__main__':
    string = input("Enter a string:\n")
    if reverse(string) == string:
        print("Palindrome!")
    else:
        print("Not a palindrome!")