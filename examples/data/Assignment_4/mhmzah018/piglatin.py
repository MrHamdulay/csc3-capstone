#to piglatin

def get_first_vowel_position(word):
    for position, letter in enumerate(word):
        if letter in ('a', 'e', 'i', 'o', 'u'):
            return position
    return -1

def ConvertToP(word):
    first_letter = word[0]
    if first_letter in ('a', 'e', 'i', 'o', 'u'):
        return word + "way"
    else:
        first_vowel_position = get_first_vowel_position(word)
        if first_vowel_position == -1: return "a" + word + "ay"
        else: return word[first_vowel_position:] + "a" + word[:first_vowel_position] + "ay"

def toPigLatin(s):
    list_of_words = s.split(" ")
    new_sentence = ""   
    for word in list_of_words:
        new_sentence = new_sentence + ConvertToP(word)    
        new_sentence = new_sentence + " "
    return new_sentence[:len(new_sentence)-1]

#to english

def a_pos(word):
    count = 0
    position1 = 0
    position2 = 0
    for i in range(len(word)-1,-1,-1):
        if word[i] == "a":count+=1
        if count == 2:
            position1=i
            count+=1
    for i in range(len(word)-1,-1,-1):
        if word[i] == "a":
            position2 = i
            break
    return position1, position2
    
def ConvertToE(word):
    if word[len(word)-3] == "w": return word[:len(word)-3]
    else:
        position1, position2 = a_pos(word)
        return word[position1+1:position2] + word[:position1]
    
def toEnglish(s):
    list_of_words = s.split(" ")
    new_sentence = ""   
    for word in list_of_words:
        new_sentence = new_sentence + ConvertToE(word)    
        new_sentence = new_sentence + " "
    return new_sentence[:len(new_sentence)-1]