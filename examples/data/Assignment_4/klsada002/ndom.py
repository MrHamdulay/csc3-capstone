#converts numbers between base 10 and base 6 convention
#Adam Kaliski
#2014-03-31
def ndom_to_decimal(a):
    nd=str(a)
    ans=0
    cnt=1
    for x in nd:
        ans+=(eval(x)*(6**(len(nd)-cnt)))
        cnt+=1
    return ans

def decimal_to_ndom(a):
    t=a//6
    anse=str(a%6)
    while t != 0:
        anse+=str(t%6)
        t=t//6
    ans=anse[::-1]
    return eval(ans)

def ndom_add(a,b):
    t=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    return(decimal_to_ndom(t+y))

def ndom_multiply(a,b):
    t=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    return(decimal_to_ndom(t*y))

if __name__ == '__main__':
    print(decimal_to_ndom(20))