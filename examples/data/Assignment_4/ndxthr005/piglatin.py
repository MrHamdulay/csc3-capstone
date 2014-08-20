#THRIANKA NAIDOO
#NDXTHR005
#Assignment 4
#question 3

#converts
def toPigLatin_word(s): 
    out=""
    if len(s) != 0:
        position=0
        first= s[0:1]
        if first=="a" or first=="e" or first=="i" or first=="o" or first=="u":
            out = s + "way"
        else:
            while position < len(s) and s[position]!="a" and s[position]!="e" and s[position]!="i" and s[position]!="o" and s[position]!="u" and s[position]!="y":
                position=position+1 
            out = s[position:] + "a" + s[:position] + "ay" 
        return out
    else:
        return s
        
def toEnglish_word(s): 
    output=""
    if len(s) != 0:
        position=0
        first= s[0:1]
        word_vowel = s[0:len(s)-3]
        a = s[:len(s)-2] 
        position = len(a)-1
        if s[len(s)-3:] == "way": 
            output =word_vowel
        else:
            while position>= 0 and a[position]!="a":
                position=position-1
            output = a[position+1:] + a[0:position]       
        return output
    else:
        return s
    
def toPigLatin(s): 
    words = s.split(" ") 
    output=""
    output+= toPigLatin_word(words[0])
    for i in range (1, len(words)):
        output += (" " + toPigLatin_word(words[i])) 
    return output
        
def toEnglish(s): 
    words = s.split(" ") 
    output=""
    output+= toEnglish_word(words[0])
    for i in range (1, len(words)):
        output += (" " + toEnglish_word(words[i])) 
    return output    
    
    
    
        
    
        
        
    