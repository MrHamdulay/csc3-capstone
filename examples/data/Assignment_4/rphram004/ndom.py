def ndom_to_decimal(a):
    x=str(a)
    y=0
    for i in x[:len(x)-1]:
        y+=int(i)
        y*=6
    z= y+int(x[len(x)-1])
    return z
def decimal_to_ndom(a):
    x=''
    i=a
    while i!=0:
        i=a//6
        x+=str(a%6)
        a=i
    return str(x)[::-1] 
def ndom_add(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
def ndom_multiply(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))

#x=input("Choose test:\n")
#if x==d:
    #print("calling function")
    #print("called function")
    #ndom_to_decimal(a)
#elif x==n:
    #print("calling function")
    #print("called function")    
    #decimal_to_ndom       
#elif x==a:
    #print("calling function")
    #print("called function")    
    #ndom_add(a,b)
#elif x==m:
    #print("calling function")
    #print("called function")    
    #ndom_multiply
                                    