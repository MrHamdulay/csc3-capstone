def toPigLatin(s):
    word=''
    for i in s.split():
    
        if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u":
            word+=i+"way"
            
        else:
            for j in i:
                if j in "aeiou":
                    p=i.find(j)
                    word+=i[p:]+"a"+i[0:p]+"ay"
                    break
    return word

def toEnglish(s):
    word=''
    for i in s.split():
        if i[-3:]=="way":
            e=i[0:-3]
        else:
            p= i[0:-2]
            if p[-2:]=="bl" or p[-2:]=="th":
                e= p[-2:]+p[0:-2]
                e= e[0:-1]
            else:
                e= p[-1:]+p[0:-1]
                e= e[0:-1]
        word+=e+' '
    
    return word
