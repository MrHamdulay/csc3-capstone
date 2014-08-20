"""A progam to convert a sentence into piglatin and to convert a piglatin into English
By Jeremy Smith SMTJER002
3 April 2014"""

def toPigLatin(s):
    sentence=s
    sentence=sentence.split()
    vowel=set("aeiou")
    consonant=set("bcdfghHjklmnpqrstvWxyz")
    wordlist=[]
    for i in sentence:
        length=len(i)
        if i[0] in vowel:
            i+="way"      
        elif length > 3 and i[0] in consonant and i[1] in consonant and i[2] in consonant and i[3] in consonant:
            i+="a"
            i=i[4:]+i[0:4]
            i+="ay"            
        elif length > 2 and i[0] in consonant and i[1] in consonant and i[2] in consonant:
            i+="a"
            i=i[3:]+i[0:3]
            i+="ay" 
        elif length > 1 and i[0] in consonant and i[1] in consonant:
            i+="a"
            i=i[2:]+i[0:2]
            i+="ay"
        else:
            i+="a"
            i=i[1:]+i[0:1]
            i+="ay"            
        wordlist.append(i)
    final=" ".join(wordlist)    
    
    return final

def toEnglish(s):
    sentence=s
    sentence=sentence.split()    
    vowel=set("aeiou")
    consonant=set("bcdfghHjklmnpqrstvWxyz")
    wordlist=[]
    for i in sentence:
        length=len(i)
        i=i[0:-2]
        if i[-1] == "w":
            i=i[0:-1]
        elif length > 4 and i[-1] in consonant and i[-2] in consonant and i[-3] in consonant and i[-4] in consonant:
            i=i[-4:]+i[0:-4]
            i=i[0:-1]
        elif length > 3 and i[-1] in consonant and i[-2] in consonant and i[-3] in consonant:
            i=i[-3:]+i[0:-3]
            i=i[0:-1]
        elif length > 2 and i[-1] in consonant and i[-2] in consonant:
            i=i[-2:]+i[0:-2]
            i=i[0:-1]
        elif length > 1 and i[-1] in consonant:
            i=i[-1:]+i[0:-1]
            i=i[0:-1]        
            
        wordlist.append(i)
   
    final=" ".join(wordlist)    
    return final
