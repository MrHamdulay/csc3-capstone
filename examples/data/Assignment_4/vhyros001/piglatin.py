"""English - Pig Latin translator
Ross van der Heyde VHYROS001
31 March 2014"""

def toPigLatin (s):
    #s = s.lower()    
    
    arWords = s.split()
    pigWord = ""
    pigSentence=""
    
    for j in range (len(arWords)):
        w = arWords[j]
        
        #starts with vowel    
        if w[0]in "aeiou" or w[0] in "AEIOU":
            pigWord = w+ "way"
        else: #doesnt start with vowel
            
            # see if there is a vowel
            vowel = False
            for i in w:
                if i in "aeiou" or i in "AEIOU":
                    vowel= True
                
            
            if vowel:
                i = 0
                end = "" # prefix of consonants to be added to the end 
                char = w[i]
                while char not in "aeiou":
                    end+=char
                    i+=1
                    if len(w)> 1:
                        char = w[i]
                else:
                    start = w[i::] #rest of word(unchanged, now the start of the latin word)
                #print("startsWith:",end)
                pigWord = start+"a"+ end + "ay"#create latin word
                #print("Translation: ", pigWord)
            
            else:
                pigWord = "a"+w+"ay"
            
        pigSentence+= pigWord+" "
   
    pigSentence = pigSentence[0:len(pigSentence)-1]
    return pigSentence   
   
def toEnglish(s):
    #s = s.lower()    
        
    arWords = s.split()
    engWord = ""
    engSen=""    
    end = 0 
    
    for j in range (len(arWords)):
        w = arWords[j]
        start= ""    
        
        if  'way' in w: # english word starts with vowel
            w= w[0:len(w)-3]
        else:
            # english word starts with consonant eg please--->easeaplay
            
            w = w[0:len(w)-2]            
            #print("w: ", w)
            # step through word, starting at end, until first 'a'
            for i in range (1, len(w)+1):
                char = w[-i]
                if char == 'a':
                    break
                else:
                    start +=char
                end = -i
                
            start = start[::-1]
            #print("start: ", start)    
            
            
            w = start+w[0:end-1]
        
        engSen += w+ " "
    engSen = engSen[0:len(engSen)-1]
    
    return engSen

#toPigLatin (s), to return the Pig Latin string for a given English string
#toEnglish (s), to return the English string for a given Pig Latin string
    
#if the word begins with a vowel, "way" should be appended (example: apple becomes appleway)
#if the word begins with a sequence of consonants, this sequence should be moved to the end,
#prefixed with "a" and followed by "ay" (example: please becomes easeaplay)
#Assume that the English text does not contain the letter "w".    
#eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway

