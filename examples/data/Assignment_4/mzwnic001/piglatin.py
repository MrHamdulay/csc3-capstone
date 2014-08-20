
vowels = ('a', 'e', 'i', 'o', 'u')

def E_to_PL_word(word):
    if word[0]in vowels:
        return word + "way"
    else:
        if word[1] in vowels:
            return word[1:] + "a" + word[0] + "ay"
        elif word[2] in vowels:
            return word[2:] + "a" + word[0] + word[1] + "ay"
        elif word[3] in vowels:
            return word[3:] + "a" + word[0] + word[1] + word[2] + "ay"
            
                
def toPigLatin(s):
    list_of_words = s.split(' ')
    new_sentence = "" 
    for word in list_of_words:
        new_sentence = new_sentence + E_to_PL_word(word)
        new_sentence = new_sentence + " "
    return new_sentence

def toEnglish(s):
    list_of_words = s.split(' ')
    new_sentence = "" 
    for word in list_of_words:
        new_sentence = new_sentence + PL_to_E(word)
        new_sentence = new_sentence + " "
    return new_sentence

def PL_to_E(word):
    if word[-3:]=="way":
        return word[:-3]
    else:
        word=word[:-2]
        word=word[::-1]
        if word[1]in vowels:
            word=word[2:]+word[:1]
            return word[::-1]
        elif word[2]in vowels:
            word=word[3:]+word[:2]
            return word[::-1]
        elif word[3]in vowels:
            word=word[4:]+word[:3]
            return word[::-1]
    









    