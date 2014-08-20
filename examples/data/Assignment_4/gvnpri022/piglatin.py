def wordChange(w):
    let= w[0].upper()
    if let in ["A","E","I","O","U"]:
        w=w+"way"
    
    else:
        x=0
        end=""
        w=w+"a"
        while (w[x].upper() not in ["A","E","I","O","U"]):
            end=end+w[x]
            x=x+1
        
        w=w[x:]+end+"ay"
        
    return w

def toPigLatin(s):
    newSent=""
    for word in s.split(" "):
        newWord= wordChange(word)
        newSent=newSent+" " +newWord
    newSent=newSent[1:]
    return newSent
def wordChange1(w):
    
    l = len(w)
    #print(l)
    a="yes"
    if(w[l-3]!="w"):
        a="no"     
        w=w[:(l-2)]
        beg=""
        x=0
            
        for i in range((l-3),0,-1):
            let= w[i]
            if(let=='a'):
                break
            else:
                beg=beg+let
                x=x+1
        beg=beg[::-1]
        w=w[:(l-3-x)]
        w=beg+w
    
                
    
    
    
    return w   
def toEnglish(s):
    newSent=""
    for word in s.split(" "):
        l=len(word)
        
        if(word[l-3]=="w"):
                newWord=word[:(l-3)]    
                newSent=newSent+" " +newWord
        else:
            newWord= wordChange1(word)
            newSent=newSent+" " +newWord
    newSent=newSent[1:]
    return newSent  
    
        