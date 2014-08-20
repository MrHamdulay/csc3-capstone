def ndom_to_decimal (a):
    a=str(a)
    p=len(a)-1
    m=0
    for i in (a):
        fact=(int(i)*(6**p))
        m+=fact
        p-=1
    return m
    

def decimal_to_ndom (a):
    ans= int(a)
    if a>=6**5:
        x1=a//7776
        x=a%7776
    elif a<6**5:
        x1=0
        x=a
    if x>=216:
        if a>7776:
            y1=x//216
            y=x%216
        else:
            y1=a//216
            y=a%216
    elif x<216:
        y=x
        y1=0
    if y>=36:
        if a>216:
            z1=y//36
            z=y%36
        else:
            z1=a//36
            z=a%36
    elif y<36:
        z=y
        z1=0
    if z>=6:
        if a>36:
            p1=z//6
            p=z%6
        else:
            p1=a//6
            p=a%6
    elif z<6:
        p=z
        p1=0
    if p>=1:
        if a>6:
            q1=p
            q=p%1
        elif a<=6:
            q1=p
            q=a%2
    elif p<1:
        q1=0
    ANS=(x1*10000)+(y1*1000)+(z1*100)+(p1*10)+(q1*1)
    return ANS
    
def ndom_add (a, b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    answ=int(a)+int(b)
    answ1=decimal_to_ndom(answ)
    return answ1

def ndom_multiply (a, b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    answ=int(a)*int(b)
    answ1=decimal_to_ndom(answ)
    return answ1