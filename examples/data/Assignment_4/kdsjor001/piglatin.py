def toPigLatin (s):
    sentence=''
    words=s.split(' ')
    for k in words:
        c=''
        x=''
        y=''
        for i in range(len(k)):
            q=str(k[i])
            if q in'aeiou':
                break
            else:
                c+=q
        d=''        
        for i in range(len(k[len(c)::])):
            j = k[len(c)::]
            h=str(j[i])
            d+=h
        if c=='':
            x=d+'way'
        else:
            y=d+'a'+c+'ay'
        sentence+=x+y+' '
    return sentence

def toEnglish (s):
    word = ""
    iii = ""
    for i in s.split(" "):
        ii = i[::-1]
        if ii[2] == "w": 
            iii = ii[3:]
            word = word + iii[::-1] + " "
        else: 
            iii = ii[2:]
            count = 0
            for j in range(len(iii)):
                k = str(iii[j])
                if k != "a": 
                    count = count + 1
                if k == "a": break
           
            word = word + ((iii[:count])[::-1]) + ((iii[count + 1:])[::-1]) + " "    
    return word