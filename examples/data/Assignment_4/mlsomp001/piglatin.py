def toPigLatin(s):
    y=''
    w= s.split()
    sa='aeiouAEIOU'
    for q in w:
        if q[0] in sa:
            y+= str(q) + 'way '

        elif q.find('a') == -1 and q.find('e') == -1 and q.find('i') == -1 and q.find('o') == -1 and q.find('u') == -1 and q.find('A') == -1 and q.find('E') == -1 and q.find('I') == -1 and q.find('O') == -1 and q.find('U') == -1:
            y+= 'a' + q[::] + 'ay '
        else:
            for h in q:
                if h in sa:
                    y+= q[q.find(h):] +'a' + q[:q.find(h)] + 'ay '
                    break        
        
    return y

def toEnglish(s):
    y = ''
    w = s.split()
    sa="AEIOUaeiou"
    con=''
    for q in w:
        if q.find('w') != -1:
            y+= q[:q.find('w')] + ' '
        else:
            q=q.replace('ay','')
            y+= q[q.rfind('a')+1:] + q[:q.rfind('a')] + ' '
            
    return y