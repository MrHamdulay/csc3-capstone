def toPigLatin(s):
    j=s.split(" ")
    new_s=""
    for i in j:
        vowels="aeiou"
        if i[0:1] in vowels:
            i=i+"way"
            new_s=new_s+i+" "
        elif i[0:1] in "w":
            i=i[1::]+"way"
            new_s=new_s+i+" "
        elif i not in vowels:
            if len(i)<3:
                i=i+"a"
                i=i[1::]+i[0]+"ay"
            else:
                i=i+"a"
                y=""
                for b in i:
                    if b in vowels: break
                    if b not in vowels:
                        y+=b
                        i=i[1::]
                i=i+y+"ay"
            new_s+=i+" "
    return new_s

def toEnglish(s):
    s=s.split(" ")
    new_s=""
    for i in s:
        i=i[:-2]
        i=i[::-1]
        g=""
        for j in i:
            if j=="w":
                r=i[1::]
                r=r[::-1]
                new_s+=r+" "
                break
            elif j!="w":
                if j=="a":
                    break            
                i=i[1::]
                g+=j
            g=g[::-1]
        g=g+i[::-1]
        g=g[::-1]
        if g[0]=="a":
            g=g[1::]
        else: continue
        g=g[::-1]
        new_s+=g+" "
    new_s=new_s[:-1]   
    return new_s