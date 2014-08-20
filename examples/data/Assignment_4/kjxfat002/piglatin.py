def toPigLatin(sent):
    x=sent.split()
    totalWords = sum(1 for word in x if word.isalpha())
    newSentance=""
    for i in range (totalWords):
        word=x[i]
        stop=0
        if word[0] in "aeiou":
            newWord=word+"way"
            newSentance=newSentance+" "+newWord
        elif "a" not in word and "e" not in word and "i" not in word and "o" not in word and "u" not in word :
                newWord="a"+word+"ay"
                newSentance=newSentance+" "+newWord        
        else:
            for j in range(0,len(word)):           
                if word[j] in "aeoiu" and stop!=1:
                    back=word[0:j]
                    front=word[j:]
                    newWord= front+"a"+back+"ay"
                    stop=1
                    newSentance=newSentance+" "+newWord
                
    finalSent=newSentance[1:]                  
    return(finalSent)
    
def toEnglish(sent):
        
    x=sent.split()
    totalWords = sum(1 for word in x if word.isalpha())
    newSentance=""
    for i in range (totalWords ):
        word=x[i]
        stop=0
        determineFactor= word[len(word)-3:]
        if determineFactor == "way":
            #started with a word
            newWord=word[0:len(word)-3]
            newSentance=newSentance+" "+newWord
        elif word[len(word)-2:] == "ay":
            newTestWord=word[:len(word)-2]
            
            for j in range(len(newTestWord),0,-1):
                if newTestWord[j-1] == "a" and stop!=1:
                    front=newTestWord[j:]
                    
                    back=newTestWord[:j-1]
                    newWord= front+back
                    stop=1
                    
                    newSentance=newSentance+" "+newWord
    newSentance=newSentance[1:len(newSentance)]                
    return(newSentance)