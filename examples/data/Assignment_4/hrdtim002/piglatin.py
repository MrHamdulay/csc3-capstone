"""converting english and pig latin
tim hardie
1/4/14"""

VOWELS = ("a", "e", "i", "o", "u")

def toPigLatin(s):
    newsentence = ''
    words = s.split(' ')
    for word in words:
        newword=''
        firstvowel = -1
        for i in range(len(word)):
            if word[i] in VOWELS:
                firstvowel = i
                break
        if firstvowel == 0:
            newword = word +'way'
        elif firstvowel == -1:
            newword = 'a'+word+'ay'
        else:
            newword = word[firstvowel:]+'a'+word[:firstvowel]+'ay'
        newsentence+=newword+' '
    return newsentence[:-1]

def toEnglish(s):
    newsentence = ''
    words = s.split(' ')
    for word in words:
        newword = ''
        word = word[:-2]
        if word[-1]=='w':
            newword = word[:-1]
        else:
            posA = len(word)-1
            while(word[posA] not in VOWELS):
                posA-=1
            newword=word[posA+1:]+word[:posA]
        newsentence+=newword+' '
    return newsentence[:-1]

#if __name__ == '__main__':
    #toPigLatin('the quick black fox jumps over the lazy apple')
    #toEnglish('eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway')