"""Daniel Schwartz
SCHDAN037
question 1 palindrome recursion
may 2014"""


def palin(s):
    """recursive function to determine if string is a palindrome"""
    if s == "":
        return True
    if s[0] == s[-1]:
        return palin(s[1:-1])
    else:
        return False

if __name__ == '__main__':
    s = input("Enter a string: \n")
    if palin(s):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
