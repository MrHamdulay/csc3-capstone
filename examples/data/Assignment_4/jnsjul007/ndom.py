def ndom_to_decimal(a):
    x=str(a)
    b=0
    t=0
    for i in range(len(x)-1,-1,-1):
        b+=int(x[i])*(6**t)
        t+=1
    return b