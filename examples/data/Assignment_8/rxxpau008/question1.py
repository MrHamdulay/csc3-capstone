#Check if an entered string is a palindrome using recursion
#Paul Roux - RXXPAU008
#08 May 2014

def check_palindrome(string):
    """Checks if a string is a palindrome by checking if the first
    and last letters of a string are the same using recursion by 
    removing the first and last character for each iteration.
    Printing 'Not a palindrome!' if it is not a palindrome and 
    'Palindrome' if it is."""
    string = str(string)
    if string[0] != string[len(string)-1]:
        print("Not a palindrome!")    
    else:
        if string[1:len(string)-1]:
            check_palindrome(string[1:len(string)-1])
        else:
            print("Palindrome!")
            
check_palindrome(input("Enter a string:\n"))