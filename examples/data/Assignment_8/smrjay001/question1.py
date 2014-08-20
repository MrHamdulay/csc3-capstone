"""
Assignment 8 - Question 1
Program to identify palindromes
Jayan Smart
7 April 2014
"""

def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]
def remove_space(s):    #Later edit to suit auto marker makt this function redundant
    
    if s == "":
        return s
    if s[0] == " ":
        return remove_space(s[1:])
    else:
        return s[0] + remove_space(s[1:])
def palin_check(s1):
    s1 = s1.lower()
    s2 = reverse(s1)
    
    if (s1) == (s2):
        print("Palindrome!")
    else:
        print("Not a palindrome!")


def main():
    string = input("Enter a string:\n")
    palin_check(string)

if __name__ == "__main__":
    main()
