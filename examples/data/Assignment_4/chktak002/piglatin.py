def toPigLatin(s):
    vowels="aeiouAEIOU"
    T = ""
    count = 0
    for word in s.split():
        if(count == 0):
            T =T +conv(word)
            count = count+1
        else:
            T = T+ " "+conv(word)
            count +=1
    return T
        

def conv(word):
    vowels="aeiouAEIOU"
    if word[0] in vowels :
            word += "way"
            return word
        
    else:
        string = ""
        string1 = ""
        for i in range(len(word)):
           
            
            if word[i] in vowels:
                                
                string1 =string1+ word[i:] + "a" +string + "ay"
                
                break 
            else:
                            
                string += word[i]  
                
            if i == (len(word)-1):
                string1 =string1+ "a" +string + "ay"
                
        return string1    
    
def toEnglish(s):
    T = ""
    count = 0
    for word in s.split():
        if count == 0:
            T =T +conv2(word)
            count +=1
        else:
            T =T +" "+conv2(word)
            count +=1
    return T
    
def conv2(word):
    T = word
    y = ""
    if T.find("way") > -1:
        x = T.find("way")
        y = word[:x]
        return y
    
    elif T.find("ay") > -1:
        st = ""
        x = T.find("ay") 
    
        for i in range(x-1,-1,-1):
            if T[i] == "a":
                index = i
                break
            else:
                st =st+ word[i]
        st = st[::-1]
        y = st + word[:index]
       
        return y   
