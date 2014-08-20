__author__ = 'Daniel'
def toPigLatin(s):
    new_s=''
    for word in s.split():
        if word[0] in 'a,e,i,o,u':
            new_s+=(word+'way' + " ")
        if word [0] not in 'a,e,i,o,u':
            x = getConsonantWord(word)
            new_s+=(x + ' ')
    return new_s

def getConsonantWord(word):
    i=0
    while i < len(word):
        if word[i] in 'a,e,i,o,u':
            break
        i += 1

    return word[(i):]+"a"+word[0:i]+"ay"

def toEnglish(s):
    new_s=''
    for word in s.split():
        if word[-3] in 'way':
            new_s +=  (word[:-3] +' ')
        elif word[0] in 'a,e,i,o,u':
            y=returnConsonantWord(word)
            new_s+=(y+' ')
    return new_s

def returnConsonantWord(word):
    i=0
    new_word=''
    while i < len(word):
        if word[i] not in 'a,e,i,o,u':
            break
        i += 1
    new_word+=word[:-2]
    new_word+=word[:(i)]
    return new_word[(i):-1]



