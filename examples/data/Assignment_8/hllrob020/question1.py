#Program to check if string is palindrome using recursion
#Robin Hall
#08/05/2014

def palindrome(string):
    if len(string) < 2: #single character is palindromic
        return True
    else:
        if string[0] == string[-1]: #checks if first and last characters of string are the same
            return palindrome(string[1:len(string) - 1]) #proceeds to check rest of string excluding first and last characters
        else:
            return False #if corresponding characters are not the same; function becomes false

string = input('Enter a string:\n')
palindrome(string)
if palindrome(string): #if recursion confirms palidrome
    print('Palindrome!')
else: #if recursion does not confirm palindrome
    print('Not a palindrome!')