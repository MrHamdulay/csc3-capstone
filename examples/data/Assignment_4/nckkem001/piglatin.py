def toPigLatin (s):
    
    s = s.split(' ')
    lengthList = len(s)
    vowel = ['a','e','i','o','u']
    sNew = ''
    for i in range(lengthList):
        iPos = 0
        string = s[i]
        
        if string[0] in vowel:
            sNew = string + 'way'
        else:
            
            for k in range(len(string)):
                
                if string[k] in vowel:
                    iPos = k 
                    break
            if iPos != 0:
                sNew = string[iPos:] + 'a' + string[:iPos] + 'ay'
            elif iPos == 0:
                sNew = 'a' + string + 'ay'
        s[i] = sNew    
            
            
    return ' '.join(s) 

def toEnglish(s):
    sentence=s.split()
    newsentence=""
    for word in range(len(sentence)):
        if sentence[word][-3:]=="way":
            newsentence+=sentence[word][:-3]+" "
        elif sentence[word][-2:]=="ay":
            nWord=sentence[word][:-2]
            aPos=nWord.rfind("a")
            newsentence+=nWord[aPos+1:]+nWord[:aPos]+" "
    
    return(newsentence)