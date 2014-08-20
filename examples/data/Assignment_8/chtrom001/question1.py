#question 3
# checking palindromes using recursion
#romelon chetty
#07 may 2014




def Palindrome(word):
    # Checks whether a string is a palindrome, using recursion.
    # Parameters:
    # word: a string
    # Returns: True if word is a palindrome, False otherwise    
    if (len(word) <= 1): # only one character are both palindromes
        return True
    elif word[0] == word[-1]: #check first letter against last letter
        return Palindrome(word[1:-1]) # if true runs a smaller part of string in function
    else:
        return False # if first not equal last ,condition is already not met
        
def main():
    string=input('Enter a string:\n') # input string from user
    if Palindrome(string)== True:      
        print('Palindrome!')          # prints palindrome if the palindrome function return true
    if Palindrome(string)== False:
        print('Not a palindrome!')    # # prints not a palindrome if the palindrome function return false

main()
        
        
        
        
        
        