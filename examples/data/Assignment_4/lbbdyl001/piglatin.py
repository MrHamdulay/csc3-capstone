vowels = ('a', 'e', 'i', 'o', 'u')
def toPigLatin(s):
    for lines in s:
        words += lines.split()
        
    for word in s:
        if word[0] in vowels:
            new_word = word + 'way'
        else:
            new_word = word[1:] + word[0] + 'ay'
            newWords.apend(new_word)

            