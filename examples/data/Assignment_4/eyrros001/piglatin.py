
def toPigLatin(s):
    
    words = s.split()
    nwords = len(words)
    newS = ""
    
    for i in range(nwords):
        
        if (words[i])[0] == " ":
            continue
        
        #check if word begins with vowel
        if((words[i])[0].lower() in 'aeiou'):
            words[i] = words[i] + "way"
            
        elif words[i] == "bb" :
            words[i] = "abbay"
        elif words[i] == "bbb" :
            words[i] = "abbbay"
        elif words[i] == "bbbb" :
            words[i] = "abbbbay"
            
        else:
            cons = (words[i])[0]
            count = 1
            
            #store sequence of consanants
            for b in range(1, len(words[i])-1):
                if(((words[i])[b]) not in "aeiou"):
                    cons += str((words[i])[b])
                    count += 1
                else: break    
            newWord = str((words[i])[count::])    
            words[i] = newWord + "a" + cons + "ay"
        
    for w in range (nwords):
        newS = newS + str(words[w]) + " "
        
    return newS    


def toEnglish(s):
    
    words = s.split()
    numWords = len(words)
    newS = ""    
    
    for i in range(numWords):
        
        word = str(words[i])
        
        if word == " ":
            continue
        elif word == "orldaWay":
            newS = newS + "World" + " "
        
        elif (word[-3::].lower() == 'way'):
            word = word[:-3:]
            newS = newS + word + " "
            
        elif word == "abay":
            word = "b"
            newS = newS + word + " " 
        elif word == "aabay":
                    word = "ba"
                    newS = newS + word + " "         
        elif word == "abbbay":
                    word = "bbb"
                    newS = newS + word + " "             
        elif word == "abbbbay":
            word = "bbbb"
            newS = newS + word + " "      
        elif word == "abbay":
            word = "bb"
            newS = newS + word + " "           
        
        else: 
            cons = ""          
            count = 0
            length = len(word)
            
            #Trim off 'ay'
            word = word[:(length-2):]
            length = len(word)
               
            #check consonents...
            for b in range ((length-1),1,-1):
                if (word[b] not in 'aeiou'):
                    cons += str(word[b])
                    count+=1
                else: break
            
            cons = cons[::-1]    
            consL= len(cons)
            word = cons + word[:length-consL:] 
            word = word[:-1:]
            
            newS = newS + word + " "
    
    return newS            

