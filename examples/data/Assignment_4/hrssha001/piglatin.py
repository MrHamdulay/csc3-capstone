def toPigLatin(s): 
    string=""
    for word in s.split(" "):
        
        x="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        y="aeiouAEIOU"
        if word[0] in y:
            word+="way"
        elif len(word)==1:
            word="a"+word+"ay"
            
        elif word[0] in x and word[1] in y:
            word=word[1:]+"a"+word[0]+"ay" 
            
        elif len(word)==2:
            word="a"+word+"ay"
        
        elif word[0] in x and word[1] in x and word[2] in y:
            word=word[2:]+"a"+word[0]+word[1]+"ay"
            
        elif len(word)==3:
            word="a"+word+"ay"
        
        elif word[0] in x and word[1] in x and word[2] in x and word[3] in y: 
            word=word[3:]+"a"+word[0]+word[1]+word[2]+"ay" 
            
        elif len(word)==4:
            word="a"+word+"ay"
        
                            
        elif word[0] in x and word[1] in x and word[2] in x and word[3] in x and word[4] in y:
            word=word[4:]+"a"+word[0]+word[1]+word[2]+word[3]+"ay"
            
        #else: 
            #word="a"+word+"ay"     
        
        #elif word[0] in x and word[1] in x:
            #word=word[2:]+"a"+word[0]+word[1]+"ay"
        
        
        string+=word+" "
    return string
       
#print(toPigLatin("the tt t ttt jumped over the fox"))
        

def toEnglish(s):
    x=''
    con=''
    for word in s.split(" "):
        if word[len(word)-3:] == 'way':
            x+=word[:len(word)-3]+' '
        else:
            con = word[::-1][2:]
            for i in word:
                if i == 'a':
                    x+=(con[con.find('a')+1:]+con[:con.find('a')])[::-1]+' '
                    break
    return x[:len(x)-1]    