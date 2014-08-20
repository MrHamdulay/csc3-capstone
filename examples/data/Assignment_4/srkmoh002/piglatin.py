#question3 

def toPigLatin(s):
    string=s
    newword=""
    vowel="aeiou"
    final=""
    for i in string.split():
        for a in i:
            if a in "aeiou":
                newword=i+"way"+" "
                break 
            if a not in "aeiou":
                c=""
                j=1
                while i[j] not in "aeiou":
                    j=j+1
                c = i[:j]
                newword=i[j:]+"a"+c+"ay"+" "
                break
        final+=newword 
    return final
    
def toEnglish(s):
    string=s
    newword=""
    final=""
    for i in string.split():
        if i[-3:]=="way":
            newword=i[:len(i)-3]+" " 
        else: 
            i=i[:len(i)-2] 
            j=len(i)-1
            while i[j]!="a":
                j=j-1
            newword=i[j+1:]+i[:j]+" " 
        final+=newword
    return final 
     

                