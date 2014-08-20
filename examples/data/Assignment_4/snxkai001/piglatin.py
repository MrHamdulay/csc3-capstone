
vstring="aeiou"
def toPigLatin(s):
    t=""
    sr=s.split()
    for i in sr:
        ex=len(i) + 1
        if i[0] in vstring:
            t+=i+"way"
        else:
            for j in range(len(i)):
                if i[j] in vstring:
                    ex=j
                    break
            t+=i[ex:]+"a"+i[:ex]+"ay"
        t+=" "
    return t
def toEnglish(s):
    t=""
    ex=0
    sr=s.split()
    for i in sr:
        if i[-3]=="w":
            t+=i[:-3]
        else:
            for j in range(len(i)-3,-1,-1):
                if i[j]=="a":
                    ex=j
                    break
            t+=i[ex+1:-2]+i[:ex]
        t+= " "
    return t