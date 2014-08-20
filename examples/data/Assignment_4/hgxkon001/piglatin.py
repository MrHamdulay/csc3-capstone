def toPigLatin(s):
    
    words=s.split(' ')
    x=''
    for i in range(0,len(words)):
        s=words[i]   
        if s[0] in "aeiouAEIOU":
            s=s+'way'
            
            x=x+s+' '
        elif s[0] not in "aeiouAEIOU":
            su=''
            
            for j in range(0, len(s)):
                if j == len(s)-1 and s[j] not in "AEIOUaeiou":
                    s="a"+s+"ay"
                    x=x+s+' ' 
                    break
                
                elif s[j] not in "AEIOUaeiou":
                    su+=s[j]
                    continue
                    
                elif s[j] in "AEIOUaeiou":
                    s=s[j:]
            
                    s=s+'a'+su+'ay'
                    x=x+s+' '
                    break
        
    return x 


def toEnglish(s):
    words=s.split(' ')
    x=''
    for i in range(0,len(words)):
        w=words[i]
        if w[-3:] == "way":
            w2=w[:-3]
            x=x+w2+' '
        else:
            w2=w[:-2]
        
            j=1
            while j<=len(w2):
                if w2[-j] == w2[0] and w2[-j] !='a':
                    w2=w2[1:]
                    x=x+w2+' '
                    break
                if w2[-j] =='a':
                
                    w2=w2[(-j)+1:]+w2[:-j]
                    x=x+w2+' '
                    break
                else:
                    j=j+1
                    continue
            
    return x       
        
                                 
    
                

            
                    
                    
                    
            