"""checking for palindrome strings
Dudley Mutero
9 may 2014"""

def palindrome(message):
    """function to check for palindrome"""
    if len (message) < 2:
        return "Palindrome!"
    if len (message) >= 2:
        if message[0] == message[-1]:
            return palindrome(message[1:-1])   
        else:
            return "Not a palindrome!"
#main program
message = input("Enter a string:\n")
print(palindrome(message))