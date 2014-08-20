def palindrome(word):
    if len(word) == 1:
        print('Palindrome!')
    else:
        if len(word) > 1 :
            if  word[0] == word[-1]:
                if len(word[1:-1]) == 0: palindrome(' ')
                else: return palindrome(word[1:-1])
            else :
                print('Not a palindrome!')
        else:
            print('Not a Palindrome!') 
            
def word_():
    word = input('Enter a string:\n')
    palindrome(word) 
word_()    