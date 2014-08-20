#GLMSUM001
#Sumayah Goolam Rassool
#Q_3


def toPigLatin_word(s): 
    
    display=""
    
    if len(s) != 0:
        
        position=0
        first= s[0:1]
        
        if first=="a" or first=="e" or first=="i" or first=="o" or first=="u":
            
            display = s + "way"
            
        else:
            
            while position < len(s) and s[position]!="a" and s[position]!="e" and s[position]!="i" and s[position]!="o" and s[position]!="u" and s[position]!="y":
                
                position=position+1 
                
            display = s[position:] + "a" + s[:position] + "ay" 
            
        return display
    
    else:
        
        return s
        
def toEnglish_word(s): 
    
    display=""
    
    if len(s) != 0:
        
        position=0
        
        first= s[0:1]
        
        word_vowel = s[0:len(s)-3]
        
        a = s[:len(s)-2] 
        
        position = len(a)-1
        
        if s[len(s)-3:] == "way": 
            
            display =word_vowel
            
        else:
            
            while position>= 0 and a[position]!="a":
                
                position=position-1
                
            display = a[position+1:] + a[0:position] 
            
        return display
    
    else:
        
        return s
    
def toPigLatin(s): 
    
    words = s.split(" ") 
    
    display=""
    
    display+= toPigLatin_word(words[0])
    
    for i in range (1, len(words)):
        
        display += (" " + toPigLatin_word(words[i])) 
        
    return display
        
def toEnglish(s):
    
    words = s.split(" ") 
    
    display=""
    
    display+= toEnglish_word(words[0])
    
    for i in range (1, len(words)):
        
        display += (" " + toEnglish_word(words[i])) 
        
    return display    
    
    
    
        
    
        
        
    