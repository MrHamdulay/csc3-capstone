
#def toPigLatin(s):
    #for i in s:
    

def toPigLatin(sent):
    sent = sent
    x = False    
    finalsent = ""    
    while x == False:
        pos = sent.find(" ")
        if (pos == -1):
            pos = len(sent)
            x = True
        word = sent[0:pos]
        sent = sent[pos + 1: len(sent)]
        #word edits
        lenword = len(word)
        if(lenword==1):
            if (word in "aeiou" or word in "AEIOU"):
                word += "way"
                finalsent+= word + " "                
            else:
                word = "a" + word + "ay"
                finalsent+= word + " "
        elif(word[0] in "aeiou" or word[0] in "AEIOU"):
            word += "way"
            finalsent+= word + " "
        elif(word[0] not in "aeiou"):
            count = 0
            for i in range (lenword):
                if (word[i] in "aeiou" or word[i] in "AEIOU"):
                    break
                else:
                   count+=1 
            word = word[count: lenword]  + "a" + word[0:count] + "ay"
            finalsent+= word + " "
                
    lensent = len(finalsent)    
    finalsent = finalsent[0:lensent-1] 
    return finalsent

def toEnglish(sent):
    x = False    
    finalsent = ""    
    while x == False:
        pos = sent.find(" ")
        if (pos == -1):
            x = True
            pos = len(sent)
        word = sent[0:pos]
        sent = sent[pos + 1: len(sent)]
        #word edits
        lenword = len(word)
        if(word[lenword-3:lenword] == "way"):
            word = word[0:lenword-3]
            finalsent += word + " "
        elif(word[lenword-2:lenword] == "ay"):
            word = word[0:lenword-2]
            lenword = len(word)
            char = word.rfind("a") #finds last a
            word = word[char+1:lenword] + word[0:char]
            finalsent += word + " "
        
        
    finalsent = finalsent[0:len(finalsent)-1]   
    return finalsent

