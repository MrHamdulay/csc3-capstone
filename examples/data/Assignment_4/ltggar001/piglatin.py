def toPigLatin (s):
    x=s.split(" ")
    start=""
    vowels="AEIOUaeiou"
    for a in x:
        count=0
        for b in a:
            if b in vowels:
                break
            count+=1
        if a[0] in vowels:
            a=a+'way'
            count+=1
        elif a[0] not in vowels:
            a=a[count:]+'a'+a[0:count]+'ay'
        start+= a+" "
    return start
def toEnglish(s):
    y=s.split(" ")
    start=""
    
    for j in y:
        plop=0
        for x in j:
            a=-3-plop
            if j[a] in 'aeiou' or j[a] in 'AEIOU':
                break
            plop+=1
        if j[-3:]=='way':
            j=j[:-3]
            
        elif j[-2:]=='ay' and j[-3] not in 'aeiou' and j[-3] not in 'AEIOU':
            a=-2-plop
            j=j[a:-2]+j[:a-1]
        start+= j+" "
    return start
    