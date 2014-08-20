# Translator: English & Pig Latin
# Khwezi Majola
# MJLKHW001
# 31 March 2014

def toPigLatin(s):
    s = s.strip()
    l = s.count(' ') + 1
    a = s.split()
    result = ''
    for i in range(l):
        b = ''
        b = ''.join(a[i])
        c = 0
        j = 0
        if b[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                b += 'way'
                result += b + ' '
        else: 
            while b[j] not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                c += 1
                j += 1
                if j == len(b):
                    break
            t = b[:c]
            b = b[c:]
            b += 'a' + t +'ay'
            result += b + ' '
    result = result[:len(result)-1]            
    return result

def toEnglish(s):
    s = s.strip()
    l = s.count(' ') + 1
    a = s.split()
    result = ''
    for i in range(l):
            b = ''
            b = ''.join(a[i])
            z = len(b)
            if b[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] and b[z-3:z] == 'way':
                b = b[:z-3]
                result += b + ' '
            else:
                b = b[:z-2]
                b = b[::-1]
                c = b.find('a')
                j = b[:c]
                j = j[::-1]
                b = b[c+1:]
                b = b[::-1]
                b = j + b
                result += b + ' '
    result = result[:len(result)-1]            
    return result            