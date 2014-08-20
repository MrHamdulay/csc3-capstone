'''pair counter
Frans Ledwaba
12 May 2014'''

def pairs(d,n,c):
    if n == s:
        c = c + 0
    elif d[n] == d[n + 1]:
        if n + 1 == s:
            return pairs(d, n + 1, c + 1)
        else:
            return pairs(d, n + 2, c + 1)
    else:
        return pairs(d, n + 1, c)
    print('Number of pairs:', c)

d = input('Enter a message:\n')
n = 0
c = 0
s = len(d) - 1
pairs(d,n,c)