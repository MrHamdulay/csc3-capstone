# Student Number: PRTNIC017
# Date: 3/28/14

vowels = ['a', 'e', 'i', 'o', 'u']


def toPigLatin(s):
    pigged = ''
    for word in s.split(' '):
        if word[0] in vowels:  # starts with vowel
            pigged += word + 'way'
        else:  # starts with consonant(s)
            end = 0
            for c in word:
                if c in vowels:  # end of consonants
                    break
                else:
                    end += 1
            pigged += word[end:] + 'a' + word[:end] + 'ay'
        pigged += ' '
    return pigged[:len(pigged) - 1]


def toEnglish(s):
    english = ''
    for word in s.split(' '):
        if word.endswith('way'):  # started with vowel
            english += word[:len(word) - 3]
        elif word.endswith('ay'):  # started with consonant
            english += consonant_to_english(word[:-2])
        else:
            english += word
        english += ' '
    return english[:-1]


def consonant_to_english(word):
    index = len(word) - 1
    while word[index] not in vowels:
        index -= 1
    word = word[index + 1:] + word[:index]
    return word