def getFirstVowel(w):
    #return the position of the first occurence of a vowel in a string
    for i in range(1,len(w)):
        if w[i] in "aeiou":
            return i

def toPigLatin(s):
    vowel = ['a','e','i','o','u']
    newSent = ''
    for word in s.split(' '):
        if word[0] in vowel:
            newSent += ' '+word+"way"
        else:
            #split the word into two parts
            pos = getFirstVowel(word)
            pre = word[0:pos]
            suf = word[pos::]
            newSent += ' '+suf+'a'+pre+"ay"
    newSent = newSent[1:]
    return newSent

def toEnglish(s):
    lang=''
    for word in s.split(' '):
        tmp = word[::-1]
        if tmp[0:3] == "yaw":
            lang+=' '+word[0:-3]
        else:
            word = word[::-1]
            word = word[2:]
            x = word.find('a')
            st = word[0:x]
            end = word[(x+1):]
            new_word = st[::-1]+end[::-1]
            lang+=' '+new_word
    return lang[1:]       