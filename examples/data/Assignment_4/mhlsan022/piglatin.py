'''This program converts English to Piglatin and Piglatin to English
Sandile Christopher Mahlangu
1 April 2014'''
def toPigLatin(s):
    q='w'
    w=s.split(' ')
    r=""
    for h in range(len(w)):
        e=w[h]
        if q in e:
            None
        else:
            a="AEIOU"
            B='aeiou'
            if e[0:1] in a or e[0:1] in B:
                e+='way'
                
            else:
                c=0
                for i in range(len(e)):
                    if e[i] not in a and e[i] not in B:
                        c+=1
                        continue
                    else: break
                    
                e=e[c:]+'a'+e[0:c]+'ay'
        r+=e+' '
    return r[:-1]

def toEnglish(s):
    w=s.split(' ')
    r=""
    for h in range(len(w)):
        e=w[h]
        
        if e[:-4:-1] =='yaw':
            e=e[:-3]
        else:
            e=e[:-2]
            x=0
            for i in e[::-1]:
                if i=='a':
                    e=e[len(e)-x:]+e[:len(e)-x-1]
                    break
                else:
                    x+=1
        r+=e+' '
    return r[:-1]
