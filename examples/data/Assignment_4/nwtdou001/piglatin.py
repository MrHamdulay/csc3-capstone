def vowel(c):
    return c.upper() in 'AEIOU'

def toPigLatin(s):
    words = s.split()
    latin = ''
    for word in words:
        if vowel(word[0]):
            word += 'way'
        else:
            i = 0
            while not vowel(word[i]):
                i += 1
                if not i < len(word): break
            word = word [i:] + 'a' + word[:i] + 'ay'
        latin += word + ' '
    return latin

def toEnglish(s):
    words = s.split()
    english = ''
    for word in words:
        if word[-3]=='w':
            word = word[:-3]
        else:
            word = word[:-2]
            apos = len(word)-word[::-1].find('a')
            word = word[apos:]+word[:apos-1]
        english += word + ' '
    return english