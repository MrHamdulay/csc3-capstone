def toPigLatin(s):
    
    l=s.split(" ")
    new=""
    vowels = "AEIOUaeiou"
    
    for j in l:
        plop=0
        
        for x in j:            
            if x in vowels:
                break
            plop+=1
            
        if j[0] in vowels:
            j= j +'way'
            plop+=1
            
        elif j[0] not in vowels:
            j= j[plop:]+'a'+j[0:plop]+'ay'
            
        new+= j+" "
    return new    

def toEnglish(s):
    
    l=s.split(" ")
    new=""
    
    for j in l:
        
        plop=0
        for x in j:
            a=-3-plop
            if j[a] in 'aeiou' or j[a] in 'AEIOU':
                break
            
            plop+=1
            
        if j[-3:] =='way':
            j= j[:-3]
            
        elif j[-2:] == 'ay' and j[-3] not in 'aeiou' and j[-3] not in 'AEIOU':
    
            a=-2-plop
            j = j[a:-2] + j[:a-1]
        
        new+= j+" "
    return new