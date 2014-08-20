def ndom_to_decimal(a):
    x=0
    index=0
    a=str(a)
    for i in a[::-1]:
        x+=int(i)*(6**index)
        index+=1
    return(x)
 
def decimal_to_ndom(a):
    if a>=(6**3):
        x=""
        pow=3
        for i in range(4):
            split=a//(6**pow)
            x+=str(split)[0]
            a=a%(6**pow)
            pow-=1
        return(int(x))
    elif a>=(6**2):
        x=""
        pow=2
        for i in range(3):
            split=a//(6**pow)
            x+=str(split)[0]
            a=a%(6**pow)
            pow-=1            
        return(int(x))
    elif a>=(6):
        x=""
        pow=1
        for i in range(2):
            split=a//(6**pow)
            x+=str(split)[0]
            a=a%(6**pow)
            pow-=1            
        return(int(x))
    else:
        return(a)

def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    return(decimal_to_ndom(z))

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    return(decimal_to_ndom(z))
