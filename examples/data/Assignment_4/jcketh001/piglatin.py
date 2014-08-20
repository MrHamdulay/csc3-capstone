def toPigLatin(s):
    piglatin = []
    for word in s.split():
        suffix = 'a'
        prefix = ''
        if word[:1].lower() in 'aeiou':
            suffix = 'way'
            prefix = word
        else:
            for letter in word[:]:
                if letter.lower() in 'aeiou':
                    break
                suffix += letter
                word = word[1:]
            suffix += 'ay'
            prefix = word
        piglatin.append(prefix + suffix)
    return ' '.join(piglatin)

def toEnglish(s):
    english = []
    for word in s.split():
        if word[-3:].lower() == 'way':
            english.append(word[:-3])
        else:
            prefix = ''
            word = word[:-2]
            for letter in reversed(word[:]):
                if letter.lower() == 'a':
                    word = word[:-1]
                    break
                
                prefix += letter
                word = word[:-1]               
            english.append(prefix[::-1] + word)
    
    return ' '.join(english)
