"""theresa ogallo 2014
calculating whether or not a string is a palindrome using recursion"""

#reversing the string
def palindrome(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return str(palindrome(input_string[1:])) + input_string[0]

initial_input =input('Enter a string:\n')

palindrome(initial_input)

#checking to see if it's a palindrome
if palindrome(initial_input) == initial_input:
    print('Palindrome!')
else:
    print('Not a palindrome!')