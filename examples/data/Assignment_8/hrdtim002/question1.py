"""program to check for palindromes using recursion
Tim Hardie
9 May 2014"""

def check_palin (str_input):
    if len (str_input) > 1:
        if str_input[0] == str_input[-1]:
            check_palin (str_input[1:-1])
        else:
            print ("Not a palindrome!")
    elif len (str_input) == 1:
        print ("Palindrome!")

if __name__ == '__main__':
    str_input = input ("Enter a string:\n")
    check_palin (str_input)