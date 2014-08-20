#print('(E)nglish or (P)ig Latin?')
#d=input()
#if d=='E':
 #   print('Enter an English sentence:')
  #  s=input()
def toPigLatin(s):
    p=s.split(" ")
    nerd=""
    
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
            
        nerd+=d+' '
    return nerd

def toEnglish(s):
    p=s.split(' ')
    nerd=''
        
    for i in p:
        c=0
        for x in i:
            meow=-3-c
            if i[meow] in "aeiou" or i in "AEIOU":
                break
            c+=1
                
        if i[-3:]=="way":
            i=i[:-3]
                
        elif i[-2:]=="ay" and i[-3] not in "aeiou" and i[-3] not in "AEIOU":
            meow=-2-c
            i= i[meow:-2] + i[:meow-1]
            
        nerd+=i+' '
    return nerd
                
            
            
        
        
        
    
        
        
        