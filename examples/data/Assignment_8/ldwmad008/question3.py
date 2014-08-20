def coder(m, n, e):
    if n == e:
        if m[n] == 'z':
            m[n] == 'a'
        else:
            return coder(chr(ord(m[n]) + 1), n, e)
    elif m[n] == ' ':
        return coder(m[n], n + 1, e)
    elif m[n] == 'z':
        return (m[n] == 'a', n + 1, e)
    else:
        return coder(chr(1 + ord(m[n])), n + 1, e)
    
    print(m)

m = input('M:\n')
n = 0
e = len(m) - 1
coder(m, n, e)