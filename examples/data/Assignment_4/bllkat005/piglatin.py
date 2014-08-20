#BLLKAT005
#Kate Bell
# 3 April 2014

def toPigLatin (s):
    """return the Pig Latin string for a given English string"""
    s = s.split(" ")
    for i in range (len(s)):
        starts_vowel = 0
        vowel= ["a","e","i","o","u","A","E","I","O","U"]
        for j in range(len(vowel)):
            if s[i].startswith(vowel[j]):
                starts_vowel=1
#starts with vowel, so add "way"        
        if starts_vowel == 1:
            s[i]=s[i]+"way"
#starts with consonants, so count consonants 
        elif starts_vowel == 0:
            count_cons = 0
            #count number of consonants at start of word
            for c in range (len(s[i])):
                    if s[i][c] in ["a","e","i","o","u","A","E","I","O","U"]:
                        break
                    else:
                        count_cons=count_cons+1
            s[i]=s[i][count_cons:]+"a"+s[i][:count_cons]+"ay"
    latin = s[0]
    for l in range (1,len(s)):
        latin=latin+" "+s[l]
    return latin            
            
            
def toEnglish (s):
    """return the English string for a given Pig Latin string"""
    s = s.split(" ")
    e=[]
    for i in range (len(s)): 
    #if it originally started with a vowel
        if s[i].endswith("way"):
            s[i]=s[i][:len(s[i])-3]
            e=e+[s[i]]
    #if it originally started with consonants      
        else:
            word = s[i][:len(s[i])-2]
            count_cons = 0
        #count number of consonants from end of word
            for c in range (-1,-len(word),-1):
                if word[c] in ["a","e","i","o","u","A","E","I","O","U"]:
                    break
                else:
                    count_cons=count_cons+1  
            e = e + [word[len(word)-count_cons:]+word[:len(word)-count_cons-1]]
    english = e[0]    
    for j in range (1,len(e)):
        english= english+" "+e[j]
    return english 
        