#piglatin

def containsW(s):
    if(s.find("w")+1)!=0:
        return not(0)
    else:
        return not(not(0))

def isVowel(s):
    if (s == "a") or (s == "e") or (s == "i") or (s == "o") or (s == "u"):
        return not(0)
    else:
        return not(not(0))

def isConsonant(s):
    if (s != "a") and (s != "e") and (s != "i") and (s != "o") and (s != "u"):
        return not(0)
    else:
        return not(not(0))

    
def removeWFromWord(s):
    news = s.replace("w","")
    return news

def toPigLatin(s):
    final = ""
    listwords = s.split()
    
    for word in listwords:
        if(isVowel(word[0:1])):
            word = word + "way"
        else:
            word = word + "a" 
            while(isConsonant(word[0])):
                word = word[1:] + word[:1]
            word = word + "ay"

        final = final + word + " "  
    final = final[0:len(final)-1]
    return final

def toEnglish(s):
    final = ""
    listword = s.split()
    
    for word in listword:
        if word[len(word)-3:len(word)] == "way":
            word = word[0:len(word)-3]
        else:
            word = word[0:len(word)-2]
            while(isConsonant(word[-1])):
                word = word[-1] + word[0:(len(word)-1)]
            word = word[0:len(word)-1]
            
        final = final + word + " "  
    final = final[0:len(final)-1]
    return final    
            
    
                        
    



   