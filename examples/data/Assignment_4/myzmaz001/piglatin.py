#02 April 2014        #Mazwi Myeza
#Assignment 4         #Question3
def toPigLatin(s):
    q='w'
    z=s.split(' ')
    t=""
    for h in range(len(z)):
        x=z[h]
        if q in x:
            None
        else:
            a="AEIOU"
            b='aeiou'
            if x[0:1] in a or x[0:1] in b:
                x+='way'
                
            else:
                c=0
                for i in range(len(x)):
                    if x[i] not in a and x[i] not in b:
                        c+=1
                        continue
                    else: break
                    
                x=x[c:]+'a'+x[0:c]+'ay'
        t+=x+' '
    return t[:-1]

def toEnglish(s):
    w=s.split(' ')
    t=""
    for h in range(len(w)):
        d=w[h]
        
        if d[:-4:-1] =='yaw':
            d=d[:-3]
        else:
            d=d[:-2]
            x=0
            for i in d[::-1]:
                if i=='a':
                    d=d[len(d)-x:]+d[:len(d)-x-1]
                    break
                else:
                    x+=1
        t+=d+' '
    return t[:-1]
