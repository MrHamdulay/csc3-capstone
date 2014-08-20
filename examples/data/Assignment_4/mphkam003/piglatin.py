def toPigLatin(s):
    pigl=""
    
    while True:
        space=s.find(" ")
        #print("space=",space)
        if space == -1:
            if s[0] in "aeiou":
                pigl+= s[:] + "way" + " " 
                        
            else:
                vowel = position(s)
                             
                consonants = s[:vowel]
                rest = s[vowel:]
                pigl+= rest + "a" + consonants + "ay" +" "
                
            break        
        
                
        if s[0] in "aeiou":
            pigl+= s[:space] + "way" +" "
        
        
        else:
            vowel = position(s)
            #print('vowel=',vowel)
        
            k = s[:vowel]
            r = s[vowel:space]
            pigl+= r + "a" + k + "ay" + " "
            
                
        s = s[space+1:]
    return pigl
            
def v(word):                        #got help from http://stackoverflow.com/questions/19106623/piglatin-translator-for-words-starting-with-multiple-consonantspython with these two functions.
    return word.lower() in "aeiou"
def position(word):
    for position, letter in enumerate(word):
        if v(letter):
            return position
        
        
        
def toEnglish (s):
    eng=""
    news=s
    c = s.replace("way","&")
    b = c.replace("ay","")+ " "
    for i in range(b.count(" ")):
        
        space=b.find(" ")
        news=b[:space]
        g = "0"+news
        if g[-1:] =="&":
            e=g.replace("0","")+ " "
            eng+=e.replace("&","")
            
        else:
            re=g.rfind("a")
            f = g[re:]
            k = g.replace(f,"")
            z=(f[1:] + k)
            e=z.replace("0","")+ " "
            #print(e)
            l = e.replace(e[0],"")
            eng+= e
            #print(g)
        b=b[space+1:]
    return eng   