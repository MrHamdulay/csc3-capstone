#S.G
word=input('Enter a string:\n')

def palindrome(word):
    
    
    if len (word)<=1:
        print('Palindrome!')
    
    elif word[0] == word[len(word)-1]:
        return palindrome(word[1:len(word)-1])
    
    else:
        print('Not a palindrome!')
        
palindrome(word)
