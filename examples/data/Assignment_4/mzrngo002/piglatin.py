def toPigLatin (s):
    z=""
    n=""
    for i in s.split(' '):
        n=''
        for a in i:
            
            if i[0] in"aeiou":
                z+=" "+i+"way"  
                break
            else:
                
                if a not in "aeiou":
                    n+=a
                else:
                    if z:
                        z+=" "+i[i.find(a):]+"a"+n+"ay"
                    else:                        
                        z+=i[i.find(a):]+"a"+n+"ay"
                    break
    return z
    
    
def toEnglish (s):
    z=""
    n=""
    for i in s.split(' '):
        if "way" in i:
            z+=i[:i.find("way")]+" "
            break
        else:
            a=i[:i.find("ay")]
            a.rfind("a")
            z+=a[a.rfind("a")+1:]+a[:a.rfind("a")]+" "
    return z
    #toEnglish ("eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway")