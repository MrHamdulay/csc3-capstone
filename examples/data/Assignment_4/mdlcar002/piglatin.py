#Q3 Assignment 4
#MDLCAR002
#Carissa Moodley

def toPigLatin (s):
    
    s = s.split(' ')
    lengthList = len(s)
    vowel = ['a','e','i','o','u']
    sNew = ''
    string = ''
    for i in range(lengthList):
        iPos = 0
        string = s[i]
        
        if string[0] in vowel:
            sNew = string + 'way'
        else:
            
            for j in range(len(string)):
                
                if string[j] in vowel:
                    iPos = j
                    break
            if iPos != 0:
                sNew = string[iPos:] + 'a' + string[:iPos] + 'ay'
            elif iPos == 0:
                sNew = 'a' + string + 'ay'
        s[i] = sNew    
            
            
    return ' '.join(s)          
def toEnglish (s):
    iPos = 0
    s = s.split(' ')
    lengthList = len(s)
    vowel = ['a','e','i','o','u']
    sNew = ''
    string = ''    
    for i in range(lengthList):
        string = s[i]
        if string[len(string)-3:] == 'way':
            sNew = string[:len(string)-3]
        else:
            sNew = string[:len(string)-2]
            iPos = sNew.rfind('a')
            sNew = sNew[(iPos)+1:] + sNew[:iPos]
        s[i] = sNew        
            
    return ' '.join(s)
