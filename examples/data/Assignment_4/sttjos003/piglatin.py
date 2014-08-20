s="the quick brown fox jumps over the lazy dog"

def toPigLatinfundamental(s):
    x=0
    z=0
    l=len(s)
    total=""
    end=""
    if s[0] in "aeiou":
        return(s+"way")    
    else:    
        for i in range(l):
            if s[i] in "aeiou":
                x=i
                break
            
            else:
                end+=s[i]
                
        new_s=s[x::]
        
        if x!=0:    
            total+=(new_s + "a" + end + "ay")
        
        elif x==0:
            total+=("a" + end + "ay")
        
        return(total)

def toPigLatin(s):
    new_sentence=""
    
    sentence=s
    
    list_of_words=sentence.split(" ")
    
    for word in list_of_words:    
        new_sentence+=toPigLatinfundamental(word)+" "
    
    return new_sentence

def toEnglish(s):
    list_of_words=s.split(" ")
    total=""
    for word in list_of_words:
        l=len(word)
        rev=word[::-1]
        if word[-3]=="w":
            total+=word[:l-3:]+ " "
            
        else:
            rev2=rev[2::]
            x=rev2.find("a")
            y=l-x-2
            begin=word[y:l-2:]
            end=word[:y-1:]
            total+=begin+end+" "
            
            
    return total