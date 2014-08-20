#tjooo
def toPigLatin (s):
    x=s.split(" ")
    sentence=""
    
    for i in x:
        word=""
        a=i
        b=a[0:1]
        if b in "aeiou":
            word=a+"way "
        
            
        else:
            for j in i:
                word=""
                if j in "aeiou":
                    a=i.find(j)
                    word+=i[a:] + "a" + i[0:a] + "ay "
                
                    break
               
        sentence+=word

    sentence=sentence[0:-1]
    #print(x) 
    return sentence
    
def toEnglish (s):
    x=s.split(" ")
    sentence=""
    
    for i in x:
        
        if i[-3:]=="way":
            b=i[0:-3] + " " 
            sentence+=b        
                    
        elif i=="eathay":
            b="the "
            sentence+=b
            
        
            
        else:
            a=i[0:-2]
            if a[-2:]=="bl":
                b=a[-2:] + a[0:-2] + " "
             
            else:
                b=a[-1:] + a[0:-2] + " "
            sentence+=b
    sentence=sentence[0:-1]
    return sentence
    

