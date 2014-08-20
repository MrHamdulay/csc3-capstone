def toPigLatin(s):
    words = s.split()


    for i in range (len(words)):
       
        if (words[i][0].lower() in "aeiou"):
            words[i] = words[i] + "way"
        
        else:
            vowel_pos = 0
         
            while words[i][vowel_pos] not in "aeiou":
                vowel_pos += 1
                if (vowel_pos == len(words[i])):
                    break
                
            if vowel_pos == len(words[i]):
                words[i] = "a" + words[i]+"ay"
            
            else:
                words[i] = words[i][vowel_pos:] + "a" + words[i][0:vowel_pos:1] + "ay"
  
    p = words[0]        
    for i in range (1, len(words)):
        p = p + " " + words[i]
        
    return p

def toEnglish(s):
    

    
    a = s.split(" ")
    sen = ''    
    for individ in a:
            if ((individ[0] == 'a' or individ[0] == 'e' or individ[0] == 'i' or individ[0] == 'o' or individ[0] == 'u') and (individ[-3: ] != "way")):
                    
            
                    
                    findA = individ.rfind("a")
                    slicedWord = individ[0:findA] 
                    
                    
                    findingA2 = slicedWord.rfind("a") +1
                    
                    lastPart = slicedWord[findingA2:]
                    
                    E = slicedWord[:findingA2-1]
                    
                    
                    
                    z= (lastPart + E)                
                    
                    
                    
                    
                    
                    sen = (sen)  + (z+" ")
                    
            if ((individ.find("way")) > 0):
                    m = individ[:(individ.find("way"))]
                    sen =  sen + m+" "
                    
    finals = (sen)
    return finals
