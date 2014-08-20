lC, i = 0, 0
def gtconsword(wd):
    while i < len(wd):
        if not isVowel(wd[i]):
            lC += i
            i += 1
        else:
            break

    return wd[(lC+1):]+"a"+wd[0:lC+1]+"ay"

def toPigLatin(s):
    S = ''
    for wd in s.split(' '):
        if isVowel(wd):
            S += " "+wd+"way"
        else:
            S += " "+getConsWord(word)
        
        return S[1:]       
    

def toEnglish(s):
    lC, i = 0, 0
    def gtconsword(wd):
        while i < len(wd):
            if not isVowel(wd[i]):
                lC += i
                i += 1
            else:
                break
    
    return wd[(lC+1):]+"a"+wd[0:lC+1]+"ay"
    
    
    
            
           
            