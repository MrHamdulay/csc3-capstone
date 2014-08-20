#Q3 Assignment 4
#KVRSHA004
#Shaheel Kooverjee

def toPigLatin(s):
    word = s.split(" ")
    plsentence = ""
    
    for i in word:
        x=0
        for j in i:
            if j in "aeiou" or j in "AEIOU":
                break
            x += 1
        
        if i[0] in "aeiou" or i[0] in "AEIOU":
            i += "way"
            x += 1
        elif i[0] not in "aeiou" and i[0] not in "AEIOU":
            i = i[x:] + "a" + i[0:x] + "ay"
        
        plsentence += i + " "
    return plsentence
    
def toEnglish(s):
    word = s.split(" ")
    esentence = ""
    
    for i in word:
        x = 0
        
        for j in i:
            y = -3-x
            if i[y] in "aeiou" or i[y] in "AEIOU":
                break
            x += 1
            
        if i[-3:] == "way":
            i = i[:-3]
            
        elif i[-2:] == "ay" and i[-3] not in "aeiou" and i[-3] not in "AEIOU":
            y = -2-x
            i = i[y:-2] + i[:y-1]
        esentence += i + " "
        
    return esentence