# Pig Latin English converter
# Bella Gorham
# 1/04/14

def isVowel(s):
    vowel = False
    if s == "a" or s=="e" or s=="u" or s=="i" or s=="o": 
        vowel=True
    return vowel

    
def toPigLatin(sentence):
    
    word = sentence.split()
    sentence=""
    length= len(word)
    
    for x in range(length):
        
        if isVowel(word[x][0])== True:
            word[x] += "way"
            sentence += word[x] + " "
        
        else:
            
            count = 0
            end = "a"
            
            for con in word[x]:
                
                if isVowel(word[x][count:count+1]) == True:
                    break
                
                else:
                    end+= word[x][count:count+1]
                    count +=1
                    
            word[x] = word[x][count:len(word[x])+1] + end + "ay"
            sentence+= word[x] + " "    
         
    return sentence


def toEnglish(sentence):
    word = sentence.split()
    sentence=""   
    length= len(word)
    beg=""
    
    for x in range(length):
    
        if word[x][-3:]=="way":
            
            word[x]= word[x][:-3]
            sentence+= word[x]+" "
            
        else:
            
            word[x]=word[x][:-2]
            count = -1
            
            for con in word[x]:
                
                if word[x][count-1:count]=="a":
                    break
                
                else:
                    beg += word[x][count-1:count]
                    count= count -1
                    
            word[x]=word[x][count:len(word[x])+1] + word[x][:count-1]
            sentence+= word[x] + " "
    return sentence
    
if '__name__'=='__main__':
    toPigLatin(sentence)
    toEnglish(sentence)
    

            
                    
                    
                
            
    

                

                  


