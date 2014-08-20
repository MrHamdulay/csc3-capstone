"""This is part of the game 32, which will then later imported
Masilela Mduduzi
02 may 2014"""

def shift(a):
    b = [i for i in a if i!=0]
    c = []
    i = 0
    while i < len(b):
        if i+1<len(b) and b[i] == b[i+1]:
            c.append(b[i]*2)
            i += 2
        else:
            c.append(b[i])
            i += 1
    for i in range(4-len(c)):
        c.append(0)
    return c
def shift2(a):
    b = [i for i in a if i!=0]
    c = []
    i = len(b)-1
    while i >=0:
        if i-1>=0 and b[i] == b[i-1]:
            if len(c) ==0:
                c.append(b[i]*2)
            else:
                c.insert(0,b[i]*2)
            i -= 2
        else:
            c.insert(0,b[i])
            i -= 1
    for i in range(4-len(c)):
        if len(c) == 0:
            c.append(0)
        else:
            c.insert(0,0)
        
    return c
    
#print(shift2([4,0,2,2]))
