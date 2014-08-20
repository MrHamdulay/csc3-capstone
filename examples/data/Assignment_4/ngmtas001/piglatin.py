#NGMTAS001
#Pig Latin program

def toPigLatin(s):
    part = s.split(" ")
    newMess = ""
    
    for x in part :
        if(x.upper()[0] in 'AEIOU'):
            newMess = newMess+x+"way "
        
        else:
            
            vowelpos1 = x.upper().find("A")
            vowelpos2 = x.upper().find("E")
            vowelpos3 = x.upper().find("I")
            vowelpos4 = x.upper().find("O")
            vowelpos5 = x.upper().find("U")
            
            #Since if the vowel is not in position it yeilds value -1
            if(vowelpos1<0):
                vowelpos1 = 999
            if(vowelpos2<0):
                vowelpos2 = 999            
            if(vowelpos3<0):
                vowelpos3 = 999
            if(vowelpos4<0):
                vowelpos4 = 999
            if(vowelpos5<0):
                vowelpos5 = 999            
            
            positionVowel = min(vowelpos1,vowelpos2,vowelpos3,vowelpos4,vowelpos5)
            newWord = x[positionVowel:]+ "a"+ x[0:positionVowel]+"ay"
            
            newMess = newMess+newWord +" "
            
    return newMess
 
 
            
def toEnglish(s):
    
    part = s.split(" ")
    newMess = ""
    
    for x in part :
        if(x.find("way") != -1):
            newMess = newMess+x[:x.find("way")]+" "
        
        if(x.find("way") == -1):
            
            word = x[:x.find("ay")]
            
            invertWord = word[::-1]
            
            #checking for the last 'a'
            valA = (invertWord.find("a"))
            
            tmp = invertWord[:valA]
            tmp = tmp [::-1]
            
           
            newWord = tmp +word[:len(word)-valA-1]
            
            newMess = newMess+newWord +" "
            
        
            
    return newMess 
    