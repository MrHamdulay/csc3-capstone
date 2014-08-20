def toPigLatin(s):
    
    w=s.split(" ")
    new=""
    
    
    for i in w:
        plop=0
        #for x in i:
        
        for x in i:            
            if x in 'aeiou' or x in 'AEIOU':
                break
            plop+=1
            
        if i[0] in 'aeiou' or i[0] in 'AEIOU':
            i= i +'way'
            plop+=1
            
        elif i[0] not in'aeiou' and i[0] not in 'AEIOU':
            i= i[plop:]+'a'+i[0:plop]+'ay'
            
        new+= i+" "
    return new    



def toEnglish(s):
    
    w=s.split(" ")
    new=""
    
    for i in w:
        
        plop=0
        for x in i:
            a=-3-plop
            if i[a] in 'aeiou' or i[a] in 'AEIOU':
                break
            
            plop+=1
            
        if i[-3:] =='way':
            i= i[:-3]
            
#i[-3] not in 'aeiou' and 
                    
            
        elif i[-2:] == 'ay' and i[-3] not in 'aeiou' and i[-3] not in 'AEIOU':
        #elif i[-3] not in 'aeiou' and i[-2:] =='ay':
            a=-2-plop
            i = i[a:-2] + i[:a-1]
        
        new+= i+" "
    return new