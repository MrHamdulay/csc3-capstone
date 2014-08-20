def toPigLatin(s):
    vow=('a','e','i','o','u')
    v=''
    c=s.split()
    for i in c:
        if i[0] in vow:
            v=v+(i+'way ')
        if i[0] not in vow:
            w=''
            for j in i:
                if j not in vow:
                    w=w+j
                    
                if j in vow:
                    break
            v=v+(i[len(w):]+'a'+w+'ay ')
            
    return v


def toEnglish(s):
    vow=('a','e','i','o','u')
    v=''           
    c=s.split()
    for i in c:
        if i[-1]+i[-2]+i[-3]=="yaw" and i[0] in vow:
            v+=i[0:(len(i)-3)]+' '
            
        else:
            i=i[0:len(i)-2]
            x=''
            
            for u in i[::-1]:
                if u=='a':
                    break
                x=x+u
                
                
            v+=x[::-1]+i[:len(i)-(len(x)+1)]+' '
            
    return v
                
                 
                 
                 
                 
                 
                 
                 
                 
                 
                
        
    
    
    