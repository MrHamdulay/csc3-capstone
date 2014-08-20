# Program to see if string is palindrome
# Mutali Mashamba
# [day] May 2013

# Get input from user
string = input('Enter a string:\n')

def palindrome(string):
    #Base case
    if len(string)<= 1 :
        return 'Palindrome!'
    # Recursive step
    else:
        if string[0] == string[len(string)-1]:
            return palindrome(string[1:len(string)-1])
        else :
            return "Not a palindrome!"
print(palindrome(string))