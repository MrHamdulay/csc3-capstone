def toPigLatinWords (word):
    vowels="aeiou"
    a=word[0]
    l=len(word)
    if a in vowels:
        pigWord= (word+"way")
        return pigWord
    
    else:
        minimum= None
        c=0
        for i in range(len(vowels)):
            b=word.find(vowels[i])
            c+=b
            if b>0:
                if minimum is None or b< minimum:
                    minimum=b
                    x=minimum   
                    pigWord= (word[x:l]+"a"+word[0:x]+"ay")                   
                    return pigWord 
    if c == -5:
        pigWord= ("a"+word+"ay")
        return pigWord       

def toPigLatin(s):
    s=s.split(' ')
    sntnc=""
    for i in range (len(s)):
        sntnc+=toPigLatinWords (s[i])+" "
    return(sntnc)

def toEnglish(s):
    s=s.split(' ')
    vow="way"
    sntnc=""
    for i in range (len(s)):
        m=len(s[i])
        if (s[i])[(m-3):(m)]==vow:
            part2= ((s[i])[0:(m-3)])
            sntnc+=(part2)+" "
            
        else:
            word2=(s[i][0:m-2])
            k=word2.rfind("a")
            word3=word2[0:k]
            word3=(word2[k+1:m-2]+word2[0:k])
            sntnc+=(word3)+" "
    return(sntnc)

    
    
        