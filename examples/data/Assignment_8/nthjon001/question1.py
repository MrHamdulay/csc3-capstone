"""recursively calculates whether input is a palindrome or not
jonathan nathan 
7 May 2014"""

def palindrome(string):
    """recursively determines palindrome"""
    # base case when empty string or when string of length one
    if len(string) < 2:
        return 'Palindrome!'
    # case when first character in string is not equal to the last character
    if string[0] != string[-1]:
        return 'Not a palindrome!'
    # recursive step
    return palindrome(string[1:-1])

# gets input from user
string = input('Enter a string:\n')
# prints result from palindrome function
print(palindrome(string)) 