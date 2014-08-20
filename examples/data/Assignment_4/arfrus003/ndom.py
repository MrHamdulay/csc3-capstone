def ndom_to_decimal(a):
    third=a//100
    endom3=third*36
    third_rmd=a%100
    sec=third_rmd//10
    endom2=sec*6
    sec_rmd=a%10
    return(endom3+endom2+sec_rmd)

def decimal_to_ndom(a):
    third=a//36
    endom3=third*100
    third_rmd=a%36
    sec=third_rmd//6
    endom2=sec*10
    sec_rmd=a%6
    return(endom3+endom2+sec_rmd)

def ndom_add(a,b):
    d=ndom_to_decimal(a)
    e=ndom_to_decimal(b)
    f=d+e
    g=decimal_to_ndom(f)
    return(g)

def ndom_multiply(a,b):
    d=ndom_to_decimal(a)
    e=ndom_to_decimal(b)
    h=d*e
    m=decimal_to_ndom(h)
    return(m)
