#sarayn subroyen 
#03/04/2014
#pig latin translator

def toPigLatin(s):
    a=s.split(" ")
    b=""
    
    for i in a:
        c=0
        for d in i:
            if d in "aeiou" or d in "AEIOU":
                break
            c+=1
            
        if i[0] in "aeiou" or i[0] in "AEIOU":
            e=i+"way"
            c+=1
        elif i[0] not in "aeiou" or i[0] not in "AEIOU":
            e=i[c:]+"a"+i[0:c]+"ay"
            
        b+=e+" "
    return b

def toEnglish(s):
    a=s.split(" ")
    b=""
    
    for i in a:
        
        c=0
        for d in i:
            e=-3-c
            if i[e] in "aeiou" or i in "AEIOU":
                break
            
            c+=1
            
        if i[-3:]=="way":
            i=i[:-3]
            
        elif i[-2:]=="ay" and i[-3] not in "aeiou" and i[-3] not in "AEIOU":
            e=-2-c
            i=i[e:-2] +i[:e-1]
                    
        b+=i+" "
    return b
            
            