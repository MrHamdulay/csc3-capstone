s_word=input('Enter a string:\n')
def palindrome(s_word):    
    if len(s_word)<=1:
        print('Palindrome!')
        return
    elif len(s_word)>1:
        if s_word[0]==s_word[-1]:
            new_s_word=s_word[1:-1]
            return palindrome(new_s_word)
        else:
            print('Not a palindrome!')
            return
            
palindrome(s_word)
        
        