def toPigLatin (s):
    
    words=s.split(" ")
    out=""
    
    for i in words:
                
        if(i[0:1]!='a' and i[0:1]!='e' and i[0:1]!='i' and i[0:1]!='o' and i[0:1]!='u'):
            
            y=1
            cons=""
        
            while(i[y-1:y]!='a' and i[y-1:y]!='e' and i[y-1:y]!='i' and i[y-1:y]!='o' and i[y-1:y]!='u' and y<=len(i)):
                
                cons=cons+i[y-1:y]
                y+=1
        
            out+=i[y-1:]+"a"+cons+"ay "
        else:
            
            out=out+i+"way "
    return out[:-1]

def toEnglish(s):
    
    words=s.split(" ")
    out=""    
    
    for i in words:
        
        i=i[:-2]
        
        
        if(i[-1:]=='w'):
            out+=i[:-1]+" "
            
            
        else:
            
            y=len(i)
            cons=""
            
            while(i[y-1:y]!='a' and y!=0):
                
                cons+=i[y-1:y]
                
                y+=-1
                
            cons=cons[::-1]+i[:y-1]
            out+=cons+" "
            
    return out[:-1]