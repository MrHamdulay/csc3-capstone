def toPigLatin(s):
    
    s=s.split(' ')
    
    piglatin=''
    for a in range(len(s)):
        if s[a][0] not in "bcdfghjklmnpqrstvwxyz":
            s[a]+='way'
        elif s[a][0]  in 'bcdfghijklmnpqrstvwxyz':
            s[a]= s[a]+'a'
            while s[a][0] in 'bcdfghjklmnpqrstvwxyz':
                s[a] = s[a][1::] + s[a][0]
            s[a]= s[a]+ 'ay'
        piglatin += s[a]+' '
    return piglatin

def toEnglish(s):
    
    s=s.split(' ')
    
    english=''
    for a in range(len(s)):
        if s[a][-3::]=='way':
            s[a]=s[a][:-3]
        if s[a][-2::]=='ay':
            s[a]=s[a][:-2]
            while s[a][-1] in 'bcdfghjklmnpqrstvwxyz':
                s[a]=s[a][-1]+s[a][:-1]
            s[a]=s[a][:-1]
        english +=s[a]+' '
    return english


