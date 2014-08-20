"""checks if a string is a palindrome
Paul Freund
May 2014"""


def pal_checker(s):
    """checks if string s is a palindrome"""
    if len(s) == 1:
        return "Palindrome!"
    else:
        if len(s) > 2:
            if s[0] == s[len(s) - 1]:
                s = s[1:]
                s = s[:len(s) - 1]
                return pal_checker(s)
            else:
                return "Not a palindrome!"
        else:
            if s[0] == s[1]:
                return 'Palindrome!'
            else:
                return 'Not a palindrome!'
def main():
    """formats input and output for marker"""
    s = input("Enter a string:\n")
    x = pal_checker(s)
    print(x)

if __name__ == "__main__":
    main()