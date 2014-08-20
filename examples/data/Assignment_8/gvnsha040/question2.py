#S.G
word=input('Enter a message:\n')

acc=0
def pairZ(word,acc):

    if len(word)== 0 or len(word)== 1:
        return acc
    
    elif word[0]==word[1]:
        acc+=1

        return pairZ(word[2:],acc)
    
    else:
        return pairZ(word[1:],acc)

print('Number of pairs:',pairZ(word,acc))
