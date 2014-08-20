def toPigLatin(s):
    b=["a","e","i","o","u"]
    g=s#.lower()
    p=''
    for i in g.split():
        if i[0] in b:
            new_str=i+'way'
            
        else:
            q=0
            for j in range (len(i)):
                if i[q] in b:
                    break
                else:
                    q+=1        
            new_str=i[q:]+'a'+i[0:q]+'ay'
        p=p+new_str+' '
    return p
                
#a=toPigLatin(input('enter\n'))
#print(a)
def toEnglish(s):
    k=s.split()
    b=["a","e","i","o","u"]
    english=''
    for i in k:
        if i.find('w') != -1:
            p=i.find('w')
            new_str=i[:p]
        else:
            h=i[:-2]
            f=h[::-1]
            q=0
            while f[q] not in b :
                q+=1
                continue
            middle_str=f[q:]+f[:q+1][:-1]
            new_str=middle_str[::-1][:-1]
           
        english=english+new_str+' '
    return english
#o=toEnglish(input('enter\n'))
#print(o)
                
                    
            