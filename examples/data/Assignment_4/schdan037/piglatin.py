def toPigLatin_word(s):
    final = ""
    consonants= ""
    starts_vowel = False
    no_vowel = True
    for vowels in "aeiou":
        if s[:1] == vowels:
            starts_vowel = True
    if starts_vowel:
        final = s + "way"
    else:
        for l in s:
            for vowel in "aeiou":
                if l == vowel:
                    no_vowel = False
            if no_vowel:
                consonants += l
        final = s[len(consonants):] + "a" + consonants + "ay"
        
    return final

def toEnglish_word(s):
    final = ""
    starts_vowel = False
    no_vowel = True
    consonant = ""
    for i in s:
        if i == "w":
            starts_vowel = True
    if starts_vowel:
        final = s[:-3]
    else:
        s = s[:-2]
        for l in s[::-1]:
            for vowel in "aeiou":
                if l == vowel:
                    no_vowel = False
            if no_vowel:
                consonant += l
        consonant = consonant[::-1]
        final = consonant + s[:len(consonant)*(-1)-1]
    return final

def toEnglish(s):
    final = ""
    for i in s.split(" "):
        final += toEnglish_word(i) + " "
    return final[:-1]

def toPigLatin(s):
    final = ""
    for i in s.split(" "):
        final += toPigLatin_word(i) + " "
    return final[:-1]