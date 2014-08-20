def toPigLatin (s):
    pl=""
    vowels="aeiou"
    pos=0
    vowPos=-1
    vowLas=-1
    str=""
    words=s.split()
    last=words[(len(words)-1)]
    begin=0
    for k in range(len(last)):
        if last[k] in vowels:
            vowLas=k
            break    
    if last[0].lower() in vowels:
        last=last+"way"
    else:
        if vowLas>-1:
            last=last[vowLas:]+"a"+last[0:vowLas]+"ay"
        else:
            last="a"+last+"ay"
    for i in range(len(s)):
        if s[i].isspace():
            pos=i
            str=s[begin:pos]

            begin=pos+1
            for j in range(len(str)):
                if str[j] in vowels:
                    vowPos=j
                    break
            
                    
            if str[0].lower() in vowels:
                str=str+"way"
            
            else:
                if vowPos>-1:
                    str=str[vowPos:]+"a"+str[0:vowPos]+"ay"
                else:
                    str="a"+str+"ay"
                    
                
            pl+=str+" "
    pl+=last
    return pl
def toEnglish(s):
    pos=0
    begin=0
    str=""
    back=""
    incr=0
    startSp=0
    reverse=s[::-1]
    for z in range(len(reverse)):
        if reverse[z].isalpha()==True:
            startSp=z
            break
    if startSp==0:
        s=s+" "
        
    pl=""
    posA=0
    cons=""
    for i in range(len(s)):
        if s[i].isspace():
            pos=i
            str=s[begin:pos]
            begin=pos+1
            str=str[:len(str)-2]
           
            if str[len(str)-1]=='w':
                if len(str)==2:
                    str=str[0]
                else: str=str[0:(len(str)-1)]
            else:
                back=str[::-1]
                for k in range(len(back)):
                    if back[k].lower()=='a':
                        posA=k
                        break
                cons=back[0:posA]
                cons=cons[::-1]
                
                posA=-posA+len(str)
                str=cons+str[0:posA-1]
            pl+=str+" "
    pl=pl[:len(pl)-1]
    return pl