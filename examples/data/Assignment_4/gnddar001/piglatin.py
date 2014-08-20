notgood = "aeiou"
def toPigLatin(s):
    word = ""
    s = s.split()
    
    
    for i in s:
        
        
        count = len(i) + 1
        
        if i[0] in notgood:
            word += i + "way"
        
        else:
            for j in range(len(i)):
                
                if i[j] in notgood:
                    count = j
                    break
            word += i[count:] + "a" + i[:count] + "ay"
        word += " "
    
    return word

def toEnglish(s):
   
    word = ""
    count = 0
    s = s.split()
    
    
    for i in s:
        
        if i[-3] == "w":
            word += i[:-3]

        else:
            for j in range(len(i) - 3, -1, -1):
                
                if i[j] == "a":
                    count = j
                    break
            word += i[count+1:-2] + i[:count]
        word += " "
    
    return word