
def toPigLatin(s):
    temp = ""
    counter = 0
    for word in s.split():
        if(counter == 0):
            temp =temp +convertWord(word)
            counter = counter+1
        else:
            temp =temp +" "+convertWord(word)
            counter = counter+1
    return temp
        

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
    temp = ""
    counter = 0
    for word in s.split():
        if(counter == 0):
            temp =temp +convertWord2(word)
            counter = counter+1
        else:
            temp =temp +" "+convertWord2(word)
            counter = counter+1
    return temp
    
def convertWord2(word):
    temp = word
    y = ""
    if temp.find("way") > -1:
        x = temp.find("way")
        y = word[:x]
        return y
    
    elif temp.find("ay") > -1:
        st = ""
        x = temp.find("ay") 
    
        for i in range(x-1,-1,-1):
            if temp[i] == "a":
                index = i
                break
            else:
                st += word[i]
        st = st[::-1]
        y = st + word[:index]
       
        return y   
