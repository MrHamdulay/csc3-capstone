
def toPigLatin(s):
    tmp = ""
    counter = 0
    for word in s.split():
        if(counter == 0):
            tmp =tmp +convertWord(word)
            counter = counter+1
        else:
            tmp = tmp+ " "+convertWord(word)
            counter = counter+1
    return tmp
        

def convertWord(word):
    if word[0] in "AEIOU" or word[0] in "aeiou":
            word += "way"
            return word
        
    else:
        snew = ""
        s1 = ""
        for i in range(len(word)):
           
            
            if word[i] in "AEIOU" or word[i] in "aeiou":
                                
                s1 += word[i:] + "a" + snew + "ay"
                
                break 
            else:
                            
                snew += word[i]  
                
            if i == (len(word)-1):
                s1 += "a" + snew + "ay"
                
        return s1    
    
def toEnglish(s):
    tmp = ""
    counter = 0
    for word in s.split():
        if(counter == 0):
            tmp =tmp +convertWord2(word)
            counter = counter+1
        else:
            tmp =tmp +" "+convertWord2(word)
            counter = counter+1
    return tmp
    
def convertWord2(word):
    tmp = word
    y = ""
    if tmp.find("way") > -1:
        x = tmp.find("way")
        y = word[:x]
        return y
    
    elif tmp.find("ay") > -1:
        st = ""
        x = tmp.find("ay") 
    
        for i in range(x-1,-1,-1):
            if tmp[i] == "a":
                index = i
                break
            else:
                st += word[i]
        st = st[::-1]
        y = st + word[:index]
       
        return y   
