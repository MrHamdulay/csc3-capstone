
def decimal_to_ndom(a):
    thirthysixes=(a//36)
    sixes=((a-(36*thirthysixes))//6)
    x=(a%6)
    list=[thirthysixes,sixes,x]
    string=str(list[0]) + str(list[1]) + str(list[2])
    string=int(string)
    return string

def ndom_to_decimal(a):
    a=str(a)
    if len(a)>1:
        sixes=eval(a[-2])*6
    else:
        sixes=0
    if len(a)>2:
        thirthysixes=eval(a[-3])*36
    else:
        thirthysixes=0
    x=eval(a[-1])
    num=thirthysixes+sixes+x
    return num

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    answer=a+b
    answer=decimal_to_ndom(answer)
    return answer

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    answer=a*b
    answer=decimal_to_ndom(answer)
    return answer

