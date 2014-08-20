def toPigLatin1(s):
    str(s)
    if s[0] == "a" or s[0] == "e" or s[0] == "i" or s[0] == "o" or s[0] == "u":
        s+="way"
        return s
    else:
        word = "aeiou"
        x =""
        for i in word:
            new_x=s.find(i)
            if new_x<0:
                x+=""
            else:
                x+=str(new_x)
        if x=="":
            s = "a"+s+"ay"
            #print(s)
            return s
            
        if len(x)==1:
            y = x
            y =int(y)
            s=s[y:]+"a"+s[0:y]
            s+="ay"
            #print(s)
            return s
        else:
            y =min(x)
            y = int(y)
            s=s[y:]+"a"+s[0:y]
            s+="ay"
            #print(s)
            return s


def toPigLatin(s):
    s = s.split()
    sentence = ""
    
    for i in s:
        i = toPigLatin1(i)
        sentence+=i+" "
    return sentence
#toPigLatin("the quick black fox jumps over the lazy apple")
    


def toEnglish1(s):
    s.lower()
    
    s=s[::-1]
    s=s[2:]
    if s[0]=="w":
        s=s[1:]
        s=s[::-1]
        return s
    else:
        m = s.find("a")
        s=s[m+1:]+s[0:m]
        s=s[::-1]
        return s

def toEnglish(s):
    s = s.split()
    sentence=""
    for i in s:
            #str(i)
            i = toEnglish1(i)
            sentence+=i+" "
    return sentence
            
#toEnglish("eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway")
