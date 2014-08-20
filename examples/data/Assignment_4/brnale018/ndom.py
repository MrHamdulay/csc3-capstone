
def ndom_to_decimal (x):
    a=x%100
    b=a%10
    answer = ((x//100)*36)+((a//10)*6)+b
    return answer 
def decimal_to_ndom(x):
    a=x%36
    b=a%6
    answer=((x//36)*100)+((a//6)*10)+b 
    return answer
def ndom_add (x , y):
    e= ndom_to_decimal(x)
    f= ndom_to_decimal(y)
    g = e + f
    answer = ndom_to_decimal(g)
    return answer
def ndom_multiply (x,y):
    e= ndom_to_decimal(x)
    f= ndom_to_decimal(y)
    g= e + f
    answer = decimal_to_ndom(g)
    return answer


    
            