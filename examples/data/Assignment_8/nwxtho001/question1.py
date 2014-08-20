'''program to determine palindromity of a string using recursion (new word!?)
tom new
2014/05/05'''

def reverse (s):
    '''recursive reverser!'''
    lens = len (s)
    if lens == 1: return s # end point a
    elif lens == 0: return '' # end point b (copes with the empty string)
    else: return s [lens - 1:] + reverse (s [:lens - 1]) # returns final character added to result of sending the rest of string to reverse ( )
    
# gets input from user if program is run directly
if __name__ == '__main__':
    s = input ('Enter a string:\n')
    if s == reverse (s): print ('Palindrome!')
    else: print ('Not a palindrome!')