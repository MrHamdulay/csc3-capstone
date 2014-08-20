# Student Number: PRTNIC017
# Date: 5/9/14

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()

def asci(a):
    return ord(a)

def encrypt(s):
    if len(s) == 1:
        if s in lower:
            if asci(s[0]) == asci('z'):
                return 'a'
            else:
                return str(chr(asci(s[0]) + 1))
        else:
            return s
    else:
        if s[0] in lower:
            zero = ''
            if asci(s[0]) == asci('z'):
                zero = 'a'
            else:
                zero = str(chr(asci(s[0]) + 1))
            s = s.replace(s[0], '', 1)
            return zero + encrypt(s)
        else:
            zero = str(s[0])
            s = s.replace(s[0], '', 1)
            return zero + encrypt(s)

into = input('Enter a message:\n')
print('Encrypted message:\n',encrypt(into), sep='')