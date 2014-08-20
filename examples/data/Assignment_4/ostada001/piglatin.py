vowels = "aeiou"

def test(a):
    x = False
    for i in range(0,len(vowels)-1,1):
        if a.lower()[0] == vowels[i]:
            x = True
            break
    return x
def pigWord(s):
    p = ""
    sT = s.lower()
    if test(s) == True:
        p = s+"way"
        return p
    
    else:
        conCount = 0
        for i in range (0, len(s)-1,1):
            if not sT[i] in vowels:
                conCount += 1
            else:
                break
        return (s[conCount:len(s)]+"a"+s[:conCount]+"ay")
              


def toPigLatin(s):
    final = ""
    for i in s.split():
        final += pigWord(i)+" "
    return final

def toEnglish(s):
    final = ""
    for i in s.split():
        final += engWord(i)+" "
    
    return final

def engWord(s):
    final = ""
    
    if s[len(s)-3:len(s)] == "way":
        final = s[0:len(s)-3]
    
    else:
        c = 0
        s = s[0:len(s)-2]
        
        for i in range (len(s)-1,0,-1):
            
            if s[i] != 'a':
                c+=1
            
            else:
                break

                
        final = s[len(s)-c:len(s)] + s[0:len(s)-(c+1)]     
    return final