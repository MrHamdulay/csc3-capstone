def toPigLatin(sent):
    sent += ' '
    word = ''
    nSent = ''
    Add = ''
    
    for k in sent:
        if k != ' ': #build the word string
            word += k
            
        else: #have the word string
            
            if word[0].upper() in ('A', 'E', 'I', 'O', 'U'):
                word += 'way '
                nSent += word
                
            elif not (word[0].upper() in ('A', 'E', 'I', 'O', 'U')): 
                while not(word[0].upper() in ('A', 'E', 'I', 'O', 'U')): #carry on
                    Add = Add + word[0]
                    word = word[1 : len(word)]
                word += 'a' + Add + 'ay'
                nSent += word + ' '
                

            word = ''
            Add = ''
            
    return nSent
    
def toEnglish(sent):
    sent += ' '
    word = ''
    nSent = ''
    skip = 0
    
    for k in sent:
        if k != ' ': #build the word string
            word += k
            
        else:
            
            if word[len(word) - 3 : len(word)] == 'way':
                word = word[0:len(word) - 3]
                nSent += word + ' '
                
            elif (word[len(word) - 2 : len(word)] == 'ay') and (word[len(word) - 3] != 'w'):
                word = word[0: len(word) - 2]
                
                for i in range(len(word) - 1, 0, -1):
                    if word[i] == 'a':
                        skip = i
                        continue

                word = word[skip + 1: len(word)] + word[0 : skip]
                nSent += word + ' '
                
            word = '' #correct. Do not remove
            
    return nSent  #CHANGE TO RETURN WHEN COMPLETE