
def convert_word(word):
    VOWELS = ('a','e','i','o','u')
    first_letter = word[0]
    first_sequence = ""
    for x in word:
        if x in VOWELS:
            break
        first_sequence += x    
    if first_letter in VOWELS:
        return word + "way"
    else:
        first_sequence1 = "a" + first_sequence + "ay"
        return word[len(first_sequence):len(word)+2] + first_sequence1
    
def revert_word(word):
    VOWELS = ('a','e','i','o','u')
    last_sequence = ""
    for x in word[-3::-1]:
        if x in ('a','A'):
            break
        last_sequence += x
    last_sequence = last_sequence[::-1]   
    if word[-3] in ('w'):
        return word[0:len(word)-3]
    else:
        return last_sequence + word[0:-(len(last_sequence)+3)]
        
        
def toEnglish(s):
    VOWELS = ('a','e','i','o','u')
    
    list_of_words = s.split(' ')
    new_sentence = ""
    for word in list_of_words:
        new_sentence += revert_word(word) + " "
    return new_sentence
def toPigLatin(s):
    VOWELS = ('a','e','i','o','u')
    
    list_of_words = s.split(' ')
    new_sentence = ''
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word) + " "
    return new_sentence
        


#Q = input("(E)nglish or (P)ig Latin?\n")

#if Q == "e" or Q == "E":
    
    #s = input("Enter an English sentence:\n")
    #toPigLatin(s)
    
#elif Q == "p" or Q == "P":
    
    #s = input("Enter a Pig Latin sentence:\n")
    #toEnglish(s)
    
