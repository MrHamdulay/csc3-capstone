"""Program to check for palindromic strings
Pankaj Munnbodh
6 May 2014"""
get_str=input("Enter a string:\n")

def reverse(string):
    if string=='':
        return''              #stopping case
    rev_str=string[len(string)-1]+reverse(string[:-1])   #take last character and put it at beginning. Continue recursing to add characters.          

    return rev_str

#Compare input with output of function to check if it is a palindrome
rev_str=reverse(get_str)   
if rev_str==get_str:
    print('Palindrome!')
else:
    print('Not a palindrome!')