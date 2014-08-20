"""Question 1 of Assignment 8
Checks whether a supplied string is a palindrome
SWNREI001
05/05/2014"""

def reverse(string, acc = ""):
    """Recursively reverse 'string', storing results between recursions in 'acc'"""
    if string == "": # base case is empty string
        return acc
    else:
        # take first character from string and add to beginning of acc
        # ie in front of first character from previous recursion
        return reverse(string[1:], string[0] + acc) 

def is_palindrome(string):
    """Determines if a string is a palindrome by comparing it to its reverse
    string"""
    string_rev = reverse(string)
    return string_rev == string


def main():
    """Main function of module - gets input and checks if it is a palindrome"""
    line = input("Enter a string:\n")
    if is_palindrome(line):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

if __name__ == "__main__":
    main()