'''A Program to verify if an inputted string is a palindrome
By Daniel Newton
04/05/14'''

def palindrome(string):     #checks if the string is palindromic
    if len(string)<2:
        return True
    if string[0]!=string[-1]:   #If characters at either end of the string are not equal, it is not a palindrome
        return False
    return palindrome(string[1:-1])     #Removes first and last character (since these must be equal) and repeats check until the length of the string < 2.


string=input("Enter a string:\n")    #Asks user input for a string
if palindrome(string)==True:    #If it is a palindrome, the program prints out such, if it isn't, it shows this too.
    print("Palindrome!")
else:
    print("Not a palindrome!")
