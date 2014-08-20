

def mp(s):
    if s[0] in 'aeiou':
        return s + 'way'
    else:
        x = len(s)
        for i in 'aeiou':
            if i in s:
                x = min(s.find(i), x)
        return s[x:] + 'a' + s[:x] + 'ay'

def toPigLatin(s):
    return ' '.join(map(mp, s.split()))

def me(s):
    s = s[:len(s) - 2]
    if s[-1] == 'w':
        return s[:len(s) - 1]
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'a':
            return (s[i + 1:] + s[:i])

def toEnglish(s):
    return ' '.join(map(me, s.split()))
