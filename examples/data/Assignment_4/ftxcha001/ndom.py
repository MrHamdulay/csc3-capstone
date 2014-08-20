#progam to test question 2
#number fors ndom program

def ndom_to_decimal(a):
    number=str(a)
    p=0
    for i in number[:len(number)-1]:
        p+=int(i)
        p*=6
    y= p +int(number[len(number)-1])
    return y
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
                                    