#Shahrain Coovadia
#CVDSHA002
def toPigLatin(s):
    m=""
    y=len(s)
    a=1
    for i in range(y):
        if s[i]==" ":
            a+=1
    t=s.split(" ") #separate word
    for i in range(a):
        h=t[i]
        if h[0] in 'aeiou':
            h+='way'
        else:
            y=0
            for r in h[ : ]:
                if r not in 'aeiou':
                    y=y+1
                else: break
            h=h[y:len(h)] +'a' +h[0:y] +'ay'
        if i==a:
            m=m+h
        else:m+=h+' '
    return m
        
def toEnglish(s):
    g=s.split()
    m=''
    for h in range(len(g)):
        if g[h][-3: ]=='way':
            m+=g[h][ :-3]+' '
        elif g[h][-2: ]=='ay':
            L = g[h][ :-2]
            Q=L.rfind("a")
            m+=L[Q+1: ]+L[ :Q] + " "
    return m
        
             
     
                    
            