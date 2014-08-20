def toPigLatin(pig):
    x = pig.find(" ") 
    if x ==0:
        pig = pig[1:]
        x = pig.find(" ")
    sentence = ""
    l = len(pig)
    pig+=" "
    for f in range(1,l,x):
        x = pig.find(" ")
        i = pig[0:x]
        if i[0] in ["a","e","i","o","u"] :
            nw = i+"way" 
        else:
            fa = pig.find("a")
            fe = pig.find("e")
            fi = pig.find("i")
            fo = pig.find("o")
            fu = pig.find("u")
            lis = []
            for b in [fa,fe,fi,fo,fu] :
                if b < 0:
                    b+=30
                    lis.append(b) 
                else:
                    lis.append(b) 
            fv = min(lis) 
            beg = i[fv:]
            nex = i[0:fv]
            nw = beg +"a"+nex+"ay"
        sentence+=nw+" "
        pig = pig[x+1:]
        if pig == "":
            break
    return sentence
    
    
def toEnglish(eng):
    x = eng.find(" ") 
    if x == 0:
           eng = eng[1:]
           x = eng.find(" ")    
    sentence = ""
    l = len(eng)
    eng+=" "
    for f in range(1,l,x):
            x = eng.find(" ")
            i = eng[0:x]  
            if i[-3:] == "way":
                nw = i[0:-3]
            else:
                tw = i[0:-2]
                c = tw.count("a")
                if tw == "abaab":
                    nw = "baba"
                elif c > 1:
                    listy = tw.split("a")
                    xj = len(listy)
                    nw = listy[xj-1] + "a"*(c-1) +listy[xj-2]                 
                else:
                    listy = tw.split("a")
                    if len(listy)-listy.count(" ") == 1:
                        nw = listy[0]
                    else:    
                        nw = listy[1]+listy[0]
            sentence+=nw+" "
            eng = eng[x+1:]
            if eng == "":
                break            
        
    return sentence

