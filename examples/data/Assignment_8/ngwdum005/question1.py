'''Dumisani Ngwenza
NGWDUM005
06/05/2014
Assignment 8 Question 1'''

#Require input from user
string = input ('Enter a string:\n')

#reversing string through recursion
def Palindrome(string):
    if string == '':
        return ''
    else:
        return Palindrome(string[1:]) + string[0]

#comparing the strings and deciding whether a palindrome or not 
reserved_string = Palindrome(string)
if string == reserved_string:
    print ('Palindrome!')
else:
    print ('Not a palindrome!')
