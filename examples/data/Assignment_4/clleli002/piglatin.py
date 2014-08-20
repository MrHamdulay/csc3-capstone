def toPigLatin(s):
    
    conCount= 0 #consonant count
    newStr="" #new word 
    newSent=""  #overall sentence
    
    for numStr in s.split(): #for every  word in list of words
        newStr=numStr #word=newStr
        conCount=0 #consonant count is zero'ed
        if numStr[0] in "aeiou": #if the first letter in the word is a vowel then....
            numStr= numStr+ "way" #word will be appended with "way" at the end
            newSent= newSent+ numStr+ " " #add word to new sentence
            continue 
        else:
            newStr= newStr + "a"
        
        for x in range(len(numStr)): #for each letter in word
            if numStr[x] in "bcdfghjklmnpqrstvwxyz": #if letter in position x is consonant....
                conCount= conCount+1 #the consonant position gets added to the consonant count
                newStr= newStr+numStr[x] #new word becomes word appended with consonant
                
            else: #when it reaches the letter "a"at the end of the word
                newStr= newStr[conCount::]+"ay" #consonants in beginning get cut off and "ay is added to end of word
                break 
        newSent=newSent + newStr + " "
    return(newSent)    
            
            
def toEnglish(s):
    newSent2=""
    numStr2=""
    
    for numStr2 in s.split():
        if numStr2[-3] in "w": #if word had letter w in it...
            numStr2=numStr2[0:len(numStr2)-3]
            newSent2=newSent2+numStr2+ " "
            
        else:
            numStr2=numStr2[:-2] #take away "ay" at the end of every word
            numStr2=numStr2[::-1] #temporarily reverse word in order to find "a" at the end
            ind=numStr2.find("a") #find position of "a"
            prefix=numStr2[ind-1::-1] 
            suffix=numStr2[:ind:-1]
            numStr2=prefix+suffix
            newSent2=newSent2+numStr2+ " "
        
    return (newSent2)        
  