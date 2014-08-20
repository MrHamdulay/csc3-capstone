def toPigLatin(s):
    listWords = s.split()
    for i in range(len(listWords)):
        word = listWords[i]
        if word[0] in ('aeiou'):
            listWords[i] = word+'way'
        else:
            pos=0
            for x in range(len(word)):
                if word[x] in ('aeiou'):
                    break
                elif word[x] not in ('aeiou'):
                    pos+=1
                listWords[i] = word[pos:len(word)]+'a'+word[0:pos]+'ay'
    translate = ''    
    for i in range(len(listWords)):
        translate = translate+listWords[i]+' '
    return translate[:len(translate)-1]

    
def toEnglish(s):
    listWords = s.split()
    for i in range(len(listWords)):
        word = listWords[i]
        if  word[len(word)-3:len(word)] == 'way':
            listWords[i] = word[:len(word)-3]
        else:
            word = word[:len(word)-2]
            z = len(word)-1
            while word[z] != 'a':
                z-=1
            word = word[z+1:len(word)]+word[:z]
            listWords[i]=word
    translate = ''    
    for i in range(len(listWords)):
        translate = translate+listWords[i]+' '
    return translate[:len(translate)-1]