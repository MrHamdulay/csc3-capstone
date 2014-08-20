

def contop(mystring):
    if mystring[0] in 'aeiouAEIOU':
        return mystring + 'way'
    else:
        y = len(mystring)
        for i in 'aeiouAEIOU':
            if i in mystring:
                y = min(mystring.find(i), y)
        return mystring[y:] + 'a' + mystring[:y] + 'ay'

def toPigLatin(s):
    return ' '.join(map(contop, s.split()))

def contoe(s):
    s = s[:len(s) - 2]
    if s[-1] == 'w':
        return s[:len(s) - 1]
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'a':
            return (s[i + 1:] + s[:i])

def toEnglish(s):
    return ' '.join(map(contoe, s.split()))
