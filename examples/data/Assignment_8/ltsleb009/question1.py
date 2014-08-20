'''Checks whether or not string is palindrome'''

string = input("Enter a string:\n")

def palindrome():
    """Returns True if given string is palindrome, False otherwise"""
    #checks for empty string
    if not string:
        return
    else:
        #checks for equality of reversed string with original    
        if string[-1::-1] == string: 
            print("Palindrome!")
        else: #execute else clause if string not palindrome
            print("Not a palindrome!")
#function call
palindrome()

