def toPigLatin(s):
    p=s.split(' ')
    k=''
    
    for i in p:
        c=0
        for g in i:
            if g in "aeiou" or g in "AEIOU":
                break
            c+=1
            
        if i[0] in "aeiou" or i[0] in "AEIOU":
            d=i+"way"
            c+=1
        elif i[0] not in "aeiou" or i[0] not in "AEIOU":
            d=i[c:]+"a"+i[0:c]+"ay"
            
        k+=d+' '
    return k

def toEnglish(s):
    p=s.split(' ')
    k=''
    
    for i in p:
        
        c=0
        for x in i:
            z=-3-c
            if i[z] in "aeiou" or i in "AEIOU":
                break
            
            c+=1
            
        if i[-3:] =="way":
            i=i[:-3]
            
        elif i[-2:]=="ay" and i[-3] not in "aeiou" and i[-3] not in "AEIOU":
            z=-2-c
            i= i[z:-2] +  i[:z-1]
            
        k+=i+' '
    return k