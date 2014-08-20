def toPigLatin(s):
    pl=""
    chunk=""
    word=""
    for i in range(0,len(s)):
        x=s[i]
        if x!=" ":
            word=word+x
        if x==" ": 
            if word[0] in "aeiou":
                word=word+"way"
                pl=pl+word+" "
                word=""
                chunk=""
                continue
            else:
                while not word[0] in "aeiou":
                    chunk=chunk+word[0]
                    word=word[1:]
                word=word+"a"+chunk+"ay"
                pl=pl+word+" "
                word=""
                chunk=""
                continue
        
        if i==len(s)-1:
            if word[0] in "aeiou":
                word=word+"way"
                pl=pl+word
                break
            else:
                while not word[0] in "aeiou":
                    chunk=chunk+word[0]
                    word=word[1:]
                    if word=="":
                        break
                word=word+"a"+chunk+"ay"
                pl=pl+word
                break
    return pl
               
def toEnglish(s):
    eng=""
    word=""
    chunk=""
    for i in range(0,len(s)):
        x=s[i]
        if x!=" ":
            word=word+x
        if x==" ":
            if "way" in word:
                word=word[:-3]
                eng=eng+word+" "
                word=""
                continue
            else:
                word=word[:-2]
                while word[-1]!="a":
                    chunk=chunk+word[-1]
                    word=word[0:-1]
                chunk=chunk[::-1]
                word=chunk+word[:-1]
                eng=eng+word+" "
                word=""
                chunk=""
                continue
        if i==len(s)-1:
            if "way" in word:
                word=word[:-3]
                eng=eng+word+" "
                word=""
                break
            else:
                word=word[:-2]
                while word[-1]!="a":
                    chunk=chunk+word[-1]
                    word=word[0:-1]                
                    chunk=chunk[::-1]
                word=chunk+word[:-1]
                eng=eng+word
                word=""
                chunk=""
                break
    return eng
                    
                        
                        
                        
                
            