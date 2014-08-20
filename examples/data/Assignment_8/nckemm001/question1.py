# Emmalene Naicker
# Assignment 8
# Programme to determine whether a string is a palindrome

def palindrome(word):
    
    if len (word)<=1 :# when there is 1 or 0 words in the string and it is a palindrome: execute this
        
        print('Palindrome!')
    
    elif word[0] == word[len(word)-1]: #checks if the letter in the front is the same as the letter at the back
        
        return palindrome(word[1:len(word)-1])
    else:
        
        print('Not a palindrome!')

if __name__=='__main__':
    word=input('Enter a string:\n')
    palindrome(word)
    