def toPigLatin(s):
    listwords=s.split()
    for i in range(len(listwords)):
        word=listwords[i]
        if word[0] in ('aeiou'):
            listwords[i]=word+"way"
        else:
            pos=0
            for x in range(len(word)):
                if word[x]in ('aeiou'):
                    break
                elif word[x] not in ('aeiou'):
                    pos+=1
                    listwords[i]=word[pos:len(word)]+'a'+word[0:pos]+'ay'
    translate=''
    for i in range(len(listwords)):
        translate=translate+listwords[i]+' '
    return translate[:len(translate)-1]

def toEnglish(s):
    listwords=s.split()
    for i in range(len(listwords)):
        word=listwords[i]
        if word[len(word)-3:len(word)]=='way':
            listwords[i]=word[:len(word)-3]
        else:
            word=word[:len(word)-2]
            z=len(word)-1
            while word[z]!='a':
                z-=1
            word=word[z+1:len(word)]+word[:z]
            listwords[i]=word
    translate=''
    for i in range(len(listwords)):
        translate=translate+listwords[i]+' '
    return translate[:len(translate)-1]    
    