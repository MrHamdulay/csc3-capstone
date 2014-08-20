def toPigLatin(s):
    sen = s.split(' ')
    for i in range(len(sen)):
        f = sen[i]
        if(f[0] in ['a','e','i','o','u']):
            sen[i] += 'way'
        else:
            last = ''
            x = 0
            for j in range(len(f)):
                x = j
                if (f[j] not in ['a','e','i','o','u']):
                    last += f[j]
                    sen[i] = sen[i][1:]
                else:
                    break
            sen[i] += 'a' + last + 'ay'
            
    return ' '.join(sen)
def toEnglish(s):
    sen = s.split(' ')
    for i in range(len(sen)):
        f = sen[i]
        if(f[-3:] == 'way'):
            sen[i] = f[:len(f)-3]
        else:
            a1 = 0
            a2 = 0
            for j in range(len(f)-1,-1,-1):
                if f[j] == 'a':
                    if a1 == 0:
                        a1 = j
                    elif a2 == 0:
                        a2 = j
                    else:
                        break
            sen[i] = f[a2+1:a1]+f[:a2]
    return ' '.join(sen)
