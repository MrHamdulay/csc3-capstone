def ndom_to_decimal(num):
    x=str(num)
    if len(x)==1:
        answer=num
    if len(x)==2:
        answer=6*eval(x[0])+eval(x[1])
    if len(x)==3:
        answer=36*eval(x[0])+6*eval(x[1])+eval(x[2])
    return(answer)   
        
def decimal_to_ndom(num):
    answer=num%6+10*((num//6)%6)+100*(((num//6)//6)%6)+1000*((((num//6)//6)//6)%6)
    return (answer)
                
def ndom_add(num1,num2):
    n1=ndom_to_decimal(num1)
    n2=ndom_to_decimal(num2)
    n3=n1+n2
    answer=decimal_to_ndom(n3)
    return(answer)  

def ndom_multiply(num1,num2):
    n1=ndom_to_decimal(num1)
    n2=ndom_to_decimal(num2)
    n3=n1*n2
    answer=decimal_to_ndom(n3)
    return(answer)
