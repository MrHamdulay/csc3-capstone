#Marilynn Bianca Naidoo (NDXMAR020)
#Assignment 4, question 3

def toPigLatin_word(s): #converts a word from Enlish to Pig Latin
    out=""
    if len(s) != 0:
        pos=0
        first= s[0:1]
        if first=="a" or first=="e" or first=="i" or first=="o" or first=="u": #If the word starts with a vowel add "way" to the end of the word
            out = s + "way"
        else:
            while pos < len(s) and s[pos]!="a" and s[pos]!="e" and s[pos]!="i" and s[pos]!="o" and s[pos]!="u" and s[pos]!="y": #If word begins with a consonant
                pos=pos+1 #Continue going through letters in the word and stop once you reach a vowel
            out = s[pos:] + "a" + s[:pos] + "ay" #Remove consonants before first vowel and add them to the end of the word with an "a" before the consonants and "ay" after
        return out
    else:
        return s
        
    def toEnglish_word(s): #Converts Pig Latin word to English
        out=""
    if len(s) != 0:
        pos=0
        first= s[0:1]
        word_vowel = s[0:len(s)-3]
        a = s[:len(s)-2] #Removes "ay" from words beginning with consonants in English
        pos = len(a)-1
        if s[len(s)-3:] == "way": #Removes "way" from words beginning with vowels
            out =word_vowel
        else:
            while pos>= 0 and a[pos]!="a":#For english words that begin with consonants
                pos=pos-1
            out = a[pos+1:] + a[0:pos] #Puts English work back together by taking the consonants at the end of the word until it reaches an "a" and putting it at the beginning of the word, while removing the "a"       
        return output
    else:
        return s
    
def toPigLatin(s): #Converts English sentence to Pig Latin sentence
    words = s.split(" ") #makes a list of all words in sentence
    out=""
    out+= toPigLatin_word(words[0])
    for i in range (1, len(words)):
        out += (" " + toPigLatin_word(words[i])) #adds individual Pig Latin words to the string to make it a sentence again
    return out
        
def toEnglish(s): #Converts Pig Latin sentence to English
    words = s.split(" ") #Makes list of all words in sentence
    out=""
    out+= toEnglish_word(words[0])
    for i in range (1, len(words)):
        out+= (" " + toEnglish_word(words[i])) #Adds individual Engish words to string to make it sentence again
    return out    
    
    
    
        
    
        
        
    