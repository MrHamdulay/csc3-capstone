"""Check if a presented string's a palindrome
Trevor Byaruhanga
09 May 2014"""

def is_palindrome(s):
    #checks if the first letter equals the second
    if s[0] != s[-1]:
       # if it doesnt, print the phrase below.
       print ('Not a palindrome!')
       #if it does search through the second an second to last letter.
    elif not s[1:-1]:
       print ('Palindrome!')
    else:
       return is_palindrome(s[1:-1])
   #search through the string until you get no more equal leters. If all opposite letters are equal its a palindrome
question= input('Enter a string:\n')
is_palindrome(question)