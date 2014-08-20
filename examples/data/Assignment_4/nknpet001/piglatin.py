# piglatin to english tranlator
# Nkuna Peter
# 3 April 2014

v = ('AEIOUaeiou')

def toPigLatin(s):
    p = s.split(" ")
    l = ""
    for word in p:
        if word[0] in v:
            l += word + "way" + " "
        else:
            VI = 0
            for letter in word:
                if letter not in v: 
                    VI += 1
                    continue
                else: 
                    break
            l += word[VI:] + "a" + word[:VI] + "ay" + " "
    return l[:len(l) - 1]

def toEnglish(s):
    p = s.split(" ")
    e = ""
    for word in p:
        if word[:len(word) - 4:-1] == 'yaw':
            e += word[:len(word) - 3] + " "
        else: 
            n = word[:len(word) - 2]
            FC = n.split("a")[-1]
            CR = n[:len(n) - (len(FC)+1)]
            e += FC + CR + " "
    return e