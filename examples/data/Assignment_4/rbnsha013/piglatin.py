def toPigLatin(p):
    sentence = ""
    vowels = ("a", "e", "i", "o", "u")
    for j in range(len(p.split())):
        for word in p.split():
                if word[0] in vowels:
                    word = (word+"way")
                    sentence = sentence+word+" "
                else:
                    if 'a' in word:
                        a = word.find('a')
                    else: a = 1e+10
                    
                    if 'e' in word:
                        e = word.find('e')
                    else: e = 1e+10
                    
                    if 'i' in word:
                        i = word.find('i')
                    else: i = 1e+10
                    
                    if 'o' in word:
                        o = word.find('o')
                    else: o = 1e+10
                    
                    if 'u' in word:
                        u = word.find('u')
                    else: u = 1e+10
                    
                    i = min(a,e,i,o,u)
                    
                    for j in range(len(word)):
                        #i = word.find(vowel)
                        if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
                            word = word[i:] + "a" + word[:i] + "ay"
                            sentence = sentence+word+" "
                            break
                        elif 'aeiou' not in word:
                            word = "a"+word+"ay"
                            sentence = sentence+word+" "
                            break
        return sentence

def toEnglish(e):
    sentence = ""
    vowels = ("a", "e", "i", "o", "u")
    for word in e.split():
        if 'w' in word:
            i = word.find('w')
            word = word[:i]
            sentence = sentence+word+" "
        else:
            for vowel in vowels:
                if vowel in word:
                    word = word[::-1]
                    word = word[2:]
                    j = word.find('a')
                    part = word[0:j]
                    part = part[::-1]
                    word = word[j+1:]
                    word = word[::-1]
                    word = part + word
                    sentence = sentence+word+" "
                    break
            else: sentence = sentence+word+" "
    return sentence