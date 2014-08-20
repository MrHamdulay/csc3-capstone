#akshay




def toPigLatin(s):
    pig=""
    num=0
    words=[]
    pos=0
    
    for i in range(len(s)):
        if(s[i:(i+1)]==" "):
            words.insert(num,s[(pos):i])    #refer to nots 1.1
            pos=i+1
            num+=1
    words.insert(num+1,s[(pos):]) #refer to pyhton
    
    for j in range(num+1):
        word=words[j]
        x=True
        for l in range(len(word)):
            if word[l:l+1] not in "aeiou":
                x=True
            else:
                x=False
                break
        if x==True:
            word="a"+word+"ay"
            pig+=word+" "
        
        
        elif(word[:1] in "aeiou"):
            word=word+"way"
            words[j]=word
            pig+=word+" "
        else:
            for k in range(len(word)):
                if word[k:k+1] in "aeiou":
                    word=word[k:]+"a"+word[0:k]+"ay"
                    break
            words[j]=word
            pig+=word+" "
    #print(pig)
    return pig
                     
   
   
   
    
def toEnglish(s):
    eng=""
    num=0
    words=[]
    pos=0
    for i in range(len(s)):
        if(s[i:(i+1)]==" "):
            words.insert(num,s[(pos):i])
            pos=i+1
            num+=1
    words.insert(num+1,s[(pos):])
    
    for j in range(num+1):
        word=words[j]
        
        x=True
        for l in range(1,len(word)-2):
            if word[l:l+1] not in "aeiou":
                x=True
            else:
                x=False
                break
        if x==True and word[:1]=="a" and word[1:2]!="w" and word[-3:]!="way":
            word=word[1:len(word)-2]
            words[j]=word
            eng+=word+" "        
        
        
        elif word[-3:]=="way" and word[:1]=="a":
            word=word[:-3]
            words[j]=word
            eng+=word+" "
        
        elif word[-3:]=="way":
            word=word[:-3]
            words[j]=word
            eng+=word+" "        
            
        elif len(word)==4:
            w=word[1:2]
            words[j]=word
            eng+=word+" "
            
        else:
            for k in range((len(word)-3),0,-1):
                if word[k:k+1] == "a":
                    word=word[k+1:(len(word)-2)]+word[:k]
                    break   
            words[j]=word
            eng+=word+" "
    return eng