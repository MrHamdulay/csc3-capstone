"""Assignment 8 Question 1
Thabang Bhili
4 May 2014"""

#Getting the string
string = input ("Enter a string:\n")

def palindrome (string):
    """Recursive function to determine palindromes"""
    #Setting the base cases empty string, 1 and 2
    if string == '':
        return "Palindrome!"
    if len (string) == 1:
        return "Palindrome!"
    elif len (string) == 2:
        if string [0] == string [1]:
            return "Palindrome!"
    #Checking if the first and last characters are equal and then removing them
    elif string [0] == string [-1]:
        return palindrome (string [1:-1])
    #Returning not if string fails all tests
    else:
        return "Not a palindrome!"

#Printing the palindrome    
print (palindrome (string))

        