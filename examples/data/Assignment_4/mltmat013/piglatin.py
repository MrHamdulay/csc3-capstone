def toPigLatin(s):
    s += ' '
    word = ''
    cons = ''
    pLatin = ''
    for i in s:
        if i != ' ':
            word += i
        else:
            if word[0].upper() in ('A','E','I','O','U'):
                word += 'way '
                pLatin += word
                
            elif not (word[0].upper() in ('A','E','I','O','U')):
                while not (word[0].upper() in ('A','E','I','O','U')):
                    cons = cons + word[0]
                    word = word[1:len(word)]
                word += 'a' + cons + 'ay '
                pLatin += word
            
            word = ''
            cons = ''
    #print(pLatin)    
    return pLatin

def toEnglish(s):
    s += ' '
    word = ''
    pLatin = ''
    skip = 0
    
    for i in s:
        if i != ' ':
            word += i 
        
        else:
            if word[len(word)-3 : len(word)] == 'way':
                word = word[0: len(word) -3]
                pLatin += word + ' '
                    
            elif (word[ len(word) - 2: len(word)] == 'ay') and (word[len(word)-3] != 'w'):
                word = word[0: len(word) -2]
                
                for j in range(len(word)-1,0,-1):
                    if word[j] == 'a':
                        skip = j
                        continue
                word = word[skip+1: len(word)] + word[0:skip]
                pLatin +=  word + ' '
            
            word = ''
    return pLatin