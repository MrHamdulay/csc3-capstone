"""Phillip Ruhesi
05/05/2014
program to check for a palindrome"""

def palindrome(x):
    if len(x)<2:
                print('Palindrome!')          #All words with less than 2 characters are palindrome
    elif x[0]==x[len(x)-1]:
        return palindrome(x[1:len(x)-1])      #Check for same letters at the ends of the word
       
    else:
        print('Not a palindrome!')

x=input('Enter a string:\n')
palindrome(x)    