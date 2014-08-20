def encrypt(word):
    #print(word)
    if len(word) != 0:
        if 97<= ord(word[0])  <= 122 :
            letter = ord(word[0])
            if letter == 122:
                return 'a' + encrypt(word[1:])
            else:
                new_word = chr(ord(word[0])+1)
                return new_word + encrypt(word[1:])
        else:
            return word[0] + encrypt(word[1:])
    else:
        return ''
    
def word_():
    word = input('Enter a message:\n')
    print('Encrypted message:\n',encrypt(word),sep='')
    
word_()            