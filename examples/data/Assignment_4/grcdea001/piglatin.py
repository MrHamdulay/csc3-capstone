def toPigLatin(s):
    
    listw = s.split(' ')
    nsentence = ""   
    for word in listw:
        nsentence = nsentence + etplword(word) + " "   
        
    return nsentence   
    
def etplword(word):
        fstring = ""
        
        prefix =""
        suffix = ""
        vowels = "aeiou"
        
        if(word[0] in vowels):
            word = word+"way"
            fstring = fstring + word
            return fstring
            
        else:
            for i in word:   
                if(i not in vowels):
                    suffix = suffix + i
                    word = word[1::]
    
    
                else:
                    
                    #fstring = fstring + word + "a" + suffix + "ay"
                    break
        fstring = fstring + word + "a" + suffix + "ay"              
        return fstring 
    
def toEnglish(s):
    
    listw = s.split(' ')
    nsentence = ""   
    for word in listw:
        nsentence = nsentence + plte(word) + " "   
        
    return nsentence        
def plte(word):
    way = "way"
    fstring = ""
    
    if way in word:
        for i in word:
            if i != "w":
                fstring = fstring+i
                
            else:
                break
            
    else:
        word = word[0:-2]
        word = word[::-1]
        firstr = ""
        secondr = ""
        found = False
        for i in (word):
            if(i != "a") and found == False:
                firstr = firstr + i
            if(i == "a") and found == False:
                found = True
                continue
                
            if (found == True):
                secondr = secondr +i

        fstring = firstr[::-1] + secondr[::-1]
    return fstring
                              