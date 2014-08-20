# palindrome checker
# Lwazi Shezi
# 5 May 2014


def palindrome (string) :
    ''' Reverse the input string'''
    if len(string) == 1:
        return string
    else:
        first_letter = string[0]
        #the_rest = string[1:]
        string = palindrome(string[1:]) + first_letter
        return string
    
# Get string from user
string = input('Enter a string:\n')

# Reverse the string
reverse_string = palindrome(string)

# The condition is :If the reversed string is the same as the input string, it's a palindrome, otherwise it's not. Evaluate the input string to the condition.
if string == reverse_string :
    print('Palindrome!')
else:
    print('Not a palindrome!')

if __name__ == '__main__':
    palindrome(string)