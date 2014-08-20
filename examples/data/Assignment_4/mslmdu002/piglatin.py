"""This program converts English to Piglatin and vice versa
Author :Masilela Mduduzi
01 April 2014"""
def toPigLatin(s):
    x='word'
    word=s.split(' ')
    y=""
    for h in range(len(word)):
        q=word[h]
        if x in q:
            None
        else:
            if q[0:1] in 'aeiou' or q[0:1] in 'AEIOU':
                q+='way'
                
            else:
                c=0
                for i in range(len(q)):
                    if q[i] not in 'aeiou' and q[i] not in 'AEIOU':
                        c+=1
                        continue
                    else: break
                    
                q=q[c:]+'a'+q[0:c]+'ay'
        y+=q+' '
    return y[:-1]

def toEnglish(s):
    word=s.split(' ')
    k=""
    for h in range(len(word)):
        e=word[h]
        
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
        k+=e+' '
    return k[:-1]
