def ndom_to_decimal(a):
    answer = 0
    l = len(str(a))-1
    for i in str(a):
        answer = answer + int(i)*6**l
        l -= 1
    return answer

def decimal_to_ndom(a):
    j = ""
    while a > 0:
        j = j + str(a%6)
        a=a//6
    return int(j[::-1])

def ndom_add(a, b):
    answer = ndom_to_decimal(a) + ndom_to_decimal(b)
    answer = decimal_to_ndom(answer)
    return answer

def ndom_multiply(a,b):
    answer = ndom_to_decimal(a) * ndom_to_decimal(b)
    answer = decimal_to_ndom(answer) 
    return answer