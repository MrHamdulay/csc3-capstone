#Raeesa Behardien
#BHRRAEOO3
#Assignment 4 - 04 April 2014

def ndom_to_decimal(a):
    third_dig=a//100
    endom3=third_dig*36
    third_dig_rem=a%100
    sec_dig=third_dig_rem//10
    endom2=sec_dig*6
    sec_dig_rem=a%10
    return(endom3+endom2+sec_dig_rem)
  


def decimal_to_ndom(a):
    third_dig=a//36
    endom3=third_dig*100
    third_dig_rem=a%36
    sec_dig=third_dig_rem//6
    endom2=sec_dig*10
    sec_dig_rem=a%6
    return(endom3+endom2+sec_dig_rem)


def ndom_add(a,b):
    h=ndom_to_decimal(a)
    i=ndom_to_decimal(b)
    j=h+i
    k=decimal_to_ndom(j)
    return (k)
   


def ndom_multiply(a,b):
    c=ndom_to_decimal(a)
    d=ndom_to_decimal(b)
    g=c*d
    l=decimal_to_ndom(g)
    return(l)

