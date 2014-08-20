def toPigLatin (s):
    s=s.split(" ")
    h=""
    for i in s:
        x=0
        a=""
        c=""
        if i[x]=="a" or i[x]=="e" or i[x]=="i" or i[x]=="o" or i[x]=="u":
            while True:
                if x>(len(i)-1):  
                    if len(i)==1:      
                        c=i+"way"
                    break                
                if i[x]=="a" or i[x]=="e" or i[x]=="i" or i[x]=="o" or i[x]=="u":
                    a+=i[x]
                    c=i+"way"
                    x+=1
                else: 
                    x+=-1  
                    break
        else: 
            a=""
            while True:
                if x>(len(i)-1): 
                    if len(i)==1:
                        c=i[x+1:]+"a"+a+"ay"
                    break  
                if i[x]!="a" and i[x]!="e" and i[x]!="i" and i[x]!="o" and i[x]!="u":
                    a+=i[x]
                    c=i[x+1:]+"a"+a+"ay"
                    x+=1
                else: 
                    x+=-1 
                    c=i[x+1:]+"a"+a+"ay"
                    break        
        if not h:
            h+=c
        else:
            h+=" "+c    
    return h
def toEnglish (s):
    s=s.split(" ")
    h=""    
    for i in s:
        if i.find("way")!=-1:
            x=i.find("way")
            if not h:
                h+=i[:x]
            else:    
                h+=" "+i[:x]            
        else:
            x=i.find("ay")
            y=i[:x].rfind("a")
            if not h:
                h+=i[y+1:x]+i[:y]
            else:    
                h+=" "+i[y+1:x]+i[:y] 
    return h