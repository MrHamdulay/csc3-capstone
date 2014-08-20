def ndom_to_decimal(a):
    first = int(str(a)[0])
    if len(str(a)) == 1:
        return first
    elif len(str(a)) == 2:
        fDec = int(str(a)[1])
        second = first*6
        sDec = int(fDec + second)
        return sDec
    elif len(str(a)) == 3:    
        fDec = int(str(a)[2])
        second = int(str(a)[1])
        sDec = second*6
        third = first*36
        final = int(sDec+fDec+third)
        return final
    
def decimal_to_ndom(a):
    if a<6:
        return a
    elif 6<a<36:
        first = a//6
        rem = a%6
        return (int(str(first)+str(rem)))
    elif a>36:
        first = a//36
        rem = a%36
        second = rem//6
        reme = a%6
        return (int(str(first)+str(second)+str(reme)))
    
def ndom_add(a, b):
    n1 = ndom_to_decimal(a)
    n2 = ndom_to_decimal(b)
    result = n1+n2
    ans = decimal_to_ndom(result)
    return ans
    
def ndom_multiply(a, b):
    n1 = ndom_to_decimal(a)
    n2 = ndom_to_decimal(b)
    result = n1*n2
    ans = decimal_to_ndom (result)
    return ans