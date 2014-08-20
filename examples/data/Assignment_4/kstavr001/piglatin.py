def toPigLatin(s):
    sentence = s.split()


    for i in range (len(sentence)):
       
        if (sentence[i][0].lower() in "aeiou"):
            sentence[i] = sentence[i] + "way"
        
        else:
            vowel_position = 0
         
            while sentence[i][vowel_position] not in "aeiou":
                vowel_position += 1
                if (vowel_position == len(sentence[i])):
                    break
                
            if vowel_position == len(sentence[i]):
                sentence[i] = "a" + sentence[i]+"ay"
            
            else:
                sentence[i] = sentence[i][vowel_position:] + "a" + sentence[i][0:vowel_position:1] + "ay"
  
    p_l = sentence[0]        
    for i in range (1, len(sentence)):
        p_l = p_l + " " + sentence[i]
        
    return p_l

def toEnglish(s):
    
    sentence = s.split()
    
    for i in range(len(sentence)):
        
        if (sentence[i][-1:-4:-1] == "yaw"):
            sentence[i] = sentence[i][:-3]
            
        else:
            sentence[i] = sentence[i][:-2]
            
            a_position = -1
            
            while sentence[i][a_position] != "a":
                a_position -= 1
                     
            
            sentence[i] = sentence[i][a_position+1:] + sentence[i][:a_position]
             
            
            
    p_l = sentence[0]          
    for i in range (1, len(sentence)):
        p_l = p_l + " " + sentence[i]
                    
    return p_l   