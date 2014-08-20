# Dalise Steynfaard
# STYDAL001
# Assignment 4, question 3
# 04-04-2014

def toPigLatin(s):
    v = ['a','e','i','o','u']
    words = s.split(' ')
    piglatin = []
    pl_sentence = ''
    c = 0
    count = 0

    for word in words:
        count = 0
        c = 0
        if not(word[0] in v):
            word += 'a'
            while not(word[c] in v):
                word += word[c]
                count += 1
                c += 1
            word += 'ay'
            word = word[count::]
        else:
            word += 'way'
        piglatin.append(word)
    
    for i in piglatin:
        pl_sentence = pl_sentence + i + ' '
        
    return pl_sentence

def toEnglish(s):
    words = s.split(' ')
    english = []
    eng_sentence = ''
    c = 0
    count = 0
    
    for word in words:
        c = 0
        count = 0
        word = word[::-1]
        if not(word[:3] == 'yaw'):
            word = word[2:]
            while not(word[c] == 'a'):
                word += word[c]
                c += 1
                count += 1
            word = word[count+1:]
        else:
            word = word[3:]
        word = word[::-1]
        english.append(word)
    
    for i in english:
        eng_sentence = eng_sentence + i + ' '
    
    return eng_sentence