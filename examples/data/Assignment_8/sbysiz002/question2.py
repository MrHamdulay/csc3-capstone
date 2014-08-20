def wordcount(word):
    #print("Checking",word)
    if len(word) != 0 and len(word)!=1 :
            if word[0]==word[1]:
                return 1 + wordcount(word[2:])
            else:
                return 0 + wordcount(word[1:])
    else:
        return 0        
            
def word_():
    word = input('Enter a message:\n')
    print('Number of pairs:',wordcount(word))
    
word_()        