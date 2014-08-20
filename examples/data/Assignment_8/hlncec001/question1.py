#HLNCEC001
#Assignment 8
#Quesion 1
#Recursion for palandrome

def Palindrome(String):
    if len(String) <= 1: #Any one word is a palindrome
        print('Palindrome!')
    elif String[0] == String[-1]: 
        return String[0] == String[-1] and Palindrome(String[1:-1])
    else:
        print('Not a palindrome!')
Palindrome(String = input('Enter a string:\n'))