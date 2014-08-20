def ndom_to_decimal(choice):
    thousands = choice//1000
    hundreds = (choice%1000)//100
    tens = (choice%100)//10
    digits = (choice%10)//1
    return ((thousands*6+hundreds)*6+tens)*6+digits

def decimal_to_ndom(choice):
    a = choice%6
    b = (choice//6)%6
    c = (choice//36)%6
    d = (choice//216)%6
    if d==0 and c==0 and b==0 and a==0:
        return ""
    if d==0 and c==0 and b==0:
        return str(a)
    if d==0 and c==0:
        return str(b)+str(a)
    if d==0:
        return str(c)+str(b)+str(a)
    else:
        return str(d)+str(c)+str(b)+str(a)

def ndom_add(num1, num2):
    num1 = ndom_to_decimal(num1)
    num2 = ndom_to_decimal(num2)
    ans = num1+num2
    ans = decimal_to_ndom(ans)
    return ans

def ndom_multiply(num1, num2):
    num1 = ndom_to_decimal(num1)
    num2 = ndom_to_decimal(num2)
    ans = num1*num2
    ans = decimal_to_ndom(ans)
    return ans