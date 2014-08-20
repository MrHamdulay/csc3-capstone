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
    
    words = s.split()
    
    for i in range(len(words)):
        
        if (words[i][-1:-4:-1] == "yaw"):
            words[i] = words[i][:-3]
            
        else:
            words[i] = words[i][:-2]
            
            a_pos = -1
            
            while words[i][a_pos] != "a":
                a_pos -= 1
                     
            
            words[i] = words[i][a_pos+1:] + words[i][:a_pos]
             
            
            
    p = words[0]          
    for i in range (1, len(words)):
        p = p + " " + words[i]
                    
    return p    