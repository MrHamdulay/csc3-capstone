def toPigLatin(s):
    new = ""
    words = s.split(" ")        
    for s in words:
        if s[0] in "aeiouAEIOU":     #first letter a vowel
            new += (s+'way ')          #add 'way'
        else:
            i = 0
            seq = ""
            while s[i] not in "aeiouAEIOU" and i < len(s)-1:       #start with consonant
                seq += s[i]
                i+=1
            new += (s[len(seq):len(s):1]+"a"+seq+"ay ")
    return new
        
def toEnglish(s):
    new = ""
    words = s.split(" ")
    for s in words:
        if s[len(s)-3:len(s)] == "way": #handles 'way' case
            new += s[0:len(s)-3]+" "
        else:
            s = s[0:len(s)-2] #remove 'ay'
            seq = "" #consonants
            
            #finds sequence of consonants
            i = len(s)-1
            while s[i] not in "aeiouAEIOU" and i > 0:
                seq = s[i] + seq
                i-=1
                
            new += seq + (s[0:len(s)-len(seq)-1])+" " #adds resulting word
    return new
