'''A module to convert English to Pig Latin and vice-versa
Written by Tom New on 01/04/14'''

def vowlcheck (word):
    '''Returns False if there are no vowls in a string'''
    a = word.find ('a')
    e = word.find ('e')
    i = word.find ('i')
    o = word.find ('o')
    u = word.find ('u')
    if (a == -1) and (e == -1) and (i == -1) and (o == -1) and (u == -1):
        return False
    else:
        return True

def WordtoPL (word):
    '''Converts a lower-case word in English to its Pig Latin equivalent, provided the English word does not contain the character w'''
    length = len (word)
    if vowlcheck (word):
        if word[0] in 'aeiou':
            word += 'way'
            return word
        else:
            for i in range (length):
                char = word[i]
                if char in 'aeiou':
                    word = word[i:] + 'a' + word[:i] +'ay'
                    return word
    else:
        word = 'a' + word + 'ay'
        return word
            
def toPigLatin (EngStr):
    '''Converts a lower-case sentence in English to its Pig Latin equivalent, provided the English word does not contain the character w'''
    EngWord = ''
    PLStr = ''
    PLWord = ''
    length = len (EngStr)
    while length > 0:
        pos = EngStr.find (' ')
        if pos != -1:
            EngWord = EngStr[:pos]
            EngStr = EngStr[pos+1:]
            PLWord = WordtoPL (EngWord)
            PLStr += PLWord + ' '
            length = len (EngStr)
        else:
            PLWord = WordtoPL (EngStr)
            PLStr += PLWord
            return PLStr
        
def WordtoEng (word):
    if 'way' in word:
        word = word[:-3]
    else:
        word = word[-3::-1]
        pos = word.find ('a')
        cons = word[pos-1::-1]
        word = cons + word[:pos:-1]
    return word

def toEnglish (PLStr):
    PLWord = ''
    EngStr = ''
    EngWord = ''
    length = len (PLStr)
    while length > 0:
        pos = PLStr.find (' ')
        if pos != -1:
            PLWord = PLStr[:pos]
            PLStr = PLStr[pos+1:]
            EngWord = WordtoEng (PLWord)
            EngStr += EngWord + ' '
            length = len (PLStr)
        else:
            EngWord = WordtoEng (PLStr)
            EngStr += EngWord
            return EngStr    
        
if __name__ == '__main__':
    print (WordtoPL ('rhythmn'))
    print (WordtoPL ('alabama'))
    print (WordtoPL ('chastise'))
    print (WordtoPL ('rhythmn'))
    print (toPigLatin ('the quick fox jumps over the lazy dog'))
    print (WordtoEng ('appleway'))
    print (WordtoEng ('astiseachay'))
    print (toEnglish ('eathay uickaqay oxafay umpsajay overway eathay azyalay ogaday'))