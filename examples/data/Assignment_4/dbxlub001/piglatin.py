#strange language of the martians

def toPigLatin(s):
    w= s.split(" ")
    newSent=""
    for i in (w):
        cons=(0)
        
        for x in i:
            if x in ("aeiou") or x in ("AEIOU"):
                break
            cons+=1
        if i[0] in "aeiou" or i[0] in "AEIOU":
            i=i+"way"
        elif i[0] not in "aeiou" and i[0] not in "AEIOU":
            i=i[cons:]+"a"+i[0:cons]+"ay"
            
        newSent+= i+" "
        
    return newSent

def toEnglish (s):
    w=s.split(" ")
    newSent=""
    for i in (w):
        cons=(0)
        for x in i:
            a=-3-cons
            if i[a] in "aeiou" or i[a] in "AEIOU":
                break
            cons+=1
        if i[-3:]=="way":
            i= i[:-3]
            
        elif i[-2:]=="ay" and i[-3] not in "aeiou" and i[-3] not in "AEIOU":
            a=-2-cons
            i=i[a:-2]+i[:a-1]
        newSent+= i+" "
    return newSent

        
        
        