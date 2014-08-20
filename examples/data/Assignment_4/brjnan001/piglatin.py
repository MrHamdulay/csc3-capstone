#Nandani Birjanund (BRJNAN001)
#Assignment 4, question 3

def toPigLatin_word(s): #converts a word from Enlish to Pig Latin
    output=""
    if len(s) != 0:
        position=0
        first= s[0:1]
        if first=="a" or first=="e" or first=="i" or first=="o" or first=="u": #if the word starts with a vowel add "way" to the end of the word
            output = s + "way"
        else:
            while position < len(s) and s[position]!="a" and s[position]!="e" and s[position]!="i" and s[position]!="o" and s[position]!="u" and s[position]!="y": #if word begins with a consonant
                position=position+1 #continue going through letters in the word and stop once you reach a vowel
            output = s[position:] + "a" + s[:position] + "ay" #remove consonants before first vowel and add them to the end of the word with an "a" before the consonants and "ay" after
        return output
    else:
        return s
        
def toEnglish_word(s): #converts Pig Latin word to English
    output=""
    if len(s) != 0:
        position=0
        first= s[0:1]
        word_vowel = s[0:len(s)-3]
        a = s[:len(s)-2] #removes "ay" from words beginning with consonants in English
        position = len(a)-1
        if s[len(s)-3:] == "way": #removes "way" from words beginning with vowels
            output =word_vowel
        else:
            while position>= 0 and a[position]!="a":#for english words that begin with consonants
                position=position-1
            output = a[position+1:] + a[0:position] #puts English work back together by taking the consonants at the end of the word until it reaches an "a" and putting it at the beginning of the word, while removing the "a"       
        return output
    else:
        return s
    
def toPigLatin(s): #converts English sentence to Pig Latin sentence
    words = s.split(" ") #makes a list of all words in sentence
    output=""
    output+= toPigLatin_word(words[0])
    for i in range (1, len(words)):
        output += (" " + toPigLatin_word(words[i])) #adds individual Pig Latin words to the string to make it a sentence again
    return output
        
def toEnglish(s): #converts Pig Latin sentence to English
    words = s.split(" ") #makes list of all words in sentence
    output=""
    output+= toEnglish_word(words[0])
    for i in range (1, len(words)):
        output += (" " + toEnglish_word(words[i])) #adds individual Engish words to string to make it sentence again
    return output    
    
    
    
        
    
        
        
    