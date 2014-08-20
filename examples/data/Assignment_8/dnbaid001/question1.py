#Assignment 8 - Question 1
#Recursive function to see if string is palindrome
#Aidan de Nobrega
#04/05/2014


def is_palindrome(string):
    if len(string) < 2:
        return True #an empty or single-character string is palindromic
    else:
        if string[0] == string[-1]: #if first letter equals last letter, recursion happens
            return is_palindrome(string[1:len(string)-1])
        else:
            return False #if don't match, function ends with False.

    
def main():
    string = input("Enter a string:\n")

    is_palindrome(string) #invoke function

    if is_palindrome(string): #if function returns True...
        print("Palindrome!")
    else:                     #otherwise...
        print("Not a palindrome!")
        
main()