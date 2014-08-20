def ndom_to_decimal(a):
    output = 0
    string = str(a)
    length = len(string)
    for i in range(length-1,-1,-1):
        if i == length-1: output+=int(string[length-1])
        elif i == length-2: output+=int(str(a)[length-2])*6
        elif i == length-3: output+=int(str(a)[length-3])*36
    return output

def decimal_to_ndom(a):
    output,first,second,third,fourth = 0,0,0,0,0
    if a != 0:
        while a > 0:
            a-=216
            first+=1
        if a != 0:
            a+=216
            first-=1        
            while a > 0:
                a-=36
                second+=1
            if a != 0:
                second-=1
                a+=36
                while a > 0:
                    a-=6
                    third+=1
                if a != 0:
                    third-=1
                    a+=6
                    while a > 0:
                        a-=1
                        fourth+=1
                    output = first*1000 + second*100 + third*10 + fourth
                else : output = first*1000 + second*100 + third*10
            else : output = first*1000 + second*100
        else : output = first*1000
    else : output = 0
    return output

def ndom_add(a, b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
