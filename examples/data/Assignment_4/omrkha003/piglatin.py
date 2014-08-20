def toPigLatin(s) :
    
    sentence_string = []
    
    for word in s.split() : # for each substring
            if word[:1] == "a" or word[:1] == "e" or word[:1] == "i" or word[:1] == "o" or word[:1] == "u" : # vowel check
                PigLatinWord = word + "way"
            else: # consonant route
                n = 0
                for i in word[:] :
                    if i not in "aeiou" : # consonant check
                        n = n + 1
                    else : break
                    PigLatinWord = word[n: len(word)] + "a" + word[0:n] + "ay"
        
            sentence_string.append(PigLatinWord)
    
    sentence = " ".join(sentence_string)
    return sentence


def toEnglish(s) :
    
    sentence_string = []
     
    for word in s.split() :
        if word[-3:] == "way" :
            EnglishWord = word[:-3]
        elif word[-2:] == "ay" :
            word = word[:-2]
            Locate_a = word.rfind("a")
            EnglishWord = word[Locate_a + 1:] + word[:Locate_a] 
        
        sentence_string.append(EnglishWord)
        
    sentence = " ".join(sentence_string)
    return sentence        