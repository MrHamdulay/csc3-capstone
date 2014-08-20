#Thembekile Dubazana
#PigLatin/English Conversion

def toPigLatin(s):
    vowels=("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    sentence=""
    for word in s.split():
        if word[0] in vowels:
            sentence+=word+"way"+" "
            continue
        
        else:   
            for i in range(len(word)):#check each letter
                if word[i] in vowels:
                    sentence+=word[i:]+"a"+word[:i]+"ay"+" "
                    break
        if word[i] not in vowels:
            sentence+="a"+word+"ay"
        
    
    return sentence
   
    
def toEnglish(s):
    sentence="" 
    vowels=("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for word in s.split():
        if word[-3:]=="way":
            sentence+=word[:-3]+" "
        else:
            word=word[:-2]
            for i in range(len(word)-1,-1,-1):
                if word[i] in vowels:
                    sentence+=word[i+1:]+word[:i]+" "
                    break
                
            
    return sentence

       
        

