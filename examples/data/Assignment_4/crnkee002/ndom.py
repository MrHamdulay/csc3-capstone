def ndom_to_decimal(a):
    num = 0
    for i in range(len(str(a))):
        num+=(int(str(a)[i])*6**(len(str(a))-1-i))
    return num
    
def decimal_to_ndom(a):
    str1=""
    result=""
    while True:
        if a<6:
            str1+= str(a) + ','        
            break
        else:
            str1+= str(a%6) + ','
            a = a//6
    for i in range(len(str1))[::-1]:
        if i%2==0:
            result = result + str1[i]
    return int(result)

def ndom_add(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))
    
def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))