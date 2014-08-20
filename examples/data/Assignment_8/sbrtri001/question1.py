''' Assignment 8, question 1
Use recursion to identify a string as a palindrome or not
Tristan Subroyen
4 May 2014 '''

def palindrome (n):
    ''' This function uses recursion to identify a palindromic string '''
    # base case:
    if n == '':
        print("Palindrome!")
    else:
        
        if n[0] == n[-1]: # if the first and last letters are the same...
            return palindrome(n[1:-1]) # check whether or not the next first and last letters are the same (and so on)
        else:
            print("Not a palindrome!")
    
# Input from user:
string = input("Enter a string:\n")
palindrome(string)
                
