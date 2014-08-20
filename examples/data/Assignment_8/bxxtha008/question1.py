'''program to test whether a word is a palindrome or not
Thabiso Beau
Assignment 8: #question1.py
4 May 2014'''


def reverse(x):#create reverse function in order to assign varaible and test equality
    if x == '':
        return x
    else:
        return reverse(x[1:]) + x[0] #slices the string backwards and concatenates the first letter

def palindrome(x):
    y = reverse(x) #assign variable to test equality
    if x == y:
        return 'Palindrome!'
    else:
        return 'Not a palindrome!'
    
x = input('Enter a string: \n') #ask user for input
print(palindrome(x))