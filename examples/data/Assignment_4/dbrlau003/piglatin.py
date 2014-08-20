def findvowel(word):
    for i in range(len(word)):
        if word[i] in "aeiou":
            return i
    
def toPigLatin(s):
    string=""    
    words=str(s).split()
    for word in words:
        vowel=findvowel(word)
        if word[0] in 'aeiou':
            string+=word+'way'+' '
        else:
            string+=word[vowel:]+"a"+ word[0:vowel]+"ay"+' '
    return string
            
def toEnglish(s):
    words=str(s).split()
    string=""
    for word in words:
        if word[-3:]=="way":
            string+=word[0:-3]+" "
        else:
            newword=word[:-2]
            newword=newword[::-1]
            posa=newword.find("a")
            prefix = newword[posa-1::-1]
            suffix = newword[:posa:-1]
            string +=prefix + suffix +' '
    return string
            
        


            
        